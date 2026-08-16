# Track & Trace Data Codebook

### Overview Section

This dataset provides a summary of cannabis harvest quantities reported by licensed harvesters within the Track & Trace system. It offers insights into the volume of cannabis harvested, categorized by harvester details and year. Each row in the `harvestqty23-24` table represents a unique harvest record for a specific licensed harvester within a given year, detailing their reported harvest quantities. The data is sourced from the Track & Trace project, covering the collection period of 2023-2024. The extraction date is not available.

**Assumptions:**
*   Data reflects reported quantities as submitted to the Track & Trace system.
*   "Pounds" refer to avoirdupois pounds.

### Table Inventory

*   **harvestqty23-24**: Contains aggregated harvest quantity data for licensed harvesters for the years 2023 and 2024.

## Table: harvestqty23-24

*   **Purpose:** To track and summarize the total dry and wet harvest quantities, along with the number of unique harvest batches, for individual licensed cannabis harvesters over the years 2023 and 2024.
*   **What one row represents:** One aggregated harvest record for a specific licensed harvester (`HarvesterLicenseNumber`) in a particular `Year`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `Year` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 7500 rows, 9 columns

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "string",
    "Units": "",
    "Description": "Unique identifier for the harvester's license.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "string",
    "Units": "",
    "Description": "Type of facility associated with the harvester's license (e.g., Cannabis - Microbusiness License).",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "string",
    "Units": "",
    "Description": "City where the harvester facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": 0.1,
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging for records without a city."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "numeric",
    "Units": "",
    "Description": "Zip code of the harvester facility.",
    "Allowed Values / Range": "Range: [4000.0, 961503674.0]",
    "Missing %": 5.5,
    "Cleaning / Notes": "Missing values present. The upper range value (961503674.0) appears to be an invalid zip code format, suggesting potential data entry errors or concatenated values. Recommend validating against standard 5-digit or 9-digit zip code formats and correcting or flagging anomalies."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "string",
    "Units": "",
    "Description": "County where the harvester facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": 0.1,
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging for records without a county."
  },
  {
    "Column Name": "Year",
    "Type": "integer",
    "Units": "",
    "Description": "Year of the harvest record.",
    "Allowed Values / Range": "Range: [2023.0, 2024.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "numeric",
    "Units": "pounds",
    "Description": "Total dry weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [-380.53733377132, 785406.9175]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. These are physically impossible for harvest quantities and likely represent data entry errors, returns, or adjustments not properly recorded. Recommend flagging these records and treating negative values as zero for aggregate analysis, or excluding them if the context requires strictly positive harvest data."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "numeric",
    "Units": "pounds",
    "Description": "Total wet weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [0.75, 4440808.26822343]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "integer",
    "Units": "batches",
    "Description": "Number of unique harvest batches recorded.",
    "Allowed Values / Range": "Range: [1.0, 1360.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry errors, misinterpretation of returns/adjustments, or system glitches allowing negative quantities to be recorded. Physically, a harvest quantity cannot be negative.
    *   **Recommended handling rule:** Flag records where `TotalHarvestPounds` is negative. For analytical purposes, these values should be treated as zero or excluded, depending on the specific analysis. Further investigation into the source system or business rules for returns/adjustments is recommended.
*   **Issue:** Anomalously large `HarvesterZipCode` values.
    *   **Likely cause:** Data entry errors, concatenation of multiple numbers, or incorrect data type mapping during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Flag zip codes that exceed the standard 5 or 9-digit format. Attempt to parse or correct these values if a clear pattern for error is identified (e.g., leading zeros removed, concatenated values). Otherwise, treat as invalid or missing.
*   **Issue:** Missing values in `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty`.
    *   **Likely cause:** Incomplete data entry during registration or reporting.
    *   **Recommended handling rule:** Flag records with missing geographical information. For analysis requiring complete location data, these records may need to be excluded or imputed if a reliable method (e.g., using other known location data for the license) is available.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Quantities:** Identify all records where `TotalHarvestPounds` is less than zero. Create a new flag column, `is_negative_harvest_pounds`, set to `TRUE` for these records. For subsequent analysis, replace negative `TotalHarvestPounds` values with `0`.
2.  **Validate Zip Codes:** For `HarvesterZipCode`, convert to string format and identify values that do not conform to 5-digit or 9-digit (e.g., 'XXXXX-XXXX') US zip code patterns. Create a flag column, `is_invalid_zip_code`, for these records. Consider setting non-conforming zip codes to `NULL` for consistency.
3.  **Handle Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, identify records with missing values. Create flag columns, `is_missing_city` and `is_missing_county`, respectively. These records should be noted for potential bias in location-based analyses.

### Limitations & Trust Section

*   **Negative `TotalHarvestPounds`:** The presence of negative harvest quantities significantly impacts the reliability of total harvest volume calculations. Without clarification from the data source, these values are untrustworthy for direct summation and require specific handling. Validation is needed to understand the business logic behind such entries.
*   **Invalid `HarvesterZipCode`:** The range of `HarvesterZipCode` suggests potential data quality issues beyond simple missingness. The extremely large values indicate a need for external validation against a comprehensive list of valid zip codes or direct consultation with the data source to understand the input format.
*   **Missing Geographical Data:** The small percentage of missing `HarvesterCity` and `HarvesterCounty` values could lead to minor inaccuracies in geographically segmented analyses. Validation would involve cross-referencing with other license information or external geographical databases.

### Appendix: Quick Reference

*   **Negative Harvest Pounds:** Treat as `0` for aggregate analysis; flag original values for investigation.
*   **Invalid Zip Codes:** Flag non-standard zip codes; consider nullifying or correcting based on validation.
*   **Missing City/County:** Flag records with missing geographical data; exclude from location-specific analyses if imputation is not feasible.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for pattern matching before any numeric operations.
*   **Primary Key:** `HarvesterLicenseNumber` and `Year` form the composite primary key for unique identification of harvest records.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for pattern matching before any numeric operations.
*   **Primary Key:** `HarvesterLicenseNumber` and `Year` form the composite primary key for unique identification of harvest records.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies, especially concerning the negative `TotalHarvestPounds` and the anomalous `HarvesterZipCode` values. Confirmation of the primary key assumption (`HarvesterLicenseNumber`, `Year`) is also crucial. Additionally, any insights into the business context that might explain the observed data quality issues would be highly valuable for refining the cleaning plan and enhancing data trust.

# Work Documentation

## Table: harvestqty23-24

**Data Operations:**
The `harvestqty23-24` dataset was integrated with other harvest quantity files (`harvestqty19-24.csv` and `harvestqty25.csv`) to create a comprehensive `harvest_df`. This combined dataset was then saved as `Data/Track and Trace Data/Harvest/harvest.csv`. Subsequent operations were performed on this consolidated `harvest_df`.

The following transformations were applied:
*   **Column Renaming:** Original column names were standardized to lowercase (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`).
*   **Data Type Conversion:** The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric data types, with any conversion errors resulting in missing values.
*   **Geographical Data Normalization:** The `harvestercounty` column underwent extensive cleaning. This involved replacing "NA" and "UNDEFINED" strings with empty strings, standardizing various county name formats (e.g., "Alameda County") to a consistent uppercase format (e.g., "ALAMEDA") using a predefined mapping, stripping leading/trailing whitespace, and removing " County" suffixes (case-insensitively).
*   **Missing Value Handling:** Rows with missing values in `harvestercounty` were dropped at multiple stages of the cleaning process to ensure data completeness for geographical analysis.
*   **Data Merging:** The processed `harvest_df` was left-merged with a `package_df` (derived from `packageqty` files, which also underwent similar cleaning) using `harvesterlicensenumber` and `year` as keys.
*   **County Resolution Post-Merge:** A unified `harvestercounty` column was established in the merged dataset. Values from the harvest data (`harvestercounty_harv`) were prioritized, falling back to package data (`harvestercounty_pkg`) if harvest data was missing.
*   **Ratio Calculation:** Several new analytical variables were computed:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds` (this variable's specific use in aggregation suggests it might represent a share within a category).
*   **Aggregation:** The merged data was aggregated at two distinct levels:
    *   **Category-level Summary:** Grouped by `harvestercounty`, `year`, and `itemcategory` to sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`.
    *   **County-level Summary:** Grouped by `harvestercounty` and `year` to sum `totalpackagepounds` and calculate the `package_to_harvest_ratio`.
*   **Output Generation:** The county-level summary was exported to an Excel file named `Data/Results/harvest_package_ratios.xlsx`.
*   **Visualization Preparation:** The county-level summary was utilized to identify the top 10 counties based on total harvest pounds. Time-series bar plots were then generated to visualize trends in total harvest pounds, total package pounds, and package-to-harvest ratios for these top counties across different years.

**Variables Affected:**
*   **Renamed:** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype`), `HarvesterCity` (to `harvestercity`), `HarvesterZipCode` (to `harvesterzipcode`), `HarvesterCounty` (to `harvestercounty`), `PkgYear` (to `year`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches`).
*   **Modified/Cleaned:** `year` (converted to numeric), `totalharvestpounds` (converted to numeric), `totalharvestwetpounds` (converted to numeric), `harvestercounty` (normalized, missing values handled, unified post-merge).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Aggregated:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (in `category_summary` and `county_summary`).

**Logic and Methodology:**
The core methodology involved consolidating harvest data from various periods, standardizing key identifiers, and enriching it by integrating package data. The intent was to create a robust dataset suitable for analyzing the flow of cannabis from harvest to packaging. Standardization of column names and data types ensured consistency, while extensive geographical data normalization addressed inconsistencies critical for location-based analysis. Merging with package data enabled the calculation of efficiency metrics like package-to-harvest and dry-to-wet ratios. Aggregations at both category and county levels were performed to facilitate macro-level insights into market dynamics and regional performance. The iterative cleaning of geographical data, including dropping rows with missing values, indicates a preference for complete and accurate location information in the final analytical outputs.

**Validation and Verification:**
*   Data type conversions for numeric fields (`year`, `totalharvestpounds`, `totalharvestwetpounds`) used an `errors="coerce"` argument, which automatically converted unparseable values to `NaN`, implicitly flagging data quality issues.
*   Explicit dropping of rows with missing `harvestercounty` values at multiple stages served as a form of data validation, ensuring that subsequent analyses are based on records with complete geographical information.
*   The calculation of ratios (`package_to_harvest_ratio`, `dry_to_wet_ratio`) implicitly relies on non-zero denominators, which would highlight potential issues if division by zero occurred (though not explicitly handled in the provided snippets).
*   The final visualization steps, which plot aggregated data for top counties, provide a high-level visual verification of the processed data's trends and distributions.

**Results and Outcomes:**
The data work resulted in a consolidated and cleaned dataset of cannabis harvest and package quantities. Key outcomes include:
*   A unified `harvest.csv` file, combining harvest data from 2019-2025.
*   Standardized and cleaned geographical information, particularly for `harvestercounty`, enhancing the reliability of location-based analyses.
*   A merged dataset (`merged`) that links harvest and package records, enriched with calculated ratios providing insights into processing efficiency.
*   Aggregated summary tables at both category and county levels, offering a structured view of harvest and package volumes and their interrelationships.
*   An Excel export (`harvest_package_ratios.xlsx`) containing county-level summaries, ready for further reporting.
*   A series of visualizations depicting trends in harvest pounds, package pounds, and package-to-harvest ratios for the top 10 counties, facilitating quick insights into regional performance.