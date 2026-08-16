import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# =====================================================
# Script B-01 - Harvest + Package - Import & Merge Data
# =====================================================

data_dir = Path("Data")

# Input files
harvest_files = [
    data_dir / "Track and Trace Data/Cultivation/harvestqty19-24.csv",
    data_dir / "Track and Trace Data/Cultivation/harvestqty23-24.csv",
    data_dir / "Track and Trace Data/Cultivation/harvestqty25.csv"
]

# Output file
output_file = data_dir / "Track and Trace Data/Harvest/harvest.csv"

# -------------------- Load & Append --------------------
dfs = []
for file in harvest_files:
    df = pd.read_csv(file, dtype=str, keep_default_na=False)
    dfs.append(df)

# Concatenate
harvest_df = pd.concat(dfs, ignore_index=True)

# -------------------- Export --------------------
output_file.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
harvest_df.to_csv(output_file, index=False)

# -------------------- HARVEST FILE --------------------
harvest_df = pd.read_csv(
    data_dir / "Track and Trace Data/Harvest/harvest.csv",
    dtype=str,
    keep_default_na=False
)

harvest_df = harvest_df.rename(columns={
    "HarvesterLicenseNumber": "harvesterlicensenumber",
    "HarvesterFacilityType": "harvesterfacilitytype",
    "HarvesterCity": "harvestercity",
    "HarvesterZipCode": "harvesterzipcode",
    "HarvesterCounty": "harvestercounty",
    "PkgYear": "year",
    "TotalHarvestPounds": "totalharvestpounds",
    "TotalHarvestWetPounds": "totalharvestwetpounds",
    "UniqueHarvestBatches": "uniqueharvestbatches"
})

harvest_df["year"] = pd.to_numeric(harvest_df["year"], errors="coerce")
harvest_df["totalharvestpounds"] = pd.to_numeric(harvest_df["totalharvestpounds"], errors="coerce")
harvest_df["totalharvestwetpounds"] = pd.to_numeric(harvest_df["totalharvestwetpounds"], errors="coerce")
# -------------------- CLEAN HARVESTER COUNTY --------------------
harvest_df["harvestercounty"] = harvest_df["harvestercounty"].replace(
    {"NA": "", "UNDEFINED": ""}
)

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
    "Yuba County": "YUBA",
}
# normalize harvestercounty
for cannabiz_val, county_val in county_map.items():
    mask = harvest_df["harvestercounty"] == cannabiz_val
    harvest_df.loc[mask, "harvestercounty"] = county_val

# strip and drop blanks
harvest_df["harvestercounty"] = harvest_df["harvestercounty"].astype(str).str.strip()
harvest_df["harvestercounty"] = harvest_df["harvestercounty"].replace("", pd.NA)
harvest_df = harvest_df.dropna(subset=["harvestercounty"])
# Input files
package_files = [
    data_dir / "Track and Trace Data/Cultivation/packageqty19-24.csv",
    data_dir / "Track and Trace Data/Cultivation/packageqty23-24.csv",
    data_dir / "Track and Trace Data/Cultivation/packageqty25.csv"
]

# Output file
output_file = data_dir / "Track and Trace Data/Package/package.csv"

# -------------------- Load & Append --------------------
dfs = []
for file in package_files:
    df = pd.read_csv(file, dtype=str, keep_default_na=False)
    dfs.append(df)

# Concatenate
package_df = pd.concat(dfs, ignore_index=True)

# -------------------- Export --------------------
output_file.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
package_df.to_csv(output_file, index=False)

# -------------------- PACKAGE FILE --------------------
package_df = pd.read_csv(
    data_dir / "Track and Trace Data/Package/package.csv",
    dtype=str,
    keep_default_na=False
)

package_df = package_df.rename(columns={
    "HarvesterLicenseNumber": "harvesterlicensenumber",
    "HarvesterFacilityType": "harvesterfacilitytype",
    "HarvesterCity": "harvestercity",
    "HarvesterZipCode": "harvesterzipcode",
    "HarvesterCounty": "harvestercounty",
    "ItemCategory": "itemcategory",
    "Year": "year",
    "TotalPackagePounds": "totalpackagepounds",
    "UniqueHarvestBatches": "uniqueharvestbatches"
})


package_df["year"] = pd.to_numeric(package_df["year"], errors="coerce")
package_df["totalpackagepounds"] = pd.to_numeric(package_df["totalpackagepounds"], errors="coerce")
# normalize harvestercounty
for cannabiz_val, county_val in county_map.items():
    mask = package_df["harvestercounty"] == cannabiz_val
    package_df.loc[mask, "harvestercounty"] = county_val

# strip and drop blanks
package_df["harvestercounty"] = package_df["harvestercounty"].astype(str).str.strip()
package_df["harvestercounty"] = package_df["harvestercounty"].replace("", pd.NA)
package_df = package_df.dropna(subset=["harvestercounty"])
# -------------------- MERGE HARVEST + PACKAGE --------------------
merged = package_df.merge(
    harvest_df,
    on=["harvesterlicensenumber", "year"],
    how="left",
    suffixes=("_pkg", "_harv")
)
if "harvestercounty_harv" in merged.columns and "harvestercounty_pkg" in merged.columns:
    merged["harvestercounty"] = merged["harvestercounty_harv"].fillna(merged["harvestercounty_pkg"])
elif "harvestercounty_harv" in merged.columns:
    merged["harvestercounty"] = merged["harvestercounty_harv"]
elif "harvestercounty_pkg" in merged.columns:
    merged["harvestercounty"] = merged["harvestercounty_pkg"]
# -------------------- RATIOS --------------------
merged["package_to_harvest_ratio"] = (
    merged["totalpackagepounds"] / merged["totalharvestpounds"]
)

merged["dry_to_wet_ratio"] = (
    merged["totalharvestpounds"] / merged["totalharvestwetpounds"]
)

merged["category_share"] = (
    merged["totalpackagepounds"] / merged["totalharvestpounds"]
)

merged["harvestercounty"] = merged["harvestercounty"].astype(str).str.strip()
merged["harvestercounty"] = merged["harvestercounty"].replace("", pd.NA)
merged = merged.dropna(subset=["harvestercounty"])

# =====================================================
# Script B-02 - Aggregate & Plot
# =====================================================

# Category-level aggregation
category_summary = (
    merged.groupby(["harvestercounty", "year", "itemcategory"], as_index=False)
          .agg({
              "totalharvestpounds": "first",  # from harvest
              "totalpackagepounds": "sum",
              "package_to_harvest_ratio": "mean"
          })
)

# County-level harvest vs package
county_summary = (
    merged.groupby(["harvestercounty", "year"], as_index=False)
          .agg({
              "totalharvestpounds": "first",
              "totalpackagepounds": "sum"
          })
)
county_summary["package_to_harvest_ratio"] = (
    county_summary["totalpackagepounds"] / county_summary["totalharvestpounds"]
)

# =====================================================
# Script B-03 - Export Results
# =====================================================
output_path = data_dir / "Results/harvest_package_ratios.xlsx"
county_summary.to_excel(output_path, index=False)
