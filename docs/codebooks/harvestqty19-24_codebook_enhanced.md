# Track & Trace Data Codebook

### Overview Section

This dataset, part of the Track & Trace project, provides aggregated harvest quantity data for licensed cannabis harvesters. Each row in the `harvestqty19-24` table represents a summary of harvest activities for a specific harvester, identified by their license number, within a given packaging year. The overall data source, collection period, and extraction date are currently unknown.

*   **Assumptions:**
    *   One row in `harvestqty19-24` represents aggregated harvest metrics for a unique harvester (`HarvesterLicenseNumber`) in a specific `PkgYear`.

### Table Inventory

*   `harvestqty19-24`: Contains aggregated harvest quantity data, including total harvest pounds, wet pounds, and unique batch counts, for licensed harvesters between 2019 and 2024.

## Table: harvestqty19-24

*   **Purpose:** To track and summarize harvest quantities and activities by licensed harvesters over several years.
*   **What one row represents:** Aggregated harvest metrics for a specific harvester (`HarvesterLicenseNumber`) during a particular `PkgYear`.
*   **Primary key(s):** Inferred composite key: `HarvesterLicenseNumber`, `PkgYear`.
*   **Relationships:** Unknown.
*   **Number of rows and columns:** 27719 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed harvester.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility associated with the harvester's license.",
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
    "Missing %": 0.2,
    "Cleaning / Notes": "Missing values (0.2%) should be investigated. Consider imputation with a common value or flagging for review if critical for analysis."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester's facility.",
    "Allowed Values / Range": "[4000.0, 961503674.0]",
    "Missing %": 8.0,
    "Cleaning / Notes": "Missing values (8.0%) should be addressed. The upper range value (961503674.0) is highly anomalous for a US zip code; likely a data entry error or concatenation. Values outside the typical 5-digit or 9-digit US zip code format should be flagged or set to null. Consider imputation for missing values if geographic analysis is required, or use HarvesterCity for broader location context."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 1.3,
    "Cleaning / Notes": "Missing values (1.3%) should be investigated. Consider imputation or flagging."
  },
  {
    "Column Name": "PkgYear",
    "Type": "int64",
    "Units": "Year",
    "Description": "The year in which the harvest was packaged.",
    "Allowed Values / Range": "[2019.0, 2024.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of harvested product in pounds.",
    "Allowed Values / Range": "[-358.596995537842, 911433642.960996]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values, which are physically impossible for harvest quantities. These should be flagged, investigated, and potentially set to null or zero, or excluded from calculations. The upper range also appears extremely high, suggesting potential outliers or data entry errors."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight of harvested product in pounds.",
    "Allowed Values / Range": "[0.0002204624420183, 1371869133.03903]",
    "Missing %": 0.0,
    "Cleaning / Notes": "The upper range appears extremely high, suggesting potential outliers or data entry errors."
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches recorded.",
    "Allowed Values / Range": "[1.0, 8875.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Negative `TotalHarvestPounds`.
    *   **Likely cause:** Data entry error, system bug, or a representation of returns/adjustments without proper flagging. Physically impossible for a harvest quantity.
    *   **Recommended handling rule:** Flag these records for investigation. For analytical purposes, treat negative values as invalid: either set to `NULL`, `0`, or exclude from calculations involving sums/averages.
*   **Issue:** Anomalous `HarvesterZipCode` values.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or inclusion of non-standard codes. The upper range value (961503674.0) is not a valid US zip code format.
    *   **Recommended handling rule:** Validate `HarvesterZipCode` against a standard US zip code format (5 or 9 digits). Flag or set to `NULL` any values that do not conform.
*   **Issue:** Extremely large values in `TotalHarvestPounds` and `TotalHarvestWetPounds`.
    *   **Likely cause:** Potential data entry errors, unit conversion mistakes, or genuine but extreme outliers.
    *   **Recommended handling rule:** Investigate these extreme values. Consider winsorization or capping if they are deemed genuine but disproportionately influence analysis, or flag as outliers for further review.
*   **Issue:** Missing values in `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`.
    *   **Likely cause:** Incomplete data entry or optional fields.
    *   **Recommended handling rule:** For `HarvesterZipCode`, address after handling anomalous values. For all, consider imputation if location data is critical (e.g., using mode for categorical fields) or exclude records with missing critical location data for specific analyses.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Quantities:** Identify all records where `TotalHarvestPounds` is negative. For analytical purposes, these values will be set to `NULL` or `0` and flagged for further investigation into their origin.
2.  **Validate Zip Codes:** Filter `HarvesterZipCode` values. Any values that are not 5-digit or 9-digit numeric strings (after converting to string) will be flagged as invalid and set to `NULL`.
3.  **Handle Missing Location Data:** For `HarvesterCity`, `HarvesterZipCode` (after validation), and `HarvesterCounty`, records with missing values will be flagged. Depending on the analysis, these may be imputed (e.g., using the mode for categorical fields) or excluded.
4.  **Review Outlier Harvest Quantities:** Identify and flag records where `TotalHarvestPounds` or `TotalHarvestWetPounds` exceed a reasonable upper bound (e.g., 99th percentile + 3*IQR or a domain-specific threshold) for further review.

### Limitations & Trust Section

The dataset's reliability is impacted by several factors. The absence of explicit primary keys and relationships makes data integration and integrity validation challenging. The presence of negative harvest quantities and anomalous zip codes indicates potential data entry or system errors, requiring careful cleaning and validation. The overall data source, collection period, and extraction date are unknown, which limits the ability to fully contextualize and trust the data's recency and provenance. Validation against external licensing or harvest records would be needed to confirm the accuracy of harvester details and reported quantities.

### Appendix: Quick Reference

*   Negative `TotalHarvestPounds` values are invalid and set to `NULL` or `0`.
*   `HarvesterZipCode` values are validated for 5 or 9-digit numeric format; invalid entries are set to `NULL`.
*   Missing `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty` values are flagged.
*   Extreme outliers in `TotalHarvestPounds` and `TotalHarvestWetPounds` are flagged for review.
*   Inferred composite primary key: `HarvesterLicenseNumber`, `PkgYear`.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for negative harvest quantities and anomalous zip codes. Specific attention should be paid to the interpretation of "what one row represents" and the inferred primary key, as these are critical for data integrity and analysis. Additionally, any domain-specific knowledge regarding typical harvest quantities or zip code formats would be valuable to refine outlier detection thresholds and validation rules.

# Work Documentation

## Table: harvestqty19-24

**Data Operations:**
The data described conceptually as `harvestqty19-24` in the codebook was processed through several steps. Initially, multiple CSV files (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and concatenated into a single dataframe named `harvest_df`. This consolidated dataframe was then saved to `Data/Track and Trace Data/Harvest/harvest.csv` and subsequently re-loaded for further processing.

Column names were standardized to a consistent lowercase format (e.g., `HarvesterLicenseNumber` was renamed to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`). The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric data types, with any non-convertible values being coerced to `NaN` (Not a Number).

The `harvestercounty` column underwent extensive cleaning and normalization. Initial string replacements converted "NA" and "UNDEFINED" values to empty strings. A predefined mapping was then applied to standardize county names (e.g., "Alameda County" was mapped to "ALAMEDA"). Rows where `harvestercounty` remained missing after this initial cleaning were removed. Further cleaning involved stripping leading/trailing whitespace, replacing empty strings with `pd.NA`, and removing the " County" suffix from all values. Any rows with `harvestercounty` values still identified as missing after these steps were subsequently dropped.

This cleaned `harvest_df` was then merged with a `package_df` (derived from separate `packageqty` files) using `harvesterlicensenumber` and `year` as keys, resulting in a `merged` dataframe. During this merge, the `harvestercounty` column was consolidated, prioritizing values from the `harvest_df` if available. New ratio-based metrics were calculated within the `merged` dataframe: `package_to_harvest_ratio` (total packaged pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total wet harvest pounds), and `category_share` (total packaged pounds divided by total harvest pounds). The `harvestercounty` column in the `merged` dataframe received additional cleaning, replacing empty strings, "<NA>", and "nan" with `pd.NA`, followed by dropping any remaining rows with missing county values.

Finally, the `merged` dataframe was used to create aggregated summaries. `category_summary` was generated by grouping data by `harvestercounty`, `year`, and `itemcategory`, calculating the sum of `totalpackagepounds` and the mean `package_to_harvest_ratio`. `county_summary` was created by grouping by `harvestercounty` and `year`, summing `totalpackagepounds`, and then calculating the `package_to_harvest_ratio` at the county level. The `county_summary` was exported to an Excel file named `harvest_package_ratios.xlsx`. Subsequent code snippets utilized this `county_summary` for generating various plots to visualize harvest and package pound trends, as well as package-to-harvest ratios across the top 10 counties by year.

**Variables Affected:**
*   `HarvesterLicenseNumber`: Renamed to `harvesterlicensenumber`.
*   `HarvesterFacilityType`: Renamed to `harvesterfacilitytype`.
*   `HarvesterCity`: Renamed to `harvestercity`.
*   `HarvesterZipCode`: Renamed to `harvesterzipcode`.
*   `HarvesterCounty`: Renamed to `harvestercounty`, extensively cleaned, normalized, and used for filtering.
*   `PkgYear`: Renamed to `year`, converted to numeric.
*   `TotalHarvestPounds`: Renamed to `totalharvestpounds`, converted to numeric, and used in ratio calculations.
*   `TotalHarvestWetPounds`: Renamed to `totalharvestwetpounds`, converted to numeric, and used in ratio calculations.
*   `UniqueHarvestBatches`: Renamed to `uniqueharvestbatches`.
*   *New variables created:* `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
The data work followed a systematic approach to prepare the harvest quantity data for analysis.
1.  **Data Consolidation:** Multiple annual harvest quantity files were combined to create a comprehensive dataset, ensuring a complete time-series view of harvest activities. This addresses the fragmented nature of the raw data.
2.  **Standardization:** Column names were converted to a consistent lowercase format to improve readability and facilitate programmatic access across different datasets.
3.  **Type Conversion:** Key quantitative and temporal columns were explicitly converted to numeric data types. This is crucial for enabling accurate mathematical operations and time-series analysis, with error coercion to `NaN` allowing for identification of problematic entries.
4.  **Geographic Data Cleaning and Normalization:** The `HarvesterCounty` column, critical for location-based analysis, underwent rigorous cleaning. This involved replacing inconsistent string values ("NA", "UNDEFINED"), standardizing county names using a predefined mapping, and removing the " County" suffix. Records with unresolvable missing county information were removed to ensure the integrity of geographic analyses.
5.  **Data Integration:** The cleaned harvest data was merged with package data. This integration is fundamental for comparative analysis, allowing for the calculation of ratios that reflect the efficiency of product flow from harvest to packaging.
6.  **Ratio Calculation:** New derived metrics, such as `package_to_harvest_ratio` and `dry_to_wet_ratio`, were introduced to provide insights into operational efficiency and product transformation. `category_share` was also calculated to understand the distribution of packaged product by category relative to total harvest.
7.  **Aggregation:** Data was aggregated at both category and county levels to provide summarized views. This enables high-level trend analysis and comparison across different segments and geographic regions.
8.  **Visualization Preparation:** The aggregated data was specifically prepared for visualization, allowing for graphical representation of trends and distributions of harvest and package quantities and their ratios across top counties and years.

**Validation and Verification:**
*   The use of `pd.to_numeric(errors="coerce")` for numeric conversions implicitly handles non-numeric values by converting them to `NaN`, which can then be explicitly addressed or investigated.
*   Multiple `dropna(subset=["harvestercounty"])` calls were strategically placed after cleaning steps to ensure that subsequent analyses are performed on records with valid and standardized county information.
*   The merge operation between `harvest_df` and `package_df` used a `left` join, preserving all records from the harvest data while incorporating matching package data.
*   Conditional logic (`if "harvestercounty_harv" in merged.columns`) was used during the consolidation of county columns in the `merged` dataframe, demonstrating a defensive programming approach to handle potential variations in column availability.

**Results and Outcomes:**
*   A consolidated and cleaned `harvest_df` was successfully created, providing a robust foundation for subsequent analysis.
*   Standardized column names and appropriate data types were established, ensuring consistency and facilitating accurate data processing.
*   The quality of geographic data in the `harvestercounty` column was significantly improved, leading to more reliable location-based insights.
*   A `merged` dataset integrating harvest and package information was generated, enabling the calculation of key performance ratios that track product flow.
*   Aggregated summaries at the category and county levels were produced, offering high-level insights into harvest and packaging trends.
*   An Excel file (`harvest_package_ratios.xlsx`) containing county-level summaries was generated, providing a structured output for further review and reporting.
*   A series of visualizations were created to illustrate harvest and package quantity trends and their ratios for top counties over time, aiding in the rapid identification of patterns, outliers, and operational efficiencies.