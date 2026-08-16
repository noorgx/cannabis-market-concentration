# Track & Trace Data Codebook

### Overview Section

This dataset provides aggregated monthly sales and quantity data for cannabis products within the Track & Trace project. It captures transactional information at the retailer level, detailing sales volumes and revenues across various item categories. Each row in the `salesquantity22` table represents the total sales and quantity for a specific item category by a unique licensed retailer for a given month. The data originates from the Track & Trace system, with the `salesquantity22` table specifically covering data for the year 2022. The exact data extraction date is not available.

**Assumptions:**
*   The table name `salesquantity22` indicates that the data pertains to the calendar year 2022.
*   The `Date` column, exemplified by "01-2022", represents the month and year for which the sales and quantity data are aggregated.

### Table Inventory

*   **salesquantity22:** Provides aggregated monthly sales and quantity data for various item categories across different licensed cannabis retailers.

### Table: salesquantity22

*   **Purpose:** To track monthly sales volume and revenue for different cannabis product categories by individual licensed retailers, facilitating analysis of market trends and retailer performance.
*   **What one row represents:** One month's aggregated sales and quantity data for a specific `ItemCategory` by a unique `RetailerLicenseNumber`.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 53469 rows, 10 columns
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000622-LIC",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility or license held by the retailer.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: STOCKTON",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "int64",
    "Units": "",
    "Description": "Zip code of the retailer's facility.",
    "Allowed Values / Range": "Range: [90008.0, 961610393.0]",
    "Missing %": "0.0",
    "Cleaning / Notes": "The wide range suggests potential inclusion of ZIP+4 codes or data entry errors. Standardization to 5-digit zip codes is recommended."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: SAN JOAQUIN",
    "Missing %": "10.0",
    "Cleaning / Notes": "10% of values are missing. Imputation using RetailerZipCode or RetailerCity, if a reliable mapping exists, is recommended."
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
    "Description": "Total quantity of the item category sold in grams for the given month.",
    "Allowed Values / Range": "Range: [0.4191, 622627.02]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the item category in USD for the given month.",
    "Allowed Values / Range": "Range: [0.5, 8184776.28]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per gram",
    "Description": "Average price per gram for the item category for the given month.",
    "Allowed Values / Range": "Range: [0.5, 129.516666666667]",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the aggregated sales data.",
    "Allowed Values / Range": "Example: 01-2022",
    "Missing %": "0.0",
    "Cleaning / Notes": "Consider converting to a datetime format for easier temporal analysis."
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerCounty` (10% missing).
    *   **Likely cause:** Incomplete data entry during the initial data collection process or issues during data extraction/transformation.
    *   **Recommended handling rule:** Attempt to impute missing `RetailerCounty` values by leveraging `RetailerZipCode` or `RetailerCity` through a reliable external mapping. If imputation is not feasible or reliable, flag these records for further investigation or exclude them from analyses requiring county-level granularity.
*   **Issue:** Inconsistent formatting and wide range in `RetailerZipCode` values.
    *   **Likely cause:** The presence of both 5-digit ZIP codes and ZIP+4 extensions, or potential data entry errors, leading to a very broad numerical range that is not representative of standard 5-digit zip codes.
    *   **Recommended handling rule:** Standardize all `RetailerZipCode` values to a consistent 5-digit format. This may involve truncating any ZIP+4 extensions. Subsequently, validate these standardized zip codes against a master list of valid zip codes for the relevant geographic region to identify and correct or flag invalid entries.

### Reproducible Cleaning Plan

1.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column to a string data type and then extract only the first five characters to ensure a consistent 5-digit zip code format.
2.  **Impute `RetailerCounty`:** Utilize an external, validated mapping (e.g., a zip-to-county lookup table) to impute missing `RetailerCounty` values based on the standardized `RetailerZipCode` or `RetailerCity`.
3.  **Validate `RetailerZipCode`:** Cross-reference the standardized 5-digit `RetailerZipCode` values against a comprehensive list of valid zip codes for the operational region. Flag any entries that do not match a valid zip code for further review or correction.
4.  **Convert `Date` to Datetime:** Transform the `Date` column from its current object type (e.g., "01-2022") into a proper datetime object for enhanced temporal analysis capabilities.

### Limitations & Trust Section

*   **`RetailerCounty`:** The 10% missing values in `RetailerCounty` introduce a limitation for analyses that rely on complete geographic data at the county level. The trustworthiness of county-level aggregations will be compromised without successful and validated imputation. Validation requires a robust and up-to-date mapping of zip codes or cities to counties.
*   **`RetailerZipCode`:** The observed wide range and potential for mixed ZIP+4 formats in `RetailerZipCode` suggest data inconsistency. If not properly standardized and validated, this could lead to inaccurate geographic assignments and flawed location-based analyses. Trust in location-specific insights depends on thorough cleaning and validation against authoritative zip code data.

### Appendix: Quick Reference

*   Standardize `RetailerZipCode` to a 5-digit string format.
*   Impute missing `RetailerCounty` values using a reliable zip-to-county or city-to-county mapping.
*   Validate `RetailerZipCode` entries against a master list of valid zip codes.
*   Convert the `Date` column to a datetime data type for improved temporal analysis.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the column descriptions, especially for inferred units and purposes. Particular attention should be paid to the proposed handling rules for `RetailerCounty` imputation and `RetailerZipCode` standardization, ensuring they align with project requirements and data privacy guidelines. Additionally, confirm that the primary key assumptions are sound for the intended analytical use cases.

---

# Work Documentation

## Table: salesquantity22

**Data Operations:**
The `salesquantity22` data, originally sourced from `sales22.csv`, was integrated into a larger, consolidated sales dataset (`sales_df`) encompassing sales data from 2018 through 2024. This consolidation served as the foundation for subsequent cleaning, transformation, and analytical processes.

*   **Data Ingestion and Consolidation:** Individual sales files, including `sales22.csv`, were read into pandas DataFrames with all columns initially treated as strings. During this process, columns named `meanprice` and `v1` were systematically dropped if present in any of the input files. The individual year-specific DataFrames were then concatenated to form a single, comprehensive `sales_df`.
*   **Column Renaming:** For consistency and ease of use, several columns were renamed: `RetailerLicenseNumber` became `retailerlicensenumber`, `RetailerCounty` became `retailercounty`, `RetailerFacilityType` became `retailerfacilitytype`, `RetailerCity` became `retailercity`, `RetailerZipCode` became `retailerzipcode`, `Date` became `date`, and `ItemCategory` became `itemcategory`. The `totalsales` column name was confirmed.
*   **Data Sorting:** The consolidated `sales_df` was sorted by a composite key including `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales` to ensure a consistent ordering for subsequent operations.
*   **External Data Integration:** The sales data was enriched by merging with an external `parent_df` (derived from a "Cannabis Market Intelligence Platform Report - Licenses") using the `retailerlicensenumber` as the join key. This merge introduced `primary_company` (identifying the ultimate parent company) and `cannabiz_county` information. Records present only in the external license data were excluded from the merged dataset.
*   **Geographic Data Cleaning and Imputation:**
    *   Initial cleaning steps involved replacing "NA" and "UNDEFINED" string values in the `retailercounty` column with empty strings.
    *   Missing `retailercounty` values were then imputed using the `cannabiz_county` column, which was brought in via the external license data merge. A predefined mapping was applied to standardize full county names (e.g., "Alameda County") to their uppercase short forms (e.g., "ALAMEDA").
    *   Specific `retailercounty` values for certain `retailerlicensenumber` entries were manually corrected based on known information.
    *   All `retailercounty` values were converted to uppercase for further standardization.
    *   A `license_county` mapping was generated from unique, non-empty `retailerlicensenumber` and `retailercounty` pairs within the dataset. This mapping was subsequently used to fill any remaining empty `retailercounty` values.
    *   The `retailerzipcode` column was standardized by extracting only the first five digits, creating a new `zip5` column.
    *   Further imputation of missing `retailercounty` values was performed by merging the dataset with an external `zip_df` (from "HUD/ZIP_COUNTY_122024.xlsx"), which provides a mapping from 5-digit zip codes to counties.
    *   An additional set of manual corrections was applied to `retailercounty` for specific `retailerlicensenumber` entries.
    *   Finally, empty strings, "NA", and "nan" values in `retailercounty` were converted to `pd.NA` (missing values), and any records still containing missing `retailercounty` values were dropped from the dataset.
*   **Temporal Data Transformation:** A `year` column was extracted from the `date` column by slicing characters 3 through 7 of the string representation.
*   **Type Conversion:** The `totalsales` and the newly extracted `year` columns were converted to numeric data types, with any conversion errors being coerced to `NaN`.
*   **Hierarchical Aggregation for HHI Calculation:** The processed sales data was extensively aggregated to calculate the Herfindahl-Hirschman Index (HHI) for market concentration at various levels:
    *   **Statewide HHI (Overall):** Aggregated `totalsales` by individual retailer and year to calculate market share and HHI for the entire state.
    *   **Statewide HHI (Parent Company):** Aggregated `totalsales` by primary parent company and year to calculate market share and HHI for the entire state at the parent company level.
    *   **County-level HHI (Overall):** Aggregated `totalsales` by individual retailer, county, and year to calculate market share and HHI within each county.
    *   **County-level HHI (Parent Company):** Aggregated `totalsales` by primary parent company, county, and year to calculate market share and HHI within each county at the parent company level.
*   **Derived Metrics:** Additional metrics such as `county_sales` (total sales per county) and `opacity` (county sales relative to maximum sales) were calculated to provide further context for market analysis.
*   **Trend Analysis and Clustering:**
    *   Linear regression was applied to the HHI values over time for each county to classify their HHI trajectories as "increasing," "decreasing," or "stable."
    *   K-Means clustering was performed on the HHI values to group counties with similar market concentration trends.
*   **Percentage Change Analysis:** Year-over-year percentage change in HHI (`hhi_change`) was calculated to quantify the rate of change in market concentration.
*   **City-level Sales Analysis:** `totalsales` was aggregated by `date` and `retailercity` to identify and visualize sales trends in the top-performing cities.
*   **Data Export:** The final processed sales data, including parent company information and cleaned geographic details, was saved as a Stata file (`sales_w_parent_co_test.dta`). Various HHI results and summary tables were exported to CSV and Excel formats (`hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`). Visualizations were also generated and saved as image files or interactive HTML files.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber`, `RetailerCounty`, `RetailerFacilityType`, `RetailerCity`, `RetailerZipCode`, `Date`, `ItemCategory`, `totalsales` (all underwent renaming, type conversion, and/or extensive cleaning). The `retailercounty` column was significantly transformed through imputation and standardization.
*   **Created:** `primary_company` (identifying parent entities), `cannabiz_county` (from external merge), `zip5` (standardized zip code), `year` (extracted from date), `industry_sales` (total sales for a given scope), `mkt_share` (market share percentage), `mkt_share2` (squared market share for HHI), `county_sales`, `county_sales_parent` (aggregated sales by county), `opacity`, `opacity_parent` (visual weighting metrics), `cluster` (K-Means cluster assignment), `hhi_change` (year-over-year HHI percentage change).
*   **Validated:** `retailercounty` and `retailerzipcode` were implicitly validated through multiple imputation steps and the removal of records where geographic information remained unresolvable.

**Logic and Methodology:**
The overarching goal of the data work was to transform raw sales data, including the `salesquantity22` component, into a robust dataset suitable for in-depth market concentration analysis. The methodology addressed several key data quality challenges identified in the original Codebook, particularly concerning geographic data. By consolidating multi-year sales data, the analysis gained a temporal dimension. The integration of external license data allowed for the identification of parent companies, which is critical for a more accurate assessment of market power beyond individual licenses. The multi-stage imputation and standardization of county and zip code information aimed to maximize data completeness and accuracy for location-based analyses. The calculation of HHI at various granularities (statewide, county, individual retailer, parent company) provides a comprehensive view of market structure. Subsequent analyses, such as trend classification and clustering, were designed to extract actionable insights into the evolution of market concentration.

**Validation and Verification:**
Data validation was embedded throughout the process:
*   Merge operations included `indicator=True` to track the success and nature of joins, allowing for verification of data integration.
*   Manual corrections for specific license numbers and counties indicate a process of human review and expert-driven data refinement.
*   The creation of internal `license_county` mappings and the use of external `zip_df` for imputation represent systematic attempts to establish authoritative sources for geographic data.
*   The final step of converting ambiguous string values to `pd.NA` and dropping records with persistent missing `retailercounty` values served as a crucial quality control measure, ensuring that downstream analyses are performed on reliable geographic data.
*   The rounding of HHI values to integers for final exports suggests a focus on presentation and interpretability.

**Results and Outcomes:**
The data work successfully produced a significantly cleaner, more complete, and analytically enriched sales dataset. Key outcomes include:
*   A consolidated, multi-year sales dataset (`sales_w_parent_co_test.dta`) that incorporates the `salesquantity22` data, ready for advanced analytical modeling.
*   Enhanced geographic data quality, with `retailercounty` and `retailerzipcode` being largely standardized and imputed, directly addressing the "Data Quality & Anomalies" noted in the Codebook.
*   The creation of `primary_company` identifiers, enabling a more sophisticated analysis of market concentration at the parent company level.
*   A comprehensive set of HHI metrics, calculated at statewide and county levels for both individual retailers and parent companies, providing critical insights into market structure.
*   Identification of HHI trends (increasing, decreasing, stable) and clusters of counties with similar market dynamics, offering valuable strategic intelligence.
*   Generation of various analytical outputs, including summary tables and a suite of visualizations (e.g., HHI trends over time, city sales trends, HHI distributions), to support data-driven decision-making and reporting.