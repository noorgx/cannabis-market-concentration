# Track & Trace Data Codebook

### Overview Section

This dataset provides a detailed view into the "Track & Trace" project, focusing on the journey of cannabis products from harvest to packaging. It primarily captures information related to packaged products, their originating harvests, and the licensed harvesters involved. Each row in the `harvestpackagemerge25` table represents a specific package or a record associated with a package, detailing its characteristics, the harvester's location, and metrics related to the harvest from which it originated. The overall data source, collection period, and extraction date are not explicitly provided in the current summary.

**Assumptions:**
*   The `PkgYear` field indicating '2025' suggests this dataset might represent future projections, planned activities, or a specific reporting period for the year 2025, rather than historical data.
*   The data is intended for analysis of harvest-to-package yields and harvester performance.

### Table Inventory

*   **harvestpackagemerge25:** This table consolidates information about packaged products, linking them to their originating harvests and providing details about the harvester.

### Table: harvestpackagemerge25

*   **Purpose:** To track and analyze the packaging of harvested cannabis products, including harvester details and yield metrics.
*   **What one row represents:** One record of a packaged product derived from a harvest, including associated harvester and yield information.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 4125 rows, 14 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique license number of the harvester facility.",
    "Allowed Values / Range": "",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the harvester (e.g., Microbusiness License).",
    "Allowed Values / Range": "",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester facility is located.",
    "Allowed Values / Range": "",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester facility.",
    "Allowed Values / Range": "89019.0 - 960679768.0",
    "Missing %": "3.2",
    "Cleaning / Notes": "3.2% missing values. Consider imputation or flagging for analysis requiring complete location data. The upper range value 960679768.0 appears to be an outlier or data entry error, as zip codes are typically 5 digits."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester facility is located.",
    "Allowed Values / Range": "",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "PkgYear",
    "Type": "int64",
    "Units": "Year",
    "Description": "The year associated with the package.",
    "Allowed Values / Range": "2025.0 - 2025.0",
    "Missing %": "0.0",
    "Cleaning / Notes": "All values are '2025'. This suggests the data may be for a future period, a projection, or a placeholder. Verify the intended meaning of this field with data owners."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the packaged item (e.g., Flower).",
    "Allowed Values / Range": "",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of the package in pounds.",
    "Allowed Values / Range": "0.0004188786398349 - 282901.024047837",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches contributing to this package.",
    "Allowed Values / Range": "1.0 - 478.0",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total dry weight from harvest associated with this package.",
    "Allowed Values / Range": "0.0022 - 282901.024047837",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight from harvest associated with this package.",
    "Allowed Values / Range": "1.4625 - 2500998.83340094",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "dryshare",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Ratio of TotalHarvestPounds to TotalHarvestWetPounds (dry weight / wet weight).",
    "Allowed Values / Range": "1.62150769302827e-05 - 3.262834",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values exceeding 1.0 (e.g., 3.26) suggest potential data entry errors or miscalculation, as dry weight should not exceed wet weight. Investigate records where dryshare > 1.0."
  },
  {
    "Column Name": "pkgsharedry",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Share of package pounds relative to total dry harvest pounds (TotalPackagePounds / TotalHarvestPounds).",
    "Allowed Values / Range": "1.86714224365046e-07 - 1.0059936674625",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values slightly exceeding 1.0 (e.g., 1.00599) indicate that the package weight is marginally greater than the total dry harvest pounds it's attributed to. This could be due to rounding, minor data discrepancies, or measurement inaccuracies. Flag these for review or consider capping at 1.0 if appropriate for analysis."
  },
  {
    "Column Name": "pkgsharewet",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Share of package pounds relative to total wet harvest pounds (TotalPackagePounds / TotalHarvestWetPounds).",
    "Allowed Values / Range": "3.36485567872677e-08 - 2.2928",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values exceeding 1.0 (e.g., 2.2928) suggest a package weight greater than the total wet harvest pounds it's attributed to, which is physically impossible. Investigate these records for data entry errors or miscalculations."
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestpackagemerge25` table.

*   **Issue:** Missing `HarvesterZipCode` values.
    *   **Likely cause:** Incomplete data entry or optional field during data collection.
    *   **Recommended handling rule:** For analyses requiring complete location data, rows with missing zip codes can be excluded or the zip code can be imputed based on `HarvesterCity` and `HarvesterCounty` if a reliable mapping exists. Otherwise, flag these records.
*   **Issue:** Anomalous `HarvesterZipCode` range.
    *   **Likely cause:** Data entry error or incorrect data type conversion. The upper range value `960679768.0` is not a valid 5-digit zip code.
    *   **Recommended handling rule:** Identify and correct or remove records with non-standard zip codes. Convert `HarvesterZipCode` to string type to preserve leading zeros and handle non-numeric entries more robustly.
*   **Issue:** `PkgYear` exclusively '2025'.
    *   **Likely cause:** The dataset represents future projections, planned data, or a specific reporting period for the year 2025. It is unlikely to be historical data if collected prior to 2025.
    *   **Recommended handling rule:** Confirm the intended meaning of this field with data stakeholders. If it's a projection, clearly document this assumption in any analysis. If it's a placeholder, investigate the actual intended year.
*   **Issue:** `dryshare` values greater than 1.0.
    *   **Likely cause:** Miscalculation or data entry error, as dry weight should not exceed wet weight.
    *   **Recommended handling rule:** Flag records where `dryshare > 1.0`. Investigate the source data for these records. For analysis, these values may need to be capped at 1.0 or excluded if the discrepancy is significant.
*   **Issue:** `pkgsharedry` values slightly greater than 1.0.
    *   **Likely cause:** Minor rounding errors, measurement inaccuracies, or slight discrepancies between reported package weight and harvest weight.
    *   **Recommended handling rule:** For practical purposes, values marginally above 1.0 can often be capped at 1.0, assuming they represent 100% allocation. Flag these records for potential review if high precision is critical.
*   **Issue:** `pkgsharewet` values greater than 1.0.
    *   **Likely cause:** Significant data entry error or miscalculation, as package weight cannot exceed the total wet harvest weight it originated from.
    *   **Recommended handling rule:** Flag records where `pkgsharewet > 1.0`. These are strong indicators of erroneous data and should be investigated thoroughly. Depending on the severity, these records may need to be excluded or corrected.

### Reproducible Cleaning Plan

1.  **Standardize Harvester Zip Codes:** Convert `HarvesterZipCode` to a string type to preserve leading zeros and handle non-numeric entries. Identify and flag or correct zip codes that are not 5-digit numeric values (e.g., `960679768.0`).
2.  **Address Missing Zip Codes:** For records with missing `HarvesterZipCode`, either impute based on `HarvesterCity` and `HarvesterCounty` using a lookup table if available, or flag these records for exclusion from analyses requiring complete location data.
3.  **Validate `PkgYear`:** Confirm the intended meaning of the `PkgYear` field with data owners. If it represents a future projection, document this clearly. No direct cleaning action is proposed without further clarification.
4.  **Correct `dryshare` Anomalies:** Identify and flag all records where `dryshare` is greater than 1.0. Investigate these records for potential data entry errors or miscalculations. For analytical purposes, consider capping these values at 1.0 or excluding them if the discrepancy is substantial.
5.  **Handle `pkgsharedry` Overages:** For `pkgsharedry` values slightly exceeding 1.0, cap these values at 1.0 to ensure logical consistency (package weight cannot exceed total harvest weight). Flag these records for potential review.
6.  **Address `pkgsharewet` Anomalies:** Identify and flag all records where `pkgsharewet` is greater than 1.0. These represent significant data inconsistencies and should be investigated thoroughly. Exclude these records from analyses or correct them if the true values can be ascertained.

### Limitations & Trust Section

The reliability of this dataset is subject to several limitations:

*   **`PkgYear` Discrepancy:** The uniform `PkgYear` of '2025' raises questions about whether this data represents actual historical events, future projections, or a placeholder. This significantly impacts the interpretability and trustworthiness of any time-series analysis or historical reporting. Validation with the data source is crucial.
*   **Missing and Anomalous `HarvesterZipCode`:** The presence of missing values and an extremely anomalous upper range for `HarvesterZipCode` indicates potential data entry issues or inconsistent data collection practices. This limits the accuracy of geographical analysis based solely on this field.
*   **Inconsistent Weight Ratios (`dryshare`, `pkgsharedry`, `pkgsharewet`):** Values in `dryshare`, `pkgsharedry`, and `pkgsharewet` that exceed logical bounds (e.g., dry weight > wet weight, package weight > total harvest weight) suggest underlying data quality issues, potentially from measurement errors, calculation errors, or incorrect data linkages. These inconsistencies reduce the trust in yield and allocation metrics.
*   **Lack of Primary Keys and Relationships:** The absence of identified primary keys and explicit relationship definitions makes it challenging to ensure data integrity and accurately join this table with other potential datasets within the Track & Trace ecosystem.

To validate these elements, it is essential to:
*   Consult with the data engineering or source system team to understand the origin and intended meaning of `PkgYear`.
*   Review data entry procedures for `HarvesterZipCode` and implement validation rules at the point of data capture.
*   Investigate the calculation logic for `dryshare`, `pkgsharedry`, and `pkgsharewet` and cross-reference with raw harvest and package weight data where available.
*   Obtain a comprehensive data model or schema diagram to understand primary keys and relationships across all Track & Trace tables.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Convert `HarvesterZipCode` to string; validate and correct non-standard 5-digit entries.
*   **Missing Data Handling:** Flag or impute missing `HarvesterZipCode` based on analysis needs.
*   **`PkgYear` Verification:** Confirm '2025' meaning with data owners; document as projection if applicable.
*   **`dryshare` Validation:** Flag records where `dryshare > 1.0`; investigate and potentially cap at 1.0.
*   **`pkgsharedry` Adjustment:** Cap `pkgsharedry` values slightly above 1.0 to 1.0.
*   **`pkgsharewet` Correction:** Flag and investigate records where `pkgsharewet > 1.0`; exclude or correct as necessary.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of column descriptions and inferred purposes, especially for calculated fields like `dryshare`, `pkgsharedry`, and `pkgsharewet`. Particular attention should be paid to the proposed handling rules for anomalies, such as the `PkgYear` being exclusively '2025' and the various ratio fields exceeding logical bounds. Confirmation from data owners regarding the intended meaning and acceptable ranges for these fields would greatly enhance the reproducibility and reliability of any subsequent data analysis.

# Work Documentation

## Table: harvestpackagemerge25

**Data Operations:**
The `harvestpackagemerge25` table, as described in the codebook, is conceptually represented by a `merged` DataFrame in the provided Python scripts. This DataFrame is constructed by combining data from multiple source files related to cannabis harvest and package quantities.

Specifically, the process involved:
1.  **Source Data Consolidation:** Separate CSV files containing harvest data (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and concatenated into a single `harvest_df`. Similarly, package data (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were consolidated into a `package_df`. These consolidated dataframes were then saved to intermediate CSV files (`harvest.csv` and `package.csv`) and reloaded.
2.  **Column Renaming and Type Conversion:** Key columns in both `harvest_df` and `package_df` were renamed for standardization (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`). Numeric fields such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted to appropriate numeric types, with errors coerced to missing values.
3.  **Geographical Data Cleaning and Standardization:** The `HarvesterCounty` column in both `harvest_df` and `package_df` underwent extensive cleaning. This included replacing "NA" and "UNDEFINED" values with empty strings, mapping full county names (e.g., "Alameda County") to their standardized uppercase abbreviations (e.g., "ALAMEDA") using a predefined dictionary, stripping leading/trailing whitespace, replacing empty strings with proper missing value indicators (`pd.NA`), and removing the "County" suffix. Rows with resulting missing `harvestercounty` values were subsequently dropped.
4.  **Data Integration (Merge):** The cleaned `package_df` and `harvest_df` were merged using a left join operation. The merge was performed on `harvesterlicensenumber` and `year`, with suffixes `_pkg` and `_harv` applied to distinguish columns originating from each source. A unified `harvestercounty` column was then created, prioritizing the value from the harvest data (`harvestercounty_harv`) if available, otherwise using the package data (`harvestercounty_pkg`). Further cleaning and dropping of missing `harvestercounty` values were applied to the merged dataset.
5.  **Derived Metric Calculation:** Several new ratio variables were calculated:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. This corresponds to the `pkgsharedry` column in the codebook.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`. This corresponds to the `dryshare` column in the codebook.
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. This appears to be a duplicate calculation of `package_to_harvest_ratio`.
6.  **Aggregation and Export:** The `merged` DataFrame was used to create aggregated summaries:
    *   `category_summary`: Grouped by `harvestercounty`, `year`, and `itemcategory`, summing `totalpackagepounds` and averaging `package_to_harvest_ratio`.
    *   `county_summary`: Grouped by `harvestercounty` and `year`, summing `totalpackagepounds` and calculating `package_to_harvest_ratio` at the county level.
    The `county_summary` was then exported to an Excel file named `harvest_package_ratios.xlsx`.
7.  **Data Visualization:** The processed data was used to generate various plots, including bar charts illustrating total harvest pounds, total package pounds, and package-to-harvest ratios for the top 10 counties across different years.

**Variables Affected:**
*   **Modified/Renamed:** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype_pkg`/`_harv`), `HarvesterCity` (to `harvestercity_pkg`/`_harv`), `HarvesterZipCode` (to `harvesterzipcode_pkg`/`_harv`), `HarvesterCounty` (standardized and unified to `harvestercounty`), `PkgYear` (to `year`), `ItemCategory` (to `itemcategory`), `TotalPackagePounds` (to `totalpackagepounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches_pkg`/`_harv`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`).
*   **Created:**
    *   `package_to_harvest_ratio` (corresponds to codebook's `pkgsharedry`).
    *   `dry_to_wet_ratio` (corresponds to codebook's `dryshare`).
    *   `category_share` (a duplicate calculation of `package_to_harvest_ratio`).
*   **Not explicitly created/addressed:** The codebook's `pkgsharewet` (TotalPackagePounds / TotalHarvestWetPounds) is not calculated in the provided Python script.
*   **Validated/Cleaned:** `year`, `totalharvestpounds`, `totalharvestwetpounds`, `totalpackagepounds` (via numeric conversion with error coercion), `harvestercounty` (via extensive standardization and removal of missing values).

**Logic and Methodology:**
The overarching goal of these operations is to prepare a comprehensive dataset for analyzing the flow of cannabis products from harvest to packaging, focusing on yield metrics and harvester performance. The methodology involves:
*   **Data Integration:** Combining disparate harvest and package records into a single, coherent view to enable cross-source analysis.
*   **Data Standardization:** Ensuring consistency in column names, data types, and categorical values (especially for `harvestercounty`) to facilitate accurate aggregation and comparison.
*   **Feature Engineering:** Deriving new ratio variables (`package_to_harvest_ratio`, `dry_to_wet_ratio`) to quantify key performance indicators related to processing efficiency and yield.
*   **Aggregation:** Summarizing data at different granularities (category-level, county-level) to identify trends and patterns.
*   **Exploratory Visualization:** Generating plots to visually inspect the data, highlight top performers, and understand temporal changes in key metrics.

It is important to note a discrepancy with the codebook's description of `PkgYear`. While the codebook states `PkgYear` is exclusively '2025', the Python script processes data spanning multiple years (2019-2025), providing a broader historical context for analysis.

**Validation and Verification:**
Data validation steps observed in the script include:
*   **Type Coercion:** Numeric conversions (`pd.to_numeric`) use `errors='coerce'`, which automatically handles non-numeric entries by converting them to `NaN`, preventing script crashes and implicitly flagging problematic values.
*   **Missing Value Handling:** Rows with missing `harvestercounty` values are explicitly dropped at multiple stages, indicating a strict requirement for complete geographical information for analysis.
*   **Lookup-based Standardization:** The `county_map` serves as a form of data validation and standardization for county names, ensuring consistency across records.
*   **Merge Integrity:** While the merge operation for `harvestpackagemerge25` (the `merged` DataFrame) does not explicitly use a `validate` argument, the `how="left"` merge strategy ensures that all package records are retained, and harvest information is added where a match exists.

Crucially, the Python script *does not implement* the explicit validation or correction rules suggested in the codebook's "Reproducible Cleaning Plan" for ratio values like `dryshare` (now `dry_to_wet_ratio`) and `pkgsharedry` (now `package_to_harvest_ratio`) that exceed logical bounds (e.g., capping at 1.0 or flagging for investigation). The `pkgsharewet` ratio, also noted for potential anomalies in the codebook, is not calculated at all in the provided script.

**Results and Outcomes:**
The data work results in a refined and integrated dataset that serves as the foundation for further analysis. Key outcomes include:
*   A consolidated `merged` DataFrame (representing `harvestpackagemerge25`) containing harmonized harvest and package data from 2019 to 2025.
*   Cleaned and standardized geographical data, improving the reliability of location-based analysis.
*   New, analytically useful ratio metrics (`package_to_harvest_ratio`, `dry_to_wet_ratio`) that quantify yield and conversion rates.
*   Aggregated summaries at the category and county levels, providing high-level insights into market dynamics.
*   An exported Excel file (`harvest_package_ratios.xlsx`) containing county-level summary data.
*   A series of visualizations that offer immediate insights into trends and performance across different counties and years.

While the processing addresses several data quality issues identified in the codebook, particularly regarding `HarvesterCounty` standardization and the expansion of the `PkgYear` range, the script does not implement the recommended anomaly handling for ratio values exceeding logical bounds, which remains a pending data quality concern for the derived metrics.