# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated sales information for cannabis retailers participating in the Track & Trace project. It summarizes monthly sales quantities and values across various item categories. Each row in the `salesquantity21` table represents the aggregated sales data (total grams, total sales, and mean price) for a specific item category by a particular licensed retailer within a given month of 2021. The overall data source is the Track & Trace system, with data collected throughout 2021. The specific extraction date is not provided.

**Assumptions:**
*   The `Date` column represents the month and year of the aggregated sales.
*   `totalgrams` and `totalsales` represent cumulative values for the month.
*   `meanprice` is the average price per unit (e.g., per gram or per item) for the given item category in that month.

### Table Inventory

*   **salesquantity21:** Contains monthly aggregated sales quantities, total sales, and mean prices for various cannabis item categories by licensed retailers in 2021.

## Table: salesquantity21

*   **Purpose:** To provide a monthly summary of sales performance for different cannabis product categories across various retailers in 2021.
*   **What one row represents:** One row represents the aggregated monthly sales (total grams, total sales, and mean price) for a specific item category by a unique retailer license number for a given month.
*   **Primary key(s):** RetailerLicenseNumber, ItemCategory, Date
*   **Relationships:**
*   **Number of rows and columns:** 43549 rows, 10 columns

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "License Number",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "e.g., C10-0000638-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "Facility Type",
    "Description": "Type of facility operated by the retailer (e.g., Cannabis - Retailer License).",
    "Allowed Values / Range": "e.g., Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "City Name",
    "Description": "City where the retailer facility is located.",
    "Allowed Values / Range": "e.g., MODESTO",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "Zip Code",
    "Description": "Zip code of the retailer facility.",
    "Allowed Values / Range": "[90008.0, 961610393.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Investigate values like 961610393.0, which are not standard 5-digit US zip codes. This may represent ZIP+4 codes stored numerically or data entry errors. Convert to string type to preserve leading zeros and handle varying lengths."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "County Name",
    "Description": "County where the retailer facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "This column is entirely missing. It should be excluded from analysis or imputed using an external mapping if county-level aggregation is required."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "Product Category",
    "Description": "Category of the cannabis product sold (e.g., flower, edibles, concentrates).",
    "Allowed Values / Range": "e.g., flowereighth",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "Month-Year",
    "Description": "Month and year of the aggregated sales data.",
    "Allowed Values / Range": "e.g., 01-2021",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to a proper datetime object for accurate time-series analysis."
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total grams of the item category sold by the retailer in the given month.",
    "Allowed Values / Range": "[0.4819415, 481290.46]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the item category by the retailer in the given month.",
    "Allowed Values / Range": "[1.0, 4597238.18]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per unit",
    "Description": "Average price per unit (e.g., per gram or per item) for the item category by the retailer in the given month.",
    "Allowed Values / Range": "[0.817826086956522, 196.65]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column is 100% missing.
    *   **Likely cause:** Data was either not collected for this field or was lost during the extraction or processing phase.
    *   **Recommended handling rule:** Given the complete absence of data, this column should be excluded from analysis. If county-level geographical analysis is critical, imputation would require an external mapping service based on `RetailerZipCode` or `RetailerCity`, which introduces external data dependency and potential inaccuracies.
*   **Issue:** `RetailerZipCode` contains values that are not standard 5-digit US zip codes (e.g., `961610393.0`).
    *   **Likely cause:** These could be ZIP+4 codes stored as a single numeric value, data entry errors, or an incorrect data type conversion during extraction. Storing zip codes as numeric types can also lead to loss of leading zeros.
    *   **Recommended handling rule:** Convert the `RetailerZipCode` column to a string data type to preserve leading zeros and accommodate varying lengths. Validate against a comprehensive list of valid US zip codes (including ZIP+4 formats) and flag or correct entries that do not conform to expected patterns.

### Reproducible Cleaning Plan

1.  **Handle Missing `RetailerCounty`:** Remove the `RetailerCounty` column from the dataset due to 100% missing values, as it provides no analytical utility in its current state.
2.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column to a string data type. Subsequently, implement a validation step to identify and flag or correct non-standard zip code formats (e.g., values not matching 5-digit or 9-digit ZIP+4 patterns).
3.  **Convert `Date` Column:** Transform the `Date` column from its current object (string) format (e.g., "01-2021") into a proper datetime object. This will enable robust time-series analysis and filtering.

### Limitations & Trust Section

*   The complete absence of data in the `RetailerCounty` column significantly limits the ability to perform geographical analysis or aggregations at the county level. Trust in any county-level insights would be low without external data validation and imputation.
*   The `RetailerZipCode` column contains anomalous values that are not standard US zip codes. This could impact the accuracy of geographical analysis, spatial joins with other datasets, and the overall reliability of location-based insights. Validation against an authoritative zip code database is needed to ensure data integrity.
*   The `Date` column, currently stored as an object, requires conversion to a datetime format. Until this is done, time-series analysis and chronological ordering may be unreliable.

### Appendix: Quick Reference

*   **`RetailerCounty`:** Drop due to 100% missing values.
*   **`RetailerZipCode`:** Convert to string; validate and clean non-standard formats.
*   **`Date`:** Convert to datetime object for time-series analysis.
*   **Data Types:** Ensure all columns have appropriate data types for analysis (e.g., numeric for quantities/sales, string for identifiers, datetime for dates).

### Notes for Reviewers

Reviewers are requested to verify the proposed handling of the `RetailerCounty` and `RetailerZipCode` columns, particularly the decision to drop the former and the strategy for cleaning the latter. Please also confirm the interpretation of "one row represents" for the `salesquantity21` table and the appropriateness of the identified primary keys. Feedback on the completeness and clarity of column descriptions and cleaning notes is also appreciated.

# Work Documentation

## Table: salesquantity21

**Data Operations:**
The Python code processes a broader dataset (`sales_df`) that encompasses sales data from 2018 to 2024, of which `salesquantity21` represents the 2021 subset. The operations performed on this larger sales dataset, and thus implicitly on the `salesquantity21` data, include:

*   **Data Ingestion and Consolidation:** Multiple annual sales files (e.g., `sales18.csv` through `sales24.csv`) were loaded and concatenated into a single, comprehensive sales DataFrame.
*   **Column Renaming:** Several columns were systematically renamed for consistency and ease of use, including `RetailerLicenseNumber` to `retailerlicensenumber`, `RetailerCounty` to `retailercounty`, `RetailerZipCode` to `retailerzipcode`, `Date` to `date`, and `ItemCategory` to `itemcategory`.
*   **Data Enrichment (Parent Company Information):** The sales data was merged with an external dataset containing license and company information (`parent_df`). This merge introduced `primary_company` (identifying the ultimate parent company) and `cannabiz_county` (an alternative county source) based on `retailerlicensenumber`.
*   **Retailer County Imputation and Standardization:**
    *   Initial cleaning involved replacing "NA" and "UNDEFINED" values in `retailercounty` with empty strings.
    *   Missing `retailercounty` values were then imputed using `cannabiz_county` from the merged parent company data.
    *   Specific manual corrections were applied to `retailercounty` for a few identified `retailerlicensenumber` entries.
    *   All `retailercounty` values were converted to uppercase for standardization.
    *   A mapping of unique `retailerlicensenumber` to `retailercounty` was created from non-missing entries and used to further fill gaps.
    *   A 5-digit zip code (`zip5`) was extracted from `retailerzipcode`.
    *   The dataset was merged with an external ZIP-to-County mapping (`zip_df`) to obtain `retailercounty_from_zip`, which was then used to impute any remaining missing `retailercounty` values.
    *   Additional manual fixes were applied to `retailercounty` for specific licenses.
    *   Finally, empty strings, "NA", and "nan" values in `retailercounty` were converted to proper missing values (`pd.NA`), and rows with missing `retailercounty` were dropped.
*   **Data Type Conversions:**
    *   The `date` column was converted from its original string format to a datetime object, enabling time-series analysis.
    *   The `year` was extracted from the `date` column and converted to a numeric type.
    *   The `totalsales` column was converted to a numeric data type.
*   **Market Concentration Analysis (HHI):**
    *   The Herfindahl-Hirschman Index (HHI) was calculated to measure market concentration. This involved:
        *   Aggregating `totalsales` by `retailerlicensenumber` and `year` (for overall HHI) and by `primary_company` and `year` (for parent-level HHI).
        *   Calculating market share for each entity (retailer or parent company) within its respective market (statewide or county-level).
        *   Squaring the market shares and summing them to derive the HHI.
    *   HHI metrics were computed for:
        *   Statewide overall retailer level (`CA_overall`).
        *   Statewide parent company level (`CA_parent`).
        *   County-level overall retailer level (`county_overall`).
        *   County-level parent company level (`county_parent`).
*   **Derived Metrics and Analysis:**
    *   Total sales by county and parent company were calculated.
    *   An "opacity" metric was derived, representing county sales as a percentage of maximum statewide sales.
    *   Counties were clustered based on their HHI trends over time using K-Means clustering.
    *   Linear regression was applied to HHI trends for each county to categorize them as having "increasing," "decreasing," or "stable" market concentration.
    *   Year-over-year percentage change in HHI was calculated.
    *   Correlation analysis was performed between HHI, total sales, and county sales.
    *   Sales data was aggregated by city and date to analyze sales trends in top cities.
*   **Data Export and Visualization:** Various processed datasets and HHI results were exported to Excel and CSV files. Numerous plots (line plots, bar plots, heatmaps, box plots, violin plots, histograms) were generated to visualize the data and analytical findings.

**Variables Affected:**

*   **`RetailerLicenseNumber` (renamed to `retailerlicensenumber`):** Used as a key for merging, grouping, and identifying individual retailers.
*   **`RetailerCounty` (renamed to `retailercounty`):** Significantly modified through imputation, standardization, and manual corrections to improve data quality and completeness.
*   **`RetailerZipCode` (renamed to `retailerzipcode`):** Used to derive `zip5` for county imputation.
*   **`Date` (renamed to `date`):** Converted to a datetime object and used to extract `year` for time-series analysis.
*   **`ItemCategory` (renamed to `itemcategory`):** Used for grouping and aggregation.
*   **`totalsales`:** Converted to numeric, aggregated, and used as the primary metric for market share and HHI calculations.
*   **`primary_company`:** A new column created from external license data, representing the ultimate parent company, crucial for parent-level HHI analysis.
*   **`cannabiz_county`:** A new column from external license data, used as a source for `retailercounty` imputation.
*   **`zip5`:** A new column derived from `retailerzipcode`, used for merging with the ZIP-to-County mapping.
*   **`industry_sales`:** A new calculated column representing total sales for a given market (statewide or county-level) in a specific year.
*   **`mkt_share`:** A new calculated column representing the market share of each entity.
*   **`mkt_share2`:** A new calculated column representing the squared market share, a core component of HHI.
*   **`HHI` and `HHI_parent_level`:** New calculated columns representing the final Herfindahl-Hirschman Index values for overall and parent company levels, respectively.
*   **`county_sales`, `county_sales_parent`:** New calculated columns representing total sales aggregated by county for overall and parent company levels.
*   **`opacity`, `opacity_parent`:** New calculated columns indicating the relative sales volume of a county compared to the maximum statewide sales.
*   **`cluster`:** A new column assigned to each county based on K-Means clustering of HHI trends.
*   **`hhi_change`:** A new calculated column representing the year-over-year percentage change in HHI.

**Logic and Methodology:**

The primary objective of the data work was to analyze market concentration and sales trends within the cannabis retail sector, with a particular focus on California. This involved a multi-stage process:

1.  **Data Integration:** Multiple years of raw sales data (2018-2024) were combined to create a longitudinal dataset. This was then enriched by merging with external license data, which provided crucial information about parent companies and alternative county designations. A separate ZIP-to-County mapping was also integrated to enhance geographical data quality.
2.  **Robust County Imputation:** Recognizing the critical importance of accurate geographical data for market analysis, a comprehensive strategy was implemented to address missing `RetailerCounty` values. This involved a hierarchical imputation approach: first leveraging `cannabiz_county` from the license data, then applying manual corrections for known issues, and finally utilizing a ZIP-to-County lookup. This layered approach aimed to maximize the completeness and accuracy of the `retailercounty` field.
3.  **Market Concentration Measurement (HHI):** The Herfindahl-Hirschman Index (HHI) was chosen as the key metric for assessing market concentration. This index is widely used in economics to determine if a market is competitive or monopolistic. Calculations were performed at two levels of granularity (individual retailer and parent company) and across two geographical scopes (statewide and county-level) to provide a nuanced understanding of market dynamics.
4.  **Time-Series and Trend Analysis:** By converting the `Date` column to a proper datetime format and extracting the `year`, the analysis could track HHI and sales trends over time. Linear regression was applied to HHI values for each county to identify and categorize their market concentration trajectories (increasing, decreasing, or stable). K-Means clustering was further employed to group counties exhibiting similar HHI patterns, facilitating the identification of broader market trends.
5.  **Sales Performance Insights:** Beyond concentration, the work also focused on understanding sales performance. Aggregations of total sales by city and date allowed for the visualization of sales growth and identification of key retail hubs.
6.  **Data Quality Assurance:** Throughout the process, steps such as explicit data type conversions with error handling, removal of duplicates, and handling of missing values were implemented to ensure the integrity and reliability of the analytical outputs.

**Validation and Verification:**

*   **Data Type Integrity:** Explicit data type conversions for `totalsales` and `date` were performed with `errors="coerce"`, which converts unparseable values to `NaN`, allowing for identification and handling of problematic entries rather than crashing the process.
*   **Merge Verification:** The merging operations, particularly for `parent_df` and `zip_df`, included `indicator=True` to create a `_merge` column, which was then used to verify the success and nature of the merges (e.g., `left_only`, `both`, `right_only`). This allowed for targeted handling of unmatched records.
*   **County Imputation Logic:** The multi-stage county imputation process was designed to prioritize more reliable sources (e.g., license data over zip code mapping) and included manual overrides for known data issues, enhancing the trustworthiness of the `retailercounty` field.
*   **HHI Calculation Consistency:** The HHI calculations followed standard economic methodology, ensuring that the derived market concentration metrics are interpretable and comparable.
*   **Visual Data Inspection:** A wide array of visualizations (line plots for trends, bar plots for comparisons, heatmaps for multi-dimensional views, box and violin plots for distributions, histograms for overall shape) were generated. These plots served as a critical visual validation step, allowing for quick identification of anomalies, unexpected patterns, or potential errors in the data processing.
*   **Statistical Checks:** Correlation matrices were computed to quantitatively assess the relationships between HHI, total sales, and county sales, providing a statistical verification of expected associations.
*   **Missing Value Handling:** Explicit steps were taken to replace various representations of missing data (empty strings, "NA", "nan", "<NA>") with `pd.NA` and then to drop rows where critical identifiers or geographical information remained missing, ensuring that subsequent analyses were performed on complete records.

**Results and Outcomes:**

The data work successfully produced a robust and enriched dataset suitable for in-depth market analysis. Key outcomes include:

*   **Cleaned and Integrated Sales Data:** A comprehensive sales dataset spanning multiple years (2018-2024) was created, with significantly improved data quality, particularly for geographical identifiers like `RetailerCounty`.
*   **Market Concentration Insights:** Detailed Herfindahl-Hirschman Index (HHI) values were calculated for various market definitions (statewide, county-level, overall retailer, parent company), providing quantitative measures of market competition and concentration trends over time.
*   **Identification of Market Dynamics:** The analysis identified counties with increasing, decreasing, or stable HHI trajectories, offering valuable insights into evolving competitive landscapes. K-Means clustering further grouped counties with similar HHI patterns.
*   **Enhanced Geographical Analysis Capability:** The extensive cleaning and imputation of the `RetailerCounty` column enabled more reliable geographical aggregations and visualizations, which were previously hindered by missing data.
*   **Sales Performance Overview:** Aggregated sales data by city and date provided a clear picture of sales trends and the performance of key urban markets.
*   **Actionable Data Products:** The final HHI results and other aggregated data were exported into easily consumable Excel and CSV formats, ready for integration into reports, dashboards, or further analytical models.
*   **Comprehensive Visualizations:** A rich set of plots and interactive charts were generated, effectively communicating complex market trends, distributions, and relationships to stakeholders. These visualizations serve as a powerful tool for understanding the state of the cannabis retail market.