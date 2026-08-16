# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information from the Track & Trace project, detailing monthly sales performance for various cannabis retailers across different item categories. Each row in the `sales24` table represents a monthly summary of sales for a specific item category by a particular retailer. The data source is the Track & Trace project, with the collection period inferred to be January 2024 based on the 'Date' column. The extraction date is not available.

**Assumptions:**
*   The 'Date' column represents the month and year for which the sales data is aggregated.
*   `totalsales` and `meanprice` are expressed in a standard currency (e.g., USD).

### Table Inventory

*   **sales24:** Contains aggregated monthly sales data for cannabis retailers, including retailer details, item categories, total sales, and mean prices.

## Table: sales24

*   **Purpose:** To provide a summary of monthly sales transactions, detailing sales performance by retailer and item category.
*   **What one row represents:** A monthly sales summary for a specific item category by a unique retailer.
*   **Primary key(s):** Likely composite key: `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 289765 rows, 9 columns
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C10-0000007-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the licensed retailer.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: SAN ANDREAS",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility location.",
    "Allowed Values / Range": "[90003.0, 961610393.0]",
    "Missing %": 0.2,
    "Cleaning / Notes": "Convert to string to preserve leading zeros and handle non-numeric entries. Investigate unusually large values (e.g., 961610393.0) as they may indicate data entry errors or extended zip codes. Impute missing values based on RetailerCity/RetailerCounty if possible."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: CALAVERAS",
    "Missing %": 0.4,
    "Cleaning / Notes": "Impute missing values based on RetailerCity/RetailerZipCode if a reliable mapping exists. Otherwise, flag as 'Unknown'."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold.",
    "Allowed Values / Range": "Example: Vape Cartridge (weight - each)",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency",
    "Description": "Total sales amount for the specified item category by the retailer for the given month.",
    "Allowed Values / Range": "[-154888.11, 1718788.33]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. These likely represent returns, sales adjustments, or data entry errors. Flag these records for investigation. For analyses requiring positive sales, these values may be excluded or set to zero."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the specified item category.",
    "Allowed Values / Range": "[-107.412004160888, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative values likely due to returns/adjustments or calculation errors. Infinite values likely due to division by zero (e.g., zero units sold). Flag these records for investigation. For analyses requiring valid prices, these records should be excluded or imputed (e.g., with the median meanprice for the respective ItemCategory)."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "Month-Year",
    "Description": "Month and year of the sales data aggregation.",
    "Allowed Values / Range": "Example: 01-2024",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for proper temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Returns, sales adjustments, or data entry errors where a net negative sales amount was recorded for an item category in a given month.
    *   **Recommended handling rule:** Flag these records for further investigation. For analyses focused on positive revenue generation, these values should be excluded or set to zero.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these could result from returns, adjustments, or calculation errors where the total sales or quantity sold was negative, leading to a negative average price.
    *   **Recommended handling rule:** Flag these records. For analyses requiring valid positive prices, exclude these records or impute them with a reasonable value (e.g., the median `meanprice` for the specific `ItemCategory`).
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** Division by zero during calculation, implying that zero units were sold for an `ItemCategory` in a given month, but a sales record still exists.
    *   **Recommended handling rule:** Flag these records. For analyses requiring valid prices, exclude these records or impute them with a reasonable value (e.g., the median `meanprice` for the specific `ItemCategory`).
*   **Issue:** `RetailerZipCode` is stored as `float64`, contains missing values (0.2%), and includes unusually large numeric values (e.g., 961610393.0).
    *   **Likely cause:** Data type mismatch during ingestion, potential inclusion of extended zip codes, or data entry errors. Missing values are common in geographical fields.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Investigate and validate values that do not conform to standard 5-digit or 9-digit zip code formats. Impute missing values using `RetailerCity` or `RetailerCounty` if a reliable mapping is available; otherwise, flag as 'Unknown'.
*   **Issue:** Missing `RetailerCounty` data (0.4%).
    *   **Likely cause:** Incomplete data entry or extraction processes.
    *   **Recommended handling rule:** Impute missing values using `RetailerZipCode` or `RetailerCity` if a reliable geographical lookup or mapping can be applied. Otherwise, flag these records as 'Unknown'.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from its current object type (e.g., '01-2024') to a proper datetime object to enable accurate temporal analysis.
2.  **Address Missing Geographical Data:** For `RetailerZipCode` and `RetailerCounty`, attempt to impute missing values by cross-referencing with other available geographical fields (e.g., using a city-to-zip code or zip code-to-county mapping). Any values that cannot be reliably imputed should be flagged as 'Unknown'.
3.  **Correct `RetailerZipCode` Data Type and Format:** Convert the `RetailerZipCode` column to a string data type to preserve leading zeros and accommodate potential non-numeric entries. Validate the format of all zip codes, flagging or correcting entries that do not conform to standard formats (e.g., 5-digit or 9-digit).
4.  **Handle Negative `totalsales`:** Identify and flag all records where `totalsales` is negative. For analyses focused on positive revenue, these values should be set to zero or excluded, depending on the specific analytical objective.
5.  **Address Negative and Infinite `meanprice`:** Identify and flag records where `meanprice` is negative or infinite. For analyses requiring valid positive prices, these records should be excluded or imputed (e.g., with the median `meanprice` for the respective `ItemCategory`) to prevent skewed results.

### Limitations & Trust Section

Several data elements require further validation to ensure full trustworthiness:
*   The missing `RetailerZipCode` (0.2%) and `RetailerCounty` (0.4%) data could impact the accuracy of geographical analyses. The proposed imputation strategy needs to be validated against an authoritative source.
*   The primary key for the `sales24` table is inferred as a composite of `RetailerLicenseNumber`, `ItemCategory`, and `Date`. This assumption requires confirmation from the data source owner to guarantee uniqueness and data integrity.
*   The interpretation of the 'Date' column as representing the month and year of sales aggregation needs explicit confirmation.
*   The `RetailerZipCode` column's `float64` type and the presence of unusually large numeric values suggest potential data quality issues that warrant further investigation and validation against a known zip code directory.

### Appendix: Quick Reference

*   `Date` column converted to datetime objects for temporal analysis.
*   Missing `RetailerZipCode` and `RetailerCounty` values are imputed where possible or flagged as 'Unknown'.
*   `RetailerZipCode` is converted to string type, and its format is validated.
*   Negative `totalsales` values are flagged and handled based on the specific analytical context (e.g., set to zero for revenue calculations).
*   Negative and infinite `meanprice` values are flagged and either excluded or imputed for price-sensitive analyses.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred primary key for the `sales24` table and confirm the interpretation of the 'Date' column. Additionally, please review the proposed handling rules for negative and infinite `totalsales` and `meanprice` values, as well as the strategy for addressing missing and anomalous geographical data, to ensure they align with project objectives and data governance standards. Your feedback on the completeness and clarity of the column descriptions and cleaning notes is also appreciated.

# Work Documentation

## Table: sales24

**Data Operations:**
The `sales24` dataset was integrated into a larger sales dataframe by concatenating it with other historical sales files. During this process, the `meanprice` and `v1` columns were removed from the dataset if they were present. Several columns were renamed for consistency, such as `RetailerLicenseNumber` to `retailerlicensenumber` and `RetailerCounty` to `retailercounty`. Data types were standardized, with `totalsales` and the extracted `year` (from `date`) converted to numeric types, and the `date` column itself converted to datetime objects for temporal analysis.

Extensive cleaning and imputation were performed on geographical data. `retailercounty` values like "NA" and "UNDEFINED" were standardized to empty strings. Missing `retailercounty` values were then imputed through a multi-step process: first, by merging with a separate licenses dataset (`parent_temp`) using `retailerlicensenumber`; second, by extracting a 5-digit zip code (`zip5`) from `retailerzipcode` and merging with a HUD zip-to-county mapping; and finally, by applying several manual corrections for specific `retailerlicensenumber`s. All `retailercounty` values were converted to uppercase, and any remaining empty strings, "NA", or "nan" values were treated as missing and subsequently dropped.

The dataset was enriched by integrating `primary_company` information, derived from the licenses dataset, to identify the primary owning entity for each retailer, especially in cases of multiple owners. This allowed for a more accurate representation of market structure.

Aggregations of `totalsales` were performed by `retailerlicensenumber` and `year`, and also by `primary_company` and `year`, at both statewide and county levels. These aggregations were used to calculate market share and the Herfindahl-Hirschman Index (HHI), a measure of market concentration, for both individual retailers and parent companies.

Further analytical operations included categorizing counties based on the trajectory of their HHI over time (increasing, decreasing, or stable concentration) using linear regression. K-Means clustering was also applied to group counties with similar HHI trends. Various visualizations were generated to illustrate sales trends and HHI dynamics across different dimensions.

**Variables Affected:**
*   `meanprice`: This column was removed from the dataset.
*   `v1`: This column was removed from the dataset.
*   `RetailerLicenseNumber`, `RetailerCounty`, `RetailerFacilityType`, `RetailerCity`, `RetailerZipCode`, `Date`, `ItemCategory`, `totalsales`: These columns were renamed to `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales`, respectively, for standardization.
*   `retailercounty`: Values were extensively cleaned, standardized, and imputed using multiple external data sources and manual corrections to improve data quality and completeness.
*   `retailerzipcode`: This column was used to derive a new `zip5` column, representing the first five digits of the zip code.
*   `date`: Converted from an object type to datetime objects, and a `year` column was extracted from it.
*   `totalsales`: Converted to a numeric type and used as the basis for various aggregations and market share calculations.
*   New variables created include: `primary_company` (identifying the primary owning entity), `zip5` (5-digit zip code), `industry_sales` (total sales for a given industry segment), `mkt_share` (market share percentage), `mkt_share2` (squared market share for HHI calculation), `county_sales` (total sales at the county level), `opacity` (a calculated metric related to sales volume), `cluster` (from K-Means clustering), and `hhi_change` (year-over-year HHI percentage change).

**Logic and Methodology:**
The overarching goal of the data work was to transform raw sales data, including `sales24`, into a robust dataset suitable for in-depth market concentration analysis. The methodology involved several key steps:
1.  **Data Integration:** Combining `sales24` with other sales files created a comprehensive historical sales record, enabling longitudinal analysis.
2.  **Data Standardization and Cleaning:** Column renaming ensured consistency, while rigorous cleaning of geographical data (`retailercounty`, `retailerzipcode`) addressed inconsistencies and missing values. This was critical for accurate location-based analysis. Imputation strategies prioritized reliable external sources (license data, HUD zip-to-county mapping) to fill gaps.
3.  **Enrichment with Ownership Information:** The integration of `primary_company` allowed for a more accurate assessment of market power by aggregating sales under ultimate parent entities rather than just individual licenses.
4.  **Market Concentration Measurement:** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for market concentration. Calculations were performed at multiple granularities (individual retailer vs. parent company, statewide vs. county) to provide a nuanced view of market structure.
5.  **Trend Analysis and Segmentation:** Linear regression was applied to HHI trends over time to classify counties into categories of increasing, decreasing, or stable market concentration. K-Means clustering further segmented counties based on their HHI trajectories, facilitating targeted insights.
6.  **Visualization and Reporting:** The results were visualized using various plotting techniques to effectively communicate complex market dynamics and trends to stakeholders.

**Validation and Verification:**
Throughout the data processing, several validation and verification steps were implicitly or explicitly performed:
*   **Error Handling in Conversions:** Numeric conversions for `totalsales` and `year` used `errors="coerce"`, which converts unparseable values to `NaN`, allowing for identification and handling of problematic entries.
*   **Merge Tracking:** The use of `indicator=True` in merge operations allowed for tracking the origin of records after joins, ensuring that merges were successful and identifying unmatched data.
*   **Manual Data Correction:** Specific manual fixes for known `retailercounty` inconsistencies demonstrated a commitment to data accuracy where automated methods were insufficient.
*   **Missing Value Inspection:** The `value_counts(dropna=False)` method was used to inspect the distribution of key categorical variables like `itemcategory` and `retailercounty` at various stages, confirming the impact of cleaning steps.
*   **Uniqueness Checks:** `drop_duplicates()` was applied to source dataframes like `parent_df` and `license_county` to ensure that mappings used for enrichment were unique and consistent.
*   **Post-Processing Checks:** The final `retailercounty` column was explicitly checked for empty strings, "NA", and "nan" values, which were then dropped to ensure that subsequent analyses were performed on clean geographical data.

**Results and Outcomes:**
The data work successfully produced a refined and enriched sales dataset, saved as `sales_w_parent_co_test.dta`, which is now suitable for advanced market analysis. This dataset includes crucial `primary_company` identification and standardized geographical information. The core outcome is a comprehensive set of HHI metrics, calculated for both individual retailers and parent companies, at statewide and county levels, offering detailed insights into market concentration dynamics over time. These HHI results were exported into several structured files, including `HHI_by_county_test.xlsx`, `hhi_by_county.csv`, and `hhi_by_county_parent.csv`. Furthermore, the analytical processes, including clustering and linear regression, provided a deeper understanding of market concentration trends and identified counties exhibiting distinct HHI trajectories. The generated visualizations effectively communicate these findings, highlighting sales distributions over time by city and correlations between HHI and sales metrics.