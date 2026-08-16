# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information related to the Track & Trace project, likely pertaining to regulated cannabis sales. It captures various attributes of retailers and the products they sell, along with associated sales figures. Each row in the `sales19` table represents the aggregated sales for a specific retailer, item category, and month. The overall data source is inferred to be a regulatory tracking system. The collection period and extraction date are not explicitly provided in the current summary.

**Assumptions:**
*   The data pertains to the regulated cannabis industry, given the context of "Track & Trace" and typical column names in such datasets.
*   `totalsales` and `meanprice` are expressed in a local currency (e.g., USD).

### Table Inventory

*   **sales19**: Contains aggregated sales data by retailer, item category, and month for the year 2019.

## Table: sales19

*   **Purpose:** To provide a summary of sales transactions, detailing total sales and average prices across different retailers and product categories for specific time periods.
*   **What one row represents:** One row represents the aggregated sales data for a unique combination of `RetailerLicenseNumber`, `ItemCategory`, and `Date` (month).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key, inferred).
*   **Relationships:**
*   **Number of rows and columns:** 11749 rows, 9 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C10-0000004-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility associated with the retailer license.",
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
    "Allowed Values / Range": "[90019.0, 961610393.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": "The upper bound of the range (961610393.0) is highly anomalous for a standard zip code, suggesting potential data entry errors, concatenated values, or incorrect data type interpretation. Needs validation and potential truncation/correction to standard 5 or 9-digit zip codes."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "Entire column is missing. Consider dropping or attempting to impute from RetailerZipCode or RetailerCity if external mapping data is available."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the item sold.",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales data.",
    "Allowed Values / Range": "Example: 01-2019",
    "Missing %": 0.0,
    "Cleaning / Notes": "Currently stored as an object (string). Convert to a proper datetime format (e.g., YYYY-MM-DD, representing the first day of the month) for accurate time-series analysis."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency",
    "Description": "Total sales amount for the given retailer, item category, and date.",
    "Allowed Values / Range": "[-75.23, 1013321.09]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. These likely represent returns, refunds, or sales adjustments. For analyses focused on positive revenue, these values should be flagged and potentially treated as zero or excluded. For full financial reconciliation, they should be retained and understood."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the given retailer, item category, and date.",
    "Allowed Values / Range": "[-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative values could stem from negative total sales or calculation errors. Infinite values typically arise from division by zero (e.g., total sales divided by zero units sold). Flag these records for investigation. For analysis, infinite values should be converted to NaN, and negative values should be treated similarly to negative totalsales, or excluded/imputed."
  }
]
```

### Data Quality & Anomalies Section

The `sales19` table exhibits several data quality issues that require attention before analysis.

*   **Issue:** `RetailerZipCode` contains an anomalous upper range value (961610393.0).
    *   **Likely cause:** Data entry error, concatenation of multiple zip codes, or incorrect data type interpretation during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Validate zip codes against a known list of valid zip codes. Truncate or correct values that exceed standard length. Flag records with uncorrectable anomalies.
*   **Issue:** `RetailerCounty` is 100% missing.
    *   **Likely cause:** Data was never collected, or it was lost during extraction/transformation.
    *   **Recommended handling rule:** Drop the column if county-level analysis is not critical. If required, attempt to impute county information using `RetailerZipCode` or `RetailerCity` with an external geographic lookup table.
*   **Issue:** `totalsales` contains negative values.
    *   **Likely cause:** These values likely represent returns, refunds, or sales adjustments rather than actual positive sales.
    *   **Recommended handling rule:** For analyses focused on gross revenue, these values should be flagged and potentially treated as zero or excluded. For financial reconciliation, they should be retained and understood as part of the transaction history.
*   **Issue:** `meanprice` contains negative and infinite values.
    *   **Likely cause:** Negative values could be a consequence of negative `totalsales` or calculation errors. Infinite values typically result from division by zero (e.g., `totalsales` divided by zero units sold, or an invalid quantity).
    *   **Recommended handling rule:** Convert infinite values to `NaN` (Not a Number). For negative values, similar to `totalsales`, flag them for investigation. Depending on the analysis, these records might need to be excluded or imputed, especially if `meanprice` is used in calculations where negative or infinite values would distort results.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from `object` (string "MM-YYYY") to a proper datetime format (e.g., `YYYY-MM-01`) to enable accurate time-series analysis.
2.  **Address `RetailerZipCode` Anomalies:** Inspect `RetailerZipCode` values. For values exceeding standard zip code lengths, attempt to truncate to 5 or 9 digits if a clear pattern is identified. Flag or exclude records where zip codes remain invalid or uncorrectable.
3.  **Handle Missing `RetailerCounty` Data:** Due to 100% missing values, drop the `RetailerCounty` column unless external data sources are available for imputation.
4.  **Process Negative `totalsales`:** Create a new column, e.g., `gross_sales`, where negative `totalsales` values are set to 0, or flag these records for separate analysis of returns.
5.  **Clean `meanprice` Anomalies:** Convert all infinite values in `meanprice` to `NaN`. For negative `meanprice` values, investigate their origin; if they correspond to negative `totalsales` and zero units, they should also be treated as `NaN` or 0.

### Limitations & Trust Section

*   **`RetailerCounty`:** This column is entirely missing, making any county-level analysis impossible without external data integration. Its absence limits geographic granularity.
*   **`RetailerZipCode`:** The presence of extremely large values suggests potential data entry errors or non-standard formatting. Trust in the accuracy of zip code-based geographic analysis is low until these values are validated and corrected.
*   **Negative `totalsales` and `meanprice`:** While potentially representing returns or adjustments, their presence requires careful handling to avoid misinterpreting overall sales performance. The exact cause (e.g., specific return policies, data entry errors) is not clear from the summary.
*   **Infinite `meanprice`:** Indicates division by zero, implying issues with underlying quantity data or calculation logic. This impacts the reliability of average price metrics.

Validation is needed for `RetailerZipCode` against a known list of valid zip codes, and for the calculation logic behind `totalsales` and `meanprice` to understand the root causes of negative and infinite values.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` (MM-YYYY string) to `datetime` (YYYY-MM-01).
*   **Zip Code Cleaning:** Validate and potentially truncate `RetailerZipCode` to standard 5 or 9 digits.
*   **County Column:** Drop `RetailerCounty` due to 100% missing values.
*   **Negative Sales:** Flag negative `totalsales` as returns; consider setting to 0 for gross revenue analysis.
*   **Mean Price Anomalies:** Convert infinite `meanprice` to `NaN`; investigate and handle negative `meanprice` values (e.g., set to `NaN` or 0).

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred data types and descriptions, especially for `RetailerZipCode` and `Date`. Particular attention should be paid to the proposed handling rules for negative `totalsales` and the negative/infinite `meanprice` values, ensuring they align with the intended analytical goals of the Track & Trace project. Confirmation of the overall data source and collection period would also enhance the codebook's completeness.

# Work Documentation

## Table: sales19

**Data Operations:**
`sales19.csv` was integrated into a larger, multi-year sales dataset spanning from 2018 to 2024. This combined dataset underwent a series of cleaning, transformation, and enrichment steps to prepare it for market concentration analysis.

*   **Data Loading and Concatenation:** The `sales19.csv` file was loaded alongside other annual sales data files and concatenated into a single, comprehensive sales DataFrame.
*   **Column Management:** The `meanprice` column, identified in the codebook as having data quality issues, was explicitly dropped from the dataset. An additional column, `v1`, was also removed if present. The `ItemCategory` column was renamed to `itemcategory`, and other retailer-related columns were standardized to a consistent lowercase naming convention (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`).
*   **Data Integration:** The sales data was enriched by merging it with an external "Cannabis Market Intelligence Platform Report - Licenses" dataset. This merge was performed using the `retailerlicensenumber` to incorporate `primary_company` and `cannabiz_county` information. Records from the external license data that did not match any `retailerlicensenumber` in the sales data were excluded.
*   **Geographic Data Standardization and Imputation:**
    *   The `retailercounty` column, which was noted as being 100% missing in the original codebook, underwent extensive cleaning and imputation. Initial "NA" and "UNDEFINED" values were replaced with empty strings.
    *   Missing county values were then imputed using the `cannabiz_county` information obtained from the merged license data, leveraging a predefined mapping of county names.
    *   Further manual corrections were applied to specific retailer licenses to assign accurate county information where discrepancies were known.
    *   All `retailercounty` values were standardized to uppercase for consistency.
    *   A dynamic lookup table was created from existing `retailerlicensenumber` and `retailercounty` pairs within the dataset to fill any remaining missing county values based on other records for the same license.
    *   The `RetailerZipCode` column was truncated to a 5-digit format (`zip5`) and subsequently used to merge with an external ZIP-to-county mapping dataset for California, enabling the imputation of additional missing `retailercounty` values.
    *   A final set of manual county corrections was applied to address any lingering inconsistencies.
    *   Finally, empty strings, `<NA>`, and "nan" values in `retailercounty` were converted to proper missing values (`pd.NA`), and any rows still lacking county information were removed to ensure data integrity for geographic analysis.
*   **Data Type Conversion:** The `totalsales` column was converted to a numeric data type, and a `year` column was extracted from the `date` column and also converted to a numeric type to facilitate time-series analysis.
*   **Market Concentration Analysis (HHI):**
    *   The dataset was aggregated by `retailerlicensenumber` and `year` to sum `totalsales`, which served as the basis for calculating market share and the Herfindahl-Hirschman Index (HHI) at the statewide level for individual retailers.
    *   The `primary_company` column was refined by assigning the `retailerlicensenumber` to records where the `primary_company` was initially missing or empty, ensuring all sales could be attributed to an organizational entity.
    *   Similar aggregations and HHI calculations were performed at the statewide level, but this time for parent companies, providing a view of market concentration at a higher organizational level.
    *   County-level HHI metrics were computed for both individual retailers and parent companies by aggregating sales data by `retailercounty` and `year`.
*   **Derived Metrics:** An `opacity` metric was calculated, representing the relative sales volume of each county compared to the maximum statewide sales, for both individual and parent company levels.
*   **Output and Visualization:** The processed data, including all calculated HHI metrics, was saved to a Stata file (`sales_w_parent_co_test.dta`) and several Excel/CSV files (`HHI_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`). Various plots were generated to visualize HHI trends over time by county, HHI distributions, and sales trends by city.
*   **Clustering and Trend Analysis:** K-Means clustering was applied to HHI trends to identify groups of counties with similar market concentration trajectories. Linear regression was used to categorize counties into increasing, decreasing, or stable HHI trajectories, providing insights into market evolution.

**Variables Affected:**
*   `RetailerLicenseNumber` (renamed to `retailerlicensenumber`): Used as a key for merging, aggregation, and identification.
*   `RetailerFacilityType` (renamed to `retailerfacilitytype`): Standardized in naming.
*   `RetailerCity` (renamed to `retailercity`): Standardized in naming.
*   `RetailerZipCode` (renamed to `retailerzipcode`): Used to derive `zip5` for county imputation.
*   `RetailerCounty` (renamed to `retailercounty`): Heavily cleaned, imputed, standardized, and used for geographic aggregation.
*   `ItemCategory` (renamed to `itemcategory`): Standardized in naming.
*   `Date` (renamed to `date`): Used to derive the `year` variable.
*   `totalsales`: Converted to numeric, used as the primary metric for aggregation and HHI calculation.
*   `meanprice`: This column was dropped from the dataset.
*   `primary_company`: A new variable created/imputed from external license data and `retailerlicensenumber` to represent the ultimate parent company.
*   `cannabiz_county`: An intermediate variable introduced from external license data, used for `retailercounty` imputation.
*   `zip5`: A new variable derived from `retailerzipcode` for merging with ZIP-to-county mappings.
*   `year`: A new variable extracted from the `date` column.
*   `industry_sales`: A calculated variable representing total sales for a given year/county, used in market share calculations.
*   `mkt_share`: A calculated variable representing the percentage market share of a retailer or parent company.
*   `mkt_share2`: A calculated variable representing the square of market share, a component of the HHI.
*   `opacity`, `opacity_parent`: New metrics derived from sales data to indicate relative sales volume.
*   `cluster`: A new variable assigned to counties based on K-Means clustering of HHI trends.
*   `hhi_change`: A new variable representing the year-over-year percentage change in HHI.

**Logic and Methodology:**
The overarching methodology aimed to transform raw sales transaction data into a structured format suitable for in-depth market concentration analysis. A critical initial step involved consolidating sales data across multiple years, recognizing that `sales19` represents only a segment of the broader sales history. The decision to drop `meanprice` was based on its documented data quality issues (negative/infinite values), which could distort analytical outcomes, aligning with the codebook's recommendation for careful handling.

A significant portion of the work focused on standardizing and imputing geographic information, particularly the `retailercounty` column. This multi-stage imputation process, leveraging both external ZIP-to-county mappings and internal consistency checks derived from license data, was crucial for enabling reliable county-level analysis, which was severely limited by the initial 100% missing values.

The core analytical logic revolved around calculating the Herfindahl-Hirschman Index (HHI). This was performed at various granularities: statewide and county levels, and for both individual retailers and their aggregated parent companies. The `primary_company` logic was specifically designed to ensure that all sales could be accurately attributed to a parent entity, even when direct parent company identifiers were initially absent or ambiguous. This hierarchical approach provides a nuanced understanding of market structure.

Further analysis involved categorizing counties based on their HHI trends over time using linear regression and clustering techniques, providing insights into the dynamic nature of market concentration.

**Validation and Verification:**
Several implicit and explicit validation steps were observed:
*   The merging process with external license data included an `indicator=True` flag, which, although not fully utilized for explicit reporting in the provided snippets, allowed for tracking merge outcomes. The explicit filtering out of `right_only` merges ensured that only relevant license information was retained.
*   The conversion of `totalsales` and `year` to numeric types utilized `errors="coerce"`, which automatically converts unparseable values to `NaN`. This serves as an implicit data quality check, flagging records with problematic numeric data for these critical columns.
*   The multi-stage imputation and standardization of `retailercounty`, including manual corrections and final dropping of rows with persistent missing values, indicates a robust effort to validate and ensure the completeness and accuracy of this key geographic variable.
*   The sorting of the combined sales data by multiple attributes before processing suggests an attempt to ensure consistent ordering, which can be a prerequisite for certain data operations or for identifying duplicates.
*   The explicit replacement of empty strings, `<NA>`, and "nan" with `pd.NA` for `retailercounty` before dropping missing values demonstrates a thorough approach to handling various representations of missing data.

**Results and Outcomes:**
The data work resulted in a significantly enhanced and analytically ready sales dataset.
*   The `retailercounty` column, initially entirely missing, was substantially populated and standardized, thereby enabling robust geographic analysis at the county level.
*   New `primary_company` and `year` variables were successfully created, facilitating analysis at different organizational and temporal granularities.
*   The dataset was transformed to support the calculation of HHI metrics at various levels (statewide, county, individual retailer, parent company), providing a foundational understanding of market concentration dynamics.
*   The output included several derived metrics and aggregated tables (e.g., `HHI_by_county_test.xlsx`, `hhi_by_county.csv`), along with numerous visualizations. These outputs offer valuable insights into market concentration trends, sales performance over time, and across different geographic regions and organizational structures.
*   The identification of counties with increasing, decreasing, or stable HHI trends, and the clustering of counties based on HHI trajectories, provide actionable insights into market evolution and competitive landscapes.