# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated information related to cannabis harvest and packaging activities within the Track & Trace system, specifically covering the years 2023 and 2024. It aims to offer insights into the volume of cannabis processed by licensed harvesters, categorized by item type. Each row in the `harvestpackagemerge23-24` table represents an aggregated summary of harvest and package data for a specific harvester and item category within a given year. The overall data source is the Track & Trace system, with data collected during the 2023-2024 period. The exact extraction date is not specified.

**Assumptions:**
*   The table name `harvestpackagemerge23-24` indicates that the data covers activities from the years 2023 and 2024.
*   "Pounds" is the implied unit for all weight-related columns (`TotalPackagePounds`, `TotalHarvestPounds`, `TotalHarvestWetPounds`).
*   Harvester information (License Number, Facility Type, City, Zip Code, County) pertains to the entity responsible for the harvest and packaging activities.

### Table Inventory

*   **harvestpackagemerge23-24:** This table summarizes cannabis harvest and packaging metrics, including total pounds, unique harvest batches, and harvester details, aggregated by year and item category.

## Table: harvestpackagemerge23-24

*   **Purpose:** To provide an aggregated view of cannabis harvest and packaging volumes, linked to specific harvesters and item categories over the 2023-2024 period.
*   **What one row represents:** An aggregated summary of harvest and package data for a specific harvester, item category, and year.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 11869 rows, 11 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique license number of the cannabis harvester.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the harvester.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 0.1,
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging if critical for geographic analysis."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester's facility.",
    "Allowed Values / Range": "4000.0 - 961503674.0",
    "Missing %": 5.5,
    "Cleaning / Notes": "Missing values present. Some zip codes appear to be unusually large (e.g., 961503674.0), suggesting potential data entry errors or concatenated values. Validate against standard zip code formats. Consider imputation or flagging."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 0.1,
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging if critical for geographic analysis."
  },
  {
    "Column Name": "Year",
    "Type": "int64",
    "Units": "Year",
    "Description": "The calendar year of the harvest and packaging activities.",
    "Allowed Values / Range": "2023.0 - 2024.0",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item (e.g., Flower).",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight in pounds of packaged cannabis.",
    "Allowed Values / Range": "0.0 - 819416.794",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches contributing to the aggregated data.",
    "Allowed Values / Range": "1.0 - 1110.0",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight in pounds of harvested cannabis.",
    "Allowed Values / Range": "-380.53733377132 - 785406.9175",
    "Missing %": 2.5,
    "Cleaning / Notes": "Contains negative values, which are physically impossible for weight. These entries likely represent data errors or returns/adjustments not properly accounted for. Recommended handling: Flag negative values and investigate their source. For analysis, consider treating them as missing or imputing with 0 if they represent negligible quantities or errors."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight in pounds of harvested cannabis.",
    "Allowed Values / Range": "0.75 - 4440808.26822343",
    "Missing %": 2.5,
    "Cleaning / Notes": "Missing values present. Consider imputation or flagging."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `TotalHarvestPounds` contains negative values.
    *   **Likely cause:** Data entry errors, system glitches, or an incorrect representation of returns/adjustments within the tracking system where negative values are used to decrement inventory.
    *   **Recommended handling rule:** Flag all rows where `TotalHarvestPounds` is negative. For quantitative analysis, these values should be treated as invalid. Options include:
        1.  Excluding these rows from calculations involving total harvest pounds.
        2.  Imputing them with 0, assuming they represent negligible or erroneous entries that should not contribute negatively to total weight.
        3.  Investigating the source system to understand the business logic behind negative values.

*   **Issue:** `HarvesterZipCode` contains unusually large numeric values (e.g., 961503674.0) and missing values.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or inclusion of non-standard postal codes. Missing values indicate incomplete address information.
    *   **Recommended handling rule:**
        1.  For unusually large values, attempt to parse or truncate to standard 5-digit or 9-digit (ZIP+4) formats. If parsing is not feasible, flag as invalid.
        2.  For missing values, consider imputation based on `HarvesterCity` or `HarvesterCounty` if a reliable mapping exists, or flag as unknown.

*   **Issue:** Missing values in `HarvesterCity`, `HarvesterCounty`, `TotalHarvestPounds`, and `TotalHarvestWetPounds`.
    *   **Likely cause:** Incomplete data entry during the collection process or data extraction issues.
    *   **Recommended handling rule:**
        1.  For `HarvesterCity` and `HarvesterCounty`, if geographic analysis is critical, consider imputation based on other location fields or external geographic data, or flag rows with missing values.
        2.  For `TotalHarvestPounds` and `TotalHarvestWetPounds`, missing values should be handled based on the analytical context. Common approaches include exclusion, mean/median imputation, or more sophisticated methods if the missingness is not random.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Pounds:** Identify and flag all rows where `TotalHarvestPounds` is less than zero. For analytical purposes, replace these negative values with `NaN` or `0` to prevent erroneous calculations, depending on the downstream use case.
2.  **Validate and Clean Zip Codes:** Convert `HarvesterZipCode` to a string type. For values exceeding standard zip code lengths (e.g., 5 or 9 digits), attempt to extract the first 5 digits or flag as invalid. For missing zip codes, consider using `HarvesterCity` or `HarvesterCounty` to infer a plausible zip code if a lookup table is available, otherwise, leave as `NaN`.
3.  **Handle Missing Geographic Data:** For `HarvesterCity` and `HarvesterCounty` missing values, if these fields are critical for analysis, consider imputing them using the most frequent value within the same `HarvesterLicenseNumber` or leaving them as `NaN` and accounting for missingness in analysis.
4.  **Handle Missing Weight Data:** For missing values in `TotalHarvestPounds` (after addressing negative values) and `TotalHarvestWetPounds`, decide on an imputation strategy (e.g., mean, median, or zero) or exclude rows with missing values, based on the specific analytical requirements and tolerance for data loss.
5.  **Standardize Categorical Fields:** Review `HarvesterFacilityType` and `ItemCategory` for consistent capitalization and spelling to ensure accurate grouping and analysis.

### Limitations & Trust Section

*   **Geographic Data Incompleteness:** `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty` have missing values and potential inconsistencies (e.g., malformed zip codes). This limits the reliability of granular geographic analysis without further validation against external geographic datasets.
*   **Negative Harvest Pounds:** The presence of negative values in `TotalHarvestPounds` indicates a significant data quality issue that impacts the accuracy of total harvest volume calculations. Without understanding the root cause from the source system, any handling rule is an assumption.
*   **Data Aggregation Level:** The data is already aggregated by harvester, item category, and year. This limits the ability to perform analyses at a more granular level (e.g., individual transactions, specific harvest dates within a year).
*   **Lack of Primary Keys/Relationships:** The absence of explicit primary keys and relationships makes it challenging to confidently join this table with other potential datasets or to enforce data integrity rules.

To validate these elements, it would be beneficial to:
*   Consult with the data source owners to understand the meaning of negative `TotalHarvestPounds` and the data entry practices for geographic information.
*   Obtain a data dictionary or schema from the Track & Trace system for definitive column definitions, units, and expected value ranges.
*   Access raw, unaggregated data if available, to verify aggregation logic and investigate anomalies at a finer granularity.

### Appendix: Quick Reference

*   **Negative `TotalHarvestPounds`:** Flag and treat as invalid; consider replacing with 0 or `NaN` for analysis.
*   **Malformed `HarvesterZipCode`:** Validate and clean zip codes to standard formats; truncate or flag invalid entries.
*   **Missing Geographic Data:** Impute `HarvesterCity` and `HarvesterCounty` cautiously or flag for exclusion in geographic analysis.
*   **Missing Weight Data:** Address missing `TotalHarvestPounds` and `TotalHarvestWetPounds` via imputation (e.g., median) or exclusion, based on analytical needs.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for validation before any numeric conversion.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions, units, and proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative `TotalHarvestPounds` and the strategy for cleaning `HarvesterZipCode`. Any additional context regarding the Track & Trace system's data collection practices or business rules would be invaluable for refining this codebook and ensuring the reproducibility of the cleaning plan.

---

# Work Documentation

## Table: harvestpackagemerge23-24

**Data Operations:**
The provided Python script generates and processes a dataset that aligns with the description of `harvestpackagemerge23-24`. This involved several key steps:

*   **Source Data Consolidation:** Raw harvest quantity data from multiple CSV files (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and combined into a single `harvest_df`. Similarly, package quantity data from `packageqty19-24.csv`, `packageqty23-24.csv`, and `packageqty25.csv` were consolidated into a `package_df`. These consolidated dataframes were then saved as `harvest.csv` and `package.csv` respectively for future use.
*   **Column Renaming and Type Conversion:** Columns in both the `harvest_df` and `package_df` were systematically renamed to a consistent lowercase format (e.g., `HarvesterLicenseNumber` became `harvesterlicensenumber`). Critical numeric columns such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted to a numeric data type, with any conversion errors resulting in missing values.
*   **Initial Data Merging:** The cleaned `package_df` and `harvest_df` were merged using a left join operation, based on `harvesterlicensenumber` and `year`. This merge created a comprehensive dataset (`merged`) that conceptually represents the `harvestpackagemerge23-24` table, containing both harvest and package metrics alongside harvester details.
*   **Geographic Data Normalization and Imputation:**
    *   The `harvestercounty` column in both `harvest_df` and `package_df` underwent cleaning, replacing "NA" and "UNDEFINED" strings with empty values.
    *   A predefined mapping was applied to standardize various county name formats (e.g., "Alameda County" was converted to "ALAMEDA").
    *   Rows with missing `harvestercounty` values were removed after the initial mapping.
    *   Whitespace was removed from county names, and empty strings were converted to `pd.NA` (missing value indicator).
    *   The suffix "County" was removed from `harvestercounty` values to ensure consistency.
    *   In the merged dataset, the `harvestercounty` column was resolved by prioritizing the county information from the harvest data and falling back to the package data if the harvest county was missing.
    *   Further cleaning steps were applied to the `harvestercounty` column in the `merged` dataframe, replacing empty strings, "NA", and "nan" with `pd.NA`, followed by dropping any remaining rows with missing county information.
*   **Ratio Calculation:** Several new derived metrics were computed within the `merged` dataset to provide insights into processing efficiency:
    *   `package_to_harvest_ratio`: Calculated as the `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: Also calculated as `totalpackagepounds` divided by `totalharvestpounds`.
*   **Data Aggregation:** The `merged` dataset was further aggregated into two summary tables:
    *   **Category-level summary (`category_summary`):** This table was created by grouping the `merged` data by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, the first `totalharvestpounds` was taken, and the mean `package_to_harvest_ratio` was calculated.
    *   **County-level summary (`county_summary`):** This table was created by grouping the `merged` data by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, and the first `totalharvestpounds` was taken. A `package_to_harvest_ratio` was then calculated specifically for this aggregated table.
*   **Output Generation:** The final `county_summary` table was exported to an Excel file named `harvest_package_ratios.xlsx`.
*   **Exploratory Visualization:** The script also included steps to identify the top 10 counties based on total harvest pounds. For these top counties, bar plots were generated for each year to visualize trends in total harvest pounds, total package pounds, and the package-to-harvest ratio.

**Variables Affected:**
*   **Modified/Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `PkgYear` (renamed to `year`), `TotalHarvestPounds`, `TotalHarvestWetPounds`, `ItemCategory`, `TotalPackagePounds`, `UniqueHarvestBatches`. All these columns were consistently renamed to lowercase. The values within `HarvesterCounty` were standardized and cleaned across the dataset.
*   **Created:** New calculated fields include `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`. Additionally, aggregated versions of `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` were created in the `category_summary` and `county_summary` tables.

**Logic and Methodology:**
The overarching goal of these operations was to transform raw, disparate harvest and package data into a clean, standardized, and aggregated format suitable for analysis, mirroring the structure and content described for `harvestpackagemerge23-24`. The methodology involved:
*   **Data Integration:** Combining multiple years and types of data (harvest and package) into unified dataframes.
*   **Standardization:** Ensuring consistency in column names and, critically, in geographic identifiers like county names, which often suffer from varied spellings or formats in raw data.
*   **Data Cleansing:** Handling missing values and potential inconsistencies in geographic data to improve data quality and reliability for location-based analysis.
*   **Feature Engineering:** Deriving new metrics (ratios) that provide deeper insights into the efficiency of cannabis processing from harvest to final package.
*   **Aggregation:** Summarizing the data at different levels (item category and county) to support both granular and high-level analytical perspectives.
*   **Reporting and Visualization:** Generating structured outputs and visual summaries to facilitate understanding of key trends and comparisons across counties and years.

**Validation and Verification:**
*   Data type conversions were implemented with error coercion, which automatically handles non-numeric entries by converting them to `NaN`, preventing script failures due to unexpected data types.
*   Missing values in the `harvestercounty` column were explicitly addressed through multiple steps of replacement and row removal, ensuring that subsequent analyses rely on complete geographic information.
*   While the merge operation for `package_df` and `harvest_df` did not explicitly use a `validate` argument, the `how="left"` strategy ensures that all package records are retained, with harvest-related fields potentially becoming missing if no match is found.
*   No explicit data validation checks (e.g., range checks for weight values, consistency checks between related fields) were observed in the provided code snippets for the `harvestpackagemerge23-24` related processing, beyond the handling of missing or malformed county names and the numeric conversions.

**Results and Outcomes:**
The data work resulted in:
*   A consolidated and cleaned dataset that effectively represents the `harvestpackagemerge23-24` table, ready for detailed analysis.
*   Standardized and more reliable geographic information for harvesters, enhancing the accuracy of location-based insights.
*   The creation of new, insightful metrics such as `package_to_harvest_ratio` and `dry_to_wet_ratio`, which are crucial for evaluating operational efficiency.
*   The generation of aggregated summary tables at both the item category and county levels, providing a structured overview of the cannabis market.
*   An Excel report (`harvest_package_ratios.xlsx`) containing county-level summaries, serving as a direct output for stakeholders.
*   A series of visualizations that highlight key trends in harvest and package volumes, as well as processing ratios, across top-performing counties over time.