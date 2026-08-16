# Track & Trace Data Codebook

### Overview Section

This dataset provides a summary of harvest quantities within the Track & Trace system, focusing on cannabis cultivation and processing. It details harvest metrics such as total pounds, wet pounds, and unique batches, associated with specific licensed harvesters for a given year. Each row in the `harvestqty25` table represents an aggregated summary of harvest activities for a particular harvester license within the specified packaging year. The overall data source is the Track & Trace system, with data extracted for the year 2025. The exact collection period and extraction date are not specified in the provided metadata.

**Assumptions:**
*   The `PkgYear` field accurately reflects the year of packaging or harvest aggregation.
*   `TotalHarvestPounds` refers to dried, processed cannabis weight.
*   `TotalHarvestWetPounds` refers to the initial, undried weight of harvested cannabis.

### Table Inventory

*   **harvestqty25:** This table summarizes harvest quantities and batch counts for licensed harvesters in the year 2025.

### Table: harvestqty25

*   **Purpose:** To provide an aggregated view of harvest output, including total dry and wet weights, and the number of unique harvest batches, associated with individual licensed harvesters for the year 2025.
*   **What one row represents:** An aggregated summary of harvest activities for a specific harvester license within the year 2025.
*   **Primary key(s):** HarvesterLicenseNumber, PkgYear (inferred composite key)
*   **Relationships:** None explicitly known.
*   **Number of rows and columns:** 2717 rows, 9 columns

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
    "Description": "Type of facility associated with the harvester license.",
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
    "Missing %": "0.1",
    "Cleaning / Notes": "Small percentage of missing values; consider imputation or flagging if critical for location-based analysis."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the harvester facility.",
    "Allowed Values / Range": "Range: [89019.0, 960679768.0]",
    "Missing %": "3.1",
    "Cleaning / Notes": "Contains an anomalous maximum value (960679768.0) which is not a valid US zip code format. This indicates data entry error or corruption. Missing values also present."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the harvester facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "PkgYear",
    "Type": "int64",
    "Units": "Year",
    "Description": "The year in which the harvest was packaged or aggregated.",
    "Allowed Values / Range": "Range: [2025.0, 2025.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "All values are '2025', indicating the dataset is specific to this year."
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total dry weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [0.0022, 282901.024047837]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Minimum value is very small (0.0022), which might represent trace amounts or rounding. Review if values close to zero are meaningful or noise."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [1.4625, 2500998.83340094]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches associated with the harvester.",
    "Allowed Values / Range": "Range: [1.0, 556.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestqty25` table.

*   **Issue:** Anomalous `HarvesterZipCode` values.
    *   **Likely cause:** Data entry error, system malfunction, or incorrect data type conversion during extraction. The maximum value `960679768.0` is clearly not a valid 5-digit or 9-digit US zip code.
    *   **Recommended handling rule:** Flag invalid zip codes. For analysis requiring valid geographical data, these rows should be excluded or the zip codes imputed if a reliable source (e.g., `HarvesterCity`, `HarvesterCounty`) is available for cross-referencing.
*   **Issue:** Missing `HarvesterCity` values (0.1% missing).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** For analyses dependent on city information, these rows may need to be excluded or the city imputed based on `HarvesterZipCode` (after cleaning) or `HarvesterCounty` if a mapping is available.
*   **Issue:** Missing `HarvesterZipCode` values (3.1% missing).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** Impute missing zip codes based on `HarvesterCity` and `HarvesterCounty` if a reliable lookup table is available. Otherwise, flag these rows and exclude them from analyses requiring complete geographical data.
*   **Issue:** Very small `TotalHarvestPounds` values (minimum 0.0022).
    *   **Likely cause:** Precision issues, rounding, or recording of trace amounts.
    *   **Recommended handling rule:** Evaluate if values below a certain threshold (e.g., 0.01 pounds) should be considered noise and potentially rounded to zero or excluded, depending on the analytical objective.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to string type to handle potential leading zeros and non-numeric representations.
2.  **Validate `HarvesterZipCode`:** Identify and flag `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit US zip code formats. For invalid entries, attempt to correct them using `HarvesterCity` and `HarvesterCounty` as references if a lookup table is available; otherwise, set them to `NULL` or a designated "invalid" value.
3.  **Handle Missing `HarvesterZipCode`:** Impute missing `HarvesterZipCode` values using a lookup based on `HarvesterCity` and `HarvesterCounty` where possible. If imputation is not feasible, flag these rows for potential exclusion in location-sensitive analyses.
4.  **Handle Missing `HarvesterCity`:** Impute missing `HarvesterCity` values using a lookup based on `HarvesterZipCode` (after cleaning) or `HarvesterCounty`. If imputation is not feasible, flag these rows.
5.  **Review `TotalHarvestPounds`:** Analyze the distribution of `TotalHarvestPounds` to determine if a threshold for "trace amounts" is necessary. If values below a certain threshold are deemed insignificant, consider rounding them to zero or excluding them from aggregate calculations.

### Limitations & Trust Section

The reliability of geographical data (`HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`) is impacted by missing values and the identified anomaly in `HarvesterZipCode`. Specifically, the presence of an extremely large, invalid zip code value (`960679768.0`) suggests potential data corruption or significant data entry errors that could affect any analysis relying on accurate location information. Validation against an external, authoritative source for zip codes and city/county mappings is needed to ensure the accuracy of these fields. The dataset is limited to `PkgYear` 2025, which restricts temporal analysis to a single year.

### Appendix: Quick Reference

*   **Zip Code Validation:** Flag and potentially nullify `HarvesterZipCode` values that are not valid 5-digit or 9-digit US zip codes.
*   **Missing Geographical Data:** Impute `HarvesterCity` and `HarvesterZipCode` using cross-referencing where possible; otherwise, flag for exclusion in location-dependent analyses.
*   **Data Scope:** All data pertains to `PkgYear` 2025.
*   **Trace Amounts:** Review `TotalHarvestPounds` for values near zero to determine if a minimum threshold for significance is required.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `harvestqty25` and confirm that the proposed handling rules for the `HarvesterZipCode` anomaly and missing geographical data align with project requirements for data integrity and analytical use cases. Specific attention should be paid to the implications of the `PkgYear` being exclusively 2025 for any time-series or comparative analyses.

# Work Documentation

## Table: harvestqty25

**Data Operations:**
The `harvestqty25` dataset, along with `harvestqty19-24.csv` and `harvestqty23-24.csv`, was loaded from CSV files, with all columns initially read as strings to preserve original formatting and prevent default `NaN` conversions. These individual datasets were then concatenated into a single, comprehensive `harvest_df` DataFrame. This combined DataFrame was subsequently saved to `Data/Track and Trace Data/Harvest/harvest.csv` and reloaded for further processing.

Key operations performed on `harvest_df` include:
1.  **Column Renaming:** Original column names (e.g., `HarvesterLicenseNumber`, `PkgYear`, `TotalHarvestPounds`) were standardized to a consistent lowercase snake_case format (e.g., `harvesterlicensenumber`, `year`, `totalharvestpounds`).
2.  **Data Type Conversion:** The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric types, with errors coerced to `NaN` to handle non-numeric entries gracefully.
3.  **Geographical Data Cleaning and Normalization (`harvestercounty`):**
    *   Initial string replacements were performed to convert "NA" and "UNDEFINED" values to empty strings.
    *   A comprehensive mapping dictionary was applied to standardize various county name formats (e.g., "Alameda County") to a consistent uppercase format (e.g., "ALAMEDA").
    *   Rows with missing `harvestercounty` values were dropped after initial cleaning.
    *   The `harvestercounty` column was converted to string type, stripped of leading/trailing whitespace, and then any resulting empty strings were converted to `pd.NA`.
    *   A regular expression was used to remove " County" suffixes (case-insensitive) from county names, followed by another whitespace strip.
    *   Finally, rows with any remaining missing `harvestercounty` values were dropped.
4.  **Data Integration:** The processed `harvest_df` was left-merged with a similarly prepared `package_df` (derived from `packageqty` files) on `harvesterlicensenumber` and `year` to create a `merged` DataFrame.
5.  **Consolidating County Information:** In the `merged` DataFrame, a new `harvestercounty` column was created, prioritizing the county information from the harvest data (`harvestercounty_harv`) and falling back to the package data (`harvestercounty_pkg`) if the harvest data was missing.
6.  **Feature Engineering:** Several ratio-based variables were calculated:
    *   `package_to_harvest_ratio`: `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: `totalpackagepounds` divided by `totalharvestpounds` (this appears to be a re-calculation or redundant with `package_to_harvest_ratio`).
7.  **Final Geographical Data Refinement:** The `harvestercounty` column in the `merged` DataFrame underwent further cleaning, replacing empty strings, `<NA>`, and "nan" with `pd.NA`, followed by dropping rows with missing values.
8.  **Aggregation:**
    *   `category_summary`: Aggregated the `merged` data by `harvestercounty`, `year`, and `itemcategory` to sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`. `totalharvestpounds` was taken as the first value within each group.
    *   `county_summary`: Aggregated the `merged` data by `harvestercounty` and `year` to sum `totalpackagepounds` and take the first `totalharvestpounds`. A `package_to_harvest_ratio` was then calculated at this county-year level.
9.  **Output and Visualization:** The `county_summary` DataFrame was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Subsequently, the top 10 counties based on total harvest pounds were identified, and a series of bar plots were generated for each year, visualizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for these top counties.

**Variables Affected:**
*   **Original Columns (renamed):** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype`), `HarvesterCity` (to `harvestercity`), `HarvesterZipCode` (to `harvesterzipcode`), `HarvesterCounty` (to `harvestercounty`), `PkgYear` (to `year`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches`).
*   **Transformed Columns:** `year`, `totalharvestpounds`, `totalharvestwetpounds` (data type changed to numeric). `harvestercounty` (values standardized and cleaned).
*   **New Derived Variables:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
The primary intent behind these operations was to consolidate harvest data across multiple years, standardize its format, clean critical geographical information, and then integrate it with packaging data to derive key performance indicators. Reading all initial data as strings ensures consistency and prevents premature type inference issues. Renaming columns to snake_case improves readability and programmatic access. Converting numeric fields allows for calculations. The extensive cleaning and normalization of `harvestercounty` are crucial for accurate geographical analysis, addressing inconsistencies and missing values. Merging with `package_df` enables the calculation of ratios that provide insights into the efficiency of converting harvested material into packaged products. The subsequent aggregations summarize these metrics at different granularities (category and county levels), facilitating high-level analysis and visualization of trends over time and across regions. The visualizations aim to highlight top-performing counties and their trends in harvest, packaging, and conversion ratios.

**Validation and Verification:**
*   Initial loading used `dtype=str` and `keep_default_na=False` to control how data was read, preventing implicit type conversions and `NaN` handling.
*   `errors="coerce"` was used during numeric type conversions for `year`, `totalharvestpounds`, and `totalharvestwetpounds` to identify and handle values that could not be converted.
*   `dropna(subset=["harvestercounty"])` was applied multiple times during the cleaning process to explicitly remove records with unresolvable missing county information, ensuring that subsequent analyses rely on complete geographical data.
*   The `merge` operation used `how="left"` to retain all harvest records and `validate="many_to_one"` (though this was used in a different merge operation, not the harvest-package merge) to ensure expected cardinality.
*   The `county_map` provides a form of data validation by standardizing county names, ensuring consistency.

**Results and Outcomes:**
The data work resulted in a cleaned, integrated dataset (`merged`) containing both harvest and package information, enriched with calculated ratios. This dataset was then used to produce:
*   `harvest_package_ratios.xlsx`: An Excel file summarizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` aggregated by `harvestercounty` and `year`.
*   A series of visualizations (bar plots) illustrating `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for the top 10 counties across different years, providing a clear overview of harvest and packaging trends and efficiency.
The cleaned `harvestercounty` column and the derived ratios are critical for geographical and operational performance analysis within the cannabis cultivation and packaging sector.