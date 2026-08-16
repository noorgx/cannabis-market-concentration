# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated package quantity information related to the Track & Trace project, likely within the regulated cannabis industry. It summarizes package data from licensed harvesters over several years. Each row in the `packageqty19-24` table represents the total package pounds and unique harvest batches for a specific harvester, item category, and year. The overall data source, collection period, and extraction date are not specified in the provided metadata.

**Assumptions:**
*   The data pertains to the regulated cannabis supply chain, given the "HarvesterLicenseNumber" and "Flower" item category.
*   "Pounds" refers to avoirdupois pounds.

### Table Inventory

*   **packageqty19-24**: Contains aggregated package quantity data from harvesters, categorized by item type and year.

## Table: packageqty19-24

*   **Purpose:** To provide a summary of package quantities processed by harvesters, broken down by item category and year, enabling analysis of production trends and volumes.
*   **What one row represents:** One row represents the aggregated total package pounds and unique harvest batches for a distinct combination of `HarvesterLicenseNumber`, `ItemCategory`, and `PkgYear`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` (composite key, inferred).
*   **Relationships:**
*   **Number of rows and columns:** 43827 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "string",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis harvester.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "string",
    "Units": "",
    "Description": "Type of license or facility operated by the harvester (e.g., Microbusiness License).",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "string",
    "Units": "",
    "Description": "City where the harvester's facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": "0.2",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation or flagging."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float",
    "Units": "",
    "Description": "Zip code of the harvester's facility.",
    "Allowed Values / Range": "[4000.0, 961503674.0]",
    "Missing %": "7.7",
    "Cleaning / Notes": "High missing percentage. The upper range value (961503674.0) is highly suspicious and likely indicates data entry errors or concatenated values, as it does not conform to standard US zip code formats. Investigate and validate against known zip code patterns; flag or nullify invalid entries. For missing values, consider imputation based on HarvesterCity/HarvesterCounty if a reliable mapping exists, otherwise flag."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "string",
    "Units": "",
    "Description": "County where the harvester's facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "1.7",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation or flagging."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "string",
    "Units": "",
    "Description": "Category of the cannabis item (e.g., Flower, Edible).",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "PkgYear",
    "Type": "integer",
    "Units": "Year",
    "Description": "Year the package quantity data pertains to.",
    "Allowed Values / Range": "[2019.0, 2024.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Ensure values are within the expected range of years."
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float",
    "Units": "Pounds",
    "Description": "Total weight of packages in pounds for the given category, harvester, and year.",
    "Allowed Values / Range": "[2.20462442018378e-07, 911433262.960458]",
    "Missing %": "0.0",
    "Cleaning / Notes": "The upper range value (911,433,262.96 pounds) is extremely large and highly suspicious, suggesting potential outliers or data entry errors. Investigate values exceeding a reasonable threshold (e.g., 99th percentile + 3*IQR) and consider flagging or capping extreme outliers. Ensure all values are non-negative."
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "integer",
    "Units": "Count",
    "Description": "Number of unique harvest batches contributing to the total package pounds.",
    "Allowed Values / Range": "[1.0, 8875.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Ensure values are positive integers."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `HarvesterZipCode` contains values outside of standard US zip code ranges and has a high missing percentage (7.7%).
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or non-standard formatting during data collection.
    *   **Recommended handling rule:** Validate `HarvesterZipCode` against a regex pattern for 5-digit or 5+4 digit US zip codes. Invalid entries should be flagged and potentially nullified. Missing values should be imputed based on `HarvesterCity` or `HarvesterCounty` if a reliable lookup table is available, otherwise flagged as 'Unknown' or left null.
*   **Issue:** `TotalPackagePounds` has an extremely large maximum value (over 900 million pounds).
    *   **Likely cause:** Data entry error, incorrect unit conversion, or an aggregation error during data generation.
    *   **Recommended handling rule:** Identify and investigate extreme outliers. Values significantly exceeding a statistically derived upper bound (e.g., 99th percentile + 3 times the interquartile range) should be flagged for review, potentially capped, or excluded from aggregate calculations if deemed erroneous.
*   **Issue:** Missing values in `HarvesterCity` (0.2%) and `HarvesterCounty` (1.7%).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** For these relatively small percentages, consider imputing with a placeholder like "Unknown" or "Not Provided" to maintain row integrity, or flag rows for further investigation if location data is critical.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to string type. Validate values against a standard US zip code pattern (e.g., `^\d{5}(-\d{4})?$`). For values that do not match, replace them with `NULL` and flag the row.
2.  **Handle Missing `HarvesterZipCode`:** For `HarvesterZipCode` values that are `NULL` (either originally missing or invalidated in step 1), attempt to impute using a reliable mapping from `HarvesterCity` and `HarvesterCounty` if available. If imputation is not possible, leave as `NULL` and flag the row for missing zip code.
3.  **Address Missing Location Data:** For missing values in `HarvesterCity` and `HarvesterCounty`, impute with the string "Unknown" to ensure consistency and prevent errors in downstream analysis.
4.  **Review `TotalPackagePounds` Outliers:** Identify and flag rows where `TotalPackagePounds` exceeds a statistically determined upper threshold (e.g., 99th percentile + 3*IQR). These flagged rows should be reviewed manually or excluded from analyses sensitive to extreme values.
5.  **Validate `TotalPackagePounds` Non-Negativity:** Ensure all `TotalPackagePounds` values are greater than or equal to zero. If any negative values are found, flag them as erroneous and replace with `NULL` or `0`.
6.  **Validate `UniqueHarvestBatches`:** Ensure all `UniqueHarvestBatches` values are positive integers. If any non-positive or non-integer values are found, flag them as erroneous and replace with `NULL`.

### Limitations & Trust Section

The reliability of geographical analysis based on `HarvesterZipCode` is limited due to the high percentage of missing values and the presence of invalid entries. The extreme upper range observed in `TotalPackagePounds` suggests potential data entry errors or anomalies that could skew aggregate statistics; trust in these maximum values is low without further investigation. The absence of explicit primary key definitions and relationships requires inference, which could lead to incorrect assumptions about data uniqueness and join capabilities. The lack of overall data source, collection period, and extraction date limits the ability to assess data freshness and context.

### Appendix: Quick Reference

*   **Zip Code Validation:** `HarvesterZipCode` values are validated against standard US zip code patterns; invalid entries are nullified.
*   **Missing Zip Codes:** Missing `HarvesterZipCode` values are imputed if possible via city/county, otherwise flagged.
*   **Location Imputation:** Missing `HarvesterCity` and `HarvesterCounty` values are replaced with "Unknown".
*   **Outlier Flagging:** Extreme `TotalPackagePounds` values are flagged for review.
*   **Non-Negative Checks:** `TotalPackagePounds` and `UniqueHarvestBatches` are validated to be non-negative.
*   **Inferred Keys:** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` are assumed to form a unique composite key.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary keys and relationships, as these were not explicitly provided in the source metadata. Particular attention should be paid to the proposed handling rules for `HarvesterZipCode` and `TotalPackagePounds` anomalies, ensuring they align with business requirements and data integrity standards. Additionally, confirmation of the data source, collection period, and extraction date would enhance the completeness and context of this codebook.

# Work Documentation

## Table: packageqty19-24

**Data Operations:**
*   **Data Ingestion and Concatenation:** Multiple CSV files (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were read into pandas DataFrames, treating all columns as strings to preserve original formatting. These were then concatenated into a single `package_df` and saved as `package.csv` for consistent access.
*   **Column Renaming:** Original column names (e.g., `HarvesterLicenseNumber`, `PkgYear`) were standardized to lowercase snake_case (e.g., `harvesterlicensenumber`, `year`) for improved readability and consistency.
*   **Data Type Conversion:** The `year` and `totalpackagepounds` columns were converted to numeric data types. Any values that could not be converted were coerced to `NaN` (Not a Number).
*   **Geographical Data Normalization:** The `harvestercounty` column underwent a multi-step cleaning and standardization process:
    *   Specific string values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined mapping (`county_map`) was applied to standardize various county name formats (e.g., "Alameda County" to "ALAMEDA").
    *   Rows with missing `harvestercounty` values were dropped from the DataFrame.
    *   The column was stripped of leading/trailing whitespace, and empty strings were replaced with `pd.NA`.
    *   Further rows with `pd.NA` in `harvestercounty` were dropped to ensure data quality for geographical analysis.
*   **Data Integration (Merge):** The `package_df` was left-merged with a `harvest_df` (which was similarly prepared from harvest quantity files) using `harvesterlicensenumber` and `year` as common keys. This merge enriched the package data with corresponding harvest information.
*   **Post-Merge County Resolution:** After the merge, a new `harvestercounty` column was created in the `merged` DataFrame. This column prioritized the county information from the `harvest_df` (if available) over the `package_df`'s county information, using the `fillna` method.
*   **Ratio Calculation:** Three new analytical columns were computed:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds` (from the `harvest_df`).
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. (Note: This calculation is identical to `package_to_harvest_ratio` in the provided script.)
*   **Final County Cleaning on Merged Data:** The `harvestercounty` column in the `merged` DataFrame underwent another round of cleaning, replacing empty strings, `<NA>`, and "nan" with `pd.NA`, followed by dropping rows with any remaining missing values in this column.
*   **Data Aggregation:**
    *   `category_summary`: The `merged` data was grouped by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, `package_to_harvest_ratio` was averaged, and `totalharvestpounds` was taken as the first observed value.
    *   `county_summary`: The `merged` data was grouped by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, and `totalharvestpounds` was taken as the first observed value. A `package_to_harvest_ratio` was then calculated at this aggregated level (sum of package pounds / sum of harvest pounds).
*   **Export:** The `county_summary` DataFrame, containing aggregated package and harvest ratios by county and year, was exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Original Columns:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `PkgYear`, `TotalPackagePounds`, `UniqueHarvestBatches`.
*   **Renamed Columns:** `harvesterlicensenumber`, `harvesterfacilitytype`, `harvestercity`, `harvesterzipcode`, `harvestercounty`, `itemcategory`, `year`, `totalpackagepounds`, `uniqueharvestbatches`.
*   **Type-Converted Columns:** `year` (to numeric), `totalpackagepounds` (to numeric).
*   **Cleaned/Normalized Columns:** `harvestercounty` (standardized names, missing values handled).
*   **New Columns Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share` (in the `merged` DataFrame).
*   **Aggregated Columns:** `totalpackagepounds` (summed), `totalharvestpounds` (first value), `package_to_harvest_ratio` (mean or re-calculated sum/sum).

**Logic and Methodology:**
The overarching goal of these data operations is to prepare, integrate, and summarize package quantity data with harvest quantity data to facilitate analytical insights into the cannabis supply chain.
1.  **Data Consolidation:** Combining package data from various annual files into a single, comprehensive dataset (`package_df`) ensures a holistic view of package quantities across the entire period of interest.
2.  **Data Standardization:** Renaming columns to a consistent, machine-readable format and converting key metrics (`year`, `totalpackagepounds`) to appropriate numeric types are fundamental steps for enabling accurate and efficient data processing and analysis.
3.  **Geographical Data Quality Assurance:** The extensive cleaning and normalization of the `harvestercounty` column are critical. Inconsistent or missing geographical data can severely hinder spatial analysis. By standardizing names and systematically dropping records with unresolvable missing county information, the integrity of location-based analysis is maintained.
4.  **Data Enrichment and KPI Generation:** Merging package data with harvest data allows for the creation of new, insightful metrics such as `package_to_harvest_ratio` and `dry_to_wet_ratio`. These ratios serve as key performance indicators (KPIs) for evaluating processing efficiency, yield, and the transformation of raw harvested material into packaged products.
5.  **Hierarchical Aggregation:** Aggregating the data at both `category` and `county` levels provides summarized views that are essential for high-level reporting and trend identification. This allows stakeholders to quickly understand production volumes, processing efficiency, and market dynamics across different product types and geographical regions.

**Validation and Verification:**
*   **Data Type Coercion:** The use of `errors="coerce"` during numeric type conversion for `year` and `totalpackagepounds` ensures that the script does not fail due to non-numeric entries. However, this implicitly converts problematic values to `NaN`, which necessitates explicit handling (e.g., dropping or imputing) in subsequent steps if these `NaN`s are not acceptable.
*   **Missing Value Handling:** The script explicitly addresses missing `harvestercounty` values by dropping affected rows at multiple stages of processing. This ensures that analyses relying on county information are performed on complete records.
*   **Merge Strategy:** The `left` merge with `harvest_df` ensures that all records from the `package_df` are retained, even if no matching harvest data is found. The post-merge logic for `harvestercounty` prioritizes the `harvest_df`'s county information, suggesting a preference for its accuracy or completeness.
*   **Implicit Duplicate Handling:** While `pd.concat` does not explicitly drop duplicates, the subsequent aggregation steps (`groupby().agg()`) will correctly sum or average values for identical grouping keys, effectively handling any potential duplicate rows within the aggregated context.

**Results and Outcomes:**
The data processing pipeline yields a robust, cleaned, and integrated dataset suitable for in-depth analysis of cannabis package and harvest quantities.
*   A consolidated `package_df` is created, combining package quantity data from multiple years into a single, unified source.
*   A `merged` DataFrame is generated, which integrates package and harvest information, providing a comprehensive view of the supply chain. This DataFrame is enriched with calculated ratios that offer insights into processing efficiency and yield.
*   Two aggregated summary tables, `category_summary` and `county_summary`, are produced. These tables offer summarized views of package and harvest data by geographical location, year, and item category, facilitating high-level trend analysis.
*   The `county_summary` is exported to `harvest_package_ratios.xlsx`, serving as a primary output for further analytical tasks and visualizations. This output enables stakeholders to monitor production trends, assess processing efficiency, and understand market dynamics across different counties and years.