# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated monthly sales quantities and values for cannabis products from the Track & Trace project. It captures transactional data at the retailer level, categorized by item type. Each row in the `salesquantity19` table represents the total sales quantity, total sales value, and mean price for a specific item category sold by a particular retailer in a given month. The data source is the Track & Trace system, with the collection period inferred to be the year 2019 based on the table name and date examples. The exact extraction date is not available.

**Assumptions:**
*   The '19' in the table name `salesquantity19` indicates data from the year 2019.
*   `Date` column values like "01-2019" represent the month and year of the aggregated sales.
*   `totalsales` is in USD, and `totalgrams` is in grams.

### Table Inventory

*   **`salesquantity19`**: Contains monthly aggregated sales quantities, values, and mean prices for various cannabis product categories by individual retailers.

## Table: salesquantity19

*   **Purpose:** To provide a summary of monthly sales performance, including quantities sold, total revenue, and average price, for different cannabis product categories across various retailers.
*   **What one row represents:** One month's aggregated sales quantity, total sales value, and mean price for a specific item category sold by a specific retailer.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key).
*   **Relationships:** No explicit foreign key relationships are known from the provided data.
*   **Number of rows and columns:** 3142 rows, 10 columns.
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000004-LIC",
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
    "Allowed Values / Range": "Example: PALM SPRINGS",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer's facility. May include ZIP+4 or be concatenated.",
    "Allowed Values / Range": "Range: [90021.0, 961610393.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "The range and example value (922624021) suggest this might be a concatenated ZIP+4 code or an improperly formatted string. Verification of format and potential truncation/splitting may be required."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "",
    "Missing %": "100.0",
    "Cleaning / Notes": "All values are missing. This column is unusable as is. Consider dropping or investigating if county data can be derived from other location fields."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis product sold.",
    "Allowed Values / Range": "Example: flowerquarter",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the aggregated sales data.",
    "Allowed Values / Range": "Example: 01-2019",
    "Missing %": "0.0",
    "Cleaning / Notes": "Currently stored as an object (string). Should be converted to a datetime format for proper temporal analysis."
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold in grams for the given month.",
    "Allowed Values / Range": "Range: [0.4819415, 116269.5]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are non-negative, which is expected for quantities."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue in USD for the item category sold in the given month.",
    "Allowed Values / Range": "Range: [0.99, 865567.25]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are non-negative, which is expected for sales revenue."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/gram",
    "Description": "Average price per gram for the item category sold in the given month (totalsales / totalgrams).",
    "Allowed Values / Range": "Range: [0.8045, 248.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values are non-negative, which is expected for price. Division by zero is not observed as minimum totalgrams is > 0."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column is 100% missing.
    *   **Likely cause:** Data was either not collected, not extracted, or consistently null in the source system.
    *   **Recommended handling rule:** Drop the `RetailerCounty` column as it provides no information. If county-level analysis is critical, investigate alternative data sources or methods to infer county from `RetailerZipCode` or `RetailerCity`.
*   **Issue:** `RetailerZipCode` contains values that appear to be concatenated ZIP+4 codes or otherwise non-standard, with a large numeric range.
    *   **Likely cause:** Inconsistent data entry or a specific internal format for zip codes that includes extended information.
    *   **Recommended handling rule:** Standardize `RetailerZipCode` to a 5-digit format by truncating or parsing. If ZIP+4 is needed, convert to string and split. Validate against a known list of zip codes if possible.
*   **Issue:** `Date` column is of `object` (string) data type.
    *   **Likely cause:** Data was extracted as a string representation of the date.
    *   **Recommended handling rule:** Convert the `Date` column to a proper datetime data type for accurate temporal analysis and filtering.

### Reproducible Cleaning Plan

1.  **Drop `RetailerCounty`:** Remove the `RetailerCounty` column from the dataset due to 100% missing values, as it provides no analytical utility in its current state.
2.  **Standardize `RetailerZipCode`:** Convert `RetailerZipCode` to a string type, then extract the first five characters to standardize it to a 5-digit US zip code format.
3.  **Convert `Date` to Datetime:** Transform the `Date` column from its current object (string) type to a datetime object, enabling proper time-series analysis and operations.
4.  **Validate `totalgrams`, `totalsales`, `meanprice`:** Confirm that `totalgrams`, `totalsales`, and `meanprice` values remain non-negative and within expected ranges, flagging any outliers for further investigation.

### Limitations & Trust Section

The reliability of the `RetailerCounty` column is extremely low due to 100% missing data; it cannot be used for analysis. The `RetailerZipCode` column requires validation and standardization to ensure it accurately represents geographical locations, as its current format is ambiguous. The `Date` column, while complete, needs type conversion to be fully trustworthy for temporal analysis. Further validation would involve cross-referencing retailer information (license numbers, facility types, cities, and zip codes) with external, authoritative sources to confirm accuracy and completeness.

### Appendix: Quick Reference

*   **`RetailerCounty`**: Dropped due to 100% missing values.
*   **`RetailerZipCode`**: Standardized to 5-digit string format.
*   **`Date`**: Converted to datetime object for temporal analysis.
*   **`totalgrams`, `totalsales`, `meanprice`**: Validated for non-negative values.
*   **Primary Key**: Assumed composite key of `RetailerLicenseNumber`, `ItemCategory`, `Date`.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key and the proposed handling rules for `RetailerZipCode` and `Date` column transformations. Specifically, confirm that the standardization of `RetailerZipCode` aligns with the intended use case (e.g., 5-digit vs. full ZIP+4). Additionally, any external knowledge regarding the `RetailerCounty` data source or potential for imputation should be considered.

---

# Work Documentation

## Table: salesquantity19

**Data Operations:**
The data corresponding to `salesquantity19` (which is part of a larger `sales_df` encompassing sales data from 2018 to 2024) underwent extensive cleaning, transformation, and integration. Initially, multiple annual sales CSV files were loaded and concatenated into a single DataFrame. During this process, any existing `meanprice` or `v1` columns were dropped. Key columns were then renamed for consistency (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `ItemCategory` to `itemcategory`, `Date` to `date`, `totalsales` to `totalsales`).

A significant portion of the work focused on enriching and standardizing geographical information. The `sales_df` was merged with an external `parent_df` (containing license and company information) to link retailers to their primary parent companies and to provide additional county data. The `retailercounty` column, initially identified as having 100% missing values in the codebook, was subjected to a multi-step imputation and normalization process. This involved replacing "NA" and "UNDEFINED" values with blanks, applying a predefined mapping to standardize county names from the `parent_df`, and performing manual corrections for specific retailer licenses. Further, a `zip_df` (HUD ZIP-to-county mapping) was used to infer and fill missing `retailercounty` values based on the `retailerzipcode` (truncated to a 5-digit format). After these imputation efforts, any remaining rows with missing `retailercounty` were dropped.

The `date` column was parsed to extract the `year`, and `totalsales` and `year` were converted to numeric data types. The dataset was then used to calculate the Herfindahl-Hirschman Index (HHI) to measure market concentration. HHI was computed at various levels: statewide for individual retailers, statewide for parent companies, county-level for individual retailers, and county-level for parent companies. These HHI results were combined and merged into a final dataset. Additional metrics such as market share, squared market share, industry sales, and opacity (representing a county's sales contribution relative to the maximum statewide sales) were derived.

Further analytical operations included clustering counties based on their HHI trends using K-Means, performing linear regression to categorize counties into groups with increasing, decreasing, or stable HHI trajectories, and calculating year-over-year HHI percentage changes. Sales data was also aggregated by city and date to analyze sales trends in top urban areas.

**Variables Affected:**
*   **New/Derived Variables:** `primary_company` (identifying the main parent company), `multi_owner` (indicating if a company has multiple owners), `zip5` (5-digit standardized zip code), `year` (extracted from `date`), `industry_sales` (total sales for a given year/county), `mkt_share` (market share percentage), `mkt_share2` (squared market share for HHI calculation), `HHI` (Herfindahl-Hirschman Index at retailer level), `HHI_parent_level` (HHI at parent company level), `county_sales` (total sales per county), `county_sales_parent` (total parent company sales per county), `opacity` and `opacity_parent` (sales contribution metrics), `cluster` (K-Means cluster assignment for HHI trends), `hhi_change` (year-over-year HHI percentage change).
*   **Modified Variables:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, normalized, and imputed from external sources), `RetailerZipCode` (renamed to `retailerzipcode`, truncated to `zip5`), `Date` (renamed to `date`, converted to datetime, and used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric type).
*   **Dropped Variables:** `meanprice` and `v1` (if present in source files). The original `RetailerCounty` column, as described in the Codebook, was not dropped outright but rather extensively filled and then rows with persistent missing values were removed.

**Logic and Methodology:**
The core methodology involved integrating disparate sales data from multiple years with external licensing and geographical information to create a robust dataset for market analysis. The approach prioritized data completeness and consistency, particularly for the `retailercounty` field, which was critical for geographical HHI calculations. A hierarchical strategy was used for county imputation, starting with direct mappings, then leveraging license-specific information, and finally using ZIP code-based lookups.

Market concentration was quantified using the HHI, a standard economic metric, calculated at both granular (retailer) and aggregated (parent company) levels, and across different geographical scopes (statewide and county-level). This allowed for a multi-faceted view of market dynamics. Time-series analysis was performed by extracting the `year` from the `date` column, enabling the study of HHI trends over time. Advanced analytical techniques like K-Means clustering and linear regression were applied to identify and characterize distinct patterns in county-level HHI evolution. Visualizations were extensively used to explore and present the data, including line plots for trends, bar plots for comparisons, and heatmaps for multi-dimensional views.

**Validation and Verification:**
Data types were explicitly managed during loading and conversion to ensure numerical operations were performed correctly. Missing values in critical fields like `retailercounty` were systematically addressed through a series of imputation steps, and the remaining records with unresolvable missing county information were removed. Duplicate entries in the `parent_df` were handled to ensure unique license-to-company mappings. Merge operations were performed with explicit `how` parameters (e.g., `left` merge) to control data retention and `indicator=True` was used internally to track merge outcomes, although the indicator column was subsequently dropped. The HHI calculations followed standard formulas. While the Codebook's "Reproducible Cleaning Plan" suggested validating `totalgrams`, `totalsales`, and `meanprice` for non-negativity, the provided Python code did not include explicit checks for these conditions beyond the initial numeric type conversion which would coerce invalid values to `NaN`.

**Results and Outcomes:**
The data work resulted in a comprehensive and cleaned dataset suitable for in-depth market analysis of cannabis sales. The `retailercounty` field, initially unusable, was significantly improved, enabling reliable county-level analysis. The calculated HHI metrics provide valuable insights into market concentration across California's cannabis retail sector, both at the individual retailer and parent company levels, and how these dynamics have evolved over several years. The categorization of counties by HHI trajectory offers a strategic understanding of regional market competition. Key analytical outputs, including HHI summaries and sales data, were exported to Stata and Excel files (`sales_w_parent_co_test.dta`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`). A wide array of static and interactive visualizations (e.g., HTML files for Plotly charts) were generated to effectively communicate these findings, illustrating sales trends, HHI distributions, and changes over time.

**Note on Discrepancy:** The Codebook's "Reproducible Cleaning Plan" recommended dropping the `RetailerCounty` column due to 100% missing values. However, the Python code implemented a strategy of extensive imputation and normalization for this column, leveraging multiple external data sources, before dropping only those rows where the county information could not be resolved. This indicates a divergence in the handling strategy for the `RetailerCounty` column between the documented plan and the executed data work.