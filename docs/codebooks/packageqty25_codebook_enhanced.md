# Track & Trace Data Codebook

### Overview Section

This dataset provides summarized information related to cannabis packaging quantities within the Track & Trace project. It aggregates data concerning licensed harvesters, their facility types, locations, and the categories and volumes of cannabis items packaged. The dataset aims to offer insights into the distribution of packaged cannabis products across different harvesters and item categories for a specific year.

One row in the `packageqty25` table represents the total packaged pounds and the count of unique harvest batches for a specific harvester, item category, and year.

The overall data source is the Track & Trace system. The collection period and extraction date are not explicitly provided, but the `PkgYear` column indicates the data pertains to the year 2025.

**Assumptions:**
*   The `packageqty25` table name implies a specific aggregation level or version of package quantity data.
*   The `PkgYear` being uniformly '2025' suggests this dataset might be a projection, a specific annual report, or a limited snapshot.

### Table Inventory

*   **packageqty25:** Summarizes packaged cannabis quantities, aggregated by harvester, item category, and year.

## Table: packageqty25

*   **Purpose:** To provide an aggregated view of cannabis packaging activities, detailing total packaged pounds and unique harvest batches per harvester, item category, and year.
*   **What one row represents:** One row represents the total packaged pounds and unique harvest batches associated with a specific harvester (identified by `HarvesterLicenseNumber`), for a particular `ItemCategory`, during the `PkgYear`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` (composite key, inferred)
*   **Relationships:** Not explicitly defined.
*   **Number of rows and columns:** 4125 rows, 9 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the cannabis harvester's license.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility associated with the harvester's license.",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester's facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester's facility.",
    "Allowed Values / Range": "Range: [89019.0, 960679768.0]",
    "Missing %": "3.2",
    "Cleaning / Notes": "Range includes values (e.g., 960679768.0) that are not valid 5-digit or 9-digit US zip codes. These likely represent data entry errors or concatenated values. Proposed handling: Flag invalid zip codes, attempt to correct based on city/county, or set to null if uncorrectable. Convert to string type."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester's facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item (e.g., Flower, Edible).",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "PkgYear",
    "Type": "int64",
    "Units": "Year",
    "Description": "Year of packaging.",
    "Allowed Values / Range": "Range: [2025.0, 2025.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "All values are '2025', indicating the dataset may be limited to a specific year or a future projection."
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of packaged cannabis in pounds.",
    "Allowed Values / Range": "Range: [0.0004188786398349, 282901.024047837]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches contributing to the packaged quantity.",
    "Allowed Values / Range": "Range: [1.0, 478.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Invalid `HarvesterZipCode` values and incorrect data type.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or incorrect data type conversion (storing zip codes as `float64` instead of string or integer). The presence of values like `960679768.0` strongly suggests data corruption or misinterpretation.
    *   **Recommended handling rule:** Convert `HarvesterZipCode` to a string type. Validate all `HarvesterZipCode` entries against standard 5-digit or 9-digit US zip code formats. For invalid entries, attempt to correct using `HarvesterCity` and `HarvesterCounty` information. If correction is not feasible, set the `HarvesterZipCode` to NULL to indicate missing or unrecoverable data.
*   **Issue:** `PkgYear` contains only a single value (2025).
    *   **Likely cause:** The dataset might be a specific snapshot, a projection, or intentionally limited to a single year's data. It could also indicate an incomplete data extract if broader historical data is expected.
    *   **Recommended handling rule:** Document this limitation and seek clarification on the intended temporal scope of the dataset. No direct cleaning is needed unless the data is confirmed to be incomplete.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode` Data Type:** Convert the `HarvesterZipCode` column from `float64` to a `string` data type to ensure proper handling of leading zeros and non-numeric characters if they were to appear.
2.  **Validate `HarvesterZipCode` Format:** Implement a validation check to identify `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit US zip code patterns.
3.  **Address Invalid `HarvesterZipCode` Entries:** For any `HarvesterZipCode` identified as invalid, attempt to correct the value by cross-referencing with `HarvesterCity` and `HarvesterCounty` using external geographic data if available. If a valid correction cannot be determined, replace the invalid entry with a NULL value.
4.  **Document `PkgYear` Scope:** Add a metadata flag or note indicating that the `PkgYear` column exclusively contains the value '2025', highlighting the dataset's specific temporal focus.

### Limitations & Trust Section

*   **`HarvesterZipCode` Reliability:** The `HarvesterZipCode` column exhibits significant data quality issues, including an inappropriate `float64` data type and values outside the valid range for US zip codes (e.g., `960679768.0`). This compromises the accuracy of geographic analysis. Validation against a comprehensive list of US zip codes and cross-referencing with `HarvesterCity` and `HarvesterCounty` is critically needed to improve trust in location-based data.
*   **`PkgYear` Temporal Scope:** The `PkgYear` column exclusively containing '2025' limits the dataset's utility for historical trend analysis or multi-year comparisons. Clarification is required to determine if this is a future projection, a specific annual snapshot, or an incomplete data extract.
*   **Lack of Explicit Primary Keys and Relationships:** The absence of explicitly defined primary keys and foreign key relationships within the provided table summary limits the ability to confidently ensure data integrity, prevent duplicate records, and understand how this table relates to other potential tables in the Track & Trace system. This requires inferring keys, which introduces potential for error.

### Appendix: Quick Reference

*   Convert `HarvesterZipCode` to string type.
*   Validate `HarvesterZipCode` against 5-digit and 9-digit US zip code formats.
*   Nullify `HarvesterZipCode` entries that cannot be corrected or are clearly invalid.
*   Acknowledge that `PkgYear` is uniformly '2025' and represents a specific temporal scope.
*   Note the inferred composite primary key for `packageqty25` as (`HarvesterLicenseNumber`, `ItemCategory`, `PkgYear`).

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred primary key for the `packageqty25` table and to confirm the proposed handling rules for the `HarvesterZipCode` anomalies. Additionally, any further context regarding the `PkgYear` (e.g., if this is a projection or a specific annual report) would be valuable for enhancing the dataset's documentation and ensuring its appropriate use. Please also confirm if any relationships to other tables are known.

# Work Documentation

## Table: packageqty25

**Data Operations:**
The data originating from `packageqty25.csv` is integrated into a broader dataset encompassing multiple years of package quantity data. Initially, `packageqty25.csv` is concatenated with `packageqty19-24.csv` and `packageqty23-24.csv` to form a comprehensive `package_df`. This combined dataset is then saved as `package.csv` and reloaded for further processing.

Key transformations include:
1.  **Column Renaming:** Several columns are renamed for consistency, converting PascalCase to snake_case (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` (from the original CSV `Year`) to `year`, `TotalPackagePounds` to `totalpackagepounds`). The `HarvesterZipCode` column is read as a string type during initial data loading, addressing the data type anomaly noted in the codebook.
2.  **Data Type Conversion:** The `year` and `totalpackagepounds` columns are converted to numeric data types, with any conversion errors being coerced to missing values.
3.  **Geographic Data Cleaning and Normalization:** The `harvestercounty` column undergoes extensive cleaning. This involves replacing "NA" and "UNDEFINED" values with empty strings, stripping leading/trailing whitespace, and then mapping various county name formats (e.g., "Alameda County") to a standardized uppercase format (e.g., "ALAMEDA") using a predefined mapping. After normalization, any remaining empty strings are converted to `pd.NA`, and rows with missing `harvestercounty` values are removed.
4.  **Data Integration (Merge):** The processed `package_df` is left-merged with a similarly processed `harvest_df` (containing harvest quantity data from multiple years) using `harvesterlicensenumber` and `year` as keys. This merge combines packaging and harvest information for each harvester and year.
5.  **Post-Merge County Resolution:** In the merged dataset, a unified `harvestercounty` column is created, prioritizing the county information from the harvest data (`harvestercounty_harv`) and falling back to the package data (`harvestercounty_pkg`) if the harvest county is missing.
6.  **Ratio Calculation:** New analytical columns are derived: `package_to_harvest_ratio` (total package pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), and `category_share` (which is calculated identically to `package_to_harvest_ratio`).
7.  **Final County Cleaning:** The `harvestercounty` column in the merged dataset undergoes another round of cleaning, replacing empty strings, "NA", and "nan" with `pd.NA`, followed by dropping rows with missing county values.
8.  **Aggregation:** The merged data is aggregated to create `category_summary` (by `harvestercounty`, `year`, `itemcategory`) and `county_summary` (by `harvestercounty`, `year`). These aggregations sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`. The `county_summary` is then exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`), `HarvesterFacilityType` (renamed to `harvesterfacilitytype`), `HarvesterCity` (renamed to `harvestercity`), `HarvesterZipCode` (renamed to `harvesterzipcode`, data type handled as string), `HarvesterCounty` (renamed to `harvestercounty`, values normalized and cleaned), `ItemCategory` (renamed to `itemcategory`), `PkgYear` (from original CSV `Year`, renamed to `year`, converted to numeric), `TotalPackagePounds` (renamed to `totalpackagepounds`, converted to numeric), `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Used in Aggregation:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (for mean calculation).

**Logic and Methodology:**
The primary intent of these operations is to prepare a comprehensive dataset for analyzing cannabis packaging and harvest activities across multiple years and geographic regions. By combining `packageqty` data from various years, the project aims to overcome the single-year limitation noted in the codebook for `packageqty25`. Renaming columns standardizes the dataset for easier programmatic access. Converting key metrics to numeric types enables quantitative analysis. The extensive cleaning and normalization of `harvestercounty` are crucial for accurate geographic segmentation and analysis, addressing inconsistencies in the raw data. Merging with harvest data allows for the calculation of important ratios, providing insights into the efficiency and relationship between harvest and packaging volumes. The final aggregations summarize these insights at different granularities (county, year, item category), facilitating higher-level reporting and visualization. The repeated cleaning steps for `harvestercounty` indicate a robust effort to ensure data quality for this critical categorical variable.

**Validation and Verification:**
The code includes several implicit validation steps:
*   **Data Type Handling:** The `HarvesterZipCode` column is explicitly read as a string type (`dtype=str`) during the initial loading of the CSV files. This prevents the `float64` data type issue identified in the codebook, ensuring zip codes are treated as categorical strings rather than numerical values. However, explicit validation of zip code formats (e.g., 5-digit or 9-digit US zip codes) and subsequent correction or nullification of invalid entries, as recommended in the codebook's "Reproducible Cleaning Plan," are not observed in the provided Python snippets.
*   **Data Type Coercion:** `pd.to_numeric(errors="coerce")` handles non-numeric values gracefully by converting them to `NaN`, which can then be identified and managed.
*   **Missing Value Handling:** Explicit `dropna(subset=[...])` calls are used after cleaning and merging steps to remove records where critical identifiers or geographic information (`harvestercounty`) are missing or unrecoverable.
*   **County Normalization:** The use of a `county_map` and subsequent stripping/replacement of empty strings serves as a form of data validation and standardization, ensuring consistency in county names.
*   **Merge Validation:** The `how="left"` merge ensures that all package records are retained, and `suffixes` help identify the origin of columns, which is useful for debugging and understanding data lineage.

**Results and Outcomes:**
The processing results in a cleaned, integrated, and enriched dataset (`merged`) that combines package and harvest quantities over several years. This dataset is then used to generate aggregated summaries (`category_summary` and `county_summary`), which are exported for further analysis and visualization. Specifically, `county_summary` is saved as `harvest_package_ratios.xlsx`, providing county- and year-level insights into total harvest pounds, total package pounds, and the package-to-harvest ratio. This prepared data forms the foundation for subsequent analyses, such as market concentration (HHI) calculations and trend visualizations, as seen in other parts of the provided Python code. The `packageqty25` data, originally a single-year snapshot, is now part of a multi-year, harmonized dataset, significantly expanding its analytical utility.