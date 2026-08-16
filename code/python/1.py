import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# script A-01 - Retail - Import Merge Data

data_dir = Path("Data")

# -------------------- ZIP COUNTY MAPPING --------------------
zip_df = pd.read_excel(
    data_dir / "HUD/ZIP_COUNTY_122024.xlsx",
    sheet_name="Export Worksheet",
    dtype=str,
    keep_default_na=False
)
zip_df = zip_df[zip_df["USPS_ZIP_PREF_STATE"] == "CA"]

# Stata's duplicates tag + drop if >= 1 means keep ZIPs with NO duplicates
zip_df = zip_df[~zip_df.duplicated(subset=["ZIP"], keep=False)]

zip_df = zip_df[["ZIP", "retailercounty"]].rename(columns={"ZIP": "zip5"})

# -------------------- PARENT COMPANY --------------------
parent_df = pd.read_csv(
    data_dir / "Cannabiz/Cannabis Market Intelligence Platform Report - Licenses - 2025-02-21.csv",
    dtype=str,
    keep_default_na=False
)
parent_df = parent_df.rename(columns={
    "Company ID": "companyid",
    "Country": "county",
    "State License ID": "statelicenseid"
})
# Match Stata's logic exactly
parent_df['multi_owner'] = 0
parent_df['multi_owner'] = parent_df['companyid'].str.find(
    ";")  # -1 if not found
# match Stata's 0
parent_df['multi_owner'] = parent_df['multi_owner'].replace(-1, 0)
parent_df['primary_company'] = parent_df.apply(
    lambda row: row['companyid'][:row['multi_owner']
                                 ] if row['multi_owner'] > 0 else row['companyid'],
    axis=1
)

parent_df["primary_company"] = pd.to_numeric(
    parent_df["primary_company"], errors="coerce")

parent_df = parent_df[["statelicenseid", "primary_company", "county"]]
parent_df = parent_df.rename(columns={
    "statelicenseid": "retailerlicensenumber",
    "county": "cannabiz_county"
})
parent_df = parent_df.drop_duplicates()
parent_df = parent_df[parent_df["retailerlicensenumber"].notna() & (
    parent_df["retailerlicensenumber"] != "")]
parent_temp = parent_df.copy()  # tempfile parent_co


# -------------------- SALES FILES --------------------
sales_files = [
    "sales18.csv", "sales19.csv", "sales20.csv",
    "sales21.csv", "sales22.csv", "sales23v2.csv", "sales24.csv"
]
sales_dir = data_dir / "Track and Trace Data" / "Retail"

processed_sales = {}  # this replaces Stata's tempfile for each processed year

for file in sales_files:
    df = pd.read_csv(sales_dir / file, dtype=str, keep_default_na=False)
    df = df.drop(columns=[c for c in ["meanprice", "v1"] if c in df.columns])
    year_key = file.replace(".csv", "")  # e.g., sales18
    processed_sales[year_key] = df.copy()  # save in dict for later append

# Append like Stata's sequential append
sales_df = processed_sales["sales18"]
for year_key in ["sales19", "sales20", "sales21", "sales22", "sales23v2", "sales24"]:
    sales_df = pd.concat(
        [sales_df, processed_sales[year_key]], ignore_index=True)


sales_df.rename(columns={"ItemCategory": "itemcategory"}, inplace=True)

# -------------------- TABULATE ITEMCATEGORY --------------------
print(sales_df["itemcategory"].value_counts(dropna=False))


working_dir = data_dir / "Working_data"


sales_df = sales_df.rename(columns={
    "RetailerLicenseNumber": "retailerlicensenumber",
    "RetailerCounty": "retailercounty",
    "RetailerFacilityType": "retailerfacilitytype",
    "RetailerCity": "retailercity",
    "RetailerZipCode": "retailerzipcode",
    "Date": "date",
    "ItemCategory": "itemcategory",
    "totalsales": "totalsales"
})

sales_df = sales_df.sort_values(
    by=["retailerlicensenumber", "retailercounty", "retailerfacilitytype",
        "retailercity", "retailerzipcode", "date", "itemcategory", "totalsales"],
    ascending=[True, False, True, True, True, True, True, True]
)

# # ===================== 2. MERGE parent company =====================
df = sales_df.merge(parent_temp, on="retailerlicensenumber",
                    how="left", indicator=True)
df = df[df["_merge"] != "right_only"]  # drop if _merge==2
df = df.drop(columns="_merge")

# # ===================== 3. Clean retailercounty values =====================
df["retailercounty"] = df["retailercounty"].replace(
    {"NA": "", "UNDEFINED": ""})

# Fill from cannabiz_county where missing
county_map = {
    "Alameda County": "ALAMEDA",
    "El Dorado County": "EL DORADO",
    "Humboldt County": "HUMBOLDT",
    "Imperial County": "IMPERIAL",
    "Inyo County": "INYO",
    "Kern County": "KERN",
    "Kings County": "KINGS",
    "Los Angeles County": "LOS ANGELES",
    "Marin County": "MARIN",
    "Mendocino County": "MENDOCINO",
    "Merced County": "MERCED",
    "Monterey County": "MONTEREY",
    "Nevada County": "NEVADA",
    "Riverside County": "RIVERSIDE",
    "Sacramento County": "SACRAMENTO",
    "San Diego County": "SAN DIEGO",
    "San Francisco County": "SAN FRANCISCO",
    "San Luis Obispo County": "SAN LUIS OBISPO",
    "San Mateo County": "SAN MATEO",
    "Santa Barbara County": "SANTA BARBARA",
    "Santa Cruz County": "SANTA CRUZ",
    "Shasta County": "SHASTA",
    "Sonoma County": "SONOMA",
    "Stanislaus County": "STANISLAUS",
    "Tulare County": "TULARE",
    "Ventura County": "VENTURA",
    "Calaveras County": "CALAVERAS",
    "Lassen County": "LASSEN",
    "Mono County": "MONO",
    "Napa County": "NAPA",
    "San Benito County": "SAN BENITO",
    "San Bernardino County": "SAN BERNARDINO",
    "San Joaquin County": "SAN JOAQUIN",
    "Santa Clara County": "SANTA CLARA",
    "Yuba County": "YUBA"
}

for cannabiz_val, county_val in county_map.items():
    mask = (df["cannabiz_county"] == cannabiz_val) & (
        df["retailercounty"] == "")
    df.loc[mask, "retailercounty"] = county_val

# # ===================== 4. Manual county overrides (retailerlicensenumber specific) =====================
manual_county_fix = {
    "C10-0000209-LIC": "RIVERSIDE",
    "C12-0000370-LIC": "SAN BERNARDINO",
}
for lic, county in manual_county_fix.items():
    df.loc[df["retailerlicensenumber"] == lic, "retailercounty"] = county

# Uppercase everything
df["retailercounty"] = df["retailercounty"].str.upper()

# # ===================== 5. Preserve & create license_county (preserve/restore equivalent) =====================
license_county = (
    df.loc[(df["retailerlicensenumber"] != "") & (df["retailercounty"] != ""),
           ["retailerlicensenumber", "retailercounty"]]
    .drop_duplicates()
)
# Merge back with update logic
df = df.merge(
    license_county,
    on="retailerlicensenumber",
    how="left",
    suffixes=("", "_from_license_county")
)

# Start with "3" for matched rows (has using value) and "1" for unmatched
merge_code = pd.Series(1, index=df.index)
merge_code[df["retailercounty_from_license_county"].notna()] = 3

# Now detect updates: master is empty but using has a value
mask_update = (df["retailercounty"] ==
               "") & df["retailercounty_from_license_county"].notna()
merge_code[mask_update] = 4

# Apply updates
df.loc[mask_update, "retailercounty"] = df.loc[mask_update,
                                               "retailercounty_from_license_county"]

# Store merge code like Stata's _merge_lic_county
df["_merge_lic_county"] = merge_code
labels = {1: "Master only", 3: "Matched", 4: "Matched & updated"}
df["_merge_lic_county"] = df["_merge_lic_county"].map(labels)
# Drop helper
df = df.drop(columns=["retailercounty_from_license_county"])

# ===================== 6. Merge ZIP mapping =====================
# --- 1. Create zip5 as first 5 characters of retailerzipcode
df["zip5"] = df["retailerzipcode"].astype(str).str[:5]

# --- 2. Merge m:1 zip5 using zip_df, simulate update merge
df = df.merge(
    zip_df,  # your HUD ZIP dataset
    on="zip5",
    how="left",
    suffixes=("", "_from_zip")
)

# --- 3. Create merge code like Stata's _merge_zip
merge_zip_code = pd.Series(1, index=df.index)  # default: master only
merge_zip_code[df["retailercounty_from_zip"].notna()] = 3

# Rows to update: master county is empty but using has value
mask_update_zip = (df["retailercounty"] ==
                   "") & df["retailercounty_from_zip"].notna()
merge_zip_code[mask_update_zip] = 4

# Apply the updates
df.loc[mask_update_zip, "retailercounty"] = df.loc[mask_update_zip,
                                                   "retailercounty_from_zip"]
# Store merge code column
df["_merge_zip"] = merge_zip_code
# --- 4. Drop if _merge_zip == 2 (only in using)
df = df[df["_merge_zip"] != 2]


labels = {1: "Master only", 3: "Matched", 4: "Matched & updated"}
df["_merge_zip"] = df["_merge_zip"].map(labels)
# --- 5. Drop helper columns
df = df.drop(columns=["retailercounty_from_zip"])
df = df.drop(columns=["_merge_zip"])
df = df.drop(columns=["Unnamed: 0"])
# ===================== 7. More manual overrides =====================
more_manual_fixes = {
    "C10-0000279-LIC": "LOS ANGELES",
    "C10-0000747-LIC": "LOS ANGELES",
    "C12-0000056-LIC": "LOS ANGELES",
    "C9-0000499-LIC": "LOS ANGELES",
    "C10-0000248-LIC": "LOS ANGELES",
    "C9-0000386-LIC": "KINGS",
    "C10-0000343-LIC": "TULARE",
    "C10-0000299-LIC": "TULARE",
    "C10-0000078-LIC": "MONO",
    "C10-0000265-LIC": "SAN FRANCISCO",
    "C12-0000068-LIC": "SOLANO",
    "C9-0000396-LIC": "SAN BENITO",
    "C10-0000238-LIC": "SANTA CRUZ",
    "C10-0000576-LIC": "STANISLAUS",
    "C10-0000022-LIC": "STANISLAUS",
    "C12-0000157-LIC": "SACRAMENTO",
    "C10-0000190-LIC": "HUMBOLDT",
    "C10-0000148-LIC": "YOLO",
    "C10-0000111-LIC": "YOLO",
    "C9-0000088-LIC": "YOLO",
    "C10-0000449-LIC": "YUBA",
    "C10-0000707-LIC": "YUBA",
    "C10-0000398-LIC": "LOS ANGELES",
    "C10-0000382-LIC": "MONO",
    "C10-0000200-LIC": "SAN FRANCISCO",
    "C10-0000152-LIC": "SAN FRANCISCO",
    "C9-0000376-LIC": "SOLANO",
    "C10-0000098-LIC": "LOS ANGELES",
    "C10-0000196-LIC": "STANISLAUS",
    "C9-0000142-LIC": "YOLO",
    "C9-0000061-LIC": "NEVADA",
}
for lic, county in more_manual_fixes.items():
    df.loc[df["retailerlicensenumber"] == lic, "retailercounty"] = county

df = df.fillna("").astype(str)
# ===================== 8. Tabulate retailercounty =====================
print(df["retailercounty"].value_counts(dropna=False))

# ===================== 9. Save =====================
output_path = working_dir / "sales_w_parent_co_test.dta"
df.to_stata(output_path, write_index=False)


# A-02 - Retail - Calculate_Concentration


df = pd.read_stata(working_dir / "sales_w_parent_co_test.dta",
                   convert_categoricals=False)


# Create year from date string
df["year"] = df["date"].astype(str).str[3:7]
df["totalsales"] = pd.to_numeric(df["totalsales"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")

# ------------------------------
# Statewide HHI overall (CA_overall)
# ------------------------------
collapsed = (
    df.groupby(["retailerlicensenumber", "year"], as_index=False)
      .agg({
          "totalsales": "sum",
          "retailerzipcode": "first",
          "primary_company": "first"
      })
)

collapsed["industry_sales"] = collapsed.groupby(
    "year")["totalsales"].transform("sum")
collapsed["mkt_share"] = (collapsed["totalsales"] /
                          collapsed["industry_sales"]) * 100
collapsed["mkt_share2"] = collapsed["mkt_share"] ** 2

CA_overall = (
    collapsed.groupby("year", as_index=False)
    .agg({"mkt_share2": "sum", "totalsales": "sum"})
)
CA_overall["retailercounty"] = "CA"

# ------------------------------
# Statewide HHI by parent company (CA_parent)
# ------------------------------
df_parent = df.copy()
df_parent["primary_company"] = df_parent["primary_company"].where(
    df_parent["primary_company"].astype(str).str.strip() != "",
    df_parent["retailerlicensenumber"]
)

collapsed_parent = (
    df_parent.groupby(["primary_company", "year"], as_index=False)
             .agg({
                 "totalsales": "sum",
                 "retailerzipcode": "first"
             })
)

collapsed_parent["industry_sales"] = collapsed_parent.groupby(
    "year")["totalsales"].transform("sum")
collapsed_parent["mkt_share"] = (
    collapsed_parent["totalsales"] / collapsed_parent["industry_sales"]) * 100
collapsed_parent["mkt_share2"] = collapsed_parent["mkt_share"] ** 2

CA_parent = (
    collapsed_parent.groupby("year", as_index=False)
                    .agg({"mkt_share2": "sum", "totalsales": "sum"})
)
CA_parent = CA_parent.rename(columns={
    "mkt_share2": "mkt_share2_parent",
    "totalsales": "totalsales_parent"
})
CA_parent["retailercounty"] = "CA"


# =========================================================
# County-level HHI overall (county_overall)
# =========================================================
collapsed_county = (
    df.groupby(["retailerlicensenumber",
               "retailercounty", "year"], as_index=False)
    .agg({
        "totalsales": "sum",
        "retailerzipcode": "first",
        "primary_company": "first"
    })
)
collapsed_county["industry_sales"] = collapsed_county.groupby(
    ["retailercounty", "year"])["totalsales"].transform("sum")
collapsed_county["mkt_share"] = (
    collapsed_county["totalsales"] / collapsed_county["industry_sales"]) * 100
collapsed_county["mkt_share2"] = collapsed_county["mkt_share"] ** 2

county_overall = (
    collapsed_county.groupby(["retailercounty", "year"], as_index=False)
                    .agg({"mkt_share2": "sum", "totalsales": "sum"})
)

# =========================================================
# County-level HHI by parent company (county_parent)
# =========================================================
df_parent_county = df.copy()
df_parent_county["primary_company"] = df_parent_county["primary_company"].where(
    df_parent_county["primary_company"].astype(str).str.strip() != "",
    df_parent_county["retailerlicensenumber"]
)

collapsed_county_parent = (
    df_parent_county.groupby(
        ["primary_company", "retailercounty", "year"], as_index=False)
    .agg({
        "totalsales": "sum",
        "retailerzipcode": "first"
    })
)
collapsed_county_parent["industry_sales"] = collapsed_county_parent.groupby(
    ["retailercounty", "year"]
)["totalsales"].transform("sum")
collapsed_county_parent["mkt_share"] = (
    collapsed_county_parent["totalsales"] / collapsed_county_parent["industry_sales"]) * 100
collapsed_county_parent["mkt_share2"] = collapsed_county_parent["mkt_share"] ** 2

county_parent = (
    collapsed_county_parent.groupby(["retailercounty", "year"], as_index=False)
                           .agg({"mkt_share2": "sum", "totalsales": "sum"})
)
county_parent = county_parent.rename(columns={
    "mkt_share2": "mkt_share2_parent",
    "totalsales": "totalsales_parent"
})

# =========================================================
# Merge all results like Stata's append + merge sequence
# =========================================================
# county_overall + CA_overall
all_overall = pd.concat([county_overall, CA_overall], ignore_index=True)

# Merge with county_parent
merged = pd.merge(all_overall, county_parent, on=[
                  "retailercounty", "year"], how="left")

# Merge with CA_parent (update like Stata's 'update' option)
merged = pd.merge(merged, CA_parent, on=[
                  "retailercounty", "year"], how="left", suffixes=("", "_ca"))
for col in ["mkt_share2_parent", "totalsales_parent"]:
    merged[col] = merged[col].combine_first(merged[f"{col}_ca"])
    merged.drop(columns=[f"{col}_ca"], inplace=True)

# =========================================================
# Final calculations (opacity)
# =========================================================
max_sales = merged.loc[merged["retailercounty"] == "CA", "totalsales"].sum()
max_sales2 = max_sales  # Stata's max(max_sales)

merged["county_sales"] = merged.groupby(
    "retailercounty")["totalsales"].transform("sum")
merged["county_sales_parent"] = merged.groupby(
    "retailercounty")["totalsales_parent"].transform("sum")

merged["opacity"] = round((merged["county_sales"] / max_sales2) * 100)
merged["opacity_parent"] = round(
    (merged["county_sales_parent"] / max_sales2) * 100)


# Filter your merged dataset from before
plot_df = merged.copy()

# List of counties
counties = plot_df["retailercounty"].unique()

fig, ax = plt.subplots(figsize=(12, 7))

for county in sorted(counties):
    county_data = plot_df[plot_df["retailercounty"]
                          == county].sort_values("year")
    if county == "CA":
        ax.plot(
            county_data["year"],
            county_data["mkt_share2"],
            color="black",
            linewidth=2.5,
            label="CA"
        )
    else:
        ax.plot(
            county_data["year"],
            county_data["mkt_share2"],
            color="navy",
            linewidth=1,
            alpha=0.7
        )

# Axis labels & title
ax.set_xlabel("Year")
ax.set_ylabel("HHI")
ax.set_title("HHI Over Time by County")

# X-axis ticks like 2018(1)2024
ax.set_xticks(range(2018, 2025))
ax.set_xticklabels(range(2018, 2025))

# Horizontal y-axis labels
ax.tick_params(axis="y", rotation=0)

# Hide legend (like legend(off))
ax.legend().set_visible(False)

plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(12, 7))

for county in counties:
    county_data = plot_df[plot_df["retailercounty"]
                          == county].sort_values("year")
    if county == "CA":
        ax.plot(
            county_data["year"],
            county_data["mkt_share2_parent"],
            color="black",
            linewidth=2.5,
            label="CA"
        )
    else:
        ax.plot(
            county_data["year"],
            county_data["mkt_share2_parent"],
            color="navy",
            linewidth=1,
            alpha=0.7
        )

ax.set_xlabel("Year")
ax.set_ylabel("HHI")
ax.set_title("HHI Over Time by County (Parent Company Level)")

ax.set_xticks(range(2018, 2025))
ax.set_xticklabels(range(2018, 2025))

ax.tick_params(axis="y", rotation=0)

ax.legend().set_visible(False)

plt.tight_layout()
plt.show()


final_export = merged.copy()

# Rename columns like in Stata
final_export = final_export.rename(columns={
    "mkt_share2": "HHI",
    "mkt_share2_parent": "HHI_parent_level"
})

# Round numeric columns to nearest integer
final_export["HHI"] = final_export["HHI"].round(0).astype(int)
final_export["HHI_parent_level"] = final_export["HHI_parent_level"].round(
    0).astype(int)

# Keep needed columns
final_export = final_export[["retailercounty",
                             "year", "HHI", "HHI_parent_level"]]

# Convert all columns to string
final_export = final_export.astype(str)

# Export to Excel
final_export.to_excel(
    data_dir / "Results/HHI_by_county_test.xlsx", index=False)
