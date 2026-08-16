```markdown
# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information for licensed cannabis retailers within the Track & Trace project. Each row in the `sales25` table represents a summary of sales for a specific item category by a particular retailer during a given month. The data is intended to offer insights into retail sales performance and product distribution. The overall data source is the Track & Trace system, with the collection period and extraction date currently unspecified.

**Assumptions:**
*   The `sales25` table contains aggregated sales data, likely summarized monthly, given the `Date` column format.
*   `totalsales` represents the total revenue generated for the specified item category by the retailer in that period.
*   `meanprice` represents the average price per unit for the specified item category.

### Table Inventory

*   **sales25:** Contains aggregated monthly sales data for cannabis retailers, including retailer demographics, item categories, total sales, and mean prices.

## Table: sales25

*   **Purpose:** To provide a summarized view of sales performance for various item categories across different licensed cannabis retailers over time.
*   **What one row represents:** One row represents the aggregated sales data for a specific `ItemCategory` by a unique `RetailerLicenseNumber` for a particular `Date` (month).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key, inferred).
*   **Relationships:**
*   **Number of rows and columns:** 71102 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000400-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: SANTA ANA",
    "Missing %": "0.1",
    "Cleaning / Notes": "Missing values should be investigated. Consider imputation if patterns are found, or flagging for exclusion if critical."
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "Range: [90003.0, 961610393.0]",
    "Missing %": "0.3",
    "Cleaning / Notes": "Missing values should be investigated. The range includes values that appear to be concatenated ZIP+4 codes or potentially erroneous entries (e.g., 961610393.0). These should be validated against a standard ZIP code directory and potentially truncated or corrected."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: ORANGE",
    "Missing %": "0.5",
    "Cleaning / Notes": "Missing values should be investigated. Consider imputation based on RetailerCity or flagging for exclusion."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product sold.",
    "Allowed Values / Range": "Example: Flower (packaged eighth - each)",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the specified item category by the retailer in the given period.",
    "Allowed Values / Range": "Range: [-27.0, 1154419.92]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Contains negative values. Negative sales are anomalous and likely indicate returns, adjustments, or data entry errors. These should be investigated; consider setting to 0 or excluding from aggregate calculations, or flagging for further review."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per unit",
    "Description": "Average price per unit for the specified item category.",
    "Allowed Values / Range": "Range: [-Infinity, 388.51]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Contains negative and infinite values. Negative prices are anomalous and likely indicate data errors. Infinite values typically arise from division by zero (e.g., total sales divided by zero units sold). Negative values should be investigated and potentially set to 0 or excluded. Infinite values should be handled by setting to null or 0, or excluding the row, as they represent invalid calculations."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "Month-Year",
    "Description": "Month and year of the sales aggregation.",
    "Allowed Values / Range": "Example: 01-2025",
    "Missing %": "0.0",
    "Cleaning / Notes": "Should be converted to a datetime object for proper temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `sales25` table.

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Data entry errors, processing errors, or potentially legitimate (but unusual) returns/adjustments that result in a net negative for the period.
    *   **Recommended handling rule:** Investigate the business logic for negative sales. For analytical purposes, consider treating these as zero sales or excluding them from calculations of positive revenue. Flag these records for further review by data owners.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these are likely data entry or processing errors. A physical product cannot have a negative price.
    *   **Recommended handling rule:** Treat these as invalid. Set `meanprice` to `NULL` or `0` for these records, or exclude the entire row from analyses that rely on valid pricing. Flag for review.
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** This typically occurs when `totalsales` is divided by a quantity of zero (e.g., `total_sales / 0_units`). This suggests a record where sales revenue was reported but no units were sold, or the unit count was erroneously zero.
    *   **Recommended handling rule:** Treat these as invalid. Set `meanprice` to `NULL` or `0` for these records, or exclude the entire row from analyses. Flag for review.
*   **Issue:** Missing values in `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, attempt to impute based on `RetailerLicenseNumber` if historical data exists, or use a general 'Unknown' category. For `RetailerZipCode`, validate existing values and impute missing ones based on `RetailerCity` or `RetailerCounty` if possible, otherwise flag as unknown.
*   **Issue:** Anomalous `RetailerZipCode` values (e.g., `961610393.0`).
    *   **Likely cause:** Potential concatenation of ZIP+4 codes without proper formatting, or data entry errors.
    *   **Recommended handling rule:** Standardize `RetailerZipCode` to a 5-digit format. For values exceeding 5 digits, attempt to parse as ZIP+4 and retain only the 5-digit ZIP. Validate against a known list of valid 5-digit US zip codes. Flag or set to `NULL` any values that remain invalid after this process.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from `object` type (e.g., "01-2025") to a standard datetime format (e.g., `YYYY-MM-DD` representing the first day of the month) to enable proper temporal analysis.
2.  **Address Missing Geographic Data:** For `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`, identify and flag rows with missing values. Attempt to impute missing `RetailerCity` and `RetailerCounty` values using a lookup table based on `RetailerLicenseNumber` if available, or fill with 'Unknown'.
3.  **Clean RetailerZipCode:** Convert `RetailerZipCode` to string type. For values longer than 5 digits, attempt to extract the first 5 digits. Validate all zip codes against a list of valid 5-digit US zip codes. Flag or set to `NULL` any values that remain invalid after this process.
4.  **Handle Negative `totalsales`:** Identify all rows where `totalsales` is less than 0. For analytical purposes, these values will be set to 0, and a new flag column (`is_negative_sales_adjusted`) will be created to indicate these adjustments.
5.  **Handle Negative and Infinite `meanprice`:** Identify all rows where `meanprice` is less than 0 or is infinite. These values will be set to `NULL`, and a new flag column (`is_anomalous_price_adjusted`) will be created to indicate these adjustments.

### Limitations & Trust Section

The trustworthiness of the `sales25` dataset is impacted by several factors:

*   **Incomplete Geographic Data:** Missing values in `RetailerCity`, `RetailerZipCode`, and `RetailerCounty` reduce the ability to perform granular geographic analysis. Validation against an external, authoritative source of retailer addresses is needed.
*   **Anomalous Sales and Price Data:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry errors, processing issues, or unusual business events (e.g., large returns). Without further context or validation, these fields may not accurately reflect true sales performance. A clear understanding of the business rules for returns and adjustments is needed to validate these anomalies.
*   **Inferred Primary Key:** The primary key (`RetailerLicenseNumber`, `ItemCategory`, `Date`) is inferred. Confirmation from the data source owner is required to ensure uniqueness and integrity.
*   **Zip Code Accuracy:** The wide range and format of `RetailerZipCode` suggest potential inaccuracies or non-standard storage. Validation against a current, authoritative zip code database is crucial.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` column to datetime objects (e.g., `YYYY-MM-01`).
*   **Missing Geographic Data:** Impute or flag missing `RetailerCity`, `RetailerZipCode`, `RetailerCounty`.
*   **Zip Code Standardization:** Truncate `RetailerZipCode` to 5 digits and validate against known US zip codes.
*   **Negative Sales Handling:** Set `totalsales < 0` to `0` and flag.
*   **Anomalous Price Handling:** Set `meanprice < 0` or `meanprice = Infinity` to `NULL` and flag.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for the `sales25` table. Special attention should be paid to the proposed handling rules for negative and infinite `totalsales` and `meanprice` values, ensuring they align with business requirements for analysis. Additionally, the approach to standardizing and validating `RetailerZipCode` should be reviewed for robustness and accuracy against official geographic data sources. Confirmation of the data collection period and extraction date would also be beneficial.

# Work Documentation

## Table: sales25

**Data Operations:**
*   **Data Ingestion and Consolidation:** Multiple `sales*.csv` files (from 2018 to 2024) were loaded and concatenated into a single dataset. Notably, during this process, the `meanprice` and `v1` columns were explicitly dropped if present. This deviates from the Codebook's cleaning plan which specified handling for negative and infinite `meanprice` values.
*   **Column Renaming:** Column names were standardized to a consistent snake_case format (e.g., `ItemCategory` to `itemcategory`, `RetailerLicenseNumber` to `retailerlicensenumber`).
*   **Data Sorting:** The dataset was sorted by `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales`.
*   **External Data Integration (Parent Company Information):** The sales data was left-merged with an external "Cannabis Market Intelligence Platform Report - Licenses" dataset (`parent_temp`) using `retailerlicensenumber`. This introduced `primary_company` and `cannabiz_county` into the sales dataset.
*   **Geographic Data Cleaning and Imputation (`retailercounty`):**
    *   Initial cleanup: "NA" and "UNDEFINED" string values in `retailercounty` were replaced with empty strings.
    *   Imputation from Cannabiz data: Missing `retailercounty` values were filled using `cannabiz_county` from the merged parent company data, based on a predefined mapping.
    *   Manual corrections: Specific `retailercounty` values were manually updated for certain `retailerlicensenumber` entries.
    *   Standardization: `retailercounty` values were converted to uppercase.
    *   Self-imputation: A lookup table of unique `retailerlicensenumber`-`retailercounty` pairs was created from the existing data and used to fill further missing `retailercounty` values.
    *   Imputation from ZIP code data: The first five digits of `retailerzipcode` were extracted to create a `zip5` column. This `zip5` was then used to merge with an external HUD ZIP-to-County mapping (`zip_df`) to impute additional missing `retailercounty` values.
    *   Final manual corrections: Another set of specific `retailercounty` values were manually updated.
    *   Missing value handling: Remaining `NaN` values were filled with empty strings, and the entire dataframe was converted to string type before an intermediate save. The Codebook's plan to flag missing geographic values was not explicitly implemented; instead, imputation was prioritized.
*   **Date and Numeric Conversion:** The `date` column was used to extract a `year` column, and both `totalsales` and `year` were converted to numeric types for analysis. The `date` column itself was not consistently converted to a datetime object for the primary HHI calculation path, which partially deviates from the Codebook's recommendation.
*   **Market Concentration Analysis (Herfindahl-Hirschman Index - HHI):**
    *   Aggregated sales data by `retailerlicensenumber` (or `primary_company`), `year`, and `retailercounty`.
    *   Calculated `industry_sales` (total sales for a given year/county/grow type).
    *   Computed `mkt_share` (market share) and `mkt_share2` (squared market share).
    *   Aggregated `mkt_share2` to derive HHI values at statewide and county levels, for both individual retailers and parent companies.
    *   **Note on `totalsales`:** The Codebook's cleaning plan to set negative `totalsales` to 0 and flag them was not implemented; negative values were retained in the dataset for HHI calculations.
*   **Trend Analysis and Clustering:** HHI data was used for linear regression to identify increasing, decreasing, or stable HHI trends by county, and K-Means clustering was applied to group counties based on HHI trends.
*   **Visualization Data Preparation:** Data was prepared for various plots, including line plots of HHI over time, bar plots of HHI by county, and plots of HHI change.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales`.
*   **City-level Sales Analysis:** Monthly total sales were aggregated by `retailercity` and `date` to analyze sales trends for the top 10 cities.

**Variables Affected:**
*   **Modified:** `retailercounty`, `retailerzipcode` (used to derive `zip5`), `date` (used to derive `year`), `totalsales` (converted to numeric).
*   **Created:** `primary_company`, `cannabiz_county`, `zip5`, `_merge_lic_county`, `_merge_zip`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Dropped:** `meanprice`, `v1`.

**Logic and Methodology:**
*   The primary intent was to consolidate sales data, enrich it with retailer ownership and geographic information, and then analyze market concentration using the Herfindahl-Hirschman Index (HHI).
*   A robust imputation strategy was employed for `retailercounty`, leveraging multiple external and internal data sources (Cannabiz license data, HUD ZIP-to-County mapping, and internal consistency checks) to maximize geographic coverage and accuracy. Manual fixes addressed specific known data issues. The approach prioritized imputation over flagging missing values, which was a deviation from the Codebook's recommendation.
*   HHI calculations were performed at different granularities (statewide vs. county, individual retailer vs. parent company) to provide a comprehensive view of market concentration dynamics.
*   Trend analysis and clustering aimed to categorize counties based on their HHI evolution over time, providing insights into market stability or shifts.
*   The explicit dropping of the `meanprice` column suggests that this variable was either deemed unreliable or not relevant for the specific market concentration analysis being performed, despite its description and cleaning notes in the original Codebook. Similarly, the non-implementation of the negative `totalsales` handling suggests a different analytical approach or an oversight regarding data quality issues identified in the Codebook.

**Validation and Verification:**
*   Merge indicators (`_merge_lic_county`, `_merge_zip`) were used internally during the merging process to track the source of `retailercounty` values and identify records that were matched or updated.
*   `value_counts(dropna=False)` was used to inspect the distribution of `itemcategory` and `retailercounty` at various stages, indicating checks for completeness and consistency.
*   The `retailercounty` column was explicitly checked for `NA`, `UNDEFINED`, empty strings, and `nan` values at multiple points, with corresponding cleaning actions.
*   Numeric conversions (`pd.to_numeric`) used `errors="coerce"` to handle non-numeric values gracefully, converting them to `NaN`.
*   The final HHI results were rounded and converted to integer/string types for export, implying a final review of data types.
*   **Discrepancy Note:** It is important to note that the explicit validation and handling rules for negative `totalsales` and negative/infinite `meanprice` as outlined in the Codebook's "Reproducible Cleaning Plan" were not observed in the provided Python code. The `meanprice` column was dropped, and negative `totalsales` values were retained without adjustment or flagging.

**Results and Outcomes:**
*   A cleaned and enriched `sales` dataset (`sales_w_parent_co_test.dta`) was produced, containing standardized column names, imputed geographic information, and `primary_company` identifiers.
*   Comprehensive HHI metrics were calculated for various geographic and ownership levels, providing quantitative measures of market concentration.
*   Trend analysis identified counties with increasing, decreasing, or stable HHI trajectories.
*   Clustering grouped counties with similar HHI trends.
*   Several output files were generated (`Cult_HHI_DeepDive.xlsx`, `Cult_HHI_Summary.csv`, `Cult_Size_vs_HHI.csv`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`), containing the calculated HHI values and related metrics, ready for further reporting and visualization.
*   Various plots (Matplotlib, Plotly) were generated to visualize sales trends, HHI over time, and HHI changes, providing visual insights into market dynamics.
```