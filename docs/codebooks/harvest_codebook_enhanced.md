# Track & Trace Data Codebook

### Overview Section

This dataset provides a summary of cannabis harvest activities within the Track & Trace system. It aggregates information related to licensed harvesters, their locations, and the quantities of cannabis harvested over specific periods. The data aims to offer insights into production volumes and geographical distribution of harvesting operations. Each row in the `harvest` table represents a summarized record of harvest activities, likely aggregated by harvester license and year, providing key metrics such as total harvest pounds and unique batch counts. The overall data source is the Track & Trace system, with specific collection periods and extraction dates not explicitly provided in this summary.

**Assumptions:**
*   Data pertains to the regulated cannabis industry.
*   Units for harvest quantities are in pounds, unless otherwise specified.
*   Geographical information (City, Zip Code, County) refers to the harvester's location.

### Table Inventory

*   **harvest:** Contains aggregated information about cannabis harvesting activities, including harvester details, location, and total harvest quantities.

## Table: harvest

*   **Purpose:** To provide a summarized view of cannabis harvesting operations, detailing quantities harvested and associated harvester information.
*   **What one row represents:** One aggregated harvest record, likely unique per harvester license and a specific time period (e.g., year).
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 37936 rows, 10 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "HarvesterLicenseNumber",
    "Type": "object",
    "Units": "License Number",
    "Description": "Unique identifier for the licensed cannabis harvester.",
    "Allowed Values / Range": "Example: C12-0000002-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterFacilityType",
    "Type": "object",
    "Units": "Facility Type",
    "Description": "Type of facility associated with the harvester's license.",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "HarvesterCity",
    "Type": "object",
    "Units": "City Name",
    "Description": "City where the harvester's facility is located.",
    "Allowed Values / Range": "Example: SOUTH LAKE TAHOE",
    "Missing %": "0.2",
    "Cleaning / Notes": "Minor missing values; consider imputation with 'Unknown' or based on Zip Code/County if available."
  },
  {
    "Column Name": "HarvesterZipCode",
    "Type": "float64",
    "Units": "Zip Code",
    "Description": "Zip code of the harvester's facility.",
    "Allowed Values / Range": "Range: [4000.0, 961503674.0]",
    "Missing %": "7.2",
    "Cleaning / Notes": "The upper range value (961503674.0) is an invalid US zip code, indicating potential data entry errors or corruption. Values outside the standard 5-digit US zip code range (e.g., 00000-99999) should be flagged or corrected. Missing values can be imputed or flagged."
  },
  {
    "Column Name": "HarvesterCounty",
    "Type": "object",
    "Units": "County Name",
    "Description": "County where the harvester's facility is located.",
    "Allowed Values / Range": "Example: EL DORADO",
    "Missing %": "1.0",
    "Cleaning / Notes": "Minor missing values; consider imputation with 'Unknown' or based on City/Zip Code if available."
  },
  {
    "Column Name": "PkgYear",
    "Type": "float64",
    "Units": "Year",
    "Description": "Year associated with the harvest packaging or record.",
    "Allowed Values / Range": "Range: [2019.0, 2025.0]",
    "Missing %": "19.8",
    "Cleaning / Notes": "Significant missing values. This column may be redundant with 'Year' or represent a different aspect of the harvest timeline. Investigate relationship with 'Year' column. Missing values may need imputation or rows with missing values may need to be excluded if 'Year' is also missing."
  },
  {
    "Column Name": "TotalHarvestPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [-380.53733377132, 911433642.960996]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Contains negative values, which are physically impossible for harvest weight. These values likely represent data entry errors, returns, or system anomalies. Negative values should be investigated and potentially set to zero or null, or the entire row flagged for review."
  },
  {
    "Column Name": "TotalHarvestWetPounds",
    "Type": "float64",
    "Units": "Pounds",
    "Description": "Total wet weight of harvested cannabis in pounds.",
    "Allowed Values / Range": "Range: [0.0002204624420183, 1371869133.03903]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are generally positive, which is expected for wet weight. The upper range is very large, suggesting potential outliers or large-scale operations."
  },
  {
    "Column Name": "UniqueHarvestBatches",
    "Type": "int64",
    "Units": "Count",
    "Description": "Number of unique harvest batches recorded.",
    "Allowed Values / Range": "Range: [1.0, 8875.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Year",
    "Type": "float64",
    "Units": "Year",
    "Description": "Year of the harvest record.",
    "Allowed Values / Range": "Range: [2023.0, 2024.0]",
    "Missing %": "80.2",
    "Cleaning / Notes": "Extremely high percentage of missing values. This column's utility is severely limited. Investigate if 'PkgYear' can serve as a primary year indicator or if 'Year' is intended for a different purpose. Consider dropping this column if 'PkgYear' is more reliable and complete, or imputing based on 'PkgYear' if appropriate."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry errors, system glitches, or misinterpretation of return/adjustment entries. Physically, harvest weight cannot be negative.
    *   **Recommended handling rule:** Investigate the source of negative values. For analysis, consider setting negative values to `0` or `NaN` (Not a Number) and flagging the corresponding rows for further review. If these represent adjustments, a separate column for adjustments might be needed.

*   **Issue:** Invalid `HarvesterZipCode` values, specifically the upper range `961503674.0`.
    *   **Likely cause:** Typographical errors during data entry, concatenation of multiple numbers, or incorrect data type conversion. Standard US zip codes are 5 digits.
    *   **Recommended handling rule:** Filter out or correct zip codes that are not 5-digit numeric values. For values outside the standard range, consider setting them to `NaN` or flagging them as invalid. Impute missing or invalid zip codes using `HarvesterCity` or `HarvesterCounty` if possible, or mark as 'Unknown'.

*   **Issue:** High percentage of missing values in `Year` (80.2%) and significant missing values in `PkgYear` (19.8%).
    *   **Likely cause:** Inconsistent data capture, different reporting standards over time, or `Year` being a derived field that was not consistently populated.
    *   **Recommended handling rule:** Prioritize `PkgYear` as the primary year indicator due to its lower missing rate. Investigate the relationship between `PkgYear` and `Year`. If `Year` is largely redundant or unreliably populated, consider dropping it. For missing `PkgYear` values, if `Year` is present and valid, use it for imputation; otherwise, rows with missing year information may need to be excluded from time-series analyses or flagged.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Pounds:** Identify all records where `TotalHarvestPounds` is less than zero. Set these values to `0` and create a new boolean flag column, `is_harvest_pounds_adjusted`, to indicate rows where this adjustment was made.
2.  **Clean Harvester Zip Codes:** Validate `HarvesterZipCode` values. Convert to integer type. For any zip code that is not a 5-digit number (e.g., values > 99999 or < 10000), set the value to `NaN` and create a flag column, `is_zip_code_invalid`, to mark these records.
3.  **Handle Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, impute missing values with a placeholder string like "UNKNOWN" to ensure consistency and prevent issues with categorical analysis.
4.  **Consolidate Year Information:** Evaluate the `PkgYear` and `Year` columns. If `Year` is predominantly missing and `PkgYear` is more reliable, consider dropping the `Year` column. For remaining missing values in `PkgYear`, if no other reliable year information is available, these rows may need to be excluded from time-based analyses.
5.  **Standardize Data Types:** Ensure all numerical columns (`TotalHarvestPounds`, `TotalHarvestWetPounds`, `UniqueHarvestBatches`, `PkgYear`, `HarvesterZipCode`) are cast to appropriate numeric types (e.g., `float64` or `int64`) after cleaning, and categorical columns (`HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterCounty`) are cast to `category` type for efficiency.

### Limitations & Trust Section

*   **HarvesterZipCode:** The presence of extremely large, invalid zip codes significantly reduces the trustworthiness of this field for precise geographical analysis without extensive cleaning and validation against a known zip code directory.
*   **TotalHarvestPounds:** The existence of negative values indicates potential issues with data capture or reporting logic, requiring careful interpretation of total harvest figures. Without understanding the root cause, aggregated sums may be skewed.
*   **Year Information (PkgYear & Year):** The high percentage of missing values in `Year` and significant missingness in `PkgYear` limits the ability to perform robust time-series analysis or accurately track trends over time. The relationship and intended use of these two year columns are unclear, potentially leading to misinterpretation.
*   **Missing Geographical Data:** While minor, missing `HarvesterCity` and `HarvesterCounty` values can slightly impact geographical distribution analyses. Validation against external geographical data sources would be needed to fully trust these fields.

### Appendix: Quick Reference

*   **Negative Harvest Pounds:** Set to 0; flag rows as `is_harvest_pounds_adjusted`.
*   **Invalid Zip Codes:** Set to `NaN` if not 5-digit numeric; flag rows as `is_zip_code_invalid`.
*   **Missing City/County:** Impute with "UNKNOWN".
*   **Year Column:** Prioritize `PkgYear` due to lower missingness; consider dropping `Year` if redundant.
*   **Data Type Conversion:** Ensure numeric fields are `float64`/`int64` and categorical fields are `category`.
*   **Outlier Check:** Review extremely large values in `TotalHarvestPounds` and `TotalHarvestWetPounds` for plausibility, though no specific anomaly was noted beyond the range.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for anomalies, particularly the treatment of negative `TotalHarvestPounds` and invalid `HarvesterZipCode` values, to ensure they align with business requirements and analytical goals. Special attention should be paid to the decision regarding the `Year` and `PkgYear` columns, confirming that the chosen approach for handling missingness and potential redundancy is appropriate for downstream analysis. Additionally, the inferred units and descriptions for each column should be cross-referenced with domain experts for accuracy.

# Work Documentation

## Table: harvest

**Data Operations:**
The `harvest` table underwent several data operations, including consolidation, cleaning, standardization, integration, feature engineering, and aggregation. Initially, multiple CSV files containing harvest data from different periods (2019-2024, 2023-2024, 2025) were loaded and concatenated into a single comprehensive DataFrame. This combined dataset was then saved to a new CSV file (`Data/Track and Trace Data/Harvest/harvest.csv`) and subsequently re-loaded for further processing.

Column names were standardized by converting them to a consistent lowercase snake_case format (e.g., `HarvesterLicenseNumber` became `harvesterlicensenumber`, `PkgYear` became `year`). Key numerical columns, specifically `year`, `totalharvestpounds`, and `totalharvestwetpounds`, were converted to appropriate numeric data types, with errors coerced to missing values.

Extensive cleaning was performed on the `harvestercounty` column. This involved replacing "NA" and "UNDEFINED" string values with empty strings, followed by a mapping process to standardize various county name representations (e.g., "Alameda County" to "ALAMEDA"). The column values were then stripped of leading/trailing whitespace, and any remaining empty strings or "nan" representations were converted to proper missing values. Rows with unresolved missing `harvestercounty` information were subsequently removed from the dataset.

The cleaned `harvest` data was then integrated with a `package` dataset (which underwent similar cleaning and standardization) using a left merge operation, based on `harvesterlicensenumber` and `year`. This merge enriched the harvest data with related packaging information. Following the merge, new analytical features were engineered, including `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`, to derive insights into the efficiency of cannabis processing. Further cleaning of the `harvestercounty` column was applied to the merged dataset, including replacing empty strings, `<NA>`, and "nan" with missing values, and dropping rows where `harvestercounty` remained missing.

Finally, the integrated data was aggregated at both category and county levels to summarize key metrics. The county-level summary, which included the derived ratios, was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Visualizations were also generated to explore trends in harvest pounds, package pounds, and package-to-harvest ratios for the top 10 counties over time.

**Variables Affected:**
- `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`)
- `HarvesterFacilityType` (renamed to `harvesterfacilitytype`)
- `HarvesterCity` (renamed to `harvestercity`)
- `HarvesterZipCode` (renamed to `harvesterzipcode`)
- `HarvesterCounty` (renamed to `harvestercounty`)
- `PkgYear` (renamed to `year`)
- `TotalHarvestPounds` (renamed to `totalharvestpounds`)
- `TotalHarvestWetPounds` (renamed to `totalharvestwetpounds`)
- `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`)
- New derived variables: `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
- **Data Consolidation:** Multiple CSV files containing harvest data from different periods were combined to create a comprehensive dataset, ensuring all available records were included for analysis.
- **Standardization:** Column names were standardized to a consistent lowercase snake_case format, improving readability and programmatic access. Data types were enforced for numerical columns to ensure accurate calculations and prevent errors during analysis. The `PkgYear` column was explicitly chosen and renamed to `year`, effectively prioritizing it as the primary year indicator, aligning with the data cleaning plan's recommendation due to its lower missingness compared to the original `Year` column.
- **Geographical Data Cleaning:** The `harvestercounty` column underwent extensive cleaning to correct inconsistencies, standardize naming conventions (e.g., mapping "Alameda County" to "ALAMEDA"), and handle missing values. This involved replacing various representations of missing or undefined values, stripping whitespace, and removing rows with unresolvable missing county information to enhance the reliability of geographical analysis.
- **Data Integration:** The cleaned harvest data was integrated with a `package` dataset using a left merge operation on `harvesterlicensenumber` and `year`. This step was crucial for combining related information from different stages of the cannabis production pipeline, enabling a holistic view.
- **Feature Engineering:** New ratio metrics, such as `package_to_harvest_ratio` (total package pounds divided by total harvest pounds) and `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), were calculated. These ratios provide key performance indicators for understanding the efficiency of converting harvested cannabis into packaged products and the wet-to-dry weight conversion process.
- **Aggregation and Summarization:** The integrated data was aggregated at both category and county levels to summarize key metrics, facilitating higher-level analysis of harvest and package quantities and their relationships.
- **Exploratory Visualization:** Visualizations were generated to explore trends and distributions of harvest and package data, as well as the derived ratios, across top counties and over time. This aids in identifying patterns, outliers, and key insights.

**Validation and Verification:**
- Data type conversions for numerical columns included an `errors="coerce"` argument, which automatically converted unparseable values into `NaN`. This implicitly flagged problematic entries for review, rather than causing the script to fail.
- Explicit `dropna` calls were used on the `harvestercounty` column at multiple stages of cleaning to remove records with unresolvable missing geographical information, serving as a direct validation step to ensure data quality for location-based analysis.
- The `county_map` provided a predefined lookup for standardizing county names, ensuring consistency across the dataset.
- The creation of ratio metrics inherently involved division operations. While explicit checks for division by zero were not observed, the use of numeric data types would result in `inf` or `NaN` values for such cases, which would then be handled by subsequent aggregation or visualization steps.

**Results and Outcomes:**
- A unified and cleaned `harvest` dataset was successfully created, combining data from multiple source files into a single `harvest.csv`.
- The `harvestercounty` column was significantly improved in terms of consistency and completeness, making it more reliable for geographical analysis and reporting.
- Key numerical columns (`year`, `totalharvestpounds`, `totalharvestwetpounds`) were correctly typed, enabling accurate calculations and preventing data type-related errors. The `PkgYear` column was effectively utilized as the primary year indicator, aligning with the recommended data cleaning strategy.
- The `harvest` data was successfully integrated with packaging data, creating a more comprehensive view of the cannabis production pipeline and enabling cross-functional analysis.
- New analytical features (`package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`) were derived, offering deeper insights into harvest and packaging efficiency and relationships within the cannabis industry.
- Summarized data at county and category levels was generated and exported to `harvest_package_ratios.xlsx`, providing aggregated views suitable for reporting and further in-depth analysis.
- Visualizations were produced to highlight trends in harvest and packaging volumes and ratios across key geographical areas and years, aiding in data exploration, understanding, and communication of findings.