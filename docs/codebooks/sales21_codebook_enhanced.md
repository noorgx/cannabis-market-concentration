# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information for the Track & Trace project, likely pertaining to cannabis sales within a specific jurisdiction. It captures monthly sales performance across various retailers and item categories. Each row in the `sales21` table represents the total sales and mean price for a specific item category sold by a particular retailer in a given month. The overall data source, collection period, and extraction date are not specified in the provided summary.

**Assumptions:**
*   The `sales21` table contains sales data specifically for the year 2021, based on its name.
*   `totalsales` and `meanprice` are expressed in a local currency, assumed to be USD for documentation purposes.

### Table Inventory

*   **sales21:** Contains aggregated monthly sales data, including total sales and mean price, for various item categories across different retailers.

## Table: sales21

*   **Purpose:** To provide a summary of monthly sales performance for cannabis products, broken down by retailer and item category.
*   **What one row represents:** One row represents the aggregated sales data (total sales and mean price) for a specific item category sold by a unique retailer in a particular month.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key, inferred).
*   **Relationships:** Not explicitly defined in the provided data.
*   **Number of rows and columns:** 242676 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C12-0000233-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., Microbusiness License).",
    "Allowed Values / Range": "Example: Cannabis - Microbusiness License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: Maywood",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer's facility location.",
    "Allowed Values / Range": "[90008.0, 961610393.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": "The upper bound of the range (961610393.0) appears unusually large for a standard 5-digit or 9-digit zip code. Investigate these values for potential data entry errors or concatenated data. Consider flagging or excluding values outside a plausible zip code range."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "This column is entirely missing. It should be excluded from analysis or populated from an external source if county-level aggregation is required."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold (e.g., Pre-Roll Flower).",
    "Allowed Values / Range": "Example: Pre-Roll Flower",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales data.",
    "Allowed Values / Range": "Example: 01-2021",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to a proper datetime format for accurate temporal analysis and filtering."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales amount for the given item category by the retailer in the specified month.",
    "Allowed Values / Range": "[-11837.69, 4268253.77]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. Sales amounts cannot be negative. These values may represent returns, adjustments, or data entry errors. Proposed handling: Flag these records for investigation. For analysis, consider treating them as zero or excluding them, depending on the business context (e.g., if negative sales are not meaningful for revenue calculations)."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per unit",
    "Description": "Average price per unit for the given item category by the retailer in the specified month.",
    "Allowed Values / Range": "[-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative prices are illogical. Infinite values likely result from division by zero (e.g., zero units sold). Proposed handling: Flag negative values for investigation and exclude them from price calculations. Replace infinite values with NaN or zero, or exclude records where meanprice is infinite, as they indicate an underlying data issue (e.g., no sales volume)."
  }
]
```

### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `sales21` table.

*   **Issue:** `RetailerZipCode` contains values significantly outside the typical range for zip codes (e.g., 961610393.0).
    *   **Likely cause:** Data entry errors, concatenation of multiple numbers, or incorrect data type mapping during extraction.
    *   **Recommended handling rule:** Validate zip codes against a known list of valid zip codes or a plausible range. Flag or exclude records with implausible zip codes.
*   **Issue:** `RetailerCounty` is 100% missing.
    *   **Likely cause:** Data was not collected, or the column was not populated during the data generation process.
    *   **Recommended handling rule:** Exclude this column from analysis. If county-level data is critical, it must be sourced externally and joined.
*   **Issue:** `totalsales` contains negative values.
    *   **Likely cause:** Returns, adjustments, or data entry errors. Sales revenue should generally be non-negative.
    *   **Recommended handling rule:** Flag these records for further investigation. For most analytical purposes, negative sales should be treated as zero or excluded, as they can distort aggregate metrics.
*   **Issue:** `meanprice` contains negative values.
    *   **Likely cause:** Similar to `totalsales`, these could be due to returns, adjustments, or errors in calculation. Price per unit should be non-negative.
    *   **Recommended handling rule:** Flag these records. Exclude negative `meanprice` values from any price-related calculations.
*   **Issue:** `meanprice` contains infinite values.
    *   **Likely cause:** Division by zero during the calculation of mean price (e.g., if total sales were recorded but unit sales were zero, or if the denominator for the average was zero).
    *   **Recommended handling rule:** Replace infinite values with `NaN` (Not a Number) or zero, or exclude these records from price analysis. These records indicate a lack of meaningful price data for the given item category and retailer in that month.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from its current object type (e.g., "01-2021") to a standard datetime format (e.g., `YYYY-MM-DD`) to enable proper temporal analysis.
2.  **Address Missing County Data:** Remove the `RetailerCounty` column from the dataset, as it is 100% missing and provides no analytical value in its current state.
3.  **Validate and Clean Zip Codes:** Identify and flag `RetailerZipCode` values that are outside a plausible range (e.g., greater than 99999 for 5-digit codes). Consider truncating or excluding these anomalous records, or investigating their true meaning if possible.
4.  **Handle Negative Total Sales:** Identify records where `totalsales` is negative. Flag these records for review. For aggregate analysis, replace negative `totalsales` values with 0, or exclude them if they represent invalid transactions.
5.  **Handle Anomalous Mean Prices:**
    *   Identify records where `meanprice` is negative. Flag these records and exclude them from price-related calculations.
    *   Identify records where `meanprice` is infinite. Replace these infinite values with `NaN` to prevent errors in statistical calculations, or exclude these records from price analysis.

### Limitations & Trust Section

*   **Missing `RetailerCounty` Data:** The complete absence of `RetailerCounty` data limits geographical analysis at the county level. Trust in any county-level insights derived from this dataset is impossible without external data integration.
*   **Anomalous `RetailerZipCode` Values:** The presence of extremely large `RetailerZipCode` values raises concerns about data integrity. Without clarification, these values cannot be fully trusted for precise geographical mapping or aggregation. Validation against a master zip code list is needed.
*   **Negative `totalsales` and `meanprice`:** The existence of negative sales and mean prices indicates potential issues with data recording or calculation logic. The trustworthiness of these financial metrics is compromised without a clear understanding of their origin (e.g., returns vs. errors).
*   **Infinite `meanprice` Values:** Infinite mean prices suggest underlying issues with unit sales data (e.g., division by zero). This impacts the reliability of average price calculations and requires investigation into the source data.

To validate these elements, it would be beneficial to:
1.  Consult with the data source provider to understand the meaning of negative sales/prices and infinite prices.
2.  Obtain a data dictionary or schema that defines expected ranges and business rules for all fields.
3.  Acquire a master list of valid zip codes for the relevant jurisdiction to cross-reference `RetailerZipCode`.
4.  Investigate the data collection and aggregation process to understand how `RetailerCounty` became entirely missing.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` column to datetime objects.
*   **County Exclusion:** `RetailerCounty` column is to be dropped due to 100% missing values.
*   **Zip Code Validation:** Flag or exclude `RetailerZipCode` values outside plausible ranges.
*   **Negative Sales Handling:** Treat negative `totalsales` as 0 or exclude from revenue calculations.
*   **Negative Price Handling:** Exclude negative `meanprice` values from price analysis.
*   **Infinite Price Handling:** Replace infinite `meanprice` values with `NaN` or exclude from price analysis.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred column descriptions and proposed handling rules, especially for `totalsales` and `meanprice`, to ensure they align with business definitions of sales and pricing. Particular attention should be paid to the `RetailerZipCode` anomalies and the decision to exclude `RetailerCounty`. Confirmation of the assumed currency (USD) and the year of data (2021) is also recommended. The reproducibility of the cleaning plan should be tested against the raw data.

# Work Documentation

## Table: sales21

**Data Operations:**
The `sales21` table, along with sales data from other years (2018-2024), was loaded and concatenated into a single comprehensive sales dataset. During the initial loading of each individual sales file, the `meanprice` and `v1` columns were dropped. Standardized column renaming was applied across the consolidated dataset, affecting columns such as `ItemCategory` (renamed to `itemcategory`), `RetailerLicenseNumber` (to `retailerlicensenumber`), and `Date` (to `date`). The dataset was then sorted by multiple key identifiers for consistency.

A significant portion of the data work focused on cleaning and imputing the `retailercounty` column, which was initially incomplete. This involved:
1.  Replacing "NA" and "UNDEFINED" string values with empty strings.
2.  Merging the sales data with an external license dataset (`parent_temp`) using `retailerlicensenumber` to enrich records with `primary_company` and `cannabiz_county` information. Records present only in the external license data were excluded.
3.  Imputing missing `retailercounty` values from the `cannabiz_county` column (derived from the merged license data) where the `retailercounty` was initially empty.
4.  Applying specific manual county corrections for a set of identified `retailerlicensenumber` values.
5.  Standardizing all `retailercounty` entries to uppercase.
6.  Creating a lookup table of unique `retailerlicensenumber`-`retailercounty` pairs from the cleaned data and merging it back to fill any remaining missing county values.
7.  Extracting the first five digits of `retailerzipcode` to create a `zip5` column.
8.  Merging with an external ZIP-to-county mapping (`zip_df`) to further impute missing `retailercounty` values based on `zip5`.
9.  Applying additional manual county corrections for specific `retailerlicensenumber` values that remained unassigned or incorrect.
10. Finally, all remaining `NaN` values were filled with empty strings, and all columns were converted to string type to ensure consistency.

The `year` was extracted from the `date` column, and both `totalsales` and `year` were converted to numeric data types, with errors coerced to missing values.

For market concentration analysis, the data was aggregated at various levels:
*   Total sales were summed by `retailerlicensenumber` and `year`.
*   Total sales were summed by `primary_company` and `year` (after imputing missing `primary_company` values with `retailerlicensenumber`).
*   Total sales were summed by `retailerlicensenumber`, `retailercounty`, and `year`.
*   Total sales were summed by `primary_company`, `retailercounty`, and `year`.

Market share (`mkt_share`) and squared market share (`mkt_share2`, used for Herfindahl-Hirschman Index - HHI) were calculated for each aggregation level (statewide overall, statewide parent company, county overall, county parent company). All HHI results were then combined into a single `merged` dataframe. Additional metrics like `county_sales`, `county_sales_parent`, and `opacity` were derived for visualization purposes.

Further analytical steps included:
*   Clustering counties based on their HHI trends over time using KMeans.
*   Classifying counties into "increasing," "decreasing," or "stable" HHI trajectories based on linear regression slopes of HHI over time.
*   Calculating the year-over-year percentage change in HHI.
*   Analyzing sales trends by city, which involved reloading the processed sales data, converting `totalsales` to numeric and `date` to datetime, aggregating sales by `date` and `retailercity`, identifying the top 10 cities by total sales, and filtering the data to these top cities.

**Variables Affected:**
*   **Modified:** `meanprice` (dropped), `v1` (dropped), `ItemCategory` (renamed to `itemcategory`), `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerFacilityType` (renamed), `RetailerCity` (renamed), `RetailerZipCode` (renamed), `Date` (renamed to `date`, used to derive `year`), `totalsales` (renamed, converted to numeric).
*   **Created:** `companyid`, `county`, `statelicenseid` (from external license data), `multi_owner`, `primary_company`, `cannabiz_county`, `zip5`, `_merge` (temporary merge indicator), `_merge_lic_county` (temporary merge indicator), `_merge_zip` (temporary merge indicator), `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `totalsales_parent`, `mkt_share2_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.

**Logic and Methodology:**
The overarching goal of the data work was to analyze market concentration and sales trends within the cannabis industry, leveraging the `sales21` data as part of a multi-year sales record. The methodology involved:
1.  **Data Consolidation and Enrichment:** Integrating disparate sales data files and augmenting them with external license information to create a richer dataset suitable for complex analysis.
2.  **Robust Geographical Data Handling:** Addressing significant data quality issues in the `retailercounty` column through a multi-stage imputation process. This was critical for enabling accurate county-level market analysis, which was a key analytical objective.
3.  **Herfindahl-Hirschman Index (HHI) Calculation:** Employing HHI as a standard economic measure to quantify market concentration. Calculations were performed at both overall and parent company levels, and across statewide and county-level geographies, providing a comprehensive view of market structure.
4.  **Temporal Trend Analysis:** Deriving `year` from the `date` column allowed for time-series analysis of HHI, enabling the identification of market evolution and dynamic shifts in concentration.
5.  **Descriptive and Predictive Analytics:** Utilizing clustering (KMeans) and linear regression to categorize and understand the trajectories of HHI across different counties, moving beyond simple descriptive statistics to infer underlying market dynamics.
6.  **Visualization for Insight Generation:** Generating a wide array of plots (line plots, bar plots, box plots, heatmaps, interactive Plotly charts) to effectively communicate complex market concentration trends, sales performance, and data distributions to stakeholders.

**Validation and Verification:**
Several steps were incorporated to validate and verify the data transformations:
*   The use of `indicator=True` during merge operations and subsequent filtering (`df = df[df["_merge"] != "right_only"]`) allowed for explicit tracking of merge outcomes and ensuring that only relevant records were retained.
*   Temporary merge indicator columns (`_merge_lic_county`, `_merge_zip`) were created to monitor the success and source of county imputations, providing transparency into the data lineage.
*   `value_counts(dropna=False)` was explicitly used on the `retailercounty` column after imputation steps, serving as a direct check on the completeness and distribution of the cleaned county data.
*   Numeric conversions (`pd.to_numeric`) with `errors='coerce'` were applied to `totalsales` and `year`, which is a robust way to handle and identify non-numeric entries without crashing the process, indicating a form of data type validation.
*   The extensive use of data visualizations (e.g., HHI trends over time, sales by city) served as a crucial visual validation step, allowing for quick identification of anomalies or unexpected patterns in the processed data.
*   Intermediate data was saved to Stata format (`sales_w_parent_co_test.dta`), which could be reloaded and inspected, facilitating reproducibility and verification of the cleaning process.

**Results and Outcomes:**
The data work successfully produced:
*   A cleaned, integrated, and enriched sales dataset, ready for advanced analytical tasks, stored as `sales_w_parent_co_test.dta`.
*   A comprehensive set of Herfindahl-Hirschman Index (HHI) calculations, providing insights into market concentration at statewide and county levels, for both individual retailers and parent companies, across multiple years.
*   Derived metrics such as market share, county-level total sales, and "opacity" metrics, which quantify the relative size of county markets.
*   Categorization of counties into distinct clusters and trend groups (increasing, decreasing, stable HHI), offering a nuanced understanding of market evolution.
*   Multiple output files including:
    *   `hhi_by_county.csv` and `hhi_by_county_parent.csv` summarizing HHI values.
    *   `HHI_by_county_test.xlsx` containing the final HHI results.
*   A rich suite of visualizations, including static plots (Matplotlib, Seaborn) and interactive HTML plots (Plotly), illustrating:
    *   HHI trends over time by county (overall and parent company level).
    *   HHI trends by identified county clusters and trajectory groups.
    *   Distribution of HHI values by year and county.
    *   Year-over-year HHI percentage change.
    *   Correlation between HHI, total sales, and county sales.
    *   Sales performance over time for top cities.
These outputs provide a robust foundation for understanding market dynamics and competitive landscapes within the cannabis industry.