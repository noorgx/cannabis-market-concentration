# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated information related to cannabis harvest and packaging activities within the Track & Trace system, covering the period from 2019 to 2024. It aims to offer insights into the flow of cannabis products from cultivation to initial packaging, including quantities harvested and packaged, and associated harvester details. Each row in the `harvestpackagemerge19-24` table represents a unique aggregation of harvest and package data, likely at a specific harvester and item category level for a given year. The overall data source is the Track & Trace system, with data collected between 2019 and 2024. The exact extraction date is not available.

**Assumptions:**
*   The collection period (2019-2024) is inferred from the table name `harvestpackagemerge19-24`.
*   Units for weight-related columns are assumed to be pounds based on common industry practice and typical data ranges.

### Table Inventory

*   **`harvestpackagemerge19-24`**: This table consolidates data on cannabis harvests and their subsequent packaging, providing details on quantities, harvester information, and package characteristics over several years.

## Table: harvestpackagemerge19-24

*   **Purpose:** To provide a consolidated view of cannabis harvest and packaging metrics, linking harvest quantities to packaged outputs and harvester details.
*   **What one row represents:** An aggregated record of harvest and package data, likely unique by harvester, item category, and year.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 43827 rows, 14 columns

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique license number of the cannabis harvester facility.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of license held by the harvester facility (e.g., Microbusiness, Cultivation).",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the harvester facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 0.2,
    "Cleaning / Notes": "Missing values observed. Consider imputation with 'Unknown' or the most frequent city, or exclusion if geographic analysis is critical."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester facility.",
    "Allowed Values / Range": "[4000.0, 961503674.0]",
    "Missing %": 7.7,
    "Cleaning / Notes": "Missing values observed. The upper range value (961503674.0) is an invalid zip code format, indicating data entry errors or corruption. Values outside typical 5-digit or 9-digit zip code formats should be flagged or corrected. Consider imputation for missing values or exclusion if accuracy is paramount."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 1.7,
    "Cleaning / Notes": "Missing values observed. Consider imputation with 'Unknown' or the most frequent county, or exclusion if geographic analysis is critical."
  },
  {
    "Column Name": "PkgYear",
    "Type": "int64",
    "Units": "Year",
    "Description": "Year in which the package was recorded.",
    "Allowed Values / Range": "[2019.0, 2024.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the packaged item (e.g., Fresh Cannabis Plant, Flower).",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalPackagePounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of the packaged cannabis in pounds.",
    "Allowed Values / Range": "[2.20462442018378e-07, 911433262.960458]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches contributing to the package.",
    "Allowed Values / Range": "[1.0, 8875.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of the harvested cannabis in pounds.",
    "Allowed Values / Range": "[-358.596995537842, 911433642.960996]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Anomaly: Negative values observed. These are physically impossible for weight. Flag these records for investigation or set to 0, or exclude them from calculations."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight of the harvested cannabis in pounds.",
    "Allowed Values / Range": "[0.0002204624420183, 1371869133.03903]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "dryshare",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Ratio representing the dry weight share, potentially derived from harvest or package data.",
    "Allowed Values / Range": "[-0.0036930091039523, 138.765601461074]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Anomaly: Negative values observed. Ratios should not be negative. Values greater than 1 (or 100% if interpreted as percentage) may also indicate errors depending on the exact definition. Flag negative values for investigation or set to 0. Investigate values > 1."
  },
  {
    "Column Name": "pkgsharedry",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Ratio representing the dry package share, potentially derived from package data.",
    "Allowed Values / Range": "[-58.904455132272, 5.95397130872442]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Anomaly: Negative values observed. Ratios should not be negative. Values greater than 1 (or 100% if interpreted as percentage) may also indicate errors depending on the exact definition. Flag negative values for investigation or set to 0. Investigate values > 1."
  },
  {
    "Column Name": "pkgsharewet",
    "Type": "float64",
    "Units": "Ratio",
    "Description": "Ratio representing the wet package share, potentially derived from package data.",
    "Allowed Values / Range": "[3.7789324515824295e-11, 138.760593084537]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Values greater than 1 (or 100% if interpreted as percentage) may indicate errors depending on the exact definition. Investigate values > 1."
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestpackagemerge19-24` table.

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry error, calculation artifact, or incorrect data transformation. Physically, weight cannot be negative.
    *   **Recommended handling rule:** Flag these records for further investigation. For analytical purposes, consider setting negative values to 0 or excluding them from aggregate calculations, depending on the impact and business context.

*   **Issue:** Negative values in `dryshare` and `pkgsharedry`.
    *   **Likely cause:** Calculation errors, incorrect formula application, or data entry mistakes. Ratios, by definition, should be non-negative.
    *   **Recommended handling rule:** Flag these records. For analysis, set negative values to 0. Further investigation into the calculation logic for these fields is recommended.

*   **Issue:** `dryshare`, `pkgsharedry`, and `pkgsharewet` contain values greater than 1 (or 100%).
    *   **Likely cause:** If these fields represent proportions or percentages, values exceeding 1 (or 100%) indicate calculation errors or misinterpretation of the metric.
    *   **Recommended handling rule:** Flag these records for review. If they are indeed proportions, cap values at 1 or treat them as outliers. Clarification on the exact definition of these "share" metrics is needed.

*   **Issue:** Invalid `HarvesterZipCode` values, specifically the upper range `961503674.0`.
    *   **Likely cause:** Data entry error, concatenation of multiple numbers, or incorrect data type conversion during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Flag zip codes that do not conform to standard 5-digit or 9-digit formats. Consider cleaning these by truncating or setting to null if uncorrectable, or using a lookup table for validation.

*   **Issue:** Missing values in `HarvesterCity` (0.2%), `HarvesterZipCode` (7.7%), and `HarvesterCounty` (1.7%).
    *   **Likely cause:** Incomplete data entry or data not available at the time of record creation.
    *   **Recommended handling rule:** For `HarvesterCity` and `HarvesterCounty`, impute with 'Unknown' or the most frequent value if geographic precision is not critical. For `HarvesterZipCode`, consider imputation with a default value (e.g., 00000) or 'Unknown' after addressing invalid formats, or exclude records if precise location data is essential.

### Reproducible Cleaning Plan

1.  **Address Invalid `HarvesterZipCode` Formats:** Identify and flag `HarvesterZipCode` values that are not valid 5-digit or 9-digit US zip codes. For analytical purposes, these can be set to `NaN` or a placeholder like 'INVALID' to prevent erroneous geographic analysis.
2.  **Handle Negative Weight Values:** For `TotalHarvestPounds`, identify all records where the value is negative. Flag these records for review and set the `TotalHarvestPounds` to 0 for downstream analysis, as negative weight is physically impossible.
3.  **Correct Negative Ratio Values:** For `dryshare` and `pkgsharedry`, identify all records where the value is negative. Flag these records and set the values to 0, as ratios should not be negative.
4.  **Review Out-of-Range Ratio Values:** For `dryshare`, `pkgsharedry`, and `pkgsharewet`, identify values greater than 1. Flag these records for further investigation into their calculation and definition. Depending on the outcome, these might be capped at 1 or treated as outliers.
5.  **Impute Missing Geographic Data:** For `HarvesterCity` and `HarvesterCounty`, impute missing values with 'Unknown' to ensure completeness for categorical analysis. For `HarvesterZipCode`, after addressing invalid formats, impute remaining missing values with a placeholder like '00000' or 'UNKNOWN' if a numeric type is required, or 'Unknown' if treated as categorical.

### Limitations & Trust Section

The reliability of this dataset is impacted by several factors:

*   **Missing Primary Keys and Relationships:** The absence of explicitly defined primary keys and relationships makes it challenging to ensure data uniqueness and integrity, and to confidently join this table with other datasets. Validation requires domain expertise to identify natural keys.
*   **Inferred Column Descriptions and Units:** Many column descriptions and units (e.g., 'Pounds' for weight, 'Ratio' for shares) have been inferred based on column names and typical data ranges. These inferences require validation by data owners or subject matter experts to ensure accuracy.
*   **Data Quality Issues:** The presence of negative values for physical quantities (`TotalHarvestPounds`) and ratios (`dryshare`, `pkgsharedry`), along with invalid zip codes, indicates potential data entry errors, calculation flaws, or issues during data extraction. These anomalies reduce the immediate trustworthiness of affected metrics.
*   **Ambiguous Ratio Definitions:** The exact definitions and expected ranges for `dryshare`, `pkgsharedry`, and `pkgsharewet` are not fully clear, especially given values exceeding 1. This ambiguity limits the confidence in interpreting these metrics without further clarification.

To validate and improve trust in this dataset, the following are needed:
*   Confirmation of primary keys and foreign key relationships from the source system.
*   Official data dictionary or schema documentation to verify column descriptions, units, and allowed value ranges.
*   Investigation into the root causes of negative values and invalid zip codes to prevent recurrence.
*   Clear definitions for all ratio-based metrics and their expected value ranges.

### Appendix: Quick Reference

*   **Negative Weights:** `TotalHarvestPounds` negative values are invalid; set to 0 or exclude.
*   **Negative Ratios:** `dryshare`, `pkgsharedry` negative values are invalid; set to 0.
*   **Out-of-Range Ratios:** `dryshare`, `pkgsharedry`, `pkgsharewet` values > 1 require investigation; potentially cap at 1.
*   **Invalid Zip Codes:** `HarvesterZipCode` values not conforming to 5 or 9 digits should be flagged or corrected.
*   **Missing Geographic Data:** Impute `HarvesterCity`, `HarvesterCounty` with 'Unknown'; `HarvesterZipCode` with '00000' or 'UNKNOWN'.
*   **Data Source:** Track & Trace system.
*   **Collection Period:** 2019-2024 (inferred).

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions, units, and the proposed handling rules for anomalies. Particular attention should be paid to the interpretation of ratio-based fields (`dryshare`, `pkgsharedry`, `pkgsharewet`) and the implications of the identified data quality issues on potential analyses. Confirmation of primary keys and relationships, if known, would greatly enhance the utility and trustworthiness of this codebook.

# Work Documentation

## Table: harvestpackagemerge19-24

**Data Operations:**
The `harvestpackagemerge19-24` table, as described in the Codebook, is conceptually created and processed through a series of operations on raw harvest and package data files.

1.  **Source Data Loading:** Individual CSV files containing harvest quantity data (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) and package quantity data (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were loaded into separate DataFrames.
2.  **Concatenation:** The multiple harvest files were concatenated into a single `harvest_df`, and similarly, the package files were combined into a `package_df`. These combined DataFrames were then saved to intermediate CSV files (`Data/Track and Trace Data/Harvest/harvest.csv` and `Data/Track and Trace Data/Package/package.csv`) and reloaded.
3.  **Column Renaming:** Columns in both `harvest_df` and `package_df` were renamed to a consistent, lowercase snake_case format (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`).
4.  **Data Type Conversion:** Key columns such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted from string to numeric data types. Any values that could not be converted were coerced into `NaN` (Not a Number).
5.  **Geographic Data Cleaning and Normalization:**
    *   The `harvestercounty` column in both `harvest_df` and `package_df` underwent extensive cleaning. Initial string values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined mapping was applied to standardize various representations of county names (e.g., "Alameda County" was mapped to "ALAMEDA").
    *   Whitespace was stripped from `harvestercounty` values, and the suffix " County" was removed.
    *   Empty strings, pandas' `<NA>` indicator, and "nan" string representations were converted to actual missing values (`pd.NA`).
    *   Rows with missing `harvestercounty` values were dropped at multiple stages of this cleaning process.
6.  **Merging:** The cleaned `package_df` and `harvest_df` were merged into a `merged` DataFrame, which represents the `harvestpackagemerge19-24` table. The merge was performed as a left join on `harvesterlicensenumber` and `year`. Overlapping column names were suffixed with `_pkg` and `_harv`.
7.  **Column Resolution Post-Merge:** A unified `harvestercounty` column was created in the `merged` DataFrame. It preferentially used the county information from the harvest data (`harvestercounty_harv`) and fell back to the package data (`harvestercounty_pkg`) if the harvest data was missing. Further cleaning steps for `harvestercounty` (stripping whitespace, replacing empty strings/NA/nan with `pd.NA`, and dropping missing values) were applied to the `merged` DataFrame.
8.  **Feature Engineering:** New ratio-based metrics were calculated:
    *   `package_to_harvest_ratio` was computed as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio` was computed as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share` was also computed as `totalpackagepounds` divided by `totalharvestpounds`, appearing to be a duplicate of `package_to_harvest_ratio`.
9.  **Aggregation:**
    *   A `category_summary` DataFrame was created by grouping the `merged` data by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, `package_to_harvest_ratio` was averaged, and `totalharvestpounds` was taken as the first value.
    *   A `county_summary` DataFrame was created by grouping the `merged` data by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, `totalharvestpounds` was taken as the first value, and a new `package_to_harvest_ratio` was calculated at this aggregated level.
10. **Export and Visualization:** The `county_summary` DataFrame was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Subsequently, the data was used to generate various bar charts visualizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for the top 10 counties across different years.

**Variables Affected:**

*   **Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `PkgYear`, `Year`, `TotalHarvestPounds`, `TotalHarvestWetPounds`, `UniqueHarvestBatches`, `ItemCategory`, `TotalPackagePounds`.
*   **Data Type Changed:** `year`, `totalharvestpounds`, `totalharvestwetpounds`, `totalpackagepounds` were converted from string to numeric types. `HarvesterZipCode` remained as a string type in the processed data.
*   **Cleaned/Normalized:** `harvestercounty` was extensively cleaned and standardized.
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Aggregated/Summarized:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` were aggregated in the `category_summary` and `county_summary` DataFrames.

**Logic and Methodology:**

The overarching methodology aimed to integrate disparate harvest and package datasets to create a unified view of cannabis product flow. This involved a systematic approach to data preparation:
*   **Consolidation:** Combining multiple source files into single, coherent DataFrames (`harvest_df`, `package_df`) ensured all relevant data was available for analysis.
*   **Standardization:** Renaming columns and converting data types facilitated consistent data handling and enabled mathematical operations. The `errors="coerce"` strategy for numeric conversions allowed for graceful handling of malformed data by converting invalid entries to `NaN`.
*   **Geographic Data Integrity:** Significant effort was dedicated to cleaning and normalizing `harvestercounty`. This was critical to ensure accurate geographic aggregation and analysis, addressing inconsistencies and missing values through replacement, mapping, and dropping incomplete records.
*   **Relational Integration:** Merging `package_df` and `harvest_df` established the core `harvestpackagemerge19-24` dataset, linking package outputs to their harvest origins. The strategy for resolving `harvestercounty` conflicts post-merge prioritized harvest data, assuming it might be more authoritative or complete for the harvester's location.
*   **Analytical Derivations:** The creation of ratio metrics (`package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`) was intended to provide deeper insights into processing efficiency, yield, and the relationship between harvested and packaged quantities.
*   **Hierarchical Aggregation:** Data was aggregated at both item category and county levels to provide summarized views, enabling analysis at different granularities and supporting macro-level insights into market trends.
*   **Reporting and Visualization:** The final aggregated data was exported and used to generate visualizations, serving as a direct output for reporting and aiding in the exploratory analysis of trends and patterns.

**Validation and Verification:**

*   Data type conversions utilized `errors="coerce"`, which implicitly flags non-convertible values as `NaN`, providing a basic level of error handling.
*   The repeated application of `dropna(subset=["harvestercounty"])` served as a verification step to ensure that subsequent geographic analysis was based on records with complete and valid county information.
*   The iterative cleaning steps for `harvestercounty` indicate an ongoing process of identifying and refining data quality for this critical identifier.
*   The generation of plots for the top 10 counties provided a visual means to verify the aggregated data, allowing for quick identification of trends, outliers, and potential data issues.
*   **Note on Discrepancy with Codebook's Cleaning Plan:** The provided Python code does not explicitly implement several specific data quality anomaly handling rules outlined in the Codebook's "Data Quality & Anomalies Section" and "Reproducible Cleaning Plan." Specifically:
    *   Negative `TotalHarvestPounds` values are not explicitly set to zero or otherwise corrected beyond `NaN` coercion during initial numeric conversion.
    *   Negative or out-of-range ratio values (such as `dryshare`, `pkgsharedry`, `pkgsharewet` mentioned in the Codebook, or their calculated equivalents `package_to_harvest_ratio`, `dry_to_wet_ratio` in the code) are not explicitly set to zero or capped at one.
    *   Invalid `HarvesterZipCode` formats are not specifically flagged, corrected, or imputed; the column remains as a string type and is not validated against standard zip code patterns.
    *   Missing `HarvesterCity` and `HarvesterZipCode` values are not explicitly imputed with 'Unknown' or '00000' as suggested in the Codebook, although rows with missing `harvestercounty` are dropped.

**Results and Outcomes:**

*   A consolidated `merged` dataset was successfully created, integrating harvest and package information, which forms the basis for the `harvestpackagemerge19-24` table.
*   Key columns were standardized in naming and converted to appropriate data types, making the data ready for quantitative analysis.
*   The `harvestercounty` column was significantly cleaned and normalized, enhancing the reliability of location-based analyses.
*   New analytical metrics, including `package_to_harvest_ratio` and `dry_to_wet_ratio`, were derived, providing valuable insights into product transformation and yield.
*   Aggregated summaries at both the item category and county levels were produced, offering high-level views of the data for strategic analysis.
*   The `county_summary` was exported to an Excel file, making the aggregated data readily available for further reporting and integration into other tools.
*   Visualizations were generated to illustrate trends in harvest pounds, package pounds, and package-to-harvest ratios across the top counties over time, facilitating data exploration and aiding in the identification of significant patterns or anomalies.
*   **Note on Data Quality:** While substantial cleaning was performed, particularly on geographic identifiers, the Python code does not explicitly address all the specific anomaly handling rules (e.g., correcting negative weights or out-of-range ratios) suggested in the Codebook's data quality sections. Therefore, the resulting `merged` and aggregated datasets may still contain these specific anomalies if they were present in the raw source files and were not converted to `NaN` during initial numeric parsing.