# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information related to the Track & Trace project, likely pertaining to regulated product sales within specific retail contexts. Each row in the `sales22` table represents an an aggregated sales record for a particular retailer, item category, and date, summarizing total sales and mean price. The overall data source, collection period, and extraction date are not specified in the provided information.

**Assumptions:**
*   The data pertains to regulated product sales, potentially cannabis, given the "Track & Trace" context and column names like "RetailerLicenseNumber" and "ItemCategory" (e.g., "Pre-Roll Flower").
*   `totalsales` and `meanprice` are expressed in a local currency (e.g., USD).

### Table Inventory

*   **sales22:** Contains aggregated sales data, including retailer information, item categories, total sales amounts, and mean prices for specific dates.

## Table: sales22

*   **Purpose:** To provide a summary of sales transactions, including retailer details, product categories, and financial metrics, aggregated by an unspecified granularity (likely monthly, given the 'Date' format).
*   **What one row represents:** An aggregated sales record for a specific retailer, item category, and date.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 271042 rows, 9 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C9-0000034-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., Cannabis - Retailer Nonstorefront License).",
    "Allowed Values / Range": "Example: Cannabis - Retailer Nonstorefront License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer is located.",
    "Allowed Values / Range": "Example: CULVER CITY",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer's location.",
    "Allowed Values / Range": "Range: [90008.0, 961610393.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Some values appear to be concatenated ZIP+4 codes (e.g., 902306965). Standardize to 5-digit ZIP code for consistency and joinability."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer is located.",
    "Allowed Values / Range": "Example: LOS ANGELES",
    "Missing %": 9.7,
    "Cleaning / Notes": "Approximately 9.7% of values are missing. Consider imputation using RetailerCity/ZipCode or flagging records with missing county for further investigation."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the item sold (e.g., Pre-Roll Flower).",
    "Allowed Values / Range": "Example: Pre-Roll Flower",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency",
    "Description": "Total sales amount for the aggregated record.",
    "Allowed Values / Range": "Range: [-58292.28, 7820938.99]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. This likely indicates returns, refunds, or data entry errors. Recommend flagging these records and investigating their cause. For analysis, consider treating negative values as zero or excluding them, depending on the analytical objective."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the item within the aggregated record.",
    "Allowed Values / Range": "Range: [-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative values likely indicate returns or calculation errors. Infinite values typically result from division by zero (e.g., total sales divided by zero quantity). Recommend flagging these records. For analysis, negative values could be treated as zero or excluded. Infinite values should be converted to NaN/null or excluded, as they are not meaningful for statistical analysis."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales record.",
    "Allowed Values / Range": "Example: 01-2022",
    "Missing %": 0.0,
    "Cleaning / Notes": "Currently stored as an object (string). Convert to a datetime format for proper temporal analysis and filtering."
  }
]
```

### Data Quality & Anomalies Section

The `sales22` table exhibits several data quality issues that require attention before analysis.

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Returns, refunds, or erroneous data entry where sales amounts were recorded as negative.
    *   **Recommended handling rule:** Flag records with negative `totalsales` for investigation. For most analyses, these values should be treated as zero or excluded, as negative sales are not typically meaningful in aggregate.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these could stem from returns, refunds, or calculation errors where the average price was derived from negative sales or quantities.
    *   **Recommended handling rule:** Flag records with negative `meanprice`. Treat as zero or exclude for analysis.
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** Division by zero during the calculation of `meanprice`, implying zero quantity sold for a non-zero sales amount, or an error in the underlying data.
    *   **Recommended handling rule:** Convert infinite `meanprice` values to `NaN` (Not a Number) or `null`. These records should be excluded from calculations involving `meanprice`.
*   **Issue:** Missing `RetailerCounty` values (9.7%).
    *   **Likely cause:** Incomplete data entry or data collection.
    *   **Recommended handling rule:** For records with missing `RetailerCounty`, attempt to impute based on `RetailerCity` and `RetailerZipCode` using an external lookup table. If imputation is not feasible or reliable, flag these records and consider their impact on county-level analyses.
*   **Issue:** `RetailerZipCode` contains concatenated ZIP+4 codes.
    *   **Likely cause:** Data entry or system design that stores the extended ZIP code without separation.
    *   **Recommended handling rule:** Extract the first five digits to standardize `RetailerZipCode` to a standard 5-digit format for consistency and easier geographical analysis.

### Reproducible Cleaning Plan

1.  **Standardize `RetailerZipCode`:** Extract the first five digits from the `RetailerZipCode` column to ensure a consistent 5-digit format.
2.  **Handle Missing `RetailerCounty`:** Attempt to impute missing `RetailerCounty` values by cross-referencing `RetailerCity` and the standardized `RetailerZipCode` with a reliable external geographic lookup table. If imputation is not possible, flag these records.
3.  **Address Negative `totalsales`:** Identify and flag all records where `totalsales` is less than zero. For analytical purposes, replace these negative values with `0` or exclude the records, depending on the specific analysis.
4.  **Address Negative `meanprice`:** Identify and flag all records where `meanprice` is less than zero. For analytical purposes, replace these negative values with `0` or exclude the records.
5.  **Handle Infinite `meanprice`:** Convert all infinite values in the `meanprice` column to `NaN` (Not a Number) to prevent errors in statistical calculations.
6.  **Convert `Date` to Datetime:** Transform the `Date` column from its current object (string) type to a proper datetime format (e.g., 'YYYY-MM-DD' or 'YYYY-MM-01') to enable robust temporal analysis.

### Limitations & Trust Section

The current dataset lacks explicit primary key definitions and relationships between tables, which limits the ability to confidently join data or enforce referential integrity. The absence of a clear data source, collection period, and extraction date also impacts data provenance and the ability to assess its timeliness and completeness.

Specifically:
*   **Primary Keys and Relationships:** Without defined primary and foreign keys, the uniqueness of rows and the integrity of potential joins with other tables cannot be guaranteed. This requires validation if other tables are introduced.
*   **Inferred Descriptions:** Column descriptions were inferred from names and examples. Validation with domain experts is needed to confirm their accuracy and completeness.
*   **Missing `RetailerCounty`:** The 9.7% missing rate for `RetailerCounty` could lead to biased or incomplete geographical analyses if not properly addressed or if imputation is inaccurate.
*   **Anomalous Financial Data:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential issues in data collection, entry, or calculation. The exact cause needs to be validated with the data source owners to understand the true nature of these anomalies (e.g., actual returns vs. data errors).

### Appendix: Quick Reference

*   **Zip Code Standardization:** `RetailerZipCode` will be truncated to 5 digits.
*   **Missing County Handling:** `RetailerCounty` will be imputed where possible; otherwise, records will be flagged.
*   **Negative Sales:** `totalsales` < 0 will be flagged and treated as 0 or excluded.
*   **Negative Mean Price:** `meanprice` < 0 will be flagged and treated as 0 or excluded.
*   **Infinite Mean Price:** `meanprice` = Infinity will be converted to `NaN`.
*   **Date Conversion:** `Date` column will be converted to a datetime object.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions and the proposed handling rules for anomalies, especially for `totalsales` and `meanprice`. Confirmation of the data's source, collection methodology, and any existing data dictionaries would greatly enhance the codebook's completeness and the reproducibility of the cleaning plan. Additionally, feedback on the assumed currency unit and the interpretation of "Track & Trace" context is welcome.

# Work Documentation

## Table: sales22

**Data Operations:**
The `sales22` data, along with sales data from other years (`sales18.csv` through `sales24.csv`), was concatenated into a single comprehensive sales dataset. This combined dataset underwent several cleaning, transformation, and integration steps to prepare it for market concentration analysis and sales trend visualization.

Initial cleaning involved dropping the `meanprice` column entirely, as well as an auxiliary `v1` column if present, addressing the identified issues of negative and infinite values in `meanprice`. Column names were standardized to a consistent format (e.g., `ItemCategory` to `itemcategory`, `RetailerLicenseNumber` to `retailerlicensenumber`). The dataset was then sorted by multiple key identifiers to ensure consistent ordering.

A significant portion of the work focused on enriching and standardizing geographical information. The sales data was merged with an external license dataset (`parent_df`) to incorporate `primary_company` identifiers and an alternative `cannabiz_county` field. This merge facilitated the imputation of missing `RetailerCounty` values, which were initially identified as "NA", "UNDEFINED", or empty strings. Further imputation of `RetailerCounty` was performed using a self-derived lookup table based on unique `retailerlicensenumber` and `retailercounty` pairs within the dataset, and by merging with an external ZIP-to-county lookup table (`zip_df`) after standardizing `RetailerZipCode` to a 5-digit format (`zip5`). Several manual corrections were applied to `RetailerCounty` for specific retailer licenses. All county names were converted to uppercase and stripped of any "County" suffixes.

For market concentration analysis, a `year` column was extracted from the `Date` column. The `totalsales` and `year` columns were converted to numeric types, with any conversion errors resulting in missing values. The Herfindahl-Hirschman Index (HHI) was calculated at both the individual retailer (`retailerlicensenumber`) and parent company (`primary_company`) levels. These calculations were performed for statewide and county-level aggregations across different years. The `primary_company` was derived from the merged license data, with individual `retailerlicensenumber` used as a fallback if the parent company was not identified.

Further analytical steps included:
*   Calculating `opacity` metrics based on county sales relative to maximum statewide sales.
*   Analyzing HHI trends over time, including classifying counties into "increasing," "decreasing," or "stable" HHI trajectories using linear regression.
*   Applying K-Means clustering to group counties with similar HHI trends.
*   Calculating year-over-year percentage change in HHI and identifying counties with the largest average increases or decreases.
*   Computing a correlation matrix between HHI, total sales, and county sales.
*   A separate analysis focused on visualizing sales trends over time for the top 10 cities, which involved converting the `Date` column to a datetime object and aggregating `totalsales` by date and city.

**Variables Affected:**
*   `RetailerLicenseNumber`: Used as a key for merging and aggregation, and for manual county fixes.
*   `RetailerFacilityType`: Retained.
*   `RetailerCity`: Retained, used in a separate sales trend analysis.
*   `RetailerZipCode`: Standardized to `zip5` (first five digits).
*   `RetailerCounty`: Heavily cleaned, imputed, and standardized using multiple external and internal lookups, and manual corrections.
*   `ItemCategory`: Renamed to `itemcategory`.
*   `totalsales`: Converted to numeric, summed for market share and HHI calculations.
*   `meanprice`: Dropped from the dataset.
*   `Date`: Used to extract `year` for HHI analysis; converted to datetime for city-level sales trend analysis.
*   `primary_company`: New column, derived from license data, representing the ultimate parent company.
*   `zip5`: New column, standardized 5-digit zip code.
*   `year`: New column, extracted year from the `Date` column.
*   `mkt_share`, `mkt_share2`: New intermediate columns for market share and squared market share calculations.
*   `HHI`, `HHI_parent_level`: New columns, representing the calculated Herfindahl-Hirschman Index.
*   `totalsales_parent`: New column, total sales aggregated at the parent company level.
*   `industry_sales`: New column, total sales for the relevant market definition (state/county, year).
*   `opacity`, `opacity_parent`: New columns, indicating relative sales volume.
*   `hhi_change`: New column, year-over-year percentage change in HHI.
*   `cluster`: New column, assigned by K-Means clustering based on HHI trends.

**Logic and Methodology:**
The data work followed a structured approach of data integration, cleaning, transformation, and analysis.
1.  **Data Integration:** Multiple annual sales files were combined, and this unified dataset was enriched by merging with external license data (to identify parent companies and additional county information) and a ZIP-to-county lookup table.
2.  **Data Cleaning and Standardization:**
    *   The `meanprice` column was removed due to inherent data quality issues (negative and infinite values), which were deemed unsuitable for direct analysis.
    *   `RetailerZipCode` was truncated to its first five digits to create a standardized `zip5` for consistent geographical mapping.
    *   `RetailerCounty` underwent a multi-stage imputation process, prioritizing information from the merged license data, then internal consistency checks, and finally an external ZIP-to-county lookup. This robust approach aimed to minimize missing county data and improve geographical accuracy.
    *   `totalsales` was converted to a numeric type, allowing for aggregation and calculation of market shares.
    *   The `Date` column was utilized to derive a `year` for time-series analysis, and separately converted to a datetime object for more granular temporal plotting.
3.  **Market Concentration Analysis (HHI):** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for market concentration. It was calculated by first determining the market share of each entity (retailer or parent company) within a defined market (statewide or county-level, per year), and then summing the squares of these market shares. This methodology provides a quantitative measure of market competitiveness.
4.  **Trend Analysis and Clustering:** To understand the dynamics of market concentration, HHI values were analyzed over time. Linear regression was applied to HHI trends for each county to classify them into categories of increasing, decreasing, or stable concentration. K-Means clustering was employed to identify natural groupings of counties exhibiting similar HHI trajectories, providing insights into regional market evolution.
5.  **Sales Trend Analysis:** A separate analysis focused on visualizing total sales trends over time for the top-performing cities, providing a high-level overview of sales performance in key urban areas.

**Validation and Verification:**
*   During numeric conversions (e.g., `totalsales`, `year`), the `errors='coerce'` option was used, which automatically converts non-numeric values into `NaN` (Not a Number). This prevents errors but requires subsequent handling of `NaN` values.
*   Merge operations included `indicator=True` to track merge outcomes, though the indicator column was subsequently dropped.
*   The `meanprice` column, identified in the Codebook as having significant data quality issues (negative and infinite values), was explicitly removed from the dataset, effectively addressing these anomalies by exclusion.
*   **Discrepancies with Codebook Recommendations:**
    *   The Codebook recommended flagging and potentially treating negative `totalsales` values as zero or excluding them. The Python code converts `totalsales` to numeric but does not explicitly implement a rule to handle negative values (e.g., setting them to zero or filtering them out) for the HHI calculations.
    *   While the `Date` column was used to extract `year` for the main HHI pipeline, and converted to datetime for a specific sales trend analysis, it was not consistently converted to a full datetime format for all analyses as suggested in the Codebook's reproducible cleaning plan.

**Results and Outcomes:**
The data work resulted in a cleaned and enriched sales dataset, which was then used to generate several key analytical outputs:
*   **HHI Summary Tables:** Tables summarizing HHI values at statewide and county levels, for both overall retailer and parent company perspectives, across multiple years. These were exported to Excel and CSV formats.
*   **HHI Trend Visualizations:** Various plots (line plots, bar plots) illustrating HHI trends over time for individual counties, grouped by their HHI trajectory (increasing, decreasing, stable), and by K-Means clusters.
*   **Sales Trend Visualizations:** Line plots showing total sales over time for the top 10 cities.
*   **Market Dynamics Insights:** Identification of counties with significant changes in HHI and correlation analysis between HHI and sales volumes.
*   **Intermediate Data Products:** A processed Stata file (`sales_w_parent_co_test.dta`) containing the merged and cleaned sales data with parent company information, serving as a foundation for further analysis.