# Track & Trace Data Codebook

### Overview Section

This dataset provides detailed sales transaction records from the Track & Trace project, focusing on cannabis retail operations. It captures key information about retailers, product categories, and sales figures over a specified period. Each row in the `sales25q2` table represents a single sales record or aggregated sales entry for a specific item category at a retailer for a given period. The overall data source is the Track & Trace system, with the collection period inferred to be Q2 2025 based on table and date column names. The extraction date is not specified.

**Assumptions:**
*   The `sales25q2` table contains sales data specifically for the second quarter of 2025.
*   `totalsales` and `meanprice` are denominated in a local currency (e.g., USD).
*   `RetailerLicenseNumber` uniquely identifies a retailer.

### Table Inventory

*   **sales25q2:** Contains detailed sales transaction data, including retailer information, item categories, total sales, and mean prices for Q2 2025.

## Table: sales25q2

*   **Purpose:** To provide granular sales data for cannabis products, enabling analysis of retailer performance, product category trends, and pricing dynamics within the specified quarter.
*   **What one row represents:** One aggregated sales record for a specific item category at a particular retailer for a given period (likely monthly, given the 'Date' format).
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 72325 rows, 10 columns

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "",
    "Missing %": "0.0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., 'Cannabis - Retailer License').",
    "Allowed Values / Range": "",
    "Missing %": "0.0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": "0.1%",
    "Cleaning / Notes": "Missing values observed. Investigate cause; consider imputation or flagging for analysis."
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "90003.0 - 961610393.0",
    "Missing %": "0.3%",
    "Cleaning / Notes": "Missing values observed. Investigate cause; consider imputation or flagging. Anomalous upper range value (961610393.0) suggests potential data entry errors or concatenated zip codes; validate against standard zip code formats."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": "0.5%",
    "Cleaning / Notes": "Missing values observed. Investigate cause; consider imputation or flagging for analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold (e.g., 'Extract (weight - each)').",
    "Allowed Values / Range": "",
    "Missing %": "0.0%",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency",
    "Description": "Total sales amount for the item category.",
    "Allowed Values / Range": "-4.78 - 3311600.34",
    "Missing %": "0.0%",
    "Cleaning / Notes": "Contains negative values. Likely cause: returns, refunds, or data entry errors. Proposed handling: Flag negative values for investigation; consider excluding from sum calculations or treating as zero if confirmed as returns."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the item category.",
    "Allowed Values / Range": "-1.59333333333333 - Infinity",
    "Missing %": "0.0%",
    "Cleaning / Notes": "Contains negative and infinite values. Negative values likely due to negative sales or returns. Infinite values suggest division by zero (e.g., quantity sold was zero). Proposed handling: Flag negative and infinite values; exclude from mean calculations or impute with a reasonable value if context allows."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales record.",
    "Allowed Values / Range": "04-2025",
    "Missing %": "0.0%",
    "Cleaning / Notes": "Currently stored as an object; convert to datetime format for proper temporal analysis."
  },
  {
    "Column Name": "ItemGroup",
    "Type": "object",
    "Units": "",
    "Description": "Broader grouping for item categories (e.g., 'Extract/Concentrate').",
    "Allowed Values / Range": "",
    "Missing %": "0.0%",
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

The dataset exhibits several data quality issues that require attention:

*   **Issue:** Negative values in `totalsales`.
    *   **Likely cause:** These typically indicate returns, refunds, or potential data entry errors where a credit was recorded as a negative sale.
    *   **Recommended handling rule:** Flag these records for further investigation. For aggregate analysis, consider excluding them from positive sales sums or treating them as zero if they represent legitimate returns.
*   **Issue:** Negative values in `meanprice`.
    *   **Likely cause:** Similar to `totalsales`, negative mean prices could result from returns or incorrect calculations based on negative sales figures.
    *   **Recommended handling rule:** Flag these records. Exclude them from average price calculations or treat as `NaN` to prevent skewing statistical measures.
*   **Issue:** Infinite values in `meanprice`.
    *   **Likely cause:** Infinite values usually arise from division by zero, implying that the quantity sold for a particular item category was zero while a sales value was recorded, or a calculation error occurred.
    *   **Recommended handling rule:** Flag these records. Replace infinite values with `NaN` or exclude them from calculations to maintain data integrity.
*   **Issue:** Missing values in `RetailerCity` (0.1%), `RetailerZipCode` (0.3%), and `RetailerCounty` (0.5%).
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, consider imputing based on `RetailerZipCode` if a reliable mapping exists, or flag records with missing geographical information for exclusion from location-based analyses. For `RetailerZipCode`, investigate if it can be inferred from other retailer details or if it's consistently missing for certain retailers.
*   **Issue:** Anomalous upper range for `RetailerZipCode` (e.g., `961610393.0`).
    *   **Likely cause:** Data entry error, concatenation of multiple zip codes, or inclusion of non-standard postal codes. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Validate `RetailerZipCode` values against known zip code formats. Flag or correct values that fall outside expected ranges or formats.

### Reproducible Cleaning Plan

1.  **Convert Date Column:** Convert the `Date` column from object type to a datetime format (e.g., `YYYY-MM-DD` for the first day of the month) to enable proper temporal analysis.
2.  **Handle Missing Geographical Data:** For `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`, identify and flag records with missing values. If possible, impute missing city/county based on a valid zip code mapping; otherwise, exclude these records from geographical analyses.
3.  **Validate RetailerZipCode:** Identify and flag `RetailerZipCode` values that are outside the standard 5-digit or 9-digit US zip code format. Investigate these anomalies for correction or exclusion.
4.  **Address Negative `totalsales`:** Flag all records where `totalsales` is negative. For analyses requiring positive sales, create a derived column `adjusted_totalsales` where negative values are set to 0 or `NaN`.
5.  **Address Negative and Infinite `meanprice`:** Flag all records where `meanprice` is negative or infinite. For analyses requiring valid mean prices, create a derived column `adjusted_meanprice` where these anomalous values are set to `NaN`.
6.  **Document Cleaning Actions:** Maintain a log of all cleaning steps, including the number of records affected and the rationale for each transformation.

### Limitations & Trust Section

The current dataset has several limitations that impact its trustworthiness and the scope of analysis:

*   **Missing Primary Keys and Relationships:** The absence of explicitly defined primary keys and foreign key relationships makes it difficult to ensure data uniqueness, integrity, and to confidently join this table with other potential datasets. Validation of `RetailerLicenseNumber` as a unique identifier is needed.
*   **Geographical Data Incompleteness:** Missing and potentially erroneous `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` values limit the accuracy of location-based analyses and regional aggregations. Validation against a master retailer list or geographical database is required.
*   **Anomalous Sales and Pricing Data:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry errors, system glitches, or unhandled business logic (e.g., returns). Without clear definitions or business rules for these scenarios, the accuracy of aggregated sales and pricing metrics is compromised.
*   **Data Source and Extraction Details:** The lack of specific data source documentation, exact collection period, and extraction date reduces the auditability and reproducibility of the data.

To validate these elements, access to the original Track & Trace system documentation, business rules for sales and returns, and a master list of retailer information (including validated addresses and license numbers) would be crucial.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` column to datetime objects for accurate time-series analysis.
*   **Geographical Data Validation:** Cross-reference `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` with a reliable geographical database.
*   **Handle Missing Geographicals:** Flag or impute missing `RetailerCity`, `RetailerZipCode`, and `RetailerCounty` values.
*   **Negative Sales Handling:** Flag negative `totalsales` values; consider excluding from positive sum calculations.
*   **Anomalous Price Handling:** Flag negative and infinite `meanprice` values; exclude from average price calculations.
*   **Zip Code Correction:** Identify and correct or flag non-standard `RetailerZipCode` entries.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions and proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative and infinite values in `totalsales` and `meanprice`, as their appropriate handling depends heavily on business context. Additionally, please confirm the assumptions made regarding the dataset's scope and currency. Feedback on potential primary keys or relationships with other Track & Trace tables would be highly valuable for enhancing data integrity.

# Work Documentation

## Table: sales25q2

**Data Operations:**
The provided Python code does not directly process a table named `sales25q2` or data specifically for Q2 2025. Instead, it processes a broader historical sales dataset (`sales_df`) covering years 2018-2024, which shares a similar structure and column names with the `sales25q2` table described in the Codebook. The following operations were performed on this `sales_df` and related datasets:

*   **Data Ingestion & Concatenation:** Multiple historical sales CSV files (from 2018 to 2024) were loaded and combined into a single DataFrame (`sales_df`). All columns were initially read as strings, and empty strings were preserved.
*   **Column Management:**
    *   Columns named `meanprice` and `v1` were removed from the `sales_df` if present.
    *   Several columns were consistently renamed for standardization (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `ItemCategory` to `itemcategory`, `Date` to `date`, `totalsales` to `totalsales`).
*   **Data Sorting:** The dataset was sorted by multiple key identifiers and temporal columns (`retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, `totalsales`) to ensure consistent ordering.
*   **External Data Integration:** The sales data was enriched by performing a left merge with a `parent_df` (derived from an external "Cannabis Market Intelligence Platform Report - Licenses" CSV) using `retailerlicensenumber` as the key. Records present only in the `parent_df` were excluded.
*   **Geographical Data Cleaning & Imputation:**
    *   Missing or undefined `retailercounty` values ("NA", "UNDEFINED", empty strings) were standardized.
    *   A predefined `county_map` was applied to normalize county names (e.g., "Alameda County" to "ALAMEDA"), primarily using `cannabiz_county` (from the merged `parent_df`) to fill in initially missing `retailercounty` values.
    *   Specific `retailerlicensenumber` values had their `retailercounty` manually corrected based on known data issues.
    *   All `retailercounty` values were converted to uppercase for consistency.
    *   Missing `retailercounty` values were further imputed by:
        1.  Leveraging existing `retailercounty` information associated with a `retailerlicensenumber` across the dataset.
        2.  Truncating `retailerzipcode` to 5 digits (`zip5`) and merging with an external `zip_df` (a HUD ZIP-to-County mapping) to fill in additional missing county information.
    *   More manual corrections were applied to `retailercounty` for specific `retailerlicensenumber` values.
    *   Finally, any remaining empty strings, "NA", or "nan" in `retailercounty` were converted to missing values (`pd.NA`), and rows with missing `retailercounty` were dropped to ensure data quality for geographical analysis.
*   **Data Type Conversion:** `totalsales` and `year` (extracted from the `date` column) were converted to numeric types, with errors coerced to `NaN` to prevent processing failures.
*   **Hierarchical HHI Calculation:** The Herfindahl-Hirschman Index (HHI) was calculated at multiple levels of aggregation:
    *   Overall (individual retailer) and Parent Company level.
    *   Statewide and County-level.
    *   This involved grouping data by `retailerlicensenumber` or `primary_company` (parent company ID), `retailercounty`, and `year`, summing `totalsales`, calculating market share, and then squaring and summing market shares.
    *   `primary_company` was imputed with `retailerlicensenumber` where it was missing to ensure all entities were accounted for in parent company analysis.
*   **Derived Metrics:** New columns such as `industry_sales`, `mkt_share`, `mkt_share2`, `county_sales`, `county_sales_parent`, `opacity`, and `opacity_parent` were created to support HHI analysis and visualization.
*   **Clustering and Trend Analysis:** K-Means clustering was applied to HHI trends over time to identify groups of counties with similar market concentration patterns. Linear regression was used to categorize counties into "increasing," "decreasing," or "stable" HHI trajectories based on the slope of HHI values over years (from 2019 onwards).
*   **Percentage Change Calculation:** Year-over-year percentage change in HHI was calculated to show dynamic shifts in market concentration.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales` to understand relationships between market concentration and sales volumes.
*   **Aggregation for Visualization:** Sales data was aggregated by `date` and `retailercity` to analyze sales trends over time for the top 10 cities by total sales.
*   **Output Generation:** Various intermediate and final results were exported to CSV and Excel files (e.g., `sales_w_parent_co_test.dta`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`). Numerous plots were generated and displayed using `matplotlib`, `seaborn`, and `plotly`, with some saved as HTML files for interactive viewing.

**Variables Affected:**
*   **Modified:** `meanprice` (dropped), `v1` (dropped), `ItemCategory` (renamed to `itemcategory`), `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, cleaned, imputed, normalized), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `Date` (renamed to `date`, converted to datetime, `year` extracted), `totalsales` (renamed to `totalsales`, converted to numeric), `primary_company` (imputed, converted to numeric).
*   **Created:** `companyid`, `county`, `statelicenseid`, `multi_owner`, `primary_company`, `licenseNumber`, `zip5`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Validated:** `retailercounty`, `retailerzipcode`, `totalsales`.

**Logic and Methodology:**
The primary objective of the data work was to prepare a comprehensive sales dataset for in-depth market concentration analysis using the Herfindahl-Hirschman Index (HHI). A multi-step data cleaning and imputation process was employed for geographical information (`retailercounty`, `retailerzipcode`) by leveraging internal data consistency, external mapping files (HUD ZIP-to-County), and targeted manual corrections. This meticulous approach aimed to maximize the completeness and accuracy of location data, which is critical for reliable county-level analysis. HHI was calculated at both individual retailer and parent company levels, and for both statewide and county-level scopes, to provide a granular view of market concentration dynamics. This involved standard market share calculations and subsequent aggregation. Time-series analysis was performed on HHI values to understand trends over years, including categorizing counties by their HHI trajectory (increasing, decreasing, stable) using linear regression. Clustering techniques were applied to group counties with similar HHI trend patterns, aiding in identifying distinct market dynamics. Sales data was aggregated and visualized to provide insights into overall market performance and city-level contributions.

**Validation and Verification:**
Data type conversions for numeric fields (`totalsales`, `year`) were performed with error coercion, indicating an awareness of potential data inconsistencies and a strategy to handle them gracefully. Merge indicators (`_merge`, `_merge_lic_county`, `_merge_zip`) were utilized during data integration steps to track the success and source of merged records, serving as an internal validation mechanism. Explicit dropping of rows with missing `retailercounty` after multiple imputation attempts suggests a commitment to a high standard of geographical data quality for subsequent analyses. The code includes steps to identify and handle empty strings, "NA", and "nan" values, demonstrating a focus on data completeness and consistency. The generation of numerous plots and summary tables serves as a visual and statistical verification of the transformations and calculations, allowing for quick identification of anomalies or unexpected results.

**Results and Outcomes:**
A cleaned, standardized, and enriched historical sales dataset (`sales_w_parent_co_test.dta`) was produced, suitable for advanced analytical tasks. Comprehensive HHI metrics were calculated across various geographical and organizational levels (statewide, county, retailer, parent company) and over time (2018-2024). Insights into market concentration trends were generated, including the identification of counties with increasing, decreasing, or stable HHI, and clusters of counties with similar HHI trajectories. Key summary tables and visualizations were created, providing a clear overview of sales performance, market concentration, and geographical dynamics. The analysis identified top-performing cities and counties, as well as those experiencing significant shifts in market concentration. The output files (CSV, Excel, HTML plots) provide actionable data and visualizations for further reporting and decision-making.