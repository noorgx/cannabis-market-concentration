# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated package quantity and harvest batch information for licensed cannabis harvesters within the Track & Trace system. It offers insights into the volume of packaged cannabis products and the diversity of harvest batches associated with individual licensees. Each row in the `packageqty23-24` table represents the aggregated total package pounds and unique harvest batches for a specific harvester, item category, and year. The data is derived from a regulatory Track & Trace system, covering the period from 2023 to 2024. The exact extraction date is not available.

**Assumptions:**
*   Data is aggregated at the `HarvesterLicenseNumber`, `ItemCategory`, and `Year` level.
*   `TotalPackagePounds` represents the cumulative weight of all packages for the given aggregation keys.
*   `UniqueHarvestBatches` counts distinct harvest identifiers associated with the packages.

### Table Inventory

*   **`packageqty23-24`**: Contains aggregated data on total package pounds and unique harvest batches for licensed harvesters in 2023 and 2024.

## Table: packageqty23-24

*   **Purpose:** To provide an overview of the total packaged weight and the number of unique harvest batches associated with individual licensed cannabis harvesters for specific product categories and years.
*   **What one row represents:** One row represents the aggregated total package pounds and unique harvest batches for a specific `HarvesterLicenseNumber`, `ItemCategory`, and `Year`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `Year` (composite key).
*   **Relationships:** `HarvesterLicenseNumber` likely serves as a foreign key linking to a master table of licensed harvesters.
*   **Number of rows and columns:** 11869 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis harvester.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility or license held by the harvester.",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester's licensed facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": "0.1",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation from HarvesterZipCode or HarvesterLicenseNumber if a master facility table is available, or flag for review."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester's licensed facility.",
    "Allowed Values / Range": "Range: [4000.0, 961503674.0]. Example: 96150.0",
    "Missing %": "5.5",
    "Cleaning / Notes": "Significant percentage of missing values. The maximum value (961503674.0) is an anomalous, non-standard zip code, likely a data entry error or concatenation. Values outside of standard 5-digit or 9-digit zip code formats should be flagged or set to null. Imputation from HarvesterCity or HarvesterLicenseNumber should be considered."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester's licensed facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "0.1",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation from HarvesterZipCode or HarvesterLicenseNumber if a master facility table is available, or flag for review."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product being packaged.",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Year",
    "Type": "int64",
    "Units": "",
    "Description": "Calendar year for which the data is aggregated.",
    "Allowed Values / Range": "Range: [2023.0, 2024.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "pounds",
    "Description": "Total weight of all packages in pounds for the given aggregation.",
    "Allowed Values / Range": "Range: [0.0, 819416.794]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 pounds may indicate no packages or data entry issues. Investigate if 0.0 is a valid state or an anomaly."
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "",
    "Description": "Number of distinct harvest batches contributing to the packages.",
    "Allowed Values / Range": "Range: [1.0, 1110.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0 or null would indicate an anomaly, but the current range starts at 1.0, suggesting all entries have at least one batch."
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `packageqty23-24` table.

*   **Issue:** Missing `HarvesterCity` and `HarvesterCounty` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For the small percentage (0.1%) of missing values, consider imputation from other geographical identifiers (e.g., `HarvesterZipCode`) if a reliable mapping exists, or from a master facility table using `HarvesterLicenseNumber`. If imputation is not feasible or reliable, these rows should be flagged for review or excluded from analyses requiring complete location data.
*   **Issue:** Missing `HarvesterZipCode` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For the 5.5% missing values, imputation from `HarvesterCity` or `HarvesterCounty` (if available and reliable) or a master facility table is recommended. If imputation is not possible, flag these rows.
*   **Issue:** Anomalous `HarvesterZipCode` values (e.g., `961503674.0`).
    *   **Likely cause:** Data entry error, concatenation of multiple zip codes, or incorrect data type conversion during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Identify and flag or nullify `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit (ZIP+4) numeric formats. Further investigation may be needed to determine if these can be corrected or if they represent a systemic data entry problem.
*   **Issue:** `TotalPackagePounds` values of 0.0.
    *   **Likely cause:** Could represent periods of no packaging activity, or potentially data entry errors where a non-zero value should have been recorded.
    *   **Recommended handling rule:** Investigate the business context for 0.0 values. If 0.0 is a valid representation of no activity, no specific cleaning is required beyond understanding its meaning. If it indicates an error, these rows should be flagged or excluded from analyses where non-zero package quantities are expected.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to a string type to handle potential leading zeros and non-numeric entries. Identify and flag or nullify entries that do not conform to 5-digit or 9-digit numeric patterns (e.g., using regular expressions).
2.  **Impute Missing Location Data:** For missing `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty`, attempt to impute values using a hierarchical approach. Prioritize imputation from a master facility table using `HarvesterLicenseNumber` if available. Otherwise, use `HarvesterZipCode` to infer `HarvesterCity` and `HarvesterCounty`, or vice-versa, based on a reliable geographical lookup table.
3.  **Flag Imputed Values:** Create new boolean flag columns (e.g., `HarvesterCity_Imputed`, `HarvesterZipCode_Cleaned`) to indicate rows where data was imputed or corrected, allowing for transparency and traceability.
4.  **Review `TotalPackagePounds` = 0:** Analyze rows where `TotalPackagePounds` is 0.0 to understand if these represent legitimate zero activity or potential data errors. Depending on the finding, either document this as a valid state or flag these rows for further investigation or exclusion from specific analyses.

### Limitations & Trust Section

The reliability of geographical data (`HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`) is compromised by missing values and anomalous entries in `HarvesterZipCode`. This limits the ability to perform accurate location-based analyses without significant data cleaning and potential imputation. Validation of these fields would require cross-referencing with an authoritative master list of licensed facilities and their addresses, ideally provided by the regulatory body. Without such a master list, any imputation carries a degree of uncertainty. The interpretation of `TotalPackagePounds` values of 0.0 also requires further business context validation to ensure accurate representation of harvester activity.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Non-standard `HarvesterZipCode` values (e.g., > 5 or 9 digits, non-numeric) are flagged or nullified.
*   **Missing Location Imputation:** Missing `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty` are imputed using available geographical data or a master facility list.
*   **Imputation Flags:** New columns are added to explicitly mark imputed or cleaned data points.
*   **Zero Package Pounds:** Rows with `TotalPackagePounds = 0.0` are reviewed for business context; flagged if anomalous.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies, particularly concerning the `HarvesterZipCode` and missing location data. Specific attention should be paid to the assumptions made regarding the aggregation level and the interpretation of `TotalPackagePounds`. Validation against source system documentation or subject matter experts is recommended to ensure the codebook accurately reflects the data's true nature and intended use.

# Work Documentation

## Table: packageqty23-24

**Data Operations:**
The `packageqty23-24` dataset was integrated as part of a broader data consolidation effort. Initially, multiple package quantity datasets, including `packageqty19-24.csv`, `packageqty23-24.csv`, and `packageqty25.csv`, were loaded and concatenated into a single master package dataframe. This consolidated dataset underwent several cleaning and transformation steps. Key columns such as `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, and `UniqueHarvestBatches` were systematically renamed to a consistent lowercase format. Data types for `Year` and `TotalPackagePounds` were converted from string to numeric, with a mechanism to coerce invalid entries to missing values.

A significant portion of the work focused on standardizing and cleaning the `harvestercounty` column. This involved applying a predefined mapping to normalize county names (e.g., converting "X County" to "X"), stripping extraneous whitespace, and replacing various representations of missing data (empty strings, "NA") with standard missing value indicators. Rows where `harvestercounty` remained missing after these initial cleaning steps were subsequently removed.

The cleaned package data was then integrated with a separate harvest dataset through a left merge operation, using `harvesterlicensenumber` and `year` as the common keys. This merge enriched the package data with corresponding harvest information. During this integration, a strategy was implemented to resolve potential discrepancies or missingness in the `harvestercounty` column, prioritizing the county information from the harvest dataset when available, and falling back to the package dataset's value otherwise.

Following the merge, new ratio-based metrics were calculated to provide deeper insights into the relationship between package and harvest quantities. These included `package_to_harvest_ratio` (total package pounds divided by total harvest pounds) and `category_share` (which was calculated identically to `package_to_harvest_ratio`). Further cleaning and dropping of rows with missing `harvestercounty` values were performed on the merged dataset to ensure data integrity for subsequent aggregations.

Finally, the integrated data was aggregated at two distinct levels: a category-level summary (grouped by `harvestercounty`, `year`, and `itemcategory`) and a county-level summary (grouped by `harvestercounty` and `year`). These aggregations involved summing `totalpackagepounds` and calculating the mean or recalculating `package_to_harvest_ratio`. The resulting county-level summary was then exported to an Excel file for further analysis and visualization.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, `UniqueHarvestBatches` were all renamed to their lowercase equivalents. The data types of `Year` and `TotalPackagePounds` were converted to numeric. The values within `HarvesterCounty` were standardized and cleaned, and rows with missing `harvestercounty` were removed.
*   **Created:** New variables `package_to_harvest_ratio` and `category_share` were computed. The `dry_to_wet_ratio` was also created, though it primarily utilized variables from the merged harvest dataset. Aggregated columns such as summed `totalpackagepounds` and mean/recalculated `package_to_harvest_ratio` were generated in the summary tables.
*   **Validated/Filtered:** Rows containing missing or inconsistent `harvestercounty` values were identified and removed at multiple stages of the data processing pipeline.

**Logic and Methodology:**
The overarching objective of the data work was to create a robust and analytically ready dataset by consolidating package quantity information across different years and integrating it with relevant harvest data. The methodology involved a systematic approach to data cleaning, standardization, and transformation. Column renaming ensured consistency and ease of use. Explicit data type conversions, with error handling, were crucial for enabling accurate numerical computations.

The extensive cleaning of the `harvestercounty` variable was a critical step, addressing known data quality issues related to geographical identifiers. This iterative cleaning process, including mapping, stripping, and dropping missing values, aimed to maximize the reliability of location-based analyses. The integration with harvest data through a left merge was fundamental to deriving new, insightful metrics that link packaging output to cultivation input. The conflict resolution strategy for `harvestercounty` during the merge aimed to preserve the most reliable geographical information.

The creation of ratio-based features like `package_to_harvest_ratio` was designed to provide a normalized view of packaging efficiency, allowing for comparisons across different harvesters, categories, and years. The final aggregation steps were performed to summarize these key metrics at meaningful geographical and categorical levels, preparing the data for higher-level reporting, trend analysis, and visualization.

**Validation and Verification:**
Data type conversions included error coercion, which implicitly validates input by converting unparseable values to `NaN`, preventing downstream computational errors. The repeated application of `dropna` on the `harvestercounty` column served as an explicit validation step, ensuring that all records used in subsequent analyses had complete geographical information. While the merge operation for `package_df` did not explicitly use the `validate` argument, the careful handling of `harvestercounty` conflicts post-merge indicates an awareness of potential data integrity issues. The consistency of county names was enforced through a mapping dictionary, providing a form of lookup-based validation.

**Results and Outcomes:**
The data work resulted in a comprehensive and cleaned dataset that combines package quantity and harvest information across multiple years. This integrated dataset is suitable for analyzing trends in packaging activity, assessing the efficiency of converting harvested material into packaged products, and understanding market dynamics at various geographical and categorical levels. Specifically, the creation of `package_to_harvest_ratio` and aggregated summary tables provides valuable metrics for performance evaluation and strategic decision-making. The final export of the county-level summary to an Excel file facilitates direct use in reports and dashboards, enabling stakeholders to easily access and interpret key insights.