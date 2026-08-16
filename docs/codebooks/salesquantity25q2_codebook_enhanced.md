# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales and quantity data from the Track & Trace system, which monitors cannabis product movement within a regulated market. It offers insights into retailer performance, product categories, and sales trends over time. Each row in the `salesquantity25q2` table represents an aggregated sales record for a specific retailer, item category, and month. The overall data source is the Track & Trace system, with a collection period covering Q2 2025. The extraction date is not specified in the provided metadata.

**Assumptions:**
*   The `Date` column represents the month and year of the sales aggregation.
*   Currency values (e.g., `totalsales`, `meanprice`) are denominated in USD.
*   `totalgrams` refers to the total quantity sold in grams.

### Table Inventory

*   **salesquantity25q2:** Contains aggregated sales quantities, total sales values, and mean prices for various item categories by retailer and month.

### Table: salesquantity25q2

*   **Purpose:** To provide a summary of sales performance, including quantities sold, total revenue, and average pricing, for different cannabis product categories across various retailers within a specific period.
*   **What one row represents:** One aggregated sales record for a unique combination of `RetailerLicenseNumber`, `ItemCategory`, and `Date`.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key).
*   **Relationships:**
*   **Number of rows and columns:** 14698 rows, 10 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C10-0000092-LIC",
    "Missing %": "0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": "0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: Perris",
    "Missing %": "0.1%",
    "Cleaning / Notes": "Missing values observed. Consider imputation or flagging for analysis."
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "[90003.0, 961610393.0]",
    "Missing %": "0.3%",
    "Cleaning / Notes": "Stored as float64, should ideally be string or integer. Anomalously large maximum value (961610393.0) suggests data entry errors or non-standard zip codes. Missing values observed. Convert to string and validate against standard zip code formats; flag or correct anomalous values."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: RIVERSIDE",
    "Missing %": "0.5%",
    "Cleaning / Notes": "Missing values observed. Consider imputation or flagging for analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold.",
    "Allowed Values / Range": "Example: flowereighth",
    "Missing %": "0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold in grams.",
    "Allowed Values / Range": "[0.5, 457446.38]",
    "Missing %": "0%",
    "Cleaning / Notes": "Minimum value of 0.5 suggests no zero or negative quantities, which is expected for sales."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the item category.",
    "Allowed Values / Range": "[0.5, 3494699.4]",
    "Missing %": "0%",
    "Cleaning / Notes": "Minimum value of 0.5 suggests no zero or negative sales, which is expected for revenue."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/unit",
    "Description": "Average price per unit for the item category.",
    "Allowed Values / Range": "[0.5, 157.75]",
    "Missing %": "0%",
    "Cleaning / Notes": "Minimum value of 0.5 suggests no zero or negative prices, which is expected."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales aggregation.",
    "Allowed Values / Range": "Example: 04-2025",
    "Missing %": "0%",
    "Cleaning / Notes": "Stored as object, should be converted to a datetime format for proper temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerCity` (0.1%), `RetailerZipCode` (0.3%), and `RetailerCounty` (0.5%).
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, consider imputing with the most frequent value within the same `RetailerLicenseNumber` if available, or flag as 'Unknown'. For `RetailerZipCode`, imputation might be less reliable; consider flagging or excluding rows if the missingness is critical for analysis.
*   **Issue:** `RetailerZipCode` is stored as `float64` and contains an anomalously large maximum value (961610393.0).
    *   **Likely cause:** Incorrect data type assignment during extraction or processing, and potential data entry errors for the anomalous value. Standard US zip codes are 5-digit integers.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Validate values to ensure they conform to standard 5-digit (or 9-digit) zip code formats. Flag or remove rows with non-standard or clearly erroneous zip codes like 961610393.0.
*   **Issue:** `Date` column is of `object` type.
    *   **Likely cause:** Default data type inference during data loading.
    *   **Recommended handling rule:** Convert `Date` to a proper datetime object for accurate temporal analysis and filtering.

### Reproducible Cleaning Plan

1.  **Convert `Date` to Datetime:** Parse the `Date` column from its 'MM-YYYY' object format into a standard datetime object to enable proper time-series analysis.
2.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column from `float64` to a string type. Remove the `.0` suffix if present.
3.  **Validate `RetailerZipCode` Values:** Identify and flag or remove `RetailerZipCode` values that do not conform to standard 5-digit or 9-digit US zip code patterns, including the anomalous `961610393.0`.
4.  **Address Missing Location Data:** For `RetailerCity` and `RetailerCounty`, impute missing values using the most frequent value associated with the respective `RetailerLicenseNumber` if a clear majority exists, otherwise, flag these records as having 'Unknown' location data.
5.  **Review Sales and Quantity Ranges:** Verify that `totalgrams`, `totalsales`, and `meanprice` values remain within plausible business ranges after initial data loading, although the current ranges appear reasonable.

### Limitations & Trust Section

The reliability of geographical analysis based on `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` is limited due to missing values and the data quality issues identified in `RetailerZipCode`. Specifically, the `float64` type and the presence of an extremely large zip code value in `RetailerZipCode` suggest potential data entry or processing errors that require validation against an authoritative source of retailer location data. The `Date` column, while present, requires type conversion to be fully trustworthy for temporal analysis. Validation of these fields against an external retailer master data file would significantly improve data trust.

### Appendix: Quick Reference

*   **Date Conversion:** Convert 'MM-YYYY' string to datetime objects.
*   **Zip Code Type:** Convert `RetailerZipCode` from float to string.
*   **Zip Code Validation:** Flag or remove non-standard `RetailerZipCode` values (e.g., `961610393.0`).
*   **Missing Location:** Impute or flag missing `RetailerCity` and `RetailerCounty` values.
*   **No Negative Sales/Quantities:** Confirm `totalgrams`, `totalsales`, `meanprice` are non-negative.

### Notes for Reviewers

Reviewers should verify the accuracy of the proposed data types and cleaning rules, especially for `RetailerZipCode` and `Date` columns. Particular attention should be paid to the handling of missing location data and the validation of the anomalous zip code value. Confirmation of the assumed currency (USD) and units (grams) for sales and quantity metrics is also crucial for accurate interpretation.

# Work Documentation

## Table: salesquantity25q2

**Data Operations:**
The provided Python scripts do not directly process a table explicitly named `salesquantity25q2`, which is described as covering Q2 2025. However, the scripts perform extensive data cleaning, transformation, and aggregation on a broader `sales_df` dataset, which comprises historical sales data from 2018 to 2024, sourced from the same "Track and Trace Data/Retail" system. The operations performed on this `sales_df` are highly relevant and analogous to the cleaning notes and data quality issues identified for `salesquantity25q2` in the Codebook.

The key data operations performed include:
1.  **Data Loading and Concatenation:** Multiple CSV files containing sales data (e.g., `sales18.csv` through `sales24.csv`) were loaded and combined into a single `sales_df`. During this process, columns like `meanprice` and `v1` were dropped if present.
2.  **Column Renaming:** Standardized column names were applied, mapping original names such as `RetailerLicenseNumber`, `RetailerCounty`, `RetailerZipCode`, `Date`, `ItemCategory`, and `totalsales` to a consistent lowercase format (e.g., `retailerlicensenumber`, `retailercounty`, `retailerzipcode`, `date`, `itemcategory`, `totalsales`).
3.  **Parent Company Integration:** An external `parent_df` (containing license and company information) was loaded, cleaned, and used to derive `primary_company` identifiers. This `parent_df` was then merged with the `sales_df` using `retailerlicensenumber` to enrich sales records with parent company information.
4.  **Location Data Cleaning and Imputation:**
    *   `retailercounty` values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined `county_map` was used to standardize county names (e.g., "Alameda County" to "ALAMEDA").
    *   Missing `retailercounty` values were imputed using information from the merged `parent_df` (`cannabiz_county`) and a `zip_df` (containing ZIP code to county mappings).
    *   Specific manual fixes were applied to `retailercounty` for certain `retailerlicensenumber` values.
    *   `retailercounty` values were converted to uppercase for consistency.
5.  **Zip Code Standardization:** The `retailerzipcode` column was processed to extract the first five digits, creating a `zip5` column. This `zip5` was then used to merge with an external `zip_df` (from HUD data) to further validate and impute `retailercounty` where missing.
6.  **Date and Numeric Type Conversion:** The `date` column (originally 'MM-YYYY' object type) was used to extract a `year` column, which was then converted to a numeric type. The `totalsales` column was also converted to a numeric type, coercing errors.
7.  **Market Concentration (HHI) Calculation:** The cleaned sales data was used to calculate the Herfindahl-Hirschman Index (HHI) at various levels:
    *   Statewide and county-level HHI based on individual retailer sales.
    *   Statewide and county-level HHI based on parent company sales.
    *   These calculations involved grouping data by retailer/parent company and year, summing `totalsales`, calculating market share, and then squaring market shares to derive the HHI.
8.  **Trend Analysis and Clustering:** HHI values were analyzed over time (2019-2024) to identify trends (increasing, decreasing, stable) using linear regression and to group counties into clusters based on their HHI trajectories using KMeans clustering.
9.  **Aggregations and Visualizations:** Various aggregations were performed to summarize sales and HHI metrics. Numerous plots (line plots, bar plots, box plots, histograms, violin plots) were generated to visualize sales trends, HHI distributions, and changes over time.
10. **Data Export:** Intermediate and final processed dataframes, including HHI results, were exported to Stata (`.dta`) and Excel (`.xlsx`) files for further analysis and reporting.

**Variables Affected:**
*   `RetailerLicenseNumber` (renamed to `retailerlicensenumber`): Used as a key for merging and grouping.
*   `RetailerFacilityType` (renamed to `retailerfacilitytype`): Retained.
*   `RetailerCity` (renamed to `retailercity`): Retained.
*   `RetailerZipCode` (renamed to `retailerzipcode`): Standardized, `zip5` extracted.
*   `RetailerCounty` (renamed to `retailercounty`): Cleaned, standardized, and imputed.
*   `ItemCategory` (renamed to `itemcategory`): Retained.
*   `totalsales`: Converted to numeric, aggregated for HHI calculations.
*   `Date` (renamed to `date`): Used to derive `year`, converted to datetime for plotting.
*   `primary_company`: New variable created from `parent_df` to identify ultimate parent entities.
*   `year`: New numeric variable extracted from `date`.
*   `industry_sales`: New variable representing total sales for a given year/county.
*   `mkt_share`: New variable representing market share.
*   `mkt_share2`: New variable representing squared market share (HHI component).
*   `HHI`, `HHI_parent_level`: New variables representing the calculated HHI metrics.
*   `opacity`, `opacity_parent`: New variables indicating relative sales volume.
*   `hhi_change`: New variable for year-over-year HHI percentage change.
*   `cluster`: New variable for HHI trend clusters.

**Logic and Methodology:**
The primary intent behind these transformations is to prepare raw sales data for robust market concentration analysis and trend identification.
*   **Standardization and Imputation:** The extensive cleaning of `RetailerCounty` and `RetailerZipCode` aims to resolve inconsistencies and missingness in geographical identifiers, which are critical for accurate county-level analysis. By leveraging external master data (parent company licenses, HUD zip-to-county mappings) and internal consistency checks (license-to-county mappings), the project sought to create reliable location data.
*   **Date Conversion:** Converting the `Date` column to a proper datetime format and extracting `year` enables accurate temporal analysis, allowing for the study of trends and changes over time.
*   **Parent Company Identification:** Deriving `primary_company` is crucial for understanding market concentration beyond individual licenses, reflecting the true economic entities operating in the market.
*   **HHI Calculation:** The HHI is a standard economic measure of market concentration. Calculating it at both individual retailer and parent company levels, and across statewide and county geographies, provides a comprehensive view of market structure and competition. The use of squared market shares ensures that larger entities contribute disproportionately more to the index, reflecting their greater market power.
*   **Trend Analysis and Clustering:** Applying linear regression to HHI trends and KMeans clustering helps categorize counties based on their market dynamics, facilitating targeted policy or business insights.

**Validation and Verification:**
Several steps were taken to validate and verify the data:
*   **Merge Indicators:** The use of `indicator=True` during merges with `parent_df` and `zip_df` allowed for tracking the source of merged data and identifying records that did not find a match, providing transparency into the imputation process.
*   **Manual Fixes:** Specific manual overrides for known license-to-county discrepancies indicate a level of human review and correction for critical data points.
*   **Data Type Coercion:** Using `errors='coerce'` during numeric conversions for `totalsales` and `year` allowed for identifying and handling non-numeric values gracefully, converting them to `NaN` for subsequent handling.
*   **Missing Value Handling:** Explicitly replacing "NA", "UNDEFINED", and empty strings with `pd.NA` (or `np.nan`) and then dropping rows with missing critical values (e.g., `harvestercounty` in other scripts, or `totalsales` and `date` in sales analysis) ensures that calculations are performed on complete and valid records.
*   **Visualizations:** The generation of various plots (line plots, bar charts, heatmaps, box plots, histograms, violin plots) serves as a visual validation step, allowing for quick identification of outliers, unexpected trends, or data distribution issues.

**Results and Outcomes:**
The data work resulted in a cleaned, standardized, and enriched sales dataset suitable for advanced economic analysis.
*   **Enhanced Data Quality:** Significant improvements were made to the `RetailerCounty` and `RetailerZipCode` fields, addressing critical data quality issues identified in the Codebook. The `Date` column was prepared for temporal analysis.
*   **Market Concentration Metrics:** Comprehensive HHI metrics were computed for various geographical levels (statewide, county) and entity levels (individual retailer, parent company), providing quantitative measures of market concentration.
*   **Trend Insights:** The analysis identified counties with increasing, decreasing, or stable HHI trends, offering insights into evolving market dynamics. Clustering further grouped counties with similar HHI trajectories.
*   **Analytical Outputs:** Several aggregated datasets and visualizations were produced, including HHI summaries, sales over time by city, and detailed HHI trends by county, which are valuable for reporting and further research. These outputs were saved to Stata and Excel files, ready for consumption by analysts and stakeholders.
*   **Foundation for Future Analysis:** The established cleaning and transformation pipeline provides a robust framework for processing future sales data, such as the `salesquantity25q2` dataset, ensuring consistency and reliability in ongoing market intelligence efforts.