# Track & Trace Data Codebook

### Overview Section

This dataset, part of the Track & Trace project, provides aggregated sales information for licensed cannabis retailers. It aims to offer insights into sales performance by retailer, item category, and time period. Each row in the `sales18` table represents the aggregated monthly sales data for a specific item category sold by a particular licensed retailer. The overall data source is likely a regulatory or commercial cannabis tracking system, with the collection period inferred to be around 2018 (based on table name `sales18` and `Date` column example "11-2018"). The extraction date is not specified.

**Assumptions:**
*   The `sales18` table contains monthly aggregated sales data.
*   "Track & Trace" refers to a regulatory system for cannabis products.
*   The `Date` column represents the month and year of the sales aggregation.

### Table Inventory

*   **sales18:** Contains aggregated monthly sales data for various item categories by licensed cannabis retailers.

### Table: sales18

*   **Purpose:** To provide a summary of monthly sales performance, broken down by retailer and item category.
*   **What one row represents:** One row represents the total sales and mean price for a specific item category sold by a particular licensed retailer within a given month.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 21 rows, 9 columns
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000004-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer facility is located.",
    "Allowed Values / Range": "Example: PALM SPRINGS",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer facility.",
    "Allowed Values / Range": "922624021",
    "Missing %": 0.0,
    "Cleaning / Notes": "The provided range indicates all observed values are identical (922624021). This may suggest a limited dataset scope or a specific focus on a single zip code."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "This column is entirely missing (100% missing values). It should be either removed or investigated for potential data source issues."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold.",
    "Allowed Values / Range": "Example: Other Concentrate (weight - each)",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales aggregation.",
    "Allowed Values / Range": "Example: 11-2018",
    "Missing %": 0.0,
    "Cleaning / Notes": "This column is currently an object type. It should be converted to a datetime format for proper temporal analysis."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency (e.g., USD)",
    "Description": "Total sales amount for the specified item category by the retailer in the given month.",
    "Allowed Values / Range": "29.5 to 47451.82",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the specified item category by the retailer in the given month.",
    "Allowed Values / Range": "11.4811993069528 to 54.6266666666667",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column is 100% missing.
    *   **Likely cause:** Data was either not collected for this field, or it was lost during extraction/processing.
    *   **Recommended handling rule:** Exclude the column from analysis due to complete lack of data. If county-level analysis is critical, investigate original data sources for recovery.
*   **Issue:** `Date` column is of `object` (string) data type.
    *   **Likely cause:** Dates were stored or extracted as strings.
    *   **Recommended handling rule:** Convert to a proper datetime format for accurate temporal sorting and analysis.
*   **Issue:** `RetailerZipCode` shows a single unique value in the provided range, despite being an `int64`.
    *   **Likely cause:** The provided data sample (21 rows) might originate from a single zip code, or the data extraction was limited to a specific geographic area.
    *   **Recommended handling rule:** No immediate cleaning is required, but this observation should be noted when interpreting geographical insights. Verify with a larger dataset if this pattern holds.

### Reproducible Cleaning Plan

1.  **Convert `Date` column to datetime:** Transform the `Date` column from its current `object` type to a standard datetime format (e.g., YYYY-MM-DD, assuming the first day of the month for aggregation). This enables proper time-series analysis.
2.  **Handle `RetailerCounty` column:** Due to 100% missing values, drop the `RetailerCounty` column from the dataset.
3.  **Validate `RetailerZipCode` consistency:** While not requiring cleaning, document the observation that `RetailerZipCode` appears to be uniform across the current dataset. This step ensures awareness of potential data scope limitations.

### Limitations & Trust Section

*   **`RetailerCounty`:** This column is entirely missing, making any county-level analysis impossible with the current dataset. Validation would require accessing the original data source to determine if this information was ever collected or if it can be recovered.
*   **Geographic Scope:** The `RetailerZipCode` showing a single value suggests a potentially limited geographic scope for the provided data. Trust in broader geographic insights should be tempered until a more diverse dataset is available or the sampling methodology is understood.
*   **Data Source & Collection Period:** The exact data source, comprehensive collection period, and extraction date are not explicitly provided. This limits the ability to fully understand the data's provenance and timeliness.

### Appendix: Quick Reference

*   Convert `Date` column to datetime objects.
*   Drop `RetailerCounty` due to 100% missing values.
*   Note `RetailerZipCode` uniformity; investigate if broader geographic representation is needed.
*   Assume `totalsales` and `meanprice` are in currency (e.g., USD).
*   Recognize `sales18` as monthly aggregated data.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `sales18` and confirm that the proposed handling rules for missing data and data type conversions align with project requirements and data governance policies. Particular attention should be paid to the interpretation of `RetailerZipCode`'s uniformity and whether the assumed geographic scope is acceptable. Additionally, any available information regarding the original data source, collection period, and extraction date should be cross-referenced to enhance the overview section.

# Work Documentation

## Table: sales18

**Data Operations:**
The `sales18` dataset was initially loaded as part of a broader collection of annual sales files, ranging from `sales18.csv` to `sales24.csv`. These individual files were concatenated to form a single, comprehensive sales dataframe (`sales_df`) for longitudinal analysis. During this initial loading and concatenation, the `meanprice` and `v1` columns were systematically dropped if present in any of the individual sales files.

Following concatenation, column names were standardized to a consistent lowercase format (e.g., `RetailerLicenseNumber` became `retailerlicensenumber`, `ItemCategory` became `itemcategory`, `Date` became `date`, and `totalsales` became `totalsales`). The combined sales data was then sorted by multiple key identifiers including retailer license number, county, facility type, city, zip code, date, item category, and total sales.

A crucial step involved enriching the sales data by merging it with an external license dataset (`parent_temp`), using `retailerlicensenumber` as the key. This merge introduced `primary_company` and `cannabiz_county` information. Missing values in the `retailercounty` column were addressed through a multi-stage process: first, "NA" and "UNDEFINED" string values were replaced with empty strings; then, attempts were made to populate empty `retailercounty` entries using the `cannabiz_county` from the merged license data. Several specific manual corrections were applied to `retailercounty` for identified retailer license numbers. The `retailercounty` column was further standardized by converting all values to uppercase and by merging with a pre-computed lookup table of `retailerlicensenumber` to `retailercounty` mappings.

To enhance geographic data, a 5-digit zip code (`zip5`) was extracted from `retailerzipcode`. This `zip5` was then used to merge the sales data with an external HUD ZIP-to-County mapping dataset (`zip_df`), allowing for additional imputation or correction of `retailercounty` values. Further manual county corrections were applied for specific retailer license numbers. An `Unnamed: 0` column, likely an artifact of previous processing, was dropped. All remaining columns were converted to string type, and any lingering missing values were filled with empty strings to ensure data consistency.

The extensively cleaned and enriched sales data was saved as an intermediate Stata file (`sales_w_parent_co_test.dta`) and subsequently reloaded for further processing. The `year` was extracted from the `date` column, and both `totalsales` and `year` were converted to numeric data types, with errors coerced to missing values.

The core analytical work involved calculating the Herfindahl-Hirschman Index (HHI) at various levels of aggregation:
1.  Overall statewide HHI based on individual retailer sales.
2.  Statewide HHI based on primary company sales.
3.  County-level HHI based on individual retailer sales.
4.  County-level HHI based on primary company sales.
These HHI calculations involved aggregating total sales by the respective grouping variables (retailer, primary company, county, year), computing market shares, and then squaring these shares to sum them for the HHI. The various HHI results were then combined and merged into a single `merged` dataframe. Additional `opacity` metrics, representing the relative sales contribution of counties, were calculated.

The `merged` dataframe was then used for several analytical and visualization tasks:
*   Data was filtered to years 2019-2025 for specific trend analyses.
*   Counties were clustered based on their HHI trends over time using KMeans.
*   Linear regression was applied to HHI values over time for each county to categorize them into "increasing," "decreasing," or "stable" HHI trajectories.
*   Year-over-year percentage change in HHI was calculated.
*   Top counties with the largest average HHI increases and decreases were identified.
*   A correlation matrix was computed to examine relationships between HHI, total sales, and county sales.
*   Finally, the processed sales data was re-read from the Stata file, and city-level sales were aggregated by date and city to analyze sales trends over time for the top 10 cities.

**Variables Affected:**
*   **Modified:**
    *   `RetailerLicenseNumber`: Renamed to `retailerlicensenumber`.
    *   `RetailerFacilityType`: Renamed to `retailerfacilitytype`.
    *   `RetailerCity`: Renamed to `retailercity`.
    *   `RetailerZipCode`: Renamed to `retailerzipcode`.
    *   `RetailerCounty`: Renamed to `retailercounty`, extensively cleaned, imputed, and standardized (uppercase).
    *   `ItemCategory`: Renamed to `itemcategory`.
    *   `Date`: Renamed to `date`, used to derive `year`.
    *   `totalsales`: Converted to numeric type, used in aggregations.
*   **Dropped:** `meanprice`, `v1`, `_merge` (temporary), `retailercounty_from_license_county` (temporary), `zip5` (temporary after merge), `retailercounty_from_zip` (temporary), `_merge_zip` (temporary), `Unnamed: 0`.
*   **Created:**
    *   `companyid` (from external license data)
    *   `statelicenseid` (from external license data)
    *   `multi_owner` (indicator for multiple company IDs)
    *   `primary_company` (extracted from `companyid` or `retailerlicensenumber`)
    *   `cannabiz_county` (from external license data)
    *   `zip5` (5-digit zip code extracted from `retailerzipcode`)
    *   `year` (extracted from `date`)
    *   `industry_sales` (total sales for a given year/county)
    *   `mkt_share` (market share of a retailer/company)
    *   `mkt_share2` (squared market share for HHI calculation)
    *   `mkt_share2_parent` (squared market share for parent company HHI)
    *   `totalsales_parent` (total sales for parent company)
    *   `county_sales` (total sales at county level)
    *   `county_sales_parent` (total parent company sales at county level)
    *   `opacity`, `opacity_parent` (metrics based on sales contribution)
    *   `cluster` (KMeans cluster assignment for counties)
    *   `hhi_change` (year-over-year percentage change in HHI)

**Logic and Methodology:**
The overarching objective of the data work was to construct a robust dataset for analyzing market concentration within the cannabis retail sector, specifically using the Herfindahl-Hirschman Index (HHI). This involved integrating sales data from multiple years and enriching it with external license and geographic information.

A key methodological decision was to combine annual sales files into a single longitudinal dataset, enabling time-series analysis of market dynamics. Extensive effort was dedicated to cleaning and imputing the `retailercounty` variable, which was initially entirely missing in the `sales18` table. This was achieved by systematically leveraging information from merged license data (which provided `cannabiz_county`), a ZIP-to-county mapping, and targeted manual corrections. This multi-pronged approach was critical to enable county-level market analysis.

To account for complex ownership structures, a `primary_company` identifier was derived, allowing for HHI calculations at both the individual retailer and the aggregated parent company levels. Market share was consistently defined as a retailer's or company's total sales relative to the total industry sales within a specific year and geographic scope (statewide or county). The HHI was then computed by summing the squares of these market shares, providing a quantitative measure of market concentration.

Beyond static HHI calculation, the methodology extended to dynamic analysis. Linear regression was employed to model HHI trends over time for each county, classifying them into categories of "increasing," "decreasing," or "stable" concentration. KMeans clustering was also applied to group counties exhibiting similar HHI trajectories. These analytical steps aimed to provide deeper insights into the evolution of market structure.

Finally, various visualization techniques were utilized to effectively communicate the findings, including line plots for HHI trends, bar plots for market share comparisons, and heatmaps for multi-dimensional views of market concentration.

**Validation and Verification:**
Data quality and consistency were maintained through several validation and verification steps:
*   **Missing Value Handling:** The `retailercounty` column, initially 100% missing, underwent rigorous imputation using multiple external data sources and manual review, with `value_counts(dropna=False)` used to monitor progress.
*   **Data Type Conversions:** Explicit type conversions (e.g., `pd.to_numeric` with `errors="coerce"`) were applied to `totalsales` and `year` to ensure accurate mathematical operations, gracefully handling any non-numeric entries.
*   **Column Renaming and Standardization:** Consistent lowercase column naming was enforced, improving readability and programmatic access.
*   **Merge Indicators:** The `indicator=True` argument in pandas merge operations provided `_merge` columns, which were used to verify the success and type of merges (e.g., `left_only`, `both`, `right_only`), although these temporary columns were subsequently dropped.
*   **Manual Review and Correction:** Specific manual fixes for `retailercounty` were applied based on identified discrepancies, indicating a level of human oversight in data quality.
*   **String Operations:** Extensive use of `astype(str)`, `str.strip()`, and `replace` functions ensured consistent string formatting and handling of empty strings or "NA" values across various text-based columns.
*   **Intermediate Saves:** Saving the processed data to a Stata file (`sales_w_parent_co_test.dta`) served as a checkpoint, allowing for verification of the data state before subsequent analytical steps.

**Results and Outcomes:**
The data work successfully transformed raw annual sales files into a clean, enriched, and analytically ready dataset. Key outcomes include:
*   **Comprehensive Sales Dataset:** A unified sales dataset spanning multiple years was created, providing a robust foundation for longitudinal market analysis.
*   **Populated Geographic Data:** The `retailercounty` column, which was entirely missing in the original `sales18` codebook, was substantially populated and standardized, enabling detailed county-level market concentration analysis.
*   **Market Concentration Metrics:** A comprehensive set of HHI metrics was computed at statewide and county levels, for both individual retailers and their primary companies, offering granular insights into market concentration dynamics over time.
*   **Market Trend Categorization:** Counties were effectively categorized into "increasing," "decreasing," or "stable" HHI trajectories, providing a dynamic understanding of market evolution.
*   **Visualizations and Insights:** A variety of plots and tables were generated, illustrating HHI trends, sales distributions, market share comparisons, and year-over-year changes, which are crucial for understanding competitive landscapes and informing strategic decisions.
*   **Exportable Results:** Key analytical outputs, such as HHI tables and summary statistics, were exported to CSV and Excel formats, making them readily available for reporting and further analysis.