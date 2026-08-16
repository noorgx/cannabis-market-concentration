# Track & Trace Data Codebook

### Overview Section

This dataset provides detailed sales quantity and value information for cannabis products within the Track & Trace project. It captures transactional summaries at the retailer level, categorized by product type and reported for specific periods. Each row in the `salesquantity20` table represents the aggregated sales data for a particular item category at a specific licensed retailer for a given month. The overall data source is the Track & Trace system, with the collection period implied to be around 2020 based on the table name and date examples. The exact extraction date is not available.

**Assumptions:**
*   The `Date` column in `salesquantity20` represents a month-year period (MM-YYYY).
*   `totalsales` is denominated in USD.
*   `totalgrams` refers to the total weight in grams.

### Table Inventory

*   **salesquantity20:** Contains aggregated monthly sales quantities, total sales revenue, and mean prices for various cannabis product categories sold by licensed retailers.

## Table: salesquantity20

*   **Purpose:** To provide a summary of sales performance, including quantities sold, total revenue, and average pricing, for different cannabis product categories across various retailers.
*   **What one row represents:** One monthly sales record for a specific item category at a particular licensed retailer.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 38758 rows, 10 columns

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "e.g., C10-0000182-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., Cannabis - Retailer License).",
    "Allowed Values / Range": "e.g., Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "e.g., REDWAY",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "object",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "e.g., 95560",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "e.g., TUOLUMNE",
    "Missing %": 99.9,
    "Cleaning / Notes": "High percentage of missing values (99.9%). This column is largely unreliable for analysis. Consider imputation from RetailerZipCode or RetailerCity if a reliable mapping exists, otherwise flag as unreliable or exclude from analyses requiring county data."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product sold (e.g., flower, edibles).",
    "Allowed Values / Range": "e.g., flowereighth",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales record.",
    "Allowed Values / Range": "e.g., 01-2020",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for proper temporal analysis. Assumed format is MM-YYYY."
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold in grams for the given period.",
    "Allowed Values / Range": "[0.4819415, 478256.2]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Values are non-negative, which is expected for quantities."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue in USD for the item category for the given period.",
    "Allowed Values / Range": "[0.63, 5803939.28]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Values are non-negative, which is expected for sales revenue."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/gram",
    "Description": "Average price per gram for the item category for the given period, typically calculated as totalsales / totalgrams.",
    "Allowed Values / Range": "[0.5, 367.82]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Values are non-negative and within a plausible range for cannabis pricing."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column has 99.9% missing values.
    *   **Likely cause:** Data was either not collected, not recorded, or failed to be extracted for this field during the data generation process.
    *   **Recommended handling rule:** Due to the overwhelming percentage of missing values, this column should be flagged as unreliable for direct analysis. If county-level analysis is critical, consider attempting to impute values based on `RetailerZipCode` or `RetailerCity` using an external, validated mapping dataset. Otherwise, exclude it from analyses requiring complete geographical information.

### Reproducible Cleaning Plan

1.  **Handle Missing County Data:** Evaluate the necessity of the `RetailerCounty` column for downstream analysis. If required, attempt to impute missing values using a reliable external mapping from `RetailerZipCode` or `RetailerCity`. If not critical or imputation is unreliable, exclude the column from the analytical dataset.
2.  **Standardize Date Format:** Convert the `Date` column from its current object (string) type to a proper datetime object (e.g., `YYYY-MM-DD` or `YYYY-MM-01` to represent the start of the month). This will enable accurate temporal filtering and aggregation.
3.  **Verify Numeric Data Types:** Confirm that `totalgrams`, `totalsales`, and `meanprice` are correctly interpreted as numeric (float64) types to prevent calculation errors.

### Limitations & Trust Section

The `RetailerCounty` column is highly unreliable due to 99.9% missing values. Any analysis relying on county-level granularity would be severely compromised or impossible without significant imputation efforts, which would introduce assumptions and potential inaccuracies. The interpretation of the `Date` column as representing a month-year period (MM-YYYY) is an assumption based on the example format; validation with the data source owner would confirm this. The absence of explicit primary key constraints or relationship definitions in the provided metadata means these were inferred and should be verified.

### Appendix: Quick Reference

*   **County Data:** `RetailerCounty` is 99.9% missing; do not use for direct analysis without imputation.
*   **Date Conversion:** Convert `Date` (MM-YYYY) to datetime objects for temporal analysis.
*   **Numeric Validation:** `totalgrams`, `totalsales`, `meanprice` are float64 and non-negative.
*   **Primary Key:** `RetailerLicenseNumber`, `ItemCategory`, `Date` is the inferred composite primary key.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `salesquantity20` and confirm the assumed MM-YYYY format for the `Date` column. Additionally, any proposed imputation strategy for `RetailerCounty` should be thoroughly reviewed for its methodology and potential impact on data integrity and analytical outcomes. The descriptions and units for all columns should be cross-referenced with source system documentation if available.

# Work Documentation

## Table: salesquantity20

**Data Operations:**
*   **Data Ingestion & Consolidation:** Multiple annual sales CSV files (e.g., `sales18.csv` through `sales24.csv`) were loaded and concatenated into a single comprehensive sales dataset.
*   **Column Management:** The `meanprice` and `v1` columns were dropped from the dataset if present. Several columns were renamed to a consistent lowercase format (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `Date` to `date`, `ItemCategory` to `itemcategory`, `totalsales` to `totalsales`).
*   **Data Sorting:** The dataset was sorted by `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales` for consistency.
*   **License Data Integration:** The sales data was left-merged with an external "Cannabis Market Intelligence Platform Report - Licenses" dataset (`parent_temp`) using `retailerlicensenumber`. This merge enriched the sales data with `primary_company` (parent company identifier) and `cannabiz_county` information. Rows that only existed in the license data after the merge were excluded.
*   **County Data Standardization & Imputation (Multi-stage):**
    *   Initial cleaning replaced "NA" and "UNDEFINED" values in `retailercounty` with empty strings.
    *   A predefined mapping (`county_map`) was used to standardize `cannabiz_county` values (e.g., "Alameda County" to "ALAMEDA").
    *   Missing `retailercounty` values were imputed using the `cannabiz_county` from the merged license data.
    *   Specific `retailerlicensenumber` values had their `retailercounty` manually corrected based on a predefined list.
    *   A consistent `retailercounty` was established for each `retailerlicensenumber` by creating a unique license-to-county mapping and applying it to fill remaining missing values.
    *   The `retailerzipcode` was truncated to a 5-digit `zip5` and merged with an external HUD ZIP-to-County mapping (`zip_df`). Missing `retailercounty` values were further imputed using this zip-code-based county information.
    *   Additional manual corrections were applied to `retailercounty` for specific `retailerlicensenumber` values.
    *   Finally, all `retailercounty` values were converted to uppercase, and any remaining empty strings or "NA" values were converted to `pd.NA` and subsequently dropped, ensuring a clean county column.
*   **Data Type Conversion:** `totalsales` was converted to a numeric type, and `year` (extracted from the `date` column) was also converted to numeric.
*   **Herfindahl-Hirschman Index (HHI) Calculation:**
    *   HHI was calculated at four levels of granularity: statewide based on individual retailer sales, statewide based on parent company sales (where `primary_company` was imputed from `retailerlicensenumber` if missing), county-level based on individual retailer sales, and county-level based on parent company sales.
    *   Calculations involved summing `totalsales` to determine `industry_sales` (per year/county), computing `mkt_share` (market share), and then `mkt_share2` (squared market share) for the HHI.
*   **Derived Metrics:** `county_sales`, `county_sales_parent`, `opacity`, and `opacity_parent` were calculated to provide context on sales volume relative to the statewide maximum.
*   **Temporal Analysis:** HHI data was filtered to focus on years 2019-2025 for trend analysis.
*   **Clustering Analysis:** K-Means clustering was applied to the HHI data (excluding 2018) to group counties with similar HHI trends.
*   **Trend Trajectory Analysis:** Linear regression was used to determine the slope of HHI change over time for each county, classifying them into "increasing," "decreasing," or "stable" categories based on predefined thresholds.
*   **Sales Trend Analysis:** Total sales over time were aggregated by `retailercity` for the top 10 cities.
*   **HHI Change Calculation:** Year-over-year percentage change in HHI was calculated for each county.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales`.
*   **Data Export:** Various aggregated and processed datasets were exported to Stata (`.dta`), Excel (`.xlsx`), and CSV (`.csv`) formats, including `sales_w_parent_co_test.dta`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, and `HHI_by_county_test.xlsx`.
*   **Visualization Generation:** Numerous plots (line plots, bar plots, box plots, histograms, violin plots, heatmaps, scatter plots) were generated using Matplotlib, Seaborn, and Plotly to visualize HHI trends, distributions, and changes, both overall and by county/cluster. HTML files for interactive plots were also generated.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `Date` (renamed to `date`, used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric, used in aggregations).
*   **Dropped:** `meanprice`, `v1`, `_merge`, `_merge_lic_county`, `_merge_zip`, `Unnamed: 0`, `retailercounty_from_zip`.
*   **Created:** `primary_company`, `cannabiz_county`, `zip5`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Validated:** `retailercounty`, `totalsales`, `year`.

**Logic and Methodology:**
The primary objective of the data work was to prepare a comprehensive sales dataset for market concentration analysis using the Herfindahl-Hirschman Index (HHI). This involved integrating sales data from multiple years, enriching it with license and parent company information, and meticulously cleaning and imputing missing geographical data, particularly for the `retailercounty` column, which was noted as highly unreliable in the original codebook. The multi-stage imputation strategy for `retailercounty` leveraged information from the license dataset, manual corrections, and zip code mappings to maximize data completeness and accuracy. Once the data was prepared, HHI was calculated at various levels (statewide, county, overall, and parent company) to provide a granular view of market concentration. Further analysis involved identifying temporal trends in HHI, clustering counties based on their HHI trajectories, and visualizing these insights to understand market dynamics. The dropping of `meanprice` suggests a focus on total sales and market share rather than average pricing for the HHI analysis.

**Validation and Verification:**
Data validation was embedded throughout the cleaning process. Merge indicators (`_merge`, `_merge_lic_county`, `_merge_zip`) were used to track the success and nature of data joins. Explicit dropping of rows with missing `retailercounty` values after multiple imputation attempts ensured that only records with reliable county information were used for analysis. Data types were explicitly converted to numeric where appropriate, with error handling (`errors="coerce"`) to identify non-numeric values. The consistency of `retailercounty` was enforced by converting it to uppercase and standardizing values using a mapping. Visualizations (plots) were extensively used to inspect trends and distributions, serving as a form of qualitative validation for the calculated metrics and identified patterns.

**Results and Outcomes:**
The data work successfully produced a robust and enriched sales dataset suitable for market concentration analysis. Key outcomes include:
*   A consolidated sales dataset spanning multiple years with standardized and largely complete `retailercounty` information.
*   Integration of parent company identifiers, allowing for HHI calculations at both individual retailer and parent company levels.
*   Calculated HHI metrics for California statewide and for individual counties, providing quantitative measures of market concentration.
*   Identification of county clusters based on HHI trends and classification of counties into increasing, decreasing, or stable HHI trajectories.
*   Generation of numerous analytical outputs (CSV, Excel, Stata files) and comprehensive visualizations (plots) that illustrate market dynamics, HHI trends over time, and geographical variations in market concentration.
*   The work provides a foundation for understanding competitive landscapes within the cannabis market, addressing a critical data quality issue identified in the original codebook (`RetailerCounty`).