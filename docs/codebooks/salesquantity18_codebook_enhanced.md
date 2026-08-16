# Track & Trace Data Codebook

### Overview Section

This dataset represents aggregated sales information derived from the Track & Trace project, focusing on cannabis product sales. It provides insights into sales quantities, total revenue, and average prices across various retailers and item categories. Each row in the `salesquantity18` table represents aggregated sales data for a specific item category, sold by a particular retailer, within a given month. The overall data source is the Track & Trace project, with the collection period for the provided table spanning at least November 2018. The exact extraction date is not available.

**Assumptions:**
*   `totalgrams` and `totalsales` represent sums of quantities and revenues, respectively, aggregated over the specified month, retailer, and item category.
*   `meanprice` is an average price per gram, calculated for the corresponding aggregated period.
*   The `Date` column represents the month and year of aggregation.

### Table Inventory

*   **salesquantity18**: Contains monthly aggregated sales quantities, total sales revenue, and mean prices for various cannabis item categories, broken down by individual retailers.

## Table: salesquantity18

*   **Purpose:** To provide monthly aggregated sales data (quantity, value, average price) for different cannabis item categories across various retailers, enabling analysis of sales trends and performance.
*   **What one row represents:** Aggregated sales for a specific `ItemCategory` by a `RetailerLicenseNumber` in a given `Date` (month).
*   **Primary key(s):** Inferred composite key: `RetailerLicenseNumber`, `ItemCategory`, `Date`.
*   **Relationships:**
*   **Number of rows and columns:** 4 rows, 10 columns.
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
    "Allowed Values / Range": "[922624021.0, 922624021.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "100% missing values. This column is entirely empty."
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
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the aggregated sales data.",
    "Allowed Values / Range": "Example: 11-2018",
    "Missing %": 0.0,
    "Cleaning / Notes": "Currently stored as a string (object). Should be converted to datetime for time-series analysis."
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total grams sold for the given item category, retailer, and month.",
    "Allowed Values / Range": "[21.0, 2432.5]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue for the given item category, retailer, and month.",
    "Allowed Values / Range": "[201.85, 33892.26]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/gram",
    "Description": "Average price per gram for the given item category, retailer, and month.",
    "Allowed Values / Range": "[48.7658417266187, 83.1406593406593]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

### Data Quality & Anomalies Section

*   **Issue:** The `RetailerCounty` column in the `salesquantity18` table is 100% missing.
*   **Likely cause:** Data for this field was either not collected, not recorded, or was lost during the data extraction or aggregation process.
*   **Recommended handling rule:** If county-level analysis is not a critical requirement, the `RetailerCounty` column should be dropped. If county-level analysis is necessary, an attempt could be made to impute the county information using the `RetailerZipCode` in conjunction with a reliable external zip-to-county mapping dataset.

### Reproducible Cleaning Plan

1.  **Handle Missing `RetailerCounty` Data:** Assess the analytical need for the `RetailerCounty` column. If it is not essential for downstream analysis, drop the column from the `salesquantity18` table due to its 100% missing values. If county-level analysis is required, identify and integrate a reliable external dataset to map `RetailerZipCode` to `RetailerCounty` and impute the missing values.
2.  **Convert `Date` Column to Datetime:** Convert the `Date` column from its current `object` (string) data type to a proper datetime format (e.g., `YYYY-MM-DD` or `YYYY-MM`) to facilitate time-series analysis and chronological sorting.

### Limitations & Trust Section

*   **Missing `RetailerCounty` Data:** The `RetailerCounty` column is entirely missing, which severely limits any analysis requiring geographical segmentation at the county level. To validate or recover this data, an external, authoritative source mapping zip codes to counties would be required, and the accuracy of such a mapping would need to be verified.
*   **`Date` Column Format:** The `Date` column is currently stored as a string (`object`). While it contains month and year information, its string format prevents direct chronological operations or advanced time-series analysis without prior conversion. Trust in time-based aggregations or filters would be improved by converting this to a standard datetime object.
*   **Data Granularity:** The data is aggregated monthly. Finer-grained analysis (e.g., daily or weekly trends) is not possible with this dataset.

### Appendix: Quick Reference

*   **`RetailerCounty`:** 100% missing; consider dropping or imputing.
*   **`Date`:** Convert from string (`object`) to datetime for time-series analysis.
*   **Primary Key:** Inferred composite key: `RetailerLicenseNumber`, `ItemCategory`, `Date`.
*   **Quantitative Metrics:** `totalgrams`, `totalsales`, `meanprice` are key performance indicators.
*   **Data Scope:** Aggregated monthly sales data for cannabis products by retailer and item category.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred primary key for the `salesquantity18` table. Additionally, please confirm the proposed handling rules for the `RetailerCounty` column and the `Date` column's data type conversion align with project requirements and analytical objectives. Any additional known relationships between this table and other Track & Trace datasets should also be noted for completeness.

# Work Documentation

## Table: salesquantity18 (Retail Sales Data)

**Data Operations:**
The `salesquantity18` table, representing retail sales data, was loaded from multiple CSV files spanning various years (e.g., `sales18.csv` through `sales24.csv`) and concatenated into a single dataset. Initial cleaning involved dropping potentially redundant or irrelevant columns such as `meanprice` and `v1`. Key columns were consistently renamed for clarity, including `RetailerLicenseNumber` to `retailerlicensenumber`, `RetailerCounty` to `retailercounty`, `Date` to `date`, and `ItemCategory` to `itemcategory`.

A significant effort was made to standardize and impute missing `retailercounty` values. This involved:
1.  Replacing "NA" and "UNDEFINED" strings with empty strings.
2.  Merging with an external `parent_df` (licenses data) using `retailerlicensenumber` to inherit county information from a more reliable source (`cannabiz_county`).
3.  Applying a predefined `county_map` to standardize county names from the `cannabiz_county` column where `retailercounty` was still missing.
4.  Implementing specific manual fixes for known license numbers with incorrect or missing county data.
5.  Converting all `retailercounty` values to uppercase for consistency.
6.  Further imputation by deriving county information from other entries associated with the same `retailerlicensenumber` within the dataset.
7.  Extracting a 5-digit zip code (`zip5`) from `retailerzipcode` and merging with an external `zip_df` (ZIP to County mapping) to fill remaining missing `retailercounty` values.
8.  Applying additional manual fixes for specific license numbers.
9.  Finally, empty strings, "<NA>", and "nan" values in `retailercounty` were converted to proper missing values and then rows with missing `retailercounty` were dropped.

The `date` column was used to derive a `year` column, and `totalsales` and `year` were converted to numeric data types. The data was then aggregated by `retailerlicensenumber` and `year` to calculate total sales and market share. A separate aggregation was performed at the parent company level by first ensuring all retailers had an associated `primary_company` (defaulting to `retailerlicensenumber` if missing).

Herfindahl-Hirschman Index (HHI) was calculated at both the overall retailer level and the parent company level, for statewide and county-level aggregations, to measure market concentration. These HHI results were then combined and enriched with total sales and "opacity" metrics (representing county sales as a percentage of maximum statewide sales).

Further analysis involved filtering data to years 2019-2025, performing K-Means clustering on HHI trends, and classifying counties into "increasing," "decreasing," or "stable" HHI trajectories based on linear regression slopes. Year-over-year HHI percentage change was also calculated.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `Date` (renamed to `date`, used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric).
*   **Created:** `year` (derived from `date`), `zip5` (derived from `retailerzipcode`), `primary_company` (derived from `parent_df` and imputed), `industry_sales` (aggregated total sales for market share calculation), `mkt_share` (market share percentage), `mkt_share2` (squared market share for HHI), `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster` (from K-Means), `hhi_change` (year-over-year percentage change).
*   **Validated:** `retailercounty` (through multiple imputation and standardization steps).

**Logic and Methodology:**
The primary objective of the data work was to prepare the retail sales data for market concentration analysis using the Herfindahl-Hirschman Index (HHI) and to visualize sales trends. A key challenge was the high percentage of missing `RetailerCounty` data, which was addressed through a multi-stage imputation strategy leveraging external license data, ZIP code mappings, and internal consistency checks. This ensures that geographical analysis, crucial for market concentration, is as accurate and complete as possible. The calculation of HHI at both overall retailer and parent company levels provides a comprehensive view of market structure, accounting for potential common ownership. Trend analysis through linear regression and clustering helps identify dynamic shifts in market concentration across different counties. The "opacity" metric provides context on the relative economic size of each county's cannabis market.

**Validation and Verification:**
*   The `retailercounty` column underwent multiple validation steps, including cross-referencing with external license data and ZIP-to-county mappings, as well as internal consistency checks based on `retailerlicensenumber`. Manual fixes were applied for specific known discrepancies.
*   Merge operations (`parent_temp`, `zip_df`, `license_county`) included indicator columns (`_merge`, `_merge_lic_county`, `_merge_zip`) to track the success and source of merges, allowing for verification of data integration.
*   Data types for `totalsales` and `year` were explicitly converted to numeric, with error handling (`errors="coerce"`) to identify and manage non-numeric values.
*   The final HHI calculations were aggregated and exported to Excel and CSV files, allowing for external review and validation of the computed market concentration metrics.
*   Visualizations (line plots, bar charts, box plots, heatmaps, scatter plots) were generated to visually inspect trends, distributions, and relationships, providing a qualitative check on the data transformations and analytical results.
*   Correlation analysis was performed between HHI, total sales, and county sales to understand their relationships.

**Results and Outcomes:**
The data work resulted in a cleaned, standardized, and enriched retail sales dataset (`sales_w_parent_co_test.dta`) suitable for advanced market analysis. The `retailercounty` column, initially problematic, was substantially populated and standardized, enabling robust county-level analysis. The calculated HHI metrics provide quantitative measures of market concentration over time and across different geographical levels (statewide, county) and organizational structures (individual retailer, parent company). The trend analysis identified counties with increasing, decreasing, or stable HHI, offering insights into market evolution. Various visualizations were produced to illustrate these trends, distributions, and relationships, facilitating a deeper understanding of the cannabis retail market dynamics. Key outputs include `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`, and several HTML plots for interactive exploration of HHI trends and changes.

## Table: Licenses Data (parent_df)

**Data Operations:**
This dataset, referred to as `parent_df` in the scripts, was loaded from a CSV file ("Cannabis Market Intelligence Platform Report - Licenses - 2025-07-03.csv" and later "Cannabis Market Intelligence Platform Report - Licenses - 2025-02-21.csv"). It serves as a master list for company and license information.
1.  **Column Renaming:** Columns were renamed for consistency and ease of use: "Company ID" to `companyid`, "Country" to `county`, and "State License ID" to `statelicenseid`. Later, `statelicenseid` was further renamed to `licenseNumber` (or `retailerlicensenumber` in the sales context).
2.  **Multi-Owner Identification:** A `multi_owner` flag was created to identify companies with multiple owners by searching for a semicolon in the `companyid` string.
3.  **Primary Company Extraction:** A `primary_company` column was derived from `companyid`. If `multi_owner` was identified, only the first part of the `companyid` (before the semicolon) was taken as the `primary_company`; otherwise, the full `companyid` was used.
4.  **Data Type Conversion:** The `primary_company` column was converted to a numeric type, coercing errors to missing values.
5.  **Column Selection:** The dataset was reduced to essential columns: `licenseNumber` (or `retailerlicensenumber`) and `primary_company` (and `county` in some instances).
6.  **Deduplication and Filtering:** Duplicate rows were removed, and rows with missing or empty `licenseNumber` values were filtered out to ensure data integrity.

**Variables Affected:**
*   **Modified:** `Company ID` (renamed to `companyid`), `Country` (renamed to `county`), `State License ID` (renamed to `statelicenseid`, then `licenseNumber` or `retailerlicensenumber`).
*   **Created:** `multi_owner` (binary flag), `primary_company` (extracted identifier).
*   **Validated:** `licenseNumber` (filtered for non-missing/non-empty values).

**Logic and Methodology:**
The purpose of processing the Licenses Data was to create a clean and standardized lookup table for license numbers and their associated primary company identifiers. This is crucial for aggregating data at the parent company level, which is necessary for a more accurate assessment of market concentration. The `multi_owner` and `primary_company` extraction logic handles cases where a single license might be associated with multiple company IDs, ensuring a consistent primary identifier for aggregation.

**Validation and Verification:**
*   Column renames were explicitly defined.
*   The `primary_company` conversion to numeric included error coercion, indicating potential issues with the source `companyid` format.
*   Deduplication and filtering steps were applied to ensure unique and valid license entries.
*   This dataset was used as a lookup table for `cultivation_df` and `sales_df`, implying its structure and content were considered reliable for merging.

**Results and Outcomes:**
A clean `parent_df` was generated, containing unique license numbers and their corresponding primary company identifiers. This dataset was instrumental in enriching both the cultivation and retail sales data, enabling analysis at the parent company level.

## Table: Cultivation Data (cultivation_df)

**Data Operations:**
The `cultivation_df` was loaded from an Excel file ("Working Cultivation Canopy June 2025.xlsx").
1.  **Filtering by Status:** Only licenses with an "Active" `licenseStatus` were retained.
2.  **Missing Value Handling:** Rows with missing values in the `LargeDate` column were removed.
3.  **License Type Standardization:** A `type` column was created by mapping various detailed `licenseType` values (e.g., "Large Indoor", "Specialty Cottage Mixed-Light Tier 1") to broader categories like "Indoor", "Mixed_Light", and "Outdoor". Missing `type` values were filled with empty strings.
4.  **Microbusiness Classification:** `micro_cult` and `micro_indoor` flags were created based on the `activity` column to specifically classify microbusiness licenses.
5.  **Conditional Filtering:** Specific "Microbusiness" entries that were not cultivators were filtered out.
6.  **Conditional Type Assignment:** For "Microbusiness" licenses, the `type` was further refined to "Outdoor" or "Indoor" based on the `micro_indoor` flag.
7.  **Data Type Consistency:** `licenseNumber` columns in both `cultivation_df` and `parent_df` were converted to string type to ensure successful merging.
8.  **Data Integration:** `cultivation_df` was merged with `parent_df` (Licenses Data) using `licenseNumber` as the key, performing an inner join with a `many_to_one` validation. The result was saved to a Stata file ("cultivation.dta") and then reloaded.
9.  **HHI Calculation:** The core operation involved calculating the Herfindahl-Hirschman Index (HHI) for market concentration. This was performed iteratively for each `grow_type` ("Indoor", "Mixed_Light", "Outdoor") and at four levels of aggregation:
    *   Statewide, overall (by `businessLegalName`)
    *   Statewide, parent company level (by `primary_company`)
    *   County-level, overall (by `businessLegalName` and `premiseCounty`)
    *   County-level, parent company level (by `primary_company` and `premiseCounty`)
    These calculations involved grouping by relevant identifiers, summing `Canopy` and `MaxSqFt`, calculating market shares, and then squaring and summing these shares to get the HHI.
10. **Result Consolidation and Export:** All HHI results were combined into a single DataFrame, numeric columns were rounded and converted to integers, and the final dataset was exported to Excel files (e.g., `Cult_HHI__Indoor_test.xlsx`, `Cult_HHI_DeepDive.xlsx`) and CSV files (`Cult_HHI_Summary.csv`, `Cult_Size_vs_HHI.csv`).

**Variables Affected:**
*   **Modified:** `licenseStatus` (filtered), `LargeDate` (filtered), `licenseType` (used to derive `type`), `activity` (used to derive `micro_cult`, `micro_indoor`).
*   **Created:** `type` (standardized license type), `micro_cult` (cultivator flag), `micro_indoor` (indoor cultivation flag), `mkt_share_Canopy`, `mkt_share2_Canopy`, `mkt_share_MaxSqFt`, `mkt_share2_MaxSqFt` (for HHI calculations).
*   **Validated:** `licenseNumber` (through merge validation).

**Logic and Methodology:**
The processing of cultivation data aimed to analyze market concentration within the cannabis cultivation sector, segmented by grow type (Indoor, Mixed-Light, Outdoor) and organizational structure (individual business vs. parent company). The extensive cleaning and standardization of `licenseType` and the specific handling of "Microbusiness" licenses ensure that the market segmentation is accurate. The HHI calculations provide a quantitative measure of competition, which is critical for regulatory and economic analysis.

**Validation and Verification:**
*   Filtering by `licenseStatus` and `LargeDate` ensures that only relevant and complete records are used.
*   The `many_to_one` merge validation with `parent_df` helps ensure the integrity of the license number linkage.
*   The iterative HHI calculation for different grow types and aggregation levels allows for detailed scrutiny of market structure.
*   Results were exported to multiple formats for review and further analysis.

**Results and Outcomes:**
A comprehensive set of HHI metrics for the cultivation market, broken down by grow type, geography, and organizational level, was generated. This provides valuable insights into the competitive landscape of cannabis cultivation.

## Table: Harvest Data (harvest_df)

**Data Operations:**
The `harvest_df` was constructed by concatenating data from multiple CSV files (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`).
1.  **Concatenation and Initial Save:** Multiple harvest quantity files were loaded and combined into a single DataFrame, which was then saved as "harvest.csv".
2.  **Column Renaming:** Columns were renamed for consistency: `HarvesterLicenseNumber` to `harvesterlicensenumber`, `HarvesterFacilityType` to `harvesterfacilitytype`, `HarvesterCity` to `harvestercity`, `HarvesterZipCode` to `harvesterzipcode`, `HarvesterCounty` to `harvestercounty`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`, `TotalHarvestWetPounds` to `totalharvestwetpounds`, and `UniqueHarvestBatches` to `uniqueharvestbatches`.
3.  **Data Type Conversion:** `year`, `totalharvestpounds`, and `totalharvestwetpounds` were converted to numeric types, coercing errors to missing values.
4.  **County Standardization:** The `harvestercounty` column underwent extensive cleaning:
    *   "NA" and "UNDEFINED" strings were replaced with empty strings.
    *   A `county_map` was used to standardize various county name formats (e.g., "Alameda County" to "ALAMEDA").
    *   Rows with missing `harvestercounty` values were dropped.
    *   Whitespace was stripped, and " County" suffixes were removed.
    *   Empty strings were replaced with `pd.NA`, and rows with resulting missing values were dropped.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`), `HarvesterFacilityType` (renamed to `harvesterfacilitytype`), `HarvesterCity` (renamed to `harvestercity`), `HarvesterZipCode` (renamed to `harvesterzipcode`), `HarvesterCounty` (renamed to `harvestercounty`, extensively cleaned and standardized), `PkgYear` (renamed to `year`), `TotalHarvestPounds` (renamed to `totalharvestpounds`, converted to numeric), `TotalHarvestWetPounds` (renamed to `totalharvestwetpounds`, converted to numeric), `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`).
*   **Validated:** `harvestercounty` (through standardization and missing value removal).

**Logic and Methodology:**
The goal of processing the Harvest Data was to consolidate harvest information from various years and to clean and standardize key identifiers, particularly the `harvestercounty` column. This standardization is critical for accurate geographical analysis and for merging with other datasets. Converting quantitative metrics to numeric types ensures they can be used in calculations.

**Validation and Verification:**
*   Explicit column renames ensure clarity.
*   Numeric conversions with error coercion help identify data quality issues.
*   The multi-step county cleaning process, including mapping and dropping missing values, aims for high data quality in this critical geographical field.

**Results and Outcomes:**
A clean and standardized `harvest_df` was created, ready for integration with other datasets, particularly the package data, to analyze harvest-to-package ratios.

## Table: Package Data (package_df)

**Data Operations:**
The `package_df` was constructed by concatenating data from multiple CSV files (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`).
1.  **Concatenation and Initial Save:** Multiple package quantity files were loaded and combined into a single DataFrame, which was then saved as "package.csv".
2.  **Column Renaming:** Columns were renamed for consistency: `HarvesterLicenseNumber` to `harvesterlicensenumber`, `HarvesterFacilityType` to `harvesterfacilitytype`, `HarvesterCity` to `harvestercity`, `HarvesterZipCode` to `harvesterzipcode`, `HarvesterCounty` to `harvestercounty`, `ItemCategory` to `itemcategory`, `Year` to `year`, `TotalPackagePounds` to `totalpackagepounds`, and `UniqueHarvestBatches` to `uniqueharvestbatches`.
3.  **Data Type Conversion:** `year` and `totalpackagepounds` were converted to numeric types, coercing errors to missing values.
4.  **County Standardization:** Similar to `harvest_df`, the `harvestercounty` column underwent cleaning:
    *   A `county_map` was used to standardize various county name formats.
    *   Rows with missing `harvestercounty` values were dropped.
    *   Whitespace was stripped, and empty strings were replaced with `pd.NA`.
    *   Rows with resulting missing values were dropped.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`), `HarvesterFacilityType` (renamed to `harvesterfacilitytype`), `HarvesterCity` (renamed to `harvestercity`), `HarvesterZipCode` (renamed to `harvesterzipcode`), `HarvesterCounty` (renamed to `harvestercounty`, cleaned and standardized), `ItemCategory` (renamed to `itemcategory`), `Year` (renamed to `year`, converted to numeric), `TotalPackagePounds` (renamed to `totalpackagepounds`, converted to numeric), `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`).
*   **Validated:** `harvestercounty` (through standardization and missing value removal).

**Logic and Methodology:**
The processing of Package Data aimed to consolidate package information from various years and to clean and standardize key identifiers, particularly the `harvestercounty` column. This standardization is essential for accurate geographical analysis and for merging with harvest data to calculate ratios.

**Validation and Verification:**
*   Explicit column renames ensure clarity.
*   Numeric conversions with error coercion help identify data quality issues.
*   The multi-step county cleaning process, including mapping and dropping missing values, aims for high data quality in this critical geographical field.

**Results and Outcomes:**
A clean and standardized `package_df` was created, ready for integration with harvest data.

## Table: Merged Harvest and Package Data

**Data Operations:**
This table represents the integration of the cleaned `harvest_df` and `package_df`.
1.  **Merging:** `package_df` was merged with `harvest_df` using a left join on `harvesterlicensenumber` and `year`, with suffixes `_pkg` and `_harv` to distinguish columns from the two sources.
2.  **County Consolidation:** The `harvestercounty` column was consolidated, prioritizing the harvest-derived county (`harvestercounty_harv`) and falling back to the package-derived county (`harvestercounty_pkg`) if the former was missing.
3.  **Ratio Calculation:** Several new ratio metrics were calculated:
    *   `package_to_harvest_ratio`: `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: `totalpackagepounds` divided by `totalharvestpounds`.
4.  **Final County Cleaning:** The consolidated `harvestercounty` column underwent a final cleaning pass, replacing empty strings, "NA", and "nan" with `pd.NA`, and then dropping rows with missing county values.
5.  **Aggregation:** The merged data was aggregated into two summary tables:
    *   `category_summary`: Grouped by `harvestercounty`, `year`, and `itemcategory`, summing `totalpackagepounds` and averaging `package_to_harvest_ratio`.
    *   `county_summary`: Grouped by `harvestercounty` and `year`, summing `totalpackagepounds` and `totalharvestpounds`, and recalculating `package_to_harvest_ratio`.
6.  **Export:** The `county_summary` was exported to an Excel file ("harvest_package_ratios.xlsx").
7.  **Visualization:** Various plots (bar charts for harvest pounds, package pounds, and package-to-harvest ratio) were generated for the top 10 counties (based on total harvest pounds) for each year.

**Variables Affected:**
*   **Modified:** `harvestercounty` (consolidated from two sources, further cleaned).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Aggregated:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (in `category_summary` and `county_summary`).

**Logic and Methodology:**
The integration of harvest and package data is crucial for understanding the efficiency and yield of cultivation operations. By merging these datasets and calculating key ratios, the analysis can identify trends in how much harvested material is ultimately packaged and sold. The aggregation steps provide summarized views at both category and county levels, facilitating high-level analysis. The visualizations help in quickly identifying top-performing counties and trends over time.

**Validation and Verification:**
*   The merge operation explicitly handled suffixes to track column origins.
*   The `harvestercounty` consolidation logic ensures that the most reliable county information is used.
*   Ratio calculations are direct and based on the numeric conversions performed earlier.
*   The aggregation logic is clearly defined, grouping by relevant dimensions.
*   The exported summary table and generated plots provide verifiable outputs for review.

**Results and Outcomes:**
A merged dataset with calculated ratios provides insights into the conversion efficiency from harvest to package. The `harvest_package_ratios.xlsx` file and associated plots offer a clear overview of these metrics across counties and years, highlighting regional differences and temporal trends.

## Table: ZIP to County Mapping (zip_df)

**Data Operations:**
This dataset, referred to as `zip_df` in the scripts, was loaded from an Excel file ("ZIP_COUNTY_122024.xlsx").
1.  **State Filtering:** The data was filtered to include only entries for California (`USPS_ZIP_PREF_STATE == "CA"`).
2.  **Deduplication:** Duplicate entries based on the `ZIP` code were removed, keeping only one entry per ZIP code.
3.  **Column Selection and Renaming:** Only the `ZIP` and `retailercounty` columns were retained, and `ZIP` was renamed to `zip5` for consistency with other datasets.

**Variables Affected:**
*   **Modified:** `USPS_ZIP_PREF_STATE` (filtered), `ZIP` (deduplicated, renamed to `zip5`).
*   **Selected:** `retailercounty`.

**Logic and Methodology:**
The purpose of processing the ZIP to County Mapping data was to create a clean and unique lookup table that maps 5-digit ZIP codes to their corresponding counties within California. This is essential for imputing missing county information in other datasets, particularly the retail sales data, where `RetailerZipCode` is available but `RetailerCounty` might be missing.

**Validation and Verification:**
*   Filtering by state ensures relevance to the project's geographical scope.
*   Deduplication ensures a one-to-one or one-to-many (if a zip spans multiple counties, but `keep=False` implies unique zip-county pairs are desired) mapping for ZIP codes, preventing ambiguity during merges.
*   The dataset was used as a lookup table for `sales_df`, implying its structure and content were considered reliable for merging.

**Results and Outcomes:**
A clean `zip_df` was generated, providing a reliable mapping from 5-digit ZIP codes to California counties. This dataset was successfully used to enrich the retail sales data by filling in missing `retailercounty` values.