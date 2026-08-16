
import pandas as pd

# script B-03 - Cultivation - Import Cultivation

# ------------------------------------------
# Step 1: Import CSV and prepare parent company data
# ------------------------------------------
parent_df = pd.read_csv("Data/Cal Poly/Cannabis Market Intelligence Platform Report - Licenses - 2025-07-03.csv",    dtype=str,
                        keep_default_na=False)
parent_df = parent_df.rename(columns={
    "Company ID": "companyid",
    "Country": "county",
    "State License ID": "statelicenseid"
})

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


# Rename statelicenseid to licenseNumber
parent_df = parent_df.rename(columns={"statelicenseid": "licenseNumber"})

# Keep only licenseNumber and primary_company
parent_df = parent_df[["licenseNumber", "primary_company"]]

# Drop duplicates
parent_df = parent_df.drop_duplicates()
parent_df = parent_df[parent_df["licenseNumber"].notna() & (
    parent_df["licenseNumber"] != "")]

# ------------------------------------------
# Step 2: Import Excel cultivation data
# ------------------------------------------
cultivation_df = pd.read_excel(
    "Data/Cal Poly/Working Cultivation Canopy June 2025.xlsx",
    sheet_name="License data canopy",
    engine="openpyxl",
    dtype=str,
    keep_default_na=False
)

# Filter by licenseStatus == "Active"
cultivation_df = cultivation_df[cultivation_df["licenseStatus"] == "Active"]

# Keep rows where LargeDate is null/NaN
cultivation_df = cultivation_df[cultivation_df["LargeDate"].isna()]

# Create 'type' column based on licenseType mapping
mapping = {
    "Large Indoor": "Indoor",
    "Large Mixed-Light Tier 1": "Mixed_Light",
    "Large Mixed-Light Tier 2": "Mixed_Light",
    "Large Outdoor": "Outdoor",
    "Medium Indoor": "Indoor",
    "Medium Mixed-Light Tier 1": "Mixed_Light",
    "Medium Mixed-Light Tier 2": "Mixed_Light",
    "Medium Outdoor": "Outdoor",
    "Small Indoor": "Indoor",
    "Small Mixed-Light Tier 1": "Mixed_Light",
    "Small Mixed-Light Tier 2": "Mixed_Light",
    "Small Outdoor": "Outdoor",
    "Specialty Cottage Indoor": "Indoor",
    "Specialty Cottage Mixed-Light Tier 1": "Mixed_Light",
    "Specialty Cottage Mixed-Light Tier 2": "Mixed_Light",
    "Specialty Cottage Outdoor": "Outdoor",
    "Specialty Indoor": "Indoor",
    "Specialty Mixed-Light Tier 1": "Mixed_Light",
    "Specialty Mixed-Light Tier 2": "Mixed_Light",
    "Specialty Outdoor": "Outdoor",
}

cultivation_df["type"] = cultivation_df["licenseType"].map(mapping).fillna("")

# Create micro_cult and micro_indoor flags (similar to strpos)
cultivation_df["micro_cult"] = cultivation_df["activity"].astype(str).str.contains("Cultivator").astype(int)
cultivation_df["micro_indoor"] = cultivation_df["activity"].astype(str).str.contains("Indoor").astype(int)

# Drop rows where licenseType == "Microbusiness" and micro_cult == 0
cultivation_df = cultivation_df[~((cultivation_df["licenseType"] == "Microbusiness") & (cultivation_df["micro_cult"] == 0))]

# Adjust type for Microbusiness based on micro_indoor
cond_outdoor = (cultivation_df["licenseType"] == "Microbusiness") & (cultivation_df["micro_indoor"] == 0)
cond_indoor = (cultivation_df["licenseType"] == "Microbusiness") & (cultivation_df["micro_indoor"] == 1)

cultivation_df.loc[cond_outdoor, "type"] = "Outdoor"
cultivation_df.loc[cond_indoor, "type"] = "Indoor"

# ------------------------------------------
# Step 3: Merge cultivation data with parent company data on licenseNumber
# ------------------------------------------
# Ensure licenseNumber columns are comparable types (strings)
parent_df["licenseNumber"] = parent_df["licenseNumber"].astype(str)
cultivation_df["licenseNumber"] = cultivation_df["licenseNumber"].astype(str)

merged_df = cultivation_df.merge(parent_df, on="licenseNumber", how="inner", validate="many_to_one")

# ------------------------------------------
# Step 4: Save to .dta (Stata format)
# ------------------------------------------
merged_df.to_stata("Data/Working_data/cultivation.dta", write_index=False)

#script B-04 - Cultivation- Calculate_Cultivation_Concentration


# Load the cultivation data (assuming it's saved from your earlier step)
cultivation_df = pd.read_stata("Data/Working_data/cultivation.dta")

grow_types = ["Indoor", "Mixed_Light", "Outdoor"]

for grow_type in grow_types:
    df = cultivation_df[cultivation_df["type"] == grow_type].copy()
    
    # === Statewide HHI overall ===
    # Sum by businessLegalName
    statewide_overall = df.groupby("businessLegalName").agg({
        "Canopy": "sum",
        "MaxSqFt": "sum"
    }).reset_index()
    
    # Total industry canopy and maxsqft
    industry_Canopy = statewide_overall["Canopy"].sum()
    industry_MaxSqFt = statewide_overall["MaxSqFt"].sum()
    
    # Market shares
    statewide_overall["mkt_share_Canopy"] = (statewide_overall["Canopy"] / industry_Canopy) * 100
    statewide_overall["mkt_share2_Canopy"] = statewide_overall["mkt_share_Canopy"] ** 2
    
    statewide_overall["mkt_share_MaxSqFt"] = (statewide_overall["MaxSqFt"] / industry_MaxSqFt) * 100
    statewide_overall["mkt_share2_MaxSqFt"] = statewide_overall["mkt_share_MaxSqFt"] ** 2
    
    # Collapse sums of market share squared and totals
    CA_overall = pd.DataFrame({
        "mkt_share2_Canopy": [statewide_overall["mkt_share2_Canopy"].sum()],
        "Canopy": [statewide_overall["Canopy"].sum()],
        "mkt_share2_MaxSqFt": [statewide_overall["mkt_share2_MaxSqFt"].sum()],
        "MaxSqFt": [statewide_overall["MaxSqFt"].sum()]
    })
    CA_overall["premiseCounty"] = "CA"
    CA_overall["level"] = "Overall"

    # === Statewide HHI Parent Company ===
    # Collapse (sum) by primary_company (first businessLegalName not needed for calculation)
    # Step 1: sum by primary_company
    parent_group = df.groupby("primary_company").agg({
        "Canopy": "sum",
        "MaxSqFt": "sum",
        "businessLegalName": "first"  # to mimic collapse (first)
    }).reset_index()

    # Step 2: sum by businessLegalName (like collapse again)
    parent_business = parent_group.groupby("businessLegalName").agg({
        "Canopy": "sum",
        "MaxSqFt": "sum"
    }).reset_index()

    industry_Canopy = parent_business["Canopy"].sum()
    industry_MaxSqFt = parent_business["MaxSqFt"].sum()

    parent_business["mkt_share_Canopy"] = (parent_business["Canopy"] / industry_Canopy) * 100
    parent_business["mkt_share2_Canopy"] = parent_business["mkt_share_Canopy"] ** 2

    parent_business["mkt_share_MaxSqFt"] = (parent_business["MaxSqFt"] / industry_MaxSqFt) * 100
    parent_business["mkt_share2_MaxSqFt"] = parent_business["mkt_share_MaxSqFt"] ** 2

    CA_parent = pd.DataFrame({
        "mkt_share2_Canopy": [parent_business["mkt_share2_Canopy"].sum()],
        "Canopy": [parent_business["Canopy"].sum()],
        "mkt_share2_MaxSqFt": [parent_business["mkt_share2_MaxSqFt"].sum()],
        "MaxSqFt": [parent_business["MaxSqFt"].sum()]
    })
    CA_parent["premiseCounty"] = "CA"
    CA_parent["level"] = "Parent Company"

    # === County-level HHI overall ===
    # Sum by businessLegalName and premiseCounty
    county_overall = df.groupby(["businessLegalName", "premiseCounty"]).agg({
        "Canopy": "sum",
        "MaxSqFt": "sum"
    }).reset_index()

    # industry sums by premiseCounty
    industry_sum_canopy = county_overall.groupby("premiseCounty")["Canopy"].transform("sum")
    industry_sum_maxsqft = county_overall.groupby("premiseCounty")["MaxSqFt"].transform("sum")

    county_overall["mkt_share_Canopy"] = (county_overall["Canopy"] / industry_sum_canopy) * 100
    county_overall["mkt_share2_Canopy"] = county_overall["mkt_share_Canopy"] ** 2

    county_overall["mkt_share_MaxSqFt"] = (county_overall["MaxSqFt"] / industry_sum_maxsqft) * 100
    county_overall["mkt_share2_MaxSqFt"] = county_overall["mkt_share_MaxSqFt"] ** 2

    # Collapse by premiseCounty (sum)
    county_overall_agg = county_overall.groupby("premiseCounty").agg({
        "mkt_share2_Canopy": "sum",
        "Canopy": "sum",
        "mkt_share2_MaxSqFt": "sum",
        "MaxSqFt": "sum"
    }).reset_index()
    county_overall_agg["level"] = "Overall"

    # === County-level HHI Parent Company ===
    # Collapse (sum) by primary_company and premiseCounty (first businessLegalName)
    parent_county_group = df.groupby(["primary_company", "premiseCounty"]).agg({
        "Canopy": "sum",
        "MaxSqFt": "sum",
        "businessLegalName": "first"
    }).reset_index()

    # Collapse (sum) by businessLegalName and premiseCounty
    parent_county_business = parent_county_group.groupby(["businessLegalName", "premiseCounty"]).agg({
        "Canopy": "sum",
        "MaxSqFt": "sum"
    }).reset_index()

    # industry sums by premiseCounty
    industry_sum_canopy_parent = parent_county_business.groupby("premiseCounty")["Canopy"].transform("sum")
    industry_sum_maxsqft_parent = parent_county_business.groupby("premiseCounty")["MaxSqFt"].transform("sum")

    parent_county_business["mkt_share_Canopy"] = (parent_county_business["Canopy"] / industry_sum_canopy_parent) * 100
    parent_county_business["mkt_share2_Canopy"] = parent_county_business["mkt_share_Canopy"] ** 2

    parent_county_business["mkt_share_MaxSqFt"] = (parent_county_business["MaxSqFt"] / industry_sum_maxsqft_parent) * 100
    parent_county_business["mkt_share2_MaxSqFt"] = parent_county_business["mkt_share_MaxSqFt"] ** 2

    # Collapse by premiseCounty
    county_parent_agg = parent_county_business.groupby("premiseCounty").agg({
        "mkt_share2_Canopy": "sum",
        "Canopy": "sum",
        "mkt_share2_MaxSqFt": "sum",
        "MaxSqFt": "sum"
    }).reset_index()
    county_parent_agg["level"] = "Parent Company"

    # === Combine all results ===
    combined = pd.concat([
        county_overall_agg,
        CA_overall,
        county_parent_agg,
        CA_parent
    ], ignore_index=True, sort=False)
    numeric_cols = combined.select_dtypes(include=["number"]).columns
    combined[numeric_cols] = combined[numeric_cols].round(0).astype(int)
    final_export = combined.astype(str)
    # Save to Excel, replicate Stata export with firstrow(variables) replace
    output_path = f"Data/Results/Cult_HHI__{grow_type}_test.xlsx"
    final_export.to_excel(output_path, index=False)

    print(f"Saved {output_path}")