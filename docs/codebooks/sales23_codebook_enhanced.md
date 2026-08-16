# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information for licensed cannabis retailers, likely as part of a regulatory "Track & Trace" initiative. It captures key details about retailers, item categories, and associated sales metrics over time. Each row in the `sales23` table represents the aggregated sales data for a specific retailer, an item category, and a particular month. The overall data source is inferred to be a regulatory reporting system for cannabis sales. The collection period is inferred to be for the year 2023 based on the table name. The extraction date is not available.

**Assumptions:**
*   The `sales23` table name implies data from the year 2023.
*   `totalsales` and `meanprice` are denominated in USD.
*   `RetailerLicenseNumber` is a unique identifier for each retailer.

### Table Inventory

*   **sales23:** Contains aggregated sales data, including retailer information, item categories, total sales, and mean prices for specific periods.

### Table: sales23

*   **Purpose:** To provide a summary of sales transactions, detailing retailer information, product categories, and key sales metrics for analysis and regulatory oversight.
*   **What one row represents:** One row represents the aggregated sales for a specific `RetailerLicenseNumber`, `ItemCategory`, and `Date`.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 204813 rows, 9 columns
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000633-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Categorization of the retailer's licensed facility type.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the licensed retailer facility is located.",
    "Allowed Values / Range": "Example: LONG BEACH",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer facility. May include 5-digit or 9-digit formats.",
    "Allowed Values / Range": "[90003.0, 961610393.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Consider standardizing to a 5-digit format if consistency is required for geographical analysis or joins."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the licensed retailer facility is located.",
    "Allowed Values / Range": "Example: LOS ANGELES",
    "Missing %": 8.0,
    "Cleaning / Notes": "Significant missing values. Imputation strategy (e.g., based on RetailerZipCode or RetailerCity) or flagging for further investigation is recommended."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product sold.",
    "Allowed Values / Range": "Example: Extract (weight - each)",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales amount for the specified item category by the retailer during the given period.",
    "Allowed Values / Range": "[-29321.63, 9167140.17]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. Likely cause: returns, refunds, or data entry errors. Proposed handling: Flag these rows for review, or exclude them from analyses requiring positive sales figures. Alternatively, treat as legitimate returns if context allows."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per unit",
    "Description": "Average price per unit for the specified item category.",
    "Allowed Values / Range": "[-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative values are likely data entry errors. Infinite values suggest division by zero (e.g., zero quantity sold for a non-zero total sales, or zero total sales for zero quantity). Proposed handling: Flag these rows for review, or exclude them from analyses. Infinite values should be converted to NaN or null for proper numerical operations."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales data.",
    "Allowed Values / Range": "Example: 01-2023",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to a datetime object for proper temporal analysis and filtering."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Negative values in `totalsales`.
    *   **Likely cause:** Data entry errors, processing of returns/refunds without proper accounting for net sales, or system glitches.
    *   **Recommended handling rule:** Flag these records for investigation. For most analytical purposes, these should be excluded or treated as zero if they represent net zero sales after returns. If they represent legitimate returns, they should be handled according to the specific analytical goal (e.g., included in gross sales, or used to calculate net sales).
*   **Issue:** Negative values in `meanprice`.
    *   **Likely cause:** Data entry errors or incorrect calculation logic where total sales or quantity sold were negative.
    *   **Recommended handling rule:** Exclude these records from analyses involving price, as a negative price is not physically meaningful.
*   **Issue:** Infinite values in `meanprice`.
    *   **Likely cause:** Division by zero during calculation (e.g., `totalsales` divided by zero `quantity_sold`). This often occurs when a product is recorded as having sales but no quantity, or vice-versa, or if the quantity field itself is erroneous.
    *   **Recommended handling rule:** Convert infinite values to `NaN` (Not a Number) or `null` to prevent errors in subsequent numerical operations. Exclude these records from analyses requiring valid price information.
*   **Issue:** 8.0% missing values in `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry during retailer registration or reporting.
    *   **Recommended handling rule:** Attempt to impute missing county values using `RetailerZipCode` or `RetailerCity` by cross-referencing with a reliable geographical lookup table. If imputation is not feasible or reliable, flag these records and consider the impact on analyses requiring county-level aggregation.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from its current object format (e.g., "01-2023") to a standard datetime object for consistent temporal analysis.
2.  **Address `RetailerZipCode` Format:** Review `RetailerZipCode` for consistency. If a 5-digit standard is required, truncate or parse the existing values.
3.  **Handle Missing `RetailerCounty` Values:** Impute missing `RetailerCounty` values by joining with an external geographical dataset using `RetailerZipCode` or `RetailerCity`. If imputation is not possible, create a flag column to indicate missing county data.
4.  **Clean `totalsales` Anomalies:** Identify all rows where `totalsales` is negative. Create a flag column (`is_negative_sales`) and consider excluding these rows from analyses that require positive sales figures, or treat them as zero if they represent net zero transactions.
5.  **Clean `meanprice` Anomalies:** Identify all rows where `meanprice` is negative or infinite. Convert infinite values to `NaN`. Create a flag column (`is_anomalous_meanprice`) and exclude these rows from analyses that rely on valid price per unit.

### Limitations & Trust Section

*   **Missing `RetailerCounty` Data:** The 8% missing values in `RetailerCounty` could impact geographical analyses. Validation requires an external, authoritative source to cross-reference retailer addresses or zip codes to their respective counties.
*   **Anomalous `totalsales` and `meanprice`:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry errors, calculation issues, or specific business logic (e.g., returns) that is not fully transparent. Trust in these specific metrics is reduced for the affected rows. Validation would require access to raw transaction data or clarification from the data source on how returns/refunds and zero-quantity sales are handled.
*   **`RetailerZipCode` Format:** The `int64` type and range suggest a mix of 5-digit and potentially 9-digit zip codes, which might require standardization for accurate geographical mapping or joins. Validation would involve confirming the intended format and consistency of zip code entries.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` to datetime objects (e.g., `pd.to_datetime(df['Date'], format='%m-%Y')`).
*   **County Imputation:** Use `RetailerZipCode` to fill missing `RetailerCounty` from a lookup table.
*   **Negative Sales Handling:** Flag `totalsales < 0`. Exclude from sum/average calculations unless specifically accounting for returns.
*   **Negative Mean Price Handling:** Flag `meanprice < 0`. Exclude from price analyses.
*   **Infinite Mean Price Handling:** Convert `meanprice` values of `inf` to `NaN`. Exclude from price analyses.
*   **Zip Code Standardization:** Consider converting `RetailerZipCode` to a consistent 5-digit string format.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative `totalsales` and `meanprice` values, as their treatment can significantly impact analytical outcomes. Confirmation of the primary key assumptions and the overall data representation (what one row means) is also crucial for ensuring the codebook accurately reflects the dataset's structure and content.

# Work Documentation

## Table: sales23

**Data Operations:**
The data from the `sales23` table was integrated into a larger dataset by concatenating it with sales data from other years (2018-2024). This combined sales dataset underwent several cleaning and transformation steps. Initial processing involved loading all sales files as strings and dropping `meanprice` and `v1` columns if present. Key columns were then consistently renamed to lowercase for standardization. The entire dataset was sorted by multiple identifying and temporal columns.

A significant portion of the work focused on enriching and standardizing geographical information. The sales data was merged with an external license dataset to incorporate company and parent company identifiers. The `RetailerCounty` column, which had missing values, was extensively cleaned and imputed using a multi-step approach: replacing "NA" and "UNDEFINED" values, leveraging county information from the merged license data, applying specific manual corrections for known license numbers, and finally, using an external ZIP code-to-county lookup table. The `RetailerZipCode` was truncated to a 5-digit format for this lookup.

Further transformations included extracting the `year` from the `Date` column and converting `totalsales` and the newly extracted `year` to appropriate numeric data types. The dataset was then used to calculate the Herfindahl-Hirschman Index (HHI) for market concentration. This involved grouping data by retailer or parent company and year, summing total sales, calculating market shares, and squaring them to derive the HHI. These calculations were performed at both statewide and county levels, and for both individual retailers and their parent companies. The results were combined and further metrics such as `county_sales` and `opacity` (representing sales relative to maximum statewide sales) were computed.

Finally, the processed data was used for advanced analytical tasks, including clustering counties based on their HHI trends over time using KMeans, and classifying counties into "increasing," "decreasing," or "stable" HHI trajectories through linear regression analysis. Year-over-year HHI percentage changes were calculated, and correlations between HHI, total sales, and county sales were analyzed. Sales data was also aggregated by city to visualize trends for top-performing cities.

**Variables Affected:**
*   `RetailerLicenseNumber`: Renamed to `retailerlicensenumber`, used as a key for merging and grouping.
*   `RetailerFacilityType`: Renamed to `retailerfacilitytype`, used for sorting.
*   `RetailerCity`: Renamed to `retailercity`, used for sorting and city-level aggregations.
*   `RetailerZipCode`: Renamed to `retailerzipcode`, used to derive `zip5` for county imputation.
*   `RetailerCounty`: Renamed to `retailercounty`, extensively cleaned, normalized, and imputed.
*   `ItemCategory`: Renamed to `itemcategory`, used for sorting.
*   `totalsales`: Renamed to `totalsales`, converted to numeric, and aggregated for HHI calculations.
*   `meanprice`: Dropped from the dataset if present in the original files.
*   `Date`: Renamed to `date`, converted to datetime objects, and used to extract the `year`.
*   **New Variables Created/Derived:**
    *   `companyid`, `statelicenseid`, `multi_owner`, `primary_company`, `cannabiz_county`: Introduced from the external license dataset.
    *   `zip5`: A 5-digit representation of the retailer's zip code.
    *   `year`: Extracted numeric year from the `date` column.
    *   `industry_sales`: Total sales for a given year or county-year.
    *   `mkt_share`, `mkt_share2`: Market share and squared market share for HHI calculation.
    *   `mkt_share2_parent`, `totalsales_parent`: Parent company level HHI and total sales.
    *   `county_sales`, `county_sales_parent`: Total sales aggregated at the county level for overall and parent company.
    *   `opacity`, `opacity_parent`: Metrics indicating county sales relative to statewide maximum sales.
    *   `cluster`: A categorical variable assigning counties to clusters based on HHI trends.
    *   `hhi_change`: Year-over-year percentage change in HHI.

**Logic and Methodology:**
The core methodology involved a multi-stage data pipeline designed to integrate, clean, enrich, and analyze sales data.
1.  **Data Integration:** Sales data from `sales23` and other years were combined to form a comprehensive historical view, ensuring consistency in column names and data types across different periods.
2.  **Entity Resolution & Enrichment:** The combined sales data was linked with a separate license dataset using `retailerlicensenumber`. This step was crucial for associating sales records with broader company structures, including `primary_company` (parent company) information, which is vital for market concentration analysis beyond individual licensees.
3.  **Geographical Standardization:** A robust imputation strategy was implemented for `RetailerCounty`. This involved a hierarchical approach: first, leveraging county information from the merged license data, then applying targeted manual corrections, and finally, using an external ZIP code-to-county mapping. This ensured a high degree of completeness and accuracy for geographical analysis.
4.  **Market Concentration Analysis (HHI):** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for assessing market concentration. It was calculated by determining the market share of each entity (individual retailer or parent company) based on their total sales within a defined market (statewide or county-level) and then summing the squares of these market shares. This provides a quantitative measure of competition.
5.  **Temporal and Trend Analysis:** The `Date` column was transformed to extract `year`, enabling time-series analysis of HHI. Linear regression was applied to HHI trends over time for each county to classify them into increasing, decreasing, or stable market concentration trajectories, providing insights into market evolution. Clustering techniques were also employed to identify groups of counties with similar HHI trend patterns.
6.  **Sales Performance Analysis:** Aggregations of `totalsales` by `retailercity` were performed to identify and visualize sales performance in key urban centers.

**Validation and Verification:**
Several steps were taken to ensure data quality and the integrity of transformations:
*   Initial data loading specified `dtype=str` and `keep_default_na=False` to prevent unintended type conversions and ensure explicit handling of missing values.
*   Column renaming was systematically applied to maintain consistency.
*   The `meanprice` column was explicitly dropped, indicating a decision to exclude it from the analysis.
*   During merges, `indicator=True` was used to track merge outcomes, and `validate="many_to_one"` was applied in one instance to confirm expected relationships.
*   Missing values in `RetailerCounty` were systematically addressed through imputation and manual fixes, with intermediate merge codes (`_merge_lic_county`, `_merge_zip`) used to monitor the source of imputed values.
*   Numeric conversions for `totalsales` and `year` used `errors='coerce'`, which automatically converts unparseable values to `NaN`, preventing errors in subsequent calculations.
*   Duplicate rows were removed from the `parent_df` and rows with missing `retailerlicensenumber` were dropped to ensure unique keys for merging.
*   `dropna(subset=...)` was frequently used to remove records with critical missing values after imputation attempts, ensuring that subsequent analyses operate on complete and valid data points.

**Results and Outcomes:**
The data work resulted in a robust, cleaned, and enriched dataset suitable for in-depth market analysis.
*   A comprehensive, multi-year sales dataset was created, integrating `sales23` with other historical data.
*   The `RetailerCounty` column was significantly improved in terms of completeness and standardization, enabling reliable geographical analysis.
*   Detailed Herfindahl-Hirschman Index (HHI) metrics were calculated, providing quantitative insights into market concentration at various levels (statewide, county, retailer, parent company). These results were exported to Stata, Excel, and CSV formats for further use.
*   Counties were successfully categorized by their HHI trend trajectories (increasing, decreasing, stable), offering a dynamic view of market evolution.
*   Visualizations, including line plots, bar charts, box plots, histograms, violin plots, heatmaps, and scatter plots, were generated to effectively communicate HHI trends, distributions, and relationships, as well as sales performance by city. Interactive HTML plots were also produced.
*   Key insights into year-over-year HHI changes and correlations between market concentration and sales volumes were derived.
*   The output includes structured data files and visual reports that can inform regulatory bodies, market participants, and researchers about the competitive landscape and sales dynamics within the cannabis industry.