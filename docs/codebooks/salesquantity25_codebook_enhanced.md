# Track & Trace Data Codebook

### 2. Overview Section

This dataset provides aggregated sales information related to the Track & Trace project, likely focusing on regulated industries such as cannabis. It details sales quantities and values for various item categories across different retailers. Each row in the `salesquantity25` table represents a monthly aggregated sales record for a specific item category at a particular retailer, identified by their license number, within a given month and year. The overall data source, collection period, and extraction date are not specified in the provided metadata.

**Assumptions:**
*   The dataset pertains to the cannabis industry, inferred from the `RetailerFacilityType` "Cannabis - Retailer License".
*   `totalgrams` and `totalsales` represent monthly aggregates.
*   Currency is assumed to be USD for `totalsales` and `meanprice`.

### 3. Table Inventory

*   **salesquantity25:** Contains aggregated monthly sales data for various item categories by retailer, including quantities sold, total sales value, and mean price.

### 4. For Each Table

## Table: salesquantity25

*   **Purpose:** To provide a summary of monthly sales performance for different cannabis product categories across licensed retailers.
*   **What one row represents:** One month's aggregated sales data for a specific item category at a unique retailer.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 14723 rows, 10 columns

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the retailer's license.",
    "Allowed Values / Range": "Example: C10-0001030-LIC",
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
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: WILMINGTON",
    "Missing %": 0.1,
    "Cleaning / Notes": "Missing values should be investigated. Potential for imputation based on RetailerZipCode or RetailerCounty if a reliable mapping exists."
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "Range: [90003.0, 961610393.0]",
    "Missing %": 0.3,
    "Cleaning / Notes": "Contains non-standard zip code formats (e.g., 907442424.0, 961610393.0). These values are likely erroneous or concatenated. Investigate and attempt to parse into standard 5-digit US zip codes. Invalid entries should be flagged or set to null. Missing values should be handled, potentially by imputation from RetailerCity or RetailerCounty."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: LOS ANGELES",
    "Missing %": 0.5,
    "Cleaning / Notes": "Missing values should be investigated. Potential for imputation based on RetailerCity or RetailerZipCode if a reliable mapping exists."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item sold.",
    "Allowed Values / Range": "Example: flowereighth",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total grams of the item category sold in the given month.",
    "Allowed Values / Range": "Range: [0.5, 94407.74]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue in USD for the item category in the given month.",
    "Allowed Values / Range": "Range: [1.3, 1310200.93]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/unit",
    "Description": "Average price per unit for the item category in the given month.",
    "Allowed Values / Range": "Range: [0.716, 146.33]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales data.",
    "Allowed Values / Range": "Example: 01-2025",
    "Missing %": 0.0,
    "Cleaning / Notes": "Currently stored as an object (string). Needs to be converted to a proper datetime format for temporal analysis."
  }
]
```

### 5. Data Quality & Anomalies Section

*   **Issue:** `RetailerZipCode` contains values that are not standard 5-digit or 9-digit US zip codes (e.g., `907442424.0`, `961610393.0`).
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or inclusion of non-standard identifiers during data collection or processing.
    *   **Recommended handling rule:** Investigate the format of these anomalous zip codes. Attempt to parse them into standard 5-digit zip codes. If parsing is not possible or the values are clearly erroneous, flag them as invalid and set to null.

*   **Issue:** Missing values in `RetailerCity` (0.1%), `RetailerZipCode` (0.3%), and `RetailerCounty` (0.5%).
    *   **Likely cause:** Incomplete data entry or data collection.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, attempt imputation using a reliable mapping from `RetailerZipCode` (after cleaning it) or other available geographical data. For `RetailerZipCode`, if imputation is not feasible, consider flagging rows with missing values or excluding them from analyses requiring complete geographical information.

*   **Issue:** `Date` column is stored as an `object` (string) type.
    *   **Likely cause:** Default data type inference during extraction or storage.
    *   **Recommended handling rule:** Convert the `Date` column to a proper datetime format (e.g., YYYY-MM-DD) to enable accurate temporal analysis and sorting.

### 6. Reproducible Cleaning Plan

1.  **Standardize `RetailerZipCode`:** Inspect and clean the `RetailerZipCode` column to ensure all values conform to a standard 5-digit US zip code format. Invalid or unparseable entries should be set to null.
2.  **Handle Missing Geographical Data:** For missing `RetailerCity` and `RetailerCounty` values, attempt to impute them using a lookup table based on the cleaned `RetailerZipCode` or other available geographical information. If imputation is not possible, flag these rows or exclude them from analyses requiring complete location data.
3.  **Convert `Date` Column:** Convert the `Date` column from its current object (string) format (e.g., "01-2025") to a standard datetime format (e.g., "YYYY-MM-DD"). This will facilitate time-series analysis.
4.  **Validate Numerical Ranges:** Verify that `totalgrams`, `totalsales`, and `meanprice` fall within expected and logical ranges, flagging any outliers for further investigation.

### 7. Limitations & Trust Section

The reliability of geographical data, specifically `RetailerZipCode`, is currently limited due to the presence of non-standard and potentially erroneous values. This could impact analyses requiring accurate location-based insights. The completeness of `RetailerCity` and `RetailerCounty` is also a limitation due to missing values. To validate these elements, a comprehensive cross-reference with an authoritative geographical database (e.g., USPS zip code directory) is needed to correct or impute zip codes, cities, and counties.

### 8. Appendix: Quick Reference

*   **Zip Code Cleaning:** Standardize `RetailerZipCode` to 5-digit format; nullify or flag non-standard entries.
*   **Geographical Imputation:** Impute missing `RetailerCity` and `RetailerCounty` using cleaned `RetailerZipCode` where possible.
*   **Date Conversion:** Convert `Date` column to datetime objects for temporal analysis.
*   **Data Type Enforcement:** Ensure all columns have appropriate data types for analysis.
*   **Outlier Flagging:** Flag extreme values in `totalgrams`, `totalsales`, and `meanprice` for review.

### 9. Notes for Reviewers

Reviewers are requested to verify the accuracy of the proposed primary keys and relationships, as these were inferred. Additionally, please scrutinize the recommended handling rules for the `RetailerZipCode` anomaly and missing geographical data to ensure they align with project requirements and data governance policies. Verification of the `Date` column conversion logic is also crucial for reproducible temporal analysis.

---

# Work Documentation

## Table: salesquantity25

**Data Operations:**
The `salesquantity25` table, representing aggregated monthly sales data, underwent extensive cleaning, transformation, and analysis. This involved:
*   **Data Ingestion and Consolidation:** Multiple annual sales CSV files (from 2018 to 2024) were loaded and concatenated into a single comprehensive sales dataset. During this process, columns named `meanprice` and `v1` were dropped if present in the source files.
*   **Column Renaming:** Several columns were systematically renamed to ensure consistency and adherence to a standardized naming convention (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `ItemCategory` to `itemcategory`, `Date` to `date`).
*   **Geographical Data Cleaning and Imputation:**
    *   Initial cleaning involved replacing "NA" and "UNDEFINED" values in `retailercounty` with empty strings.
    *   The sales data was merged with an external "parent" dataset (containing license and company information) to enrich and potentially correct `retailercounty` values.
    *   A `county_map` was applied to standardize county names (e.g., "Alameda County" to "ALAMEDA"). Missing `retailercounty` values were imputed using corresponding values from the "parent" dataset where available.
    *   Specific manual corrections were applied to `retailercounty` for a list of known `retailerlicensenumber` values.
    *   All `retailercounty` values were converted to uppercase for consistency.
    *   A `zip5` column was extracted from `retailerzipcode` (taking the first five characters) and used to merge with an external HUD zip-to-county mapping dataset. This allowed for further imputation of missing `retailercounty` values based on zip code.
    *   Additional manual fixes were applied to `retailercounty` for another set of specific licenses.
    *   Final cleaning steps included converting all columns to string type and replacing empty strings, "<NA>", and "nan" with proper missing value indicators, followed by dropping rows with missing `retailercounty` values.
*   **Data Type Conversion:** The `date` column (originally an object/string) was used to derive a `year` column, and both `totalsales` and `year` were converted to numeric types, with errors coerced to missing values.
*   **Market Concentration Analysis (HHI):**
    *   The Herfindahl-Hirschman Index (HHI) was calculated at multiple levels:
        *   **Statewide Overall:** HHI based on individual retailer sales per year.
        *   **Statewide Parent Company:** HHI based on aggregated sales by parent company per year.
        *   **County-level Overall:** HHI based on individual retailer sales within each county per year.
        *   **County-level Parent Company:** HHI based on aggregated sales by parent company within each county per year.
    *   These calculations involved grouping data, summing `totalsales`, calculating market shares, and squaring them to derive the HHI.
*   **Derived Metrics:** `industry_sales`, `mkt_share`, `mkt_share2`, `county_sales`, `county_sales_parent`, `opacity`, and `opacity_parent` were calculated.
*   **Trend and Trajectory Analysis:**
    *   Counties were clustered based on their HHI trends over time (excluding 2018 data) using K-Means clustering.
    *   Linear regression was applied to HHI values for each county (from 2019 onwards) to determine the slope of HHI change, categorizing counties into "increasing," "decreasing," or "stable" trajectories.
    *   Year-over-year percentage change in HHI was calculated for each county.
*   **Exploratory Data Analysis and Visualization:** The processed data was used to generate various plots (line plots, bar plots, heatmaps, scatter plots, box plots, violin plots, histograms) to visualize sales trends, HHI distributions, and changes over time.
*   **Data Export:** Intermediate and final processed datasets, including HHI results, were exported to Stata (`.dta`), Excel (`.xlsx`), and CSV (`.csv`) formats. HTML files for interactive plots were also generated.

**Variables Affected:**
*   **Modified/Cleaned:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `RetailerCounty` (renamed to `retailercounty`), `ItemCategory` (renamed to `itemcategory`), `totalsales`, `Date` (renamed to `date`).
*   **Created:** `companyid`, `statelicenseid`, `multi_owner`, `primary_company`, `cannabiz_county` (from parent data), `zip5`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `HHI`, `HHI_parent_level`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Dropped (if present):** `meanprice`, `v1`, `_merge`, `retailercounty_from_license_county`, `_merge_lic_county`, `retailercounty_from_zip`, `_merge_zip`, `Unnamed: 0`.

**Logic and Methodology:**
The primary intent behind these operations was to create a robust and analytically ready dataset for understanding market dynamics and concentration within the cannabis retail sector.
*   **Standardization and Enrichment:** By consolidating data from multiple sources and years, and integrating external license and geographical information, the dataset was made more complete and consistent. This allowed for a more accurate representation of retailer and parent company affiliations and locations.
*   **Geographical Accuracy:** The multi-stage imputation strategy for `retailercounty` aimed to maximize the accuracy of location data, which is critical for county-level market analysis. Prioritizing external authoritative sources and internal consistency checks helped to mitigate data quality issues.
*   **Market Concentration Measurement:** The calculation of HHI at various granularities (statewide vs. county, individual retailer vs. parent company) provides a comprehensive view of market concentration. This methodology is standard in economic analysis for assessing competition.
*   **Temporal Analysis and Trend Identification:** Extracting the `year` and converting `date` to a proper format enabled time-series analysis, allowing for the observation of trends in sales and market concentration over several years. The use of linear regression and clustering further refined the understanding of these temporal dynamics, identifying distinct patterns of market evolution across different counties.
*   **Data-Driven Insights:** The derived metrics and visualizations were designed to provide actionable insights into market structure, competitive landscape, and geographical disparities in the cannabis retail industry.

**Validation and Verification:**
*   **Data Type Enforcement:** Explicit data type conversions were performed for numerical and date columns, with error handling to identify and manage problematic values.
*   **Missing Value Handling:** Missing values in critical geographical columns were systematically addressed through imputation and removal, with intermediate tracking of merge outcomes.
*   **Consistency Checks:** The process included steps to standardize county names and ensure consistency across different data sources.
*   **Visual Inspection:** Numerous plots were generated to visually inspect data distributions, identify outliers, and confirm the logical consistency of transformations and aggregations. For example, plots of HHI over time by county allowed for visual verification of trends and the impact of clustering/trajectory analysis.
*   **Intermediate Saves:** Saving the processed data to a Stata file (`sales_w_parent_co_test.dta`) at a key stage allowed for verification of the cleaning and merging steps before proceeding to advanced analysis.

**Results and Outcomes:**
The data work resulted in a significantly enhanced `salesquantity25` dataset, which is now suitable for advanced analytical tasks. Key outcomes include:
*   A unified and cleaned dataset of cannabis retail sales from 2018 to 2024, enriched with accurate geographical and parent company information.
*   A comprehensive set of HHI metrics, providing a detailed understanding of market concentration at both statewide and county levels, and distinguishing between individual retailer and parent company influence.
*   Identification of counties exhibiting increasing, decreasing, or stable HHI trends, offering insights into evolving competitive landscapes.
*   Categorization of counties into clusters based on their HHI trajectories, facilitating targeted policy or business strategies.
*   Visualizations that effectively communicate complex market dynamics, sales trends, and geographical disparities.
*   Exported summary tables and interactive plots that serve as direct outputs for reporting and further investigation into market structure and competition.