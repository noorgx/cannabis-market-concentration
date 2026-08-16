# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales and quantity data for cannabis products within the Track & Trace system. It captures transactional information at the retailer and item category level, offering insights into sales performance and product distribution. Each row in the `salesquantity24` table represents the aggregated sales quantity, total sales value, and mean price for a specific item category sold by a particular retailer on a given month. The data is derived from the Track & Trace system, with the `salesquantity24` table specifically covering the year 2024. The exact collection period and extraction date are not explicitly provided but are inferred from the table name and `Date` column.

**Assumptions:**
*   The `salesquantity24` table contains data exclusively for the year 2024.
*   `totalgrams` represents the total quantity sold in grams.
*   `totalsales` represents the total revenue in a local currency (e.g., USD).
*   `meanprice` represents the average price per gram.

### Table Inventory

*   **salesquantity24:** Contains aggregated monthly sales quantities, total sales, and mean prices for various cannabis item categories by individual retailers.

### Table: salesquantity24

*   **Purpose:** To provide a summary of sales performance for different cannabis product categories across various retailers, aggregated monthly.
*   **What one row represents:** One row represents the aggregated sales data (total grams sold, total sales value, and mean price per gram) for a specific `ItemCategory` by a unique `RetailerLicenseNumber` in a given `Date` (month-year).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 60280 rows, 10 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., Microbusiness, Dispensary).",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility. Appears to be stored as a float, potentially including ZIP+4 extensions.",
    "Allowed Values / Range": "90003.0 - 961610393.0",
    "Missing %": 0.3,
    "Cleaning / Notes": "Contains missing values (0.3%). The data type 'float64' and large values (e.g., 902703447.0) suggest ZIP+4 codes might be concatenated and stored numerically, which can lead to issues with leading zeros and geographic analysis. Recommend converting to string and parsing into standard 5-digit ZIP codes."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 0.4,
    "Cleaning / Notes": "Contains missing values (0.4%). Missing values should be investigated; consider imputation based on RetailerCity or RetailerZipCode if a reliable mapping exists, or flag for exclusion if critical for analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product sold (e.g., flowereighth).",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold in grams.",
    "Allowed Values / Range": "0.5 - 160733.51",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "currency (e.g., USD)",
    "Description": "Total sales value for the item category.",
    "Allowed Values / Range": "0.7 - 1346077.99",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "currency/gram (e.g., USD/gram)",
    "Description": "Average price per gram for the item category.",
    "Allowed Values / Range": "0.57 - 112.941176470588",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales data.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Stored as an object (string) in 'MM-YYYY' format. Recommend converting to a datetime object for proper temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerZipCode`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For analysis requiring complete zip code information, rows with missing `RetailerZipCode` should be flagged or excluded. If possible, attempt to impute based on `RetailerCity` or `RetailerLicenseNumber` if a reliable mapping exists in an external reference table.
*   **Issue:** `RetailerZipCode` stored as `float64` with potentially concatenated ZIP+4 values.
    *   **Likely cause:** Data storage convention that combines the 5-digit ZIP code with its 4-digit extension into a single numeric field, then cast to float, losing leading zeros.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Extract the first 5 digits to represent the standard 5-digit ZIP code. This ensures proper handling of leading zeros and facilitates geographic analysis.
*   **Issue:** Missing values in `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** Similar to `RetailerZipCode`, rows with missing `RetailerCounty` should be flagged or excluded if county-level analysis is critical. Imputation could be considered if a reliable mapping from `RetailerCity` or `RetailerZipCode` to `RetailerCounty` is available from an external source.
*   **Issue:** `Date` column stored as an object (string).
    *   **Likely cause:** Default data type assignment during extraction or initial loading.
    *   **Recommended handling rule:** Convert the `Date` column to a proper datetime object for accurate temporal sorting, filtering, and aggregation.

### Reproducible Cleaning Plan

1.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column to a string type. Then, extract the first five characters to represent the standard 5-digit ZIP code, handling any potential leading zeros by padding if necessary.
2.  **Handle Missing `RetailerZipCode`:** For rows where `RetailerZipCode` remains missing after standardization, flag these rows for further investigation or exclude them from analyses requiring complete geographic information.
3.  **Handle Missing `RetailerCounty`:** For rows with missing `RetailerCounty`, flag them. If an external lookup table mapping `RetailerCity` or 5-digit `RetailerZipCode` to `RetailerCounty` is available, attempt to impute missing values. Otherwise, these rows should be excluded from county-level aggregations.
4.  **Convert `Date` Column:** Transform the `Date` column from its current string format (`MM-YYYY`) into a datetime object to enable robust time-series analysis.

### Limitations & Trust Section

The reliability of geographic analysis (city, zip code, county) is currently limited by missing values in `RetailerZipCode` (0.3%) and `RetailerCounty` (0.4%), as well as the non-standard format of `RetailerZipCode`. While `RetailerCity` is complete, its utility for precise geographic segmentation is reduced without complete and accurate zip code and county information. Validation is needed to confirm the accuracy of the `RetailerZipCode` parsing and the completeness of `RetailerCounty` data. An external, authoritative source for retailer addresses and their corresponding geographic identifiers would be beneficial to validate and impute missing or malformed entries.

### Appendix: Quick Reference

*   **ZIP Code Cleaning:** Convert `RetailerZipCode` to string, extract first 5 digits.
*   **Missing ZIP Codes:** Flag or exclude rows with missing `RetailerZipCode`.
*   **Missing Counties:** Flag or exclude rows with missing `RetailerCounty`; impute if external mapping is available.
*   **Date Conversion:** Convert `Date` column to datetime objects for temporal analysis.
*   **Primary Key:** `RetailerLicenseNumber`, `ItemCategory`, `Date` forms the composite primary key.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for missing `RetailerZipCode` and `RetailerCounty` align with analytical requirements. Special attention should be paid to the `RetailerZipCode` conversion logic to ensure accurate extraction of 5-digit ZIP codes and proper handling of leading zeros. Additionally, confirm that the assumed primary key (`RetailerLicenseNumber`, `ItemCategory`, `Date`) accurately represents the uniqueness of each row for downstream analysis.

# Work Documentation

## Table: salesquantity24

**Data Operations:**
The `salesquantity24` table, representing aggregated sales data, was processed through a series of cleaning, transformation, and analytical steps. Initially, multiple sales CSV files (ranging from `sales18.csv` to `sales24.csv`) were loaded and concatenated into a single comprehensive sales DataFrame. During this initial load, columns such as `meanprice` and `v1` were dropped if present, and several columns were renamed for consistency (e.g., `ItemCategory` to `itemcategory`, `RetailerLicenseNumber` to `retailerlicensenumber`).

The sales data was then enriched by merging it with a `parent_df` (derived from a "Licenses" dataset), using `retailerlicensenumber` as the key. This merge incorporated information about primary companies and additional county details from an external source.

Extensive cleaning and imputation were performed on the `retailercounty` column. This involved replacing inconsistent values like "NA" and "UNDEFINED" with empty strings, applying a predefined `county_map` to standardize county names where `retailercounty` was missing, and implementing specific manual fixes for known license numbers. The `retailercounty` column was also converted to uppercase and stripped of whitespace to ensure uniformity. Further imputation was achieved by merging with a `license_county` lookup table and an external `zip_df` (HUD ZIP-County mapping) using a derived 5-digit ZIP code (`zip5`). After these steps, any remaining empty strings, "NA", or "nan" values in `retailercounty` were converted to `pd.NA`, and rows with persistent missing `retailercounty` values were dropped.

The `Date` column was used to extract the `year`, and both `totalsales` and the newly derived `year` column were converted to numeric data types.

The core analytical work involved calculating the Herfindahl-Hirschman Index (HHI) to measure market concentration. This was performed at both statewide and county levels, considering market shares based on total sales for individual retailers and their aggregated parent companies. The results were combined into a single DataFrame, and additional metrics like `opacity` (county sales relative to maximum sales) were calculated.

Finally, the processed data was used to generate various visualizations, including time-series plots of HHI by county. Counties were clustered based on their HHI trends using KMeans, and linear regression was applied to categorize counties into increasing, decreasing, or stable HHI trajectories. Year-over-year HHI percentage changes were calculated, and top counties with significant HHI shifts were identified. Several summary tables and the final processed data were exported to Excel and CSV files for reporting.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerZipCode` (renamed to `retailerzipcode`, used to derive `zip5`), `Date` (renamed to `date`, used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric, aggregated).
*   **Dropped:** `meanprice`, `v1` (if present in source files).
*   **Created:** `companyid`, `county` (renamed to `cannabiz_county`), `statelicenseid` (renamed to `retailerlicensenumber`), `multi_owner`, `primary_company`, `zip5`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.

**Logic and Methodology:**
The methodology focused on creating a robust dataset for market concentration analysis.
1.  **Data Integration and Harmonization:** Multiple years of sales data were combined, and then enriched with external license information to provide a comprehensive view of retailer and parent company structures. This ensured that all relevant attributes were available for analysis.
2.  **Geographic Data Standardization:** A multi-layered approach was implemented to clean and impute `retailercounty` data. This involved initial string replacements, application of a predefined mapping, and two stages of merging with external lookup tables (license-based and ZIP-code-based) to fill missing values. Manual corrections were applied for specific known data inconsistencies. This rigorous process aimed to maximize the accuracy and completeness of geographic identifiers, which are critical for county-level analysis.
3.  **Market Concentration Measurement:** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for market concentration. HHI was calculated by summing the squares of market shares (based on total sales) for individual retailers and, separately, for their parent companies. This was performed at both statewide and county levels to provide granular insights into market structure.
4.  **Temporal Analysis and Trend Identification:** The `Date` column was transformed to extract `year`, enabling the analysis of HHI trends over time. Linear regression was applied to HHI values for each county to classify their market concentration trajectories as increasing, decreasing, or stable. K-Means clustering was also employed to group counties exhibiting similar HHI patterns, providing a data-driven categorization of market evolution.
5.  **Reporting and Visualization:** The results were aggregated into summary tables and visualized using various plot types (line plots, bar charts, heatmaps, scatter plots) to effectively communicate market dynamics, HHI distributions, and year-over-year changes. Key findings were exported to standard file formats for broader accessibility and further review.

**Validation and Verification:**
Data quality was addressed through several validation and verification steps:
*   **Type Coercion and Error Handling:** Columns were explicitly cast to appropriate data types (`str`, `numeric`, `datetime`), with `errors='coerce'` used during numeric conversions to handle non-convertible values gracefully.
*   **Missing Value Management:** A systematic approach to handling missing `retailercounty` values was implemented, involving multiple imputation sources and subsequent dropping of rows where imputation was not possible. This ensured that analyses were performed on complete geographic data.
*   **Duplicate Handling:** Duplicates in auxiliary dataframes (e.g., `parent_df`) were removed prior to merging to prevent data inflation.
*   **Merge Integrity:** Merge operations (`how='left'`, `indicator=True`) were used to monitor the success of joins and identify unmatched records, allowing for targeted investigation and filtering.
*   **Data Standardization:** Consistent string operations (e.g., `.str.upper()`, `.str.strip()`, `.replace()`) were applied to standardize categorical text fields, particularly `retailercounty`, to ensure accurate grouping and analysis.
*   **Visual Inspection:** The generation of numerous plots served as a visual validation step, allowing for quick identification of outliers, unexpected trends, or data inconsistencies that might not be apparent in raw tabular data.

**Results and Outcomes:**
The data work resulted in a refined and analytically ready dataset derived from the original sales data.
*   A comprehensive sales dataset was created, spanning multiple years and enriched with critical retailer and parent company information.
*   Standardized and largely complete geographic information (`retailercounty`, `zip5`) was established, significantly improving the reliability of location-based analyses.
*   Detailed Herfindahl-Hirschman Index (HHI) metrics were calculated, providing a quantitative measure of market concentration at statewide and county levels for both individual retailers and parent companies.
*   Counties were successfully categorized into groups based on their HHI trends (increasing, decreasing, stable), offering actionable insights into market evolution.
*   Key summary tables and visualizations were produced, effectively communicating market structure, sales performance, and HHI dynamics over time. These outputs are suitable for inclusion in formal reports and presentations.
*   Insights into year-over-year HHI changes and the identification of counties experiencing the most significant shifts in market concentration were generated, supporting strategic decision-making.