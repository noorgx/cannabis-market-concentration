# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales and quantity information for cannabis retailers participating in the Track & Trace project. It captures key metrics such as total grams sold, total sales revenue, and mean price per unit, categorized by retailer, item category, and month. Each row in the `salesquantity23` table represents the aggregated sales and quantity data for a specific item category by a particular retailer within a given month. The overall data source is the Track & Trace system, with the collection period for the provided table being January 2023, as indicated by the 'Date' column. The extraction date is not specified.

**Assumptions:**
*   Currency values (e.g., `totalsales`, `meanprice`) are assumed to be in USD unless otherwise specified by the source system.
*   The `Date` column represents the month and year of the aggregated data.

### Table Inventory

*   **salesquantity23:** This table contains aggregated monthly sales and quantity data for various cannabis item categories across different retailers.

### Table: salesquantity23

*   **Purpose:** To provide a monthly summary of sales volume, revenue, and average pricing for different cannabis product categories across licensed retailers.
*   **What one row represents:** Aggregated sales and quantity data for a specific `ItemCategory` by a `RetailerLicenseNumber` for a given `Date` (month).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key, inferred)
*   **Relationships:**
*   **Number of rows and columns:** 41134 rows, 10 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000908-LIC",
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
    "Allowed Values / Range": "Example: CHULA VISTA",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "Range: [90003.0, 961610393.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "The upper range of zip codes (961610393.0) appears unusually large and may indicate data entry errors or concatenated zip+4 values that need to be parsed or validated against standard zip code formats."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: CONTRA COSTA",
    "Missing %": "8.1",
    "Cleaning / Notes": "8.1% of values are missing. Missing values should be investigated. Potential handling: Impute based on RetailerCity/ZipCode if a reliable mapping exists, or flag as unknown."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold.",
    "Allowed Values / Range": "Example: flowereighth",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold in grams.",
    "Allowed Values / Range": "Range: [0.5, 960114.5]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are expected to be non-negative. The current range confirms this."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the item category.",
    "Allowed Values / Range": "Range: [0.75, 6896017.44]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are expected to be non-negative. The current range confirms this."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/unit",
    "Description": "Average price per unit for the item category.",
    "Allowed Values / Range": "Range: [0.6, 131.3375]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are expected to be non-negative. The current range confirms this."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "Month-Year",
    "Description": "Month and year of the aggregated sales data.",
    "Allowed Values / Range": "Example: 01-2023",
    "Missing %": "0.0",
    "Cleaning / Notes": "Consider converting to a datetime format for easier temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerCounty`.
    *   **Likely cause:** Data entry omissions or unavailability of county information for some retailer records in the source system.
    *   **Recommended handling rule:** Investigate if `RetailerCounty` can be reliably imputed from `RetailerCity` or `RetailerZipCode` using an external lookup table. If not, these records should be flagged, and analyses involving county-level aggregation should account for the missing data or exclude affected rows.
*   **Issue:** Anomalously large values in `RetailerZipCode`.
    *   **Likely cause:** Data entry errors, concatenation of ZIP+4 codes without proper parsing, or inclusion of non-standard postal codes.
    *   **Recommended handling rule:** Validate `RetailerZipCode` against known standard 5-digit or 9-digit (parsed) US zip codes. Records with invalid zip codes should be flagged for review or corrected if a clear mapping exists. For analytical purposes, consider using only the first 5 digits or excluding invalid entries.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from its current 'MM-YYYY' object format to a standard datetime object (e.g., `YYYY-MM-DD` representing the first day of the month) to facilitate time-series analysis.
2.  **Address Missing `RetailerCounty` Values:** Attempt to impute missing `RetailerCounty` values by cross-referencing `RetailerCity` and `RetailerZipCode` with a reliable external geographic lookup table. If imputation is not possible, flag these rows and consider their impact on county-level aggregations.
3.  **Validate `RetailerZipCode`:** Parse `RetailerZipCode` to ensure it conforms to standard 5-digit or 9-digit (parsed) US zip code formats. For values exceeding standard length, attempt to extract the 5-digit base zip code. Flag or exclude records with clearly invalid or unparseable zip codes.
4.  **Verify Non-Negative Values:** Confirm that `totalgrams`, `totalsales`, and `meanprice` columns contain only non-negative values, as indicated by their ranges. While the current data shows no negative values, this is a crucial check for future data imports.

### Limitations & Trust Section

*   **`RetailerCounty` Completeness:** The 8.1% missing data in `RetailerCounty` limits the reliability of analyses requiring complete geographic segmentation at the county level. Validation is needed to determine if these missing values can be accurately imputed or if they represent a systemic data gap.
*   **`RetailerZipCode` Accuracy:** The presence of unusually large values in `RetailerZipCode` suggests potential data quality issues that could affect geographic analysis and retailer identification. Further validation against a comprehensive zip code database is required to ensure accuracy.
*   **Data Granularity:** The data is aggregated monthly. This limits the ability to perform daily or weekly trend analysis without access to more granular source data.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` to datetime objects (e.g., `pd.to_datetime(df['Date'], format='%m-%Y')`).
*   **Missing County Handling:** Impute `RetailerCounty` from `RetailerCity`/`RetailerZipCode` or flag as 'Unknown'.
*   **Zip Code Validation:** Extract 5-digit zip codes from `RetailerZipCode` and validate against a known list of US zip codes.
*   **Non-Negative Checks:** Ensure `totalgrams`, `totalsales`, `meanprice` are `>= 0`.
*   **Primary Key Validation:** Verify uniqueness of the composite key (`RetailerLicenseNumber`, `ItemCategory`, `Date`).

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key and relationships. Special attention should be paid to the proposed handling rules for `RetailerCounty` missing values and `RetailerZipCode` anomalies, ensuring they align with project requirements and data privacy considerations. Additionally, confirm that the interpretation of "one row represents" accurately reflects the business context of the Track & Trace data.

# Work Documentation

## Table: salesquantity23

**Data Operations:**
The `salesquantity23` table, representing aggregated monthly sales and quantity data, underwent significant cleaning, enrichment, and transformation. The process began by consolidating multiple annual sales datasets (from `sales18.csv` through `sales24.csv`) into a single, comprehensive sales dataframe. Key columns were then renamed for consistency with internal naming conventions (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `Date` to `date`, `totalsales` to `totalsales`).

The dataset was enriched by merging it with an external license dataset, which provided `primary_company` and `cannabiz_county` information, enabling analysis at the parent company level. A multi-faceted approach was implemented to clean and impute the `retailercounty` column, which had identified data quality issues. This involved:
1.  Replacing "NA" and "UNDEFINED" string values with empty strings.
2.  Utilizing the `cannabiz_county` from the merged license data to fill in missing `retailercounty` values where available.
3.  Applying specific manual corrections for known `retailerlicensenumber` values with incorrect or missing county information.
4.  Standardizing all `retailercounty` values to uppercase.
5.  Creating a lookup table from existing valid `retailerlicensenumber` and `retailercounty` pairs within the dataset and merging it back to fill additional missing values.
6.  Extracting the first five digits of `retailerzipcode` to create a `zip5` column.
7.  Merging with an external HUD zip-to-county mapping table to impute `retailercounty` based on `zip5`.
8.  Applying further manual corrections for specific `retailerlicensenumber` values that remained unassigned or incorrect.
Finally, any remaining empty strings, "NA", or "nan" values in `retailercounty` were converted to proper missing values, and rows with unresolved missing `retailercounty` were dropped.

The `date` column was used to extract a `year` column, and both `totalsales` and `year` were converted to numeric data types. The cleaned and enriched sales data was then used to calculate the Herfindahl-Hirschman Index (HHI) to measure market concentration. HHI was computed at various levels: statewide overall, statewide by primary parent company, county-level overall, and county-level by primary parent company, using `totalsales` as the market size metric.

Further analytical operations included:
*   Clustering counties based on their HHI trends over time using KMeans.
*   Categorizing counties into "increasing," "decreasing," or "stable" HHI trends by fitting linear regression models to their annual HHI values.
*   Calculating year-over-year percentage changes in HHI.
*   Aggregating `totalsales` by `date` and `retailercity` to analyze sales trends over time for top cities.
*   Computing a correlation matrix between HHI, total sales, and county sales.
The results of these analyses were used to generate various plots (line plots, bar plots, box plots, histograms, violin plots, heatmaps) and exported to Excel and CSV files for reporting.

**Variables Affected:**
*   `RetailerLicenseNumber` (renamed to `retailerlicensenumber`): Used as a key for merging and grouping.
*   `RetailerFacilityType` (renamed to `retailerfacilitytype`): Used for grouping in some aggregations.
*   `RetailerCity` (renamed to `retailercity`): Used for grouping in some aggregations and for plotting sales trends.
*   `RetailerZipCode` (renamed to `retailerzipcode`): Used to derive `zip5` for county imputation.
*   `RetailerCounty` (renamed to `retailercounty`): Subjected to extensive cleaning, imputation, and standardization.
*   `ItemCategory` (renamed to `itemcategory`): Used for grouping in some aggregations.
*   `totalsales`: Converted to numeric, used as the primary metric for HHI calculations and aggregations.
*   `Date` (renamed to `date`): Converted to datetime objects, and `year` was extracted from it.
*   **New Variables Created:**
    *   `primary_company`: Derived from external license data, representing the ultimate parent company.
    *   `cannabiz_county`: An alternative county designation from external license data, used for imputation.
    *   `zip5`: The first five digits of the `retailerzipcode`, used for geographic lookups.
    *   `year`: Extracted numerical year from the `date` column.
    *   `industry_sales`: Total sales for a given year/county, used in market share calculations.
    *   `mkt_share`: Individual retailer/company market share percentage.
    *   `mkt_share2`: Squared market share, a component of HHI.
    *   `mkt_share2_parent`: HHI component at the parent company level.
    *   `totalsales_parent`: Total sales at the parent company level.
    *   `county_sales`, `county_sales_parent`: Aggregated sales at the county level for overall and parent company.
    *   `opacity`, `opacity_parent`: Calculated metrics related to county sales relative to statewide maximum sales.
    *   `cluster`: A categorical variable assigning counties to clusters based on HHI trends.
    *   `hhi_change`: Year-over-year percentage change in HHI.

**Logic and Methodology:**
The core methodology involved a systematic process of data consolidation, enrichment, and rigorous data quality improvement, particularly for geographic identifiers. Multiple annual sales files were combined to create a longitudinal dataset. This was then enriched with external license data to provide a more comprehensive view of retailer ownership and an alternative source for geographic information.

A key focus was on improving the accuracy and completeness of the `retailercounty` column. This was achieved through a hierarchical imputation strategy: first leveraging internal data consistency, then external license data, followed by a standard zip code to county mapping, and finally, targeted manual corrections for persistent anomalies. This multi-step approach aimed to maximize the fill rate and accuracy of county assignments.

Market concentration was quantified using the Herfindahl-Hirschman Index (HHI), calculated at both the individual retailer and parent company levels, and across statewide and county-level geographies. This allowed for a granular understanding of market structure and competition. Temporal analysis was performed by extracting the year from the sales date and tracking HHI trends over time. Linear regression was applied to HHI time series data for each county to objectively categorize their market concentration trajectories as increasing, decreasing, or stable. Clustering techniques were also employed to group counties with similar HHI trend patterns.

The final processed data served as the foundation for generating various analytical outputs, including summary tables and a wide array of visualizations, to communicate insights into market dynamics, geographic distribution of sales, and competitive landscapes.

**Validation and Verification:**
Throughout the data work, several validation and verification steps were implicitly or explicitly performed:
*   **Type Conversion Error Handling:** Numeric conversions for `totalsales` and `year` used `errors="coerce"`, which converts unparseable values to `NaN`, allowing for identification and handling of non-numeric data.
*   **Merge Indicators:** The `_merge` column was used during the initial merge with `parent_temp` to track the success and nature of the merge operations, ensuring that records were correctly joined.
*   **Missing Value Inspection:** `value_counts(dropna=False)` was utilized to inspect the distribution of `itemcategory` and `retailercounty` at various stages, providing visibility into the impact of cleaning and imputation efforts on data completeness.
*   **Explicit Missing Value Handling:** Empty strings and placeholder values ("NA", "UNDEFINED", "nan") were explicitly converted to `pd.NA` before dropping rows with missing `retailercounty`, ensuring consistent handling of missing data.
*   **Data Inspection:** `df.head()` and `df.columns` were used to inspect the dataframe structure and content after significant transformations, confirming expected changes.
*   **Range Checks (Implicit):** While not explicitly coded as validation, the codebook's "Cleaning / Notes" for `totalgrams`, `totalsales`, and `meanprice` indicate an expectation of non-negative values, which would typically be verified in a robust data pipeline. The current code focuses on processing rather than explicit validation of these ranges.
*   **Uniqueness (Inferred):** The grouping operations for HHI calculations implicitly rely on the distinctness of `retailerlicensenumber` and `primary_company` within specific timeframes and geographies, though explicit primary key validation was not observed in the provided snippets.

**Results and Outcomes:**
The data work resulted in a robust, cleaned, and enriched sales dataset that is suitable for advanced market analysis. Key outcomes include:
*   A consolidated sales dataset (`sales_w_parent_co_test.dta`) spanning multiple years, providing a comprehensive historical view.
*   Significantly improved data quality for the `retailercounty` column, leading to more reliable geographic analyses.
*   The ability to analyze sales and market concentration at both individual retailer and parent company levels, enhancing insights into corporate structures.
*   Calculated Herfindahl-Hirschman Index (HHI) values for various market definitions and years, providing quantitative measures of market concentration and competition.
*   Categorization of counties based on their HHI trends (increasing, decreasing, stable), offering a dynamic perspective on market evolution.
*   Identification of top counties experiencing significant HHI increases or decreases, highlighting areas of changing market concentration.
*   A suite of visualizations and summary reports (exported to Excel and CSV) that effectively communicate complex market intelligence, including sales trends, HHI distributions, and geographic market dynamics.
*   Insights into the correlation between HHI, total sales, and county sales, aiding in understanding the drivers of market concentration.