# Track & Trace Data Codebook

### Overview Section

This dataset provides information related to the "Track & Trace" project, which aims to monitor and record the movement of specific items or packages through a supply chain. The data primarily focuses on package-level details, including information about the harvester, item category, and package weight. Each row in the `package` table represents a unique package record, detailing its attributes and origin. The overall data source is from the Track & Trace system. Specific collection periods and extraction dates are not provided in the current summary.

**Assumptions:**
*   The `HarvesterLicenseNumber` uniquely identifies a harvester.
*   `TotalPackagePounds` represents the weight of the package in avoirdupois pounds.

### Table Inventory

*   **package:** Contains detailed records for individual packages, including harvester information, item category, and package weight.

## Table: package

*   **Purpose:** To track individual packages, their contents, and associated harvester details within the Track & Trace system.
*   **What one row represents:** One unique package record.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 59821 rows, 10 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the harvester's license.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the harvester.",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": "0.2",
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging if critical for analysis."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester facility.",
    "Allowed Values / Range": "Range: [4000.0, 961503674.0]",
    "Missing %": "7.0",
    "Cleaning / Notes": "Significant missing values. Data type is float64, suggesting potential issues with leading zeros or non-standard formats. The upper range value (961503674.0) is anomalous for a standard US zip code (typically 5 or 9 digits). Values outside of typical 5-digit or 9-digit zip code formats should be investigated and potentially corrected or flagged."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "1.3",
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging if critical for analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the item contained within the package.",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "PkgYear",
    "Type": "float64",
    "Units": "year",
    "Description": "Year the package was created or recorded.",
    "Allowed Values / Range": "Range: [2019.0, 2025.0]",
    "Missing %": "19.8",
    "Cleaning / Notes": "High percentage of missing values. Data type is float64, which should be converted to integer if representing a year. Missing values need to be addressed, potentially by imputation or exclusion depending on analytical requirements."
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "pounds",
    "Description": "Total weight of the package in pounds.",
    "Allowed Values / Range": "Range: [0.0, 911433262.960458]",
    "Missing %": "0.0",
    "Cleaning / Notes": "The maximum value (911,433,262.96 pounds) is extremely large and warrants investigation for potential data entry errors or unit conversion issues. Values of 0.0 pounds may represent empty packages or data anomalies."
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "count",
    "Description": "Number of unique harvest batches contributing to the package.",
    "Allowed Values / Range": "Range: [1.0, 8875.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Year",
    "Type": "float64",
    "Units": "year",
    "Description": "General year associated with the package record.",
    "Allowed Values / Range": "Range: [2023.0, 2024.0]",
    "Missing %": "80.2",
    "Cleaning / Notes": "Extremely high percentage of missing values. This column is largely incomplete and may not be suitable for direct analysis without significant imputation or external data sources. Data type is float64, which should be converted to integer if representing a year. Consider if this column is redundant with 'PkgYear' or if it serves a different purpose."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** High percentage of missing values in `Year` (80.2%) and `PkgYear` (19.8%).
    *   **Likely cause:** Incomplete data entry, data extraction issues, or the field was not consistently mandatory.
    *   **Recommended handling rule:** For `Year`, due to extreme missingness, consider excluding it from most analyses or using it only where non-missing. For `PkgYear`, impute missing values if a reasonable method (e.g., mode, nearest valid date) can be determined, or flag records with missing values for exclusion in time-series analyses.
*   **Issue:** Anomalous `HarvesterZipCode` values, specifically the maximum value (961503674.0) and float64 data type.
    *   **Likely cause:** Data entry errors, incorrect data type conversion during extraction, or inclusion of non-standard zip code formats.
    *   **Recommended handling rule:** Convert `HarvesterZipCode` to string/object type to preserve leading zeros. Filter out or flag zip codes that do not conform to standard 5-digit or 9-digit (ZIP+4) US formats. Investigate the extremely large values for potential misinterpretation or corruption.
*   **Issue:** Missing values in `HarvesterCity` (0.2%) and `HarvesterCounty` (1.3%).
    *   **Likely cause:** Minor data entry omissions.
    *   **Recommended handling rule:** For `HarvesterCity` and `HarvesterCounty`, consider imputing missing values based on `HarvesterZipCode` (if cleaned) or `HarvesterLicenseNumber` if a consistent mapping exists. Alternatively, flag these records or exclude them from analyses requiring complete geographical information.
*   **Issue:** Extremely large `TotalPackagePounds` value (911,433,262.96 pounds).
    *   **Likely cause:** Data entry error, unit conversion mistake (e.g., grams entered as pounds), or an outlier representing an aggregation rather than a single package.
    *   **Recommended handling rule:** Investigate the source of this extreme outlier. If it's an error, correct it or exclude the record. If it represents a valid, albeit unusual, aggregation, document its meaning and consider winsorization or transformation for statistical analyses to mitigate its impact.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to a string data type to preserve leading zeros. Identify and flag or remove entries that do not conform to standard 5-digit or 9-digit US zip code formats, especially the anomalous large values.
2.  **Address Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, attempt to impute missing values using a lookup table based on the cleaned `HarvesterZipCode` or `HarvesterLicenseNumber`. If imputation is not feasible or reliable, flag these records.
3.  **Clean `PkgYear` and `Year`:** Convert `PkgYear` and `Year` to integer data types. For `PkgYear`, impute missing values using a suitable method (e.g., mode, or a derived value if a date column is available). For `Year`, given its high missingness, evaluate its utility; if not critical, consider dropping the column or using it only for records where it is present.
4.  **Investigate `TotalPackagePounds` Outliers:** Review records with `TotalPackagePounds` exceeding a reasonable threshold (e.g., several standard deviations above the mean or a domain-specific maximum). Correct identified data entry errors or flag these records for special handling in analyses.
5.  **Validate `TotalPackagePounds` Zero Values:** Investigate records where `TotalPackagePounds` is 0.0 to determine if these represent empty packages, errors, or specific operational states.

### Limitations & Trust Section

The reliability of the `Year` column is severely compromised due to over 80% missing values, making it unsuitable for most analytical purposes without extensive imputation or external validation. The `HarvesterZipCode` column contains anomalous values and an incorrect data type, requiring significant cleaning to ensure geographical accuracy. The extreme outlier in `TotalPackagePounds` raises concerns about data entry accuracy or unit consistency, necessitating validation against source systems or domain experts. Trust in analyses relying heavily on these specific fields should be tempered until these data quality issues are thoroughly addressed and validated.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Convert `HarvesterZipCode` to string; validate against 5/9-digit US formats.
*   **Year Imputation:** Impute `PkgYear` missing values; `Year` column has high missingness, use with caution.
*   **Outlier Detection:** Investigate extreme `TotalPackagePounds` values for data entry errors.
*   **Geographical Imputation:** Use `HarvesterZipCode` to impute `HarvesterCity` and `HarvesterCounty` where possible.
*   **Data Type Correction:** Convert `PkgYear` and `Year` from float64 to integer.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions and proposed cleaning rules, particularly for `HarvesterZipCode` and `TotalPackagePounds` where anomalies were identified. Specific attention should be paid to the handling of missing values in `PkgYear` and `Year` to ensure that the proposed approach aligns with analytical objectives. Validation of the assumed units for `TotalPackagePounds` and the interpretation of `PkgYear` vs. `Year` is also crucial.

# Work Documentation

## Table: package

**Data Operations:**
The `package` table data was sourced from multiple CSV files (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`), which were concatenated into a single dataframe. This combined dataset was then saved as `package.csv` and re-loaded for processing. Initial loading treated all columns as strings to preserve original formats.

Key cleaning and transformation steps included:
*   **Column Renaming:** Original column names were converted to a consistent lowercase snake_case format (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`).
*   **Data Type Conversion:** The `Year` and `TotalPackagePounds` columns were converted to numeric data types. Non-numeric values encountered during this conversion were coerced to missing values (NaN).
*   **Geographical Data Normalization:** The `harvestercounty` column underwent a standardization process using a predefined mapping (`county_map`) to ensure consistency in county names.
*   **Missing Value Handling:** Rows with missing values in the `harvestercounty` column were removed from the dataset at multiple stages of processing. Empty strings, "NA", and "nan" values in `harvestercounty` were explicitly replaced with `pd.NA` before dropping rows.
*   **Data Integration:** The `package` data was left-merged with a `harvest_df` (harvest data) using `harvesterlicensenumber` and `year` as keys. This enriched the package records with corresponding harvest information.
*   **Consolidation of Geographical Data:** After merging, the `harvestercounty` column was consolidated, prioritizing the county information from the harvest data if available, otherwise defaulting to the package data's county.
*   **Feature Engineering:** Several new ratio metrics were calculated: `package_to_harvest_ratio` (total package pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), and `category_share` (total package pounds divided by total harvest pounds).
*   **Aggregation:** The processed data was aggregated into two summary tables: `category_summary` (grouped by `harvestercounty`, `year`, and `itemcategory`) and `county_summary` (grouped by `harvestercounty` and `year`). These aggregations involved summing `totalpackagepounds`, taking the first `totalharvestpounds` value, and calculating the mean `package_to_harvest_ratio` for `category_summary`, and summing `totalpackagepounds` and taking the first `totalharvestpounds` for `county_summary` with a re-calculated `package_to_harvest_ratio`.
*   **Export:** The `county_summary` dataframe was exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, `UniqueHarvestBatches` were all renamed to their lowercase snake_case equivalents.
*   **Data Type Changed:** `year` (from string to numeric), `totalpackagepounds` (from string to numeric).
*   **Modified/Cleaned:** `harvestercounty` (values normalized, missing values handled).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share` (new calculated metrics).
*   **Aggregated:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (in the `category_summary` and `county_summary` tables).

**Logic and Methodology:**
The data work on the `package` table aimed to consolidate raw package data from various periods, standardize its structure, and integrate it with related harvest information. The initial loading as strings ensured no data loss due to incorrect type inference. Renaming columns provided consistency, while converting `year` and `totalpackagepounds` to numeric types enabled quantitative analysis. The `errors='coerce'` argument in numeric conversions is a pragmatic approach to handle data quality issues by converting problematic entries to `NaN` rather than halting execution.

A significant part of the methodology focused on cleaning and standardizing geographical data (`harvestercounty`) to ensure accurate spatial analysis and consistent aggregation. The repeated dropping of rows with missing county information indicates a strong requirement for complete geographical context for downstream analysis.

Merging with harvest data was crucial for enriching the package records and enabling the calculation of derived metrics like `package_to_harvest_ratio`, which provides insights into the efficiency of converting harvested material into packaged products. The aggregation steps were designed to summarize key metrics at different levels of granularity (county, year, item category), facilitating high-level reporting and trend analysis. The final export of the `county_summary` table makes this aggregated data readily available for further use.

**Validation and Verification:**
*   **Data Type Validation:** Explicit conversion of `year` and `totalpackagepounds` to numeric types, using `errors='coerce'`, serves as a form of validation, identifying and isolating non-conforming entries as `NaN`.
*   **Missing Data Handling:** The repeated use of `dropna(subset=["harvestercounty"])` and replacement of various missing value representations (`""`, "NA", "nan", "<NA>") with `pd.NA` demonstrates a consistent approach to managing and verifying the completeness of critical geographical data.
*   **Lookup-based Standardization:** The application of a `county_map` to `harvestercounty` acts as a lookup-based validation, ensuring that county names conform to a predefined set of standardized values.
*   **Merge Integrity:** While the `validate` argument was not explicitly used in the `package_df` merge, the choice of a left merge implies that all package records are retained, and harvest data is added where a match exists, preserving the primary focus on package information.

**Results and Outcomes:**
The data work resulted in a clean, standardized, and enriched `package` dataset.
*   The `package_df` is now a consolidated source of package information across multiple years, with consistent column names and appropriate data types for `year` and `totalpackagepounds`.
*   The `harvestercounty` column is standardized and free of missing values, enabling reliable geographical analysis.
*   The `merged` dataframe provides a comprehensive view by integrating package details with harvest data, allowing for a more holistic understanding of the supply chain.
*   New analytical features, such as `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`, are available for deeper insights into operational efficiency and product flow.
*   Two aggregated summary tables (`category_summary` and `county_summary`) are generated, offering pre-computed metrics for high-level analysis and reporting.
*   A final Excel output (`harvest_package_ratios.xlsx`) provides a ready-to-use summary of package-to-harvest ratios by county and year.