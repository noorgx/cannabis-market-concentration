# Track & Trace Data Codebook

## Table Of Content


### Cultivation
- [Table: cultpanelsize](#table-cultpanelsize)
- [Table: harvestpackagemerge19-24](#table-harvestpackagemerge19-24)
- [Table: harvestpackagemerge23-24](#table-harvestpackagemerge23-24)
- [Table: harvestpackagemerge25](#table-harvestpackagemerge25)
- [Table: harvestqty19-24](#table-harvestqty19-24)
- [Table: harvestqty23-24](#table-harvestqty23-24)
- [Table: harvestqty25](#table-harvestqty25)
- [Table: packageqty19-24](#table-packageqty19-24)
- [Table: packageqty23-24](#table-packageqty23-24)
- [Table: packageqty25](#table-packageqty25)

### Distribution
- [Table: Distribution_cleaned](#table-distribution_cleaned)
- [Table: Distribution_source](#table-distribution_source)

### Harvest
- [Table: harvest](#table-harvest)

### Package
- [Table: package](#table-package)

### Retail
- [Table: sales18](#table-sales18)
- [Table: sales19](#table-sales19)
- [Table: sales20](#table-sales20)
- [Table: sales21](#table-sales21)
- [Table: sales22](#table-sales22)
- [Table: sales23](#table-sales23)
- [Table: sales23v2](#table-sales23v2)
- [Table: sales24](#table-sales24)
- [Table: sales25](#table-sales25)
- [Table: sales25q2](#table-sales25q2)
- [Table: salesquantity18](#table-salesquantity18)
- [Table: salesquantity19](#table-salesquantity19)
- [Table: salesquantity20](#table-salesquantity20)
- [Table: salesquantity21](#table-salesquantity21)
- [Table: salesquantity22](#table-salesquantity22)
- [Table: salesquantity23](#table-salesquantity23)
- [Table: salesquantity23v2](#table-salesquantity23v2)
- [Table: salesquantity24](#table-salesquantity24)
- [Table: salesquantity25](#table-salesquantity25)
- [Table: salesquantity25q2](#table-salesquantity25q2)

---



## Cultivation





# Table: cultpanelsize

### Overview Section

This dataset provides a comprehensive view of cannabis cultivation licenses, tracking their status and associated canopy sizes over time. It serves as a foundational resource for analyzing trends in the regulated cannabis market, understanding license dynamics, and assessing cultivation capacity. Each row in the `cultpanelsize` table represents a monthly snapshot of a specific cultivation license, detailing its administrative information and canopy size for that particular month. The overall data source is assumed to be regulatory bodies overseeing cannabis cultivation, with data collected over an unspecified period and extracted on an unspecified date.

**Assumptions:**
*   Data primarily pertains to California's regulated cannabis market.
*   `panel_month` represents the beginning of the month for which the data snapshot is valid.
*   `Canopy.Size` is measured in square feet.

### Table Inventory

*   **cultpanelsize:** Contains detailed information about cannabis cultivation licenses, including their status, type, business details, and monthly reported canopy sizes.

## Table: cultpanelsize

*   **Purpose:** To track the status and canopy size of individual cannabis cultivation licenses on a monthly basis, providing a time-series view of license activity and cultivation capacity.
*   **What one row represents:** A monthly record for a specific cultivation license, reflecting its status and reported canopy size for that month.
*   **Primary key(s):** `id` (surrogate key), or a composite key of `(licenseNumber, panel_month)`.
*   **Relationships:**
*   **Number of rows and columns:** 448788 rows, 18 columns.
*   **Column Dictionary**


| Column Name        | Type    | Units       | Description                                                                                      | Allowed Values / Range                   |   Missing % | Cleaning / Notes                                                                                                                                                                                               |
|:-------------------|:--------|:------------|:-------------------------------------------------------------------------------------------------|:-----------------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| licenseNumber      | string  |             | Unique identifier assigned to each cultivation license.                                          |                                          |         0   |                                                                                                                                                                                                                |
| id                 | integer |             | A unique identifier for each record in the table.                                                | 1 to 19543                               |         0   |                                                                                                                                                                                                                |
| licenseStatus      | string  |             | The current administrative status of the license (e.g., 'Active', 'Expired', 'Suspended').       | e.g., 'Expired', 'Active', 'Provisional' |         0   |                                                                                                                                                                                                                |
| licenseTerm        | string  |             | The duration or type of the license term (e.g., 'Annual', 'Provisional').                        | e.g., 'Annual'                           |         0   |                                                                                                                                                                                                                |
| licenseType        | string  |             | The specific category of cultivation license (e.g., 'Medium Outdoor', 'Small Indoor').           | e.g., 'Cultivation - Medium Outdoor'     |         0   |                                                                                                                                                                                                                |
| licenseDesignation | string  |             | The designation of the license, indicating its allowed market (e.g., 'Adult-Use', 'Medicinal').  | e.g., 'Adult-Use'                        |         0   |                                                                                                                                                                                                                |
| issueDate          | date    |             | The date the license was initially issued.                                                       |                                          |         0   | Convert to datetime object for analysis.                                                                                                                                                                       |
| expirationDate     | date    |             | The date the license is set to expire.                                                           |                                          |         0   | Convert to datetime object for analysis.                                                                                                                                                                       |
| businessLegalName  | string  |             | The full legal name of the business holding the license.                                         |                                          |         0   |                                                                                                                                                                                                                |
| businessDbaName    | string  |             | The 'Doing Business As' name of the licensed entity, if different from the legal name.           |                                          |         0   | Contains 'Data Not Available' strings, which should be treated as missing values (NaN).                                                                                                                        |
| businessOwnerName  | string  |             | The name of the primary owner or contact for the business.                                       |                                          |         0   |                                                                                                                                                                                                                |
| businessStructure  | string  |             | The legal organizational structure of the business (e.g., 'Corporation', 'Sole Proprietorship'). | e.g., 'Corporation'                      |         0   |                                                                                                                                                                                                                |
| premiseCounty      | string  |             | The county where the licensed cultivation premise is physically located.                         | e.g., 'Humboldt'                         |         0   |                                                                                                                                                                                                                |
| businessEmail      | string  |             | The primary email address for business contact.                                                  |                                          |         0   | Standardize to lowercase.                                                                                                                                                                                      |
| businessPhone      | string  |             | The primary phone number for business contact.                                                   |                                          |         0   | Standardize phone number format if needed for consistency.                                                                                                                                                     |
| panel_month        | date    |             | The first day of the month to which the panel data corresponds.                                  |                                          |         0   | Convert to datetime object for analysis.                                                                                                                                                                       |
| Active             | binary  |             | Indicator if the license was active during the `panel_month` (1 = Active).                       | 1                                        |         0   | Verify if this column is always 1, suggesting the dataset is pre-filtered for active licenses.                                                                                                                 |
| Canopy.Size        | numeric | square feet | The reported cultivation canopy size for the license during the `panel_month`.                   | 0.0 to 1736868.0                         |         7.4 | Missing values (7.4%) should be investigated. Consider imputation (e.g., median, zero) or exclusion based on analysis goals. Negative values are not expected, but 0 is possible for inactive or new licenses. |


### Data Quality & Anomalies Section

*   **Issue:** `businessDbaName` contains explicit "Data Not Available" strings.
    *   **Likely cause:** Information was not provided or recorded for these businesses.
    *   **Recommended handling rule:** Convert "Data Not Available" strings to standard null values (NaN) for consistent missing data handling.
*   **Issue:** `Canopy.Size` has 7.4% missing values.
    *   **Likely cause:** Data was not reported, was not applicable (e.g., license was inactive for that month, or new license without reported canopy), or was lost during data collection/extraction.
    *   **Recommended handling rule:** For analyses requiring `Canopy.Size`, consider imputing missing values with a suitable metric (e.g., median canopy size for similar license types/counties) or excluding rows with missing values if the impact on sample size is acceptable. A flag column could also be added to indicate imputed values.
*   **Issue:** The `Active` column consistently shows a value of `1`.
    *   **Likely cause:** The dataset may have been pre-filtered to only include records for licenses that were active during their respective `panel_month`.
    *   **Recommended handling rule:** Verify this assumption with the data provider. If confirmed, this column provides no additional variance for analysis within this dataset and can be noted as such. If not confirmed, investigate if there are any records where `Active` should be `0`.

### Reproducible Cleaning Plan

1.  **Standardize Missing Values:** Convert all instances of "Data Not Available" in the `businessDbaName` column to `NaN` to ensure consistent handling of missing data.
2.  **Convert Data Types:** Transform `issueDate`, `expirationDate`, and `panel_month` columns from `object` to `datetime` objects to enable time-series analysis and proper date comparisons.
3.  **Handle Missing Canopy Sizes:** Address the 7.4% missing values in `Canopy.Size`. Depending on the analytical objective, either impute these values (e.g., using the median `Canopy.Size` for the respective `licenseType` and `premiseCounty`) or filter out rows where `Canopy.Size` is `NaN`.
4.  **Standardize Text Fields:** Convert `businessEmail` to lowercase to ensure consistency and facilitate accurate matching or grouping.
5.  **Verify 'Active' Column:** Confirm with data source whether the `Active` column is always `1` by design (pre-filtered data) or if there are expected `0` values that are missing.

### Limitations & Trust Section

*   **Incomplete Business DBA Names:** The `businessDbaName` column frequently contains "Data Not Available" entries, limiting the ability to identify businesses by their common operating names. Validation would require cross-referencing with external business registries or direct contact with licensees.
*   **Missing Canopy Size Data:** The 7.4% missing values in `Canopy.Size` could introduce bias if not handled appropriately. The reliability of analyses relying on complete canopy size data is reduced without a clear understanding of why these values are missing and a robust imputation strategy. Validation would involve understanding the data collection process for canopy sizes and potentially comparing with historical reports.
*   **'Active' Column Ambiguity:** The `Active` column consistently being `1` suggests a pre-filtered dataset. If the intention was to capture both active and inactive licenses, this limitation means the dataset might not fully represent the universe of licenses over time. Validation requires clarification from the data source regarding the filtering criteria applied during extraction.

### Appendix: Quick Reference

*   **Missing DBA Names:** "Data Not Available" in `businessDbaName` converted to `NaN`.
*   **Date Conversions:** `issueDate`, `expirationDate`, `panel_month` converted to `datetime`.
*   **Canopy Size Imputation/Exclusion:** 7.4% missing `Canopy.Size` values are either imputed (e.g., median) or rows excluded.
*   **Email Standardization:** `businessEmail` converted to lowercase.
*   **'Active' Column:** Assumed pre-filtered to active licenses; verify with source.
*   **Primary Key:** `(licenseNumber, panel_month)` is a strong candidate for a composite primary key.

### Notes for Reviewers

Reviewers should verify the accuracy of column descriptions, especially for `licenseType` and `licenseDesignation`, to ensure they align with regulatory definitions. Particular attention should be paid to the proposed handling of missing `Canopy.Size` values and the interpretation of the `Active` column, as these have significant implications for data analysis. Additionally, confirm that the assumed units for `Canopy.Size` (square feet) are correct. Any discrepancies or additional known data quality issues should be highlighted for inclusion.

# Work Documentation

## Table: cultpanelsize

**Data Operations:**
The `cultpanelsize` table, represented by `cultivation_df` in the provided Python scripts, is loaded from an Excel file (`Working Cultivation Canopy June 2025.xlsx`). Initial processing involves filtering records to include only "Active" licenses and excluding records with non-missing values in a `LargeDate` column, which likely indicates superseded or invalid entries. The `licenseType` column is then categorized into broader `Indoor`, `Mixed_Light`, and `Outdoor` types. Additionally, binary flag columns (`micro_cult`, `micro_indoor`) are created based on the `activity` column to identify specific microbusiness characteristics. Microbusiness licenses that are not cultivators are filtered out, and the `type` categorization for remaining microbusinesses is refined based on their indoor/outdoor activity. Finally, the processed cultivation data is merged with a `parent_df` (containing license-to-parent company mappings) using `licenseNumber` as the key, and the resulting combined dataset is saved as `cultivation.dta`.

**Variables Affected:**
`licenseStatus`, `LargeDate`, `licenseType`, `activity`, `licenseNumber`. New variables created include `type` (categorized license type), `micro_cult` (binary flag for microbusiness cultivator), and `micro_indoor` (binary flag for microbusiness indoor activity). The dataset is also enriched with `primary_company` from the `parent_df` during the merge.

**Logic and Methodology:**
The primary intent is to prepare a clean and categorized dataset of active cultivation licenses, enriched with parent company information, for subsequent market concentration analysis.
1.  **Filtering:** Ensures that only currently relevant and active licenses are considered, removing potentially outdated or invalid entries.
2.  **Categorization of `licenseType`:** Simplifies the detailed `licenseType` values into three broad categories (`Indoor`, `Mixed_Light`, `Outdoor`) to facilitate aggregated analysis.
3.  **Microbusiness Specific Handling:** Recognizes the unique structure of "Microbusiness" licenses and uses the `activity` field to accurately classify their cultivation type, ensuring correct categorization for market analysis.
4.  **Data Type Standardization:** `licenseNumber` is explicitly converted to string type in both `cultivation_df` and `parent_df` to ensure successful merging.
5.  **Data Enrichment:** Merging with `parent_df` integrates parent company identifiers, allowing for market concentration analysis at the corporate level.

**Validation and Verification:**
The filtering of `licenseStatus == "Active"` aligns with the Codebook's note regarding the `Active` column, suggesting a pre-filtered dataset. The `validate="many_to_one"` argument in the merge operation ensures that each cultivation license record matches at most one parent company record, preventing unintended data duplication during the join. It is noted that the Python code does not explicitly implement the Codebook's recommended handling for `Canopy.Size` missing values (7.4%) or the conversion of `panel_month` to datetime objects during this initial processing phase. These aspects would require further verification or explicit implementation to align fully with the documented cleaning plan.

**Results and Outcomes:**
A new, processed dataset, `merged_df`, is generated and saved as `Data/Working_data/cultivation.dta`. This dataset contains active cultivation license information, including categorized license types, microbusiness flags, and associated parent company identifiers. This `cultivation.dta` file serves as the foundational input for all subsequent cultivation-related Herfindahl-Hirschman Index (HHI) calculations and visualizations, providing a refined view of the cultivation market structure.

## Other Data Processing Pipelines

This section documents significant data cleaning, transformation, and analysis pipelines identified in the provided Python code that pertain to datasets not explicitly detailed in the initial Codebook. These pipelines contribute to the overall project's data work and generate key analytical outputs.

### Data Pipeline: License Parent Company Information (`parent_df`)

**Data Operations:**
This pipeline processes a dataset containing license and company information, loaded from two different CSV files (`Cannabis Market Intelligence Platform Report - Licenses - 2025-07-03.csv` and `Cannabis Market Intelligence Platform Report - Licenses - 2025-02-21.csv`). Key columns are renamed for consistency. New columns are derived to identify multi-owner companies and extract a primary company identifier. The `primary_company` column is converted to a numeric type. Duplicate records are removed, and entries with missing or empty `licenseNumber` values are excluded to ensure data integrity.

**Variables Affected:**
Original columns like "Company ID", "Country", and "State License ID" are renamed to `companyid`, `county`, and `statelicenseid` (later `licenseNumber`), respectively. New variables created include `multi_owner` (a binary flag indicating multiple owners) and `primary_company` (the extracted primary company identifier).

**Logic and Methodology:**
The primary goal is to create a clean and standardized mapping between individual licenses and their primary parent companies.
1.  **Column Renaming:** Standardizes column names for easier programmatic access and consistency across datasets.
2.  **Multi-Owner Identification:** The presence of a semicolon in the `companyid` is used as a heuristic to identify licenses potentially associated with multiple owners.
3.  **Primary Company Extraction:** For multi-owner entries, the first part of the `companyid` (before the semicolon) is extracted as the `primary_company`; otherwise, the entire `companyid` is used. This aims to consolidate ownership for market analysis.
4.  **Data Type Conversion:** `primary_company` is converted to numeric, with non-numeric values coerced to `NaN`, to prepare for potential numerical analysis or consistent handling of missing identifiers.
5.  **Deduplication and Validation:** Duplicate rows are removed, and records lacking a valid `licenseNumber` are dropped, ensuring a unique and reliable set of license-to-company mappings.

**Validation and Verification:**
The use of `errors='coerce'` during numeric conversion for `primary_company` allows the process to continue even if some company IDs are not purely numeric, gracefully handling data inconsistencies. The explicit removal of duplicates and records with missing `licenseNumber` ensures the integrity of the license identifiers, which are critical for merging with other datasets.

**Results and Outcomes:**
A cleaned and refined `parent_df` is produced, containing unique license numbers, their associated primary company identifiers, and county information. This dataset serves as a crucial lookup table for enriching both cultivation and retail sales data with parent company details, enabling market concentration analysis at the corporate level.

### Data Pipeline: Harvest Quantity Data (`harvest_df`)

**Data Operations:**
This pipeline consolidates harvest quantity data from multiple yearly CSV files into a single DataFrame. Columns are systematically renamed to a consistent format. Key numeric columns (`year`, `totalharvestpounds`, `totalharvestwetpounds`) are converted to their appropriate data types, with errors handled by coercion. The `harvestercounty` column undergoes extensive cleaning and standardization, including replacing specific "NA" and "UNDEFINED" strings, mapping various county name formats to a standardized uppercase version, removing "County" suffixes, and dropping records where the county information remains missing.

**Variables Affected:**
Original columns such as "HarvesterLicenseNumber", "PkgYear", "TotalHarvestPounds", etc., are renamed to `harvesterlicensenumber`, `year`, `totalharvestpounds`, and so on. `year`, `totalharvestpounds`, and `totalharvestwetpounds` are converted to numeric. The `harvestercounty` column is significantly transformed and standardized.

**Logic and Methodology:**
The objective is to create a unified, clean, and standardized dataset of harvest quantities suitable for analysis and merging.
1.  **Data Consolidation:** Combining multiple yearly files ensures a comprehensive time-series view of harvest data.
2.  **Column Standardization:** Renaming columns to snake_case improves readability and programmatic consistency.
3.  **Data Type Conversion:** Ensures that numerical fields are treated as numbers, enabling accurate calculations. Error coercion prevents script failure due to malformed entries.
4.  **County Normalization:** The multi-step cleaning of `harvestercounty` is critical for accurate geographical analysis, addressing inconsistencies in how county names are recorded across different source files or entries. This includes explicit string replacement, a mapping dictionary, and removal of common suffixes.
5.  **Missing Data Handling:** Dropping rows with missing `harvestercounty` ensures that all remaining records have valid geographical context.

**Validation and Verification:**
The `dtype=str` during initial CSV loading, followed by explicit numeric conversion with `errors='coerce'`, provides robust handling for potentially mixed data types in source files. The comprehensive county cleaning steps are designed to maximize data quality for geographical aggregation.

**Results and Outcomes:**
A single, cleaned, and standardized `harvest_df` is generated and saved as `Data/Track and Trace Data/Harvest/harvest.csv`. This dataset is ready for merging with package data and subsequent analysis of harvest trends and ratios.

### Data Pipeline: Package Quantity Data (`package_df`)

**Data Operations:**
Similar to the harvest data pipeline, this process involves concatenating multiple yearly CSV files containing package quantity data. Columns are renamed to a consistent snake_case format. Numeric columns (`year`, `totalpackagepounds`) are converted to their appropriate data types, with errors coerced to `NaN`. The `harvestercounty` column undergoes cleaning and standardization using a predefined county mapping, whitespace stripping, and replacement of empty strings with `pd.NA`, followed by dropping rows with missing county information.

**Variables Affected:**
Original columns like "HarvesterLicenseNumber", "Year", "TotalPackagePounds", etc., are renamed to `harvesterlicensenumber`, `year`, `totalpackagepounds`, and so on. `year` and `totalpackagepounds` are converted to numeric. The `harvestercounty` column is transformed and standardized.

**Logic and Methodology:**
The aim is to produce a unified, clean, and standardized dataset of package quantities for analysis and merging.
1.  **Data Consolidation:** Merging data from various yearly files creates a complete package data record.
2.  **Column Standardization:** Consistent column naming facilitates data manipulation.
3.  **Data Type Conversion:** Ensures numerical fields are correctly interpreted, with error handling for robustness.
4.  **County Normalization:** The cleaning of `harvestercounty` ensures geographical consistency, which is vital for accurate county-level analysis when combined with harvest data.
5.  **Missing Data Handling:** Dropping records with missing `harvestercounty` maintains data quality for geographical aggregations.

**Validation and Verification:**
The use of `dtype=str` during loading and subsequent `pd.to_numeric` with `errors='coerce'` ensures resilience against data type inconsistencies. The county standardization steps are crucial for reliable geographical analysis.

**Results and Outcomes:**
A single, cleaned, and standardized `package_df` is generated and saved as `Data/Track and Trace Data/Package/package.csv`. This dataset is prepared for merging with the `harvest_df` to create a combined view of cultivation output.

### Data Pipeline: Combined Harvest and Package Data (`merged` and Aggregations)

**Data Operations:**
The cleaned `package_df` and `harvest_df` are merged based on `harvesterlicensenumber` and `year`. The `harvestercounty` column is consolidated from the two merged sources. New ratio metrics are calculated: `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`. Further cleaning of `harvestercounty` is performed to replace various missing value representations with `pd.NA`, and rows with missing counties are dropped. The combined data is then aggregated at two levels: `category_summary` (by county, year, and item category) and `county_summary` (by county and year), calculating sums of pounds and mean ratios.

**Variables Affected:**
All columns from `package_df` and `harvest_df` are present. New variables include `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`. The `harvestercounty` column is consolidated and cleaned. Aggregated results include `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` at summary levels.

**Logic and Methodology:**
This pipeline aims to integrate harvest and package data to derive key performance indicators and aggregated summaries.
1.  **Data Integration:** Merging the two datasets provides a holistic view of cultivation output from harvest to packaging. A left merge ensures all package records are retained.
2.  **County Consolidation:** A logical rule is applied to ensure the `harvestercounty` is as complete as possible, prioritizing harvest data if available.
3.  **Ratio Calculation:** Deriving ratios like `package_to_harvest_ratio` and `dry_to_wet_ratio` provides insights into processing efficiency and product yield.
4.  **Missing Data Refinement:** Additional cleaning of `harvestercounty` after merging addresses any remaining inconsistencies or missing values.
5.  **Aggregation:** Summarizing data by county, year, and item category provides high-level overviews for trend analysis and reporting.

**Validation and Verification:**
The merge operation uses a `left` join to ensure all package records are considered. The consolidation logic for `harvestercounty` is designed to fill gaps effectively. The aggregation steps use standard `sum` and `mean` functions to produce summary statistics.

**Results and Outcomes:**
A combined dataset (`merged`) is created, which is then used to generate `category_summary` and `county_summary` tables. The `county_summary` table, containing aggregated harvest and package pounds and the `package_to_harvest_ratio` by county and year, is exported to `Data/Results/harvest_package_ratios.xlsx`. This output serves as a basis for visualizing harvest and package trends and efficiencies.

### Data Pipeline: Retail Sales Data (`sales_df` and `df`)

**Data Operations:**
This pipeline processes retail sales data by concatenating multiple yearly CSV files. Irrelevant columns are dropped, and remaining columns are renamed for consistency. The combined sales data is then merged with a subset of the `parent_df` (containing license-to-parent company mappings and Cannabiz county information). The `retailercounty` column undergoes a multi-stage cleaning and imputation process, leveraging Cannabiz data, manual fixes, and ZIP code-to-county mappings from a HUD dataset (`ZIP_COUNTY_122024.xlsx`). Temporary merge indicator columns are removed, and all columns are converted to string type, with empty strings replaced by `pd.NA` for consistent missing value handling.

**Variables Affected:**
Original sales columns like "RetailerLicenseNumber", "Date", "ItemCategory", "totalsales" are renamed and standardized. New variables include `primary_company` and `cannabiz_county` (from `parent_df`), and `zip5` (derived from `retailerzipcode`). The `retailercounty` column is extensively modified and imputed.

**Logic and Methodology:**
The primary objective is to create a comprehensive and geographically accurate retail sales dataset, linked to parent companies, for market analysis.
1.  **Data Consolidation:** Combining sales data from multiple years provides a complete historical view.
2.  **Column Standardization:** Renaming columns ensures consistency and ease of use.
3.  **Parent Company Linkage:** Merging with `parent_df` links individual sales records to their respective parent companies, enabling corporate-level market analysis.
4.  **Multi-Stage County Imputation:** This is a critical and complex step designed to maximize the completeness and accuracy of `retailercounty`. It involves:
    *   Using `cannabiz_county` to fill missing `retailercounty` values.
    *   Applying specific manual corrections for known license-county discrepancies.
    *   Deriving `retailercounty` from a `license_county` lookup table.
    *   Extracting `zip5` from `retailerzipcode` and merging with a HUD ZIP-to-county mapping to impute further missing county values.
    *   Applying additional manual fixes for specific licenses.
5.  **Data Type Consistency:** Converting all columns to string and standardizing missing value representations ensures uniformity for downstream processing.

**Validation and Verification:**
The multi-stage imputation strategy for `retailercounty` demonstrates a robust effort to address data quality issues by cross-referencing multiple reliable sources. The use of merge indicators (`_merge`, `_merge_lic_county`, `_merge_zip`) internally tracks the success of each imputation step, providing a level of auditability for the county assignment process.

**Results and Outcomes:**
A highly cleaned, enriched, and geographically standardized `df` dataset is produced, containing retail sales data linked to parent companies and accurate county information. This dataset is saved as `Data/Working_data/sales_w_parent_co_test.dta` and serves as the primary input for all subsequent sales-related HHI calculations and visualizations.

### Data Pipeline: Herfindahl-Hirschman Index (HHI) Calculations and Visualizations (Cultivation & Sales)

**Data Operations:**
This comprehensive pipeline performs Herfindahl-Hirschman Index (HHI) calculations for both cultivation and retail sales data, followed by extensive visualization and trend analysis.

For **Cultivation HHI**: The `cultivation.dta` dataset is loaded. HHI is calculated for `Canopy` and `MaxSqFt` metrics. These calculations are performed at both statewide and county levels, and for two aggregation levels: overall (individual businesses) and parent company level. This process is repeated for each `grow_type` (Indoor, Mixed_Light, Outdoor). Market shares are computed, squared, and summed to derive HHI. The results are then combined and exported to various Excel and CSV files.

For **Sales HHI**: The `sales_w_parent_co_test.dta` dataset is loaded. `totalsales` and `year` columns are converted to numeric. HHI is calculated for `totalsales` at statewide and county levels, and for overall and parent company levels, for each year. The results are merged and enriched with total sales and opacity metrics. The sales HHI data is then used for:
1.  **Clustering:** K-Means clustering is applied to county-level HHI trends (2019-2025) to group counties with similar HHI trajectories.
2.  **Trend Analysis:** Linear regression is used to determine the slope of HHI change over time for each county, categorizing them into "increasing," "decreasing," or "stable" market concentration groups.
3.  **Year-over-Year Change:** Percentage change in HHI is calculated for each county annually.
4.  **Correlation Analysis:** A correlation matrix is generated for HHI, total sales, and county sales.

**Visualization**: Numerous plots are generated using Matplotlib, Seaborn, and Plotly to illustrate:
*   HHI trends over time for cultivation and sales (overall and parent company level).
*   Market concentration by county and grow type (cultivation).
*   Sales trends over time by top cities (retail).
*   Relationships between `Canopy` and `MaxSqFt` (cultivation).
*   Distribution of HHI values by year and county (sales).
*   Year-over-year HHI percentage changes by county (sales).
*   County clusters based on HHI trends (sales).
*   Counties categorized by increasing, decreasing, or stable HHI trends (sales).

**Variables Affected:**
*   **Cultivation HHI:** `Canopy`, `MaxSqFt`, `businessLegalName`, `primary_company`, `premiseCounty`, `grow_type`, `mkt_share_Canopy`, `mkt_share2_Canopy`, `mkt_share_MaxSqFt`, `mkt_share2_MaxSqFt`, `HHI_Canopy`, `Total_Canopy`, `HHI_MaxSqFt`, `Total_MaxSqFt`.
*   **Sales HHI:** `totalsales`, `retailerlicensenumber`, `primary_company`, `retailercounty`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `HHI`, `HHI_parent_level`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`. New variables include `cluster` (from K-Means) and `hhi_change` (percentage change).
*   **Harvest/Package:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (used for visualization).
*   **Sales by City:** `totalsales`, `retailercity`, `date` (used for visualization).

**Logic and Methodology:**
The core methodology revolves around calculating the Herfindahl-Hirschman Index (HHI), a standard economic measure of market concentration.
1.  **Market Share Calculation:** For each defined market (statewide/county, overall/parent company, grow type/year), the market share of each entity (business or parent company) is calculated based on relevant metrics (Canopy, MaxSqFt, Total Sales).
2.  **HHI Derivation:** Market shares are squared and summed to obtain the HHI, providing a quantitative measure of market concentration.
3.  **Parent Company Aggregation:** Aggregating data by `primary_company` allows for an assessment of market power at the corporate level, which may differ significantly from individual license-level concentration.
4.  **Trend and Pattern Analysis:** Linear regression and K-Means clustering are applied to identify and categorize temporal trends and structural patterns in market concentration across different counties.
5.  **Data Export:** Intermediate and final HHI results are systematically exported to various file formats (Excel, CSV) to facilitate further analysis, reporting, and sharing.
6.  **Comprehensive Visualization:** A wide array of plots is generated to visually communicate complex market dynamics, trends, and distributions, making the insights accessible to a broader audience.

**Validation and Verification:**
The HHI calculations adhere to established economic principles for measuring market concentration. The use of `groupby` and `transform` functions ensures that market shares and HHI are correctly computed within their respective market definitions. Data type conversions with `errors='coerce'` enhance the robustness of the calculations against data inconsistencies. The generation of multiple visualizations provides a crucial means for visual inspection and validation of the calculated metrics and identified trends. Clustering and regression models are applied with standard parameters, and their outputs are visualized to allow for interpretation and verification of the identified patterns.

**Results and Outcomes:**
This pipeline generates a rich set of analytical outputs, including:
*   **Cultivation HHI Reports:** Excel files (`Cult_HHI__Indoor_test.xlsx`, `Cult_HHI__Mixed_Light_test.xlsx`, `Cult_HHI__Outdoor_test.xlsx`, `Cult_HHI_DeepDive.xlsx`) and CSV summaries (`Cult_HHI_Summary.csv`, `Cult_Size_vs_HHI.csv`) detailing HHI values for canopy and maximum square footage across different grow types, geographies, and company levels.
*   **Sales HHI Reports:** An Excel file (`HHI_by_county_test.xlsx`) and CSV files (`hhi_by_county.csv`, `hhi_by_county_parent.csv`) providing HHI values for total sales by county, year, and company level.
*   **Visualizations:** Numerous plots (displayed and saved as HTML files for interactive Plotly charts) illustrating:
    *   Temporal trends of HHI in both cultivation and retail markets.
    *   Geographical variations in market concentration.
    *   Sales performance by top cities.
    *   Relationships between different cultivation metrics.
    *   Categorization of counties based on HHI trends and clusters.
    *   Correlation between HHI and sales volumes.
These outputs collectively provide a comprehensive and granular understanding of market structure, competition, and dynamics within the regulated cannabis industry.






# Table: harvestpackagemerge19-24

### Overview Section

This dataset provides aggregated information related to cannabis harvest and packaging activities within the Track & Trace system, covering the period from 2019 to 2024. It aims to offer insights into the flow of cannabis products from cultivation to initial packaging, including quantities harvested and packaged, and associated harvester details. Each row in the `harvestpackagemerge19-24` table represents a unique aggregation of harvest and package data, likely at a specific harvester and item category level for a given year. The overall data source is the Track & Trace system, with data collected between 2019 and 2024. The exact extraction date is not available.

**Assumptions:**
*   The collection period (2019-2024) is inferred from the table name `harvestpackagemerge19-24`.
*   Units for weight-related columns are assumed to be pounds based on common industry practice and typical data ranges.

### Table Inventory

*   **`harvestpackagemerge19-24`**: This table consolidates data on cannabis harvests and their subsequent packaging, providing details on quantities, harvester information, and package characteristics over several years.

## Table: harvestpackagemerge19-24

*   **Purpose:** To provide a consolidated view of cannabis harvest and packaging metrics, linking harvest quantities to packaged outputs and harvester details.
*   **What one row represents:** An aggregated record of harvest and package data, likely unique by harvester, item category, and year.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 43827 rows, 14 columns

### Column Dictionary


| Column Name            | Type    | Units   | Description                                                                                | Allowed Values / Range                     |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                 |
|:-----------------------|:--------|:--------|:-------------------------------------------------------------------------------------------|:-------------------------------------------|------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique license number of the cannabis harvester facility.                                  |                                            |         0   |                                                                                                                                                                                                                                                                                                                  |
| HarvesterFacilityType  | object  |         | Type of license held by the harvester facility (e.g., Microbusiness, Cultivation).         |                                            |         0   |                                                                                                                                                                                                                                                                                                                  |
| HarvesterCity          | object  |         | City where the harvester facility is located.                                              |                                            |         0.2 | Missing values observed. Consider imputation with 'Unknown' or the most frequent city, or exclusion if geographic analysis is critical.                                                                                                                                                                          |
| HarvesterZipCode       | float64 |         | Zip code of the harvester facility.                                                        | [4000.0, 961503674.0]                      |         7.7 | Missing values observed. The upper range value (961503674.0) is an invalid zip code format, indicating data entry errors or corruption. Values outside typical 5-digit or 9-digit zip code formats should be flagged or corrected. Consider imputation for missing values or exclusion if accuracy is paramount. |
| HarvesterCounty        | object  |         | County where the harvester facility is located.                                            |                                            |         1.7 | Missing values observed. Consider imputation with 'Unknown' or the most frequent county, or exclusion if geographic analysis is critical.                                                                                                                                                                        |
| PkgYear                | int64   | Year    | Year in which the package was recorded.                                                    | [2019.0, 2024.0]                           |         0   |                                                                                                                                                                                                                                                                                                                  |
| ItemCategory           | object  |         | Category of the packaged item (e.g., Fresh Cannabis Plant, Flower).                        |                                            |         0   |                                                                                                                                                                                                                                                                                                                  |
| TotalPackagePounds     | float64 | Pounds  | Total weight of the packaged cannabis in pounds.                                           | [2.20462442018378e-07, 911433262.960458]   |         0   |                                                                                                                                                                                                                                                                                                                  |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches contributing to the package.                              | [1.0, 8875.0]                              |         0   |                                                                                                                                                                                                                                                                                                                  |
| TotalHarvestPounds     | float64 | Pounds  | Total weight of the harvested cannabis in pounds.                                          | [-358.596995537842, 911433642.960996]      |         0   | Anomaly: Negative values observed. These are physically impossible for weight. Flag these records for investigation or set to 0, or exclude them from calculations.                                                                                                                                              |
| TotalHarvestWetPounds  | float64 | Pounds  | Total wet weight of the harvested cannabis in pounds.                                      | [0.0002204624420183, 1371869133.03903]     |         0   |                                                                                                                                                                                                                                                                                                                  |
| dryshare               | float64 | Ratio   | Ratio representing the dry weight share, potentially derived from harvest or package data. | [-0.0036930091039523, 138.765601461074]    |         0   | Anomaly: Negative values observed. Ratios should not be negative. Values greater than 1 (or 100% if interpreted as percentage) may also indicate errors depending on the exact definition. Flag negative values for investigation or set to 0. Investigate values > 1.                                           |
| pkgsharedry            | float64 | Ratio   | Ratio representing the dry package share, potentially derived from package data.           | [-58.904455132272, 5.95397130872442]       |         0   | Anomaly: Negative values observed. Ratios should not be negative. Values greater than 1 (or 100% if interpreted as percentage) may also indicate errors depending on the exact definition. Flag negative values for investigation or set to 0. Investigate values > 1.                                           |
| pkgsharewet            | float64 | Ratio   | Ratio representing the wet package share, potentially derived from package data.           | [3.7789324515824295e-11, 138.760593084537] |         0   | Values greater than 1 (or 100% if interpreted as percentage) may indicate errors depending on the exact definition. Investigate values > 1.                                                                                                                                                                      |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestpackagemerge19-24` table.

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry error, calculation artifact, or incorrect data transformation. Physically, weight cannot be negative.
    *   **Recommended handling rule:** Flag these records for further investigation. For analytical purposes, consider setting negative values to 0 or excluding them from aggregate calculations, depending on the impact and business context.

*   **Issue:** Negative values in `dryshare` and `pkgsharedry`.
    *   **Likely cause:** Calculation errors, incorrect formula application, or data entry mistakes. Ratios, by definition, should be non-negative.
    *   **Recommended handling rule:** Flag these records. For analysis, set negative values to 0. Further investigation into the calculation logic for these fields is recommended.

*   **Issue:** `dryshare`, `pkgsharedry`, and `pkgsharewet` contain values greater than 1 (or 100%).
    *   **Likely cause:** If these fields represent proportions or percentages, values exceeding 1 (or 100%) indicate calculation errors or misinterpretation of the metric.
    *   **Recommended handling rule:** Flag these records for review. If they are indeed proportions, cap values at 1 or treat them as outliers. Clarification on the exact definition of these "share" metrics is needed.

*   **Issue:** Invalid `HarvesterZipCode` values, specifically the upper range `961503674.0`.
    *   **Likely cause:** Data entry error, concatenation of multiple numbers, or incorrect data type conversion during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Flag zip codes that do not conform to standard 5-digit or 9-digit formats. Consider cleaning these by truncating or setting to null if uncorrectable, or using a lookup table for validation.

*   **Issue:** Missing values in `HarvesterCity` (0.2%), `HarvesterZipCode` (7.7%), and `HarvesterCounty` (1.7%).
    *   **Likely cause:** Incomplete data entry or data not available at the time of record creation.
    *   **Recommended handling rule:** For `HarvesterCity` and `HarvesterCounty`, impute with 'Unknown' or the most frequent value if geographic precision is not critical. For `HarvesterZipCode`, consider imputation with a default value (e.g., 00000) or 'Unknown' after addressing invalid formats, or exclude records if precise location data is essential.

### Reproducible Cleaning Plan

1.  **Address Invalid `HarvesterZipCode` Formats:** Identify and flag `HarvesterZipCode` values that are not valid 5-digit or 9-digit US zip codes. For analytical purposes, these can be set to `NaN` or a placeholder like 'INVALID' to prevent erroneous geographic analysis.
2.  **Handle Negative Weight Values:** For `TotalHarvestPounds`, identify all records where the value is negative. Flag these records for review and set the `TotalHarvestPounds` to 0 for downstream analysis, as negative weight is physically impossible.
3.  **Correct Negative Ratio Values:** For `dryshare` and `pkgsharedry`, identify all records where the value is negative. Flag these records and set the values to 0, as ratios should not be negative.
4.  **Review Out-of-Range Ratio Values:** For `dryshare`, `pkgsharedry`, and `pkgsharewet`, identify values greater than 1. Flag these records for further investigation into their calculation and definition. Depending on the outcome, these might be capped at 1 or treated as outliers.
5.  **Impute Missing Geographic Data:** For `HarvesterCity` and `HarvesterCounty`, impute missing values with 'Unknown' to ensure completeness for categorical analysis. For `HarvesterZipCode`, after addressing invalid formats, impute remaining missing values with a placeholder like '00000' or 'UNKNOWN' if a numeric type is required, or 'Unknown' if treated as categorical.

### Limitations & Trust Section

The reliability of this dataset is impacted by several factors:

*   **Missing Primary Keys and Relationships:** The absence of explicitly defined primary keys and relationships makes it challenging to ensure data uniqueness and integrity, and to confidently join this table with other datasets. Validation requires domain expertise to identify natural keys.
*   **Inferred Column Descriptions and Units:** Many column descriptions and units (e.g., 'Pounds' for weight, 'Ratio' for shares) have been inferred based on column names and typical data ranges. These inferences require validation by data owners or subject matter experts to ensure accuracy.
*   **Data Quality Issues:** The presence of negative values for physical quantities (`TotalHarvestPounds`) and ratios (`dryshare`, `pkgsharedry`), along with invalid zip codes, indicates potential data entry errors, calculation flaws, or issues during data extraction. These anomalies reduce the immediate trustworthiness of affected metrics.
*   **Ambiguous Ratio Definitions:** The exact definitions and expected ranges for `dryshare`, `pkgsharedry`, and `pkgsharewet` are not fully clear, especially given values exceeding 1. This ambiguity limits the confidence in interpreting these metrics without further clarification.

To validate and improve trust in this dataset, the following are needed:
*   Confirmation of primary keys and foreign key relationships from the source system.
*   Official data dictionary or schema documentation to verify column descriptions, units, and allowed value ranges.
*   Investigation into the root causes of negative values and invalid zip codes to prevent recurrence.
*   Clear definitions for all ratio-based metrics and their expected value ranges.

### Appendix: Quick Reference

*   **Negative Weights:** `TotalHarvestPounds` negative values are invalid; set to 0 or exclude.
*   **Negative Ratios:** `dryshare`, `pkgsharedry` negative values are invalid; set to 0.
*   **Out-of-Range Ratios:** `dryshare`, `pkgsharedry`, `pkgsharewet` values > 1 require investigation; potentially cap at 1.
*   **Invalid Zip Codes:** `HarvesterZipCode` values not conforming to 5 or 9 digits should be flagged or corrected.
*   **Missing Geographic Data:** Impute `HarvesterCity`, `HarvesterCounty` with 'Unknown'; `HarvesterZipCode` with '00000' or 'UNKNOWN'.
*   **Data Source:** Track & Trace system.
*   **Collection Period:** 2019-2024 (inferred).

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions, units, and the proposed handling rules for anomalies. Particular attention should be paid to the interpretation of ratio-based fields (`dryshare`, `pkgsharedry`, `pkgsharewet`) and the implications of the identified data quality issues on potential analyses. Confirmation of primary keys and relationships, if known, would greatly enhance the utility and trustworthiness of this codebook.

# Work Documentation

## Table: harvestpackagemerge19-24

**Data Operations:**
The `harvestpackagemerge19-24` table, as described in the Codebook, is conceptually created and processed through a series of operations on raw harvest and package data files.

1.  **Source Data Loading:** Individual CSV files containing harvest quantity data (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) and package quantity data (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were loaded into separate DataFrames.
2.  **Concatenation:** The multiple harvest files were concatenated into a single `harvest_df`, and similarly, the package files were combined into a `package_df`. These combined DataFrames were then saved to intermediate CSV files (`Data/Track and Trace Data/Harvest/harvest.csv` and `Data/Track and Trace Data/Package/package.csv`) and reloaded.
3.  **Column Renaming:** Columns in both `harvest_df` and `package_df` were renamed to a consistent, lowercase snake_case format (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`).
4.  **Data Type Conversion:** Key columns such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted from string to numeric data types. Any values that could not be converted were coerced into `NaN` (Not a Number).
5.  **Geographic Data Cleaning and Normalization:**
    *   The `harvestercounty` column in both `harvest_df` and `package_df` underwent extensive cleaning. Initial string values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined mapping was applied to standardize various representations of county names (e.g., "Alameda County" was mapped to "ALAMEDA").
    *   Whitespace was stripped from `harvestercounty` values, and the suffix " County" was removed.
    *   Empty strings, pandas' `<NA>` indicator, and "nan" string representations were converted to actual missing values (`pd.NA`).
    *   Rows with missing `harvestercounty` values were dropped at multiple stages of this cleaning process.
6.  **Merging:** The cleaned `package_df` and `harvest_df` were merged into a `merged` DataFrame, which represents the `harvestpackagemerge19-24` table. The merge was performed as a left join on `harvesterlicensenumber` and `year`. Overlapping column names were suffixed with `_pkg` and `_harv`.
7.  **Column Resolution Post-Merge:** A unified `harvestercounty` column was created in the `merged` DataFrame. It preferentially used the county information from the harvest data (`harvestercounty_harv`) and fell back to the package data (`harvestercounty_pkg`) if the harvest data was missing. Further cleaning steps for `harvestercounty` (stripping whitespace, replacing empty strings/NA/nan with `pd.NA`, and dropping missing values) were applied to the `merged` DataFrame.
8.  **Feature Engineering:** New ratio-based metrics were calculated:
    *   `package_to_harvest_ratio` was computed as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio` was computed as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share` was also computed as `totalpackagepounds` divided by `totalharvestpounds`, appearing to be a duplicate of `package_to_harvest_ratio`.
9.  **Aggregation:**
    *   A `category_summary` DataFrame was created by grouping the `merged` data by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, `package_to_harvest_ratio` was averaged, and `totalharvestpounds` was taken as the first value.
    *   A `county_summary` DataFrame was created by grouping the `merged` data by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, `totalharvestpounds` was taken as the first value, and a new `package_to_harvest_ratio` was calculated at this aggregated level.
10. **Export and Visualization:** The `county_summary` DataFrame was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Subsequently, the data was used to generate various bar charts visualizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for the top 10 counties across different years.

**Variables Affected:**

*   **Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `PkgYear`, `Year`, `TotalHarvestPounds`, `TotalHarvestWetPounds`, `UniqueHarvestBatches`, `ItemCategory`, `TotalPackagePounds`.
*   **Data Type Changed:** `year`, `totalharvestpounds`, `totalharvestwetpounds`, `totalpackagepounds` were converted from string to numeric types. `HarvesterZipCode` remained as a string type in the processed data.
*   **Cleaned/Normalized:** `harvestercounty` was extensively cleaned and standardized.
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Aggregated/Summarized:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` were aggregated in the `category_summary` and `county_summary` DataFrames.

**Logic and Methodology:**

The overarching methodology aimed to integrate disparate harvest and package datasets to create a unified view of cannabis product flow. This involved a systematic approach to data preparation:
*   **Consolidation:** Combining multiple source files into single, coherent DataFrames (`harvest_df`, `package_df`) ensured all relevant data was available for analysis.
*   **Standardization:** Renaming columns and converting data types facilitated consistent data handling and enabled mathematical operations. The `errors="coerce"` strategy for numeric conversions allowed for graceful handling of malformed data by converting invalid entries to `NaN`.
*   **Geographic Data Integrity:** Significant effort was dedicated to cleaning and normalizing `harvestercounty`. This was critical to ensure accurate geographic aggregation and analysis, addressing inconsistencies and missing values through replacement, mapping, and dropping incomplete records.
*   **Relational Integration:** Merging `package_df` and `harvest_df` established the core `harvestpackagemerge19-24` dataset, linking package outputs to their harvest origins. The strategy for resolving `harvestercounty` conflicts post-merge prioritized harvest data, assuming it might be more authoritative or complete for the harvester's location.
*   **Analytical Derivations:** The creation of ratio metrics (`package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`) was intended to provide deeper insights into processing efficiency, yield, and the relationship between harvested and packaged quantities.
*   **Hierarchical Aggregation:** Data was aggregated at both item category and county levels to provide summarized views, enabling analysis at different granularities and supporting macro-level insights into market trends.
*   **Reporting and Visualization:** The final aggregated data was exported and used to generate visualizations, serving as a direct output for reporting and aiding in the exploratory analysis of trends and patterns.

**Validation and Verification:**

*   Data type conversions utilized `errors="coerce"`, which implicitly flags non-convertible values as `NaN`, providing a basic level of error handling.
*   The repeated application of `dropna(subset=["harvestercounty"])` served as a verification step to ensure that subsequent geographic analysis was based on records with complete and valid county information.
*   The iterative cleaning steps for `harvestercounty` indicate an ongoing process of identifying and refining data quality for this critical identifier.
*   The generation of plots for the top 10 counties provided a visual means to verify the aggregated data, allowing for quick identification of trends, outliers, and potential data issues.
*   **Note on Discrepancy with Codebook's Cleaning Plan:** The provided Python code does not explicitly implement several specific data quality anomaly handling rules outlined in the Codebook's "Data Quality & Anomalies Section" and "Reproducible Cleaning Plan." Specifically:
    *   Negative `TotalHarvestPounds` values are not explicitly set to zero or otherwise corrected beyond `NaN` coercion during initial numeric conversion.
    *   Negative or out-of-range ratio values (such as `dryshare`, `pkgsharedry`, `pkgsharewet` mentioned in the Codebook, or their calculated equivalents `package_to_harvest_ratio`, `dry_to_wet_ratio` in the code) are not explicitly set to zero or capped at one.
    *   Invalid `HarvesterZipCode` formats are not specifically flagged, corrected, or imputed; the column remains as a string type and is not validated against standard zip code patterns.
    *   Missing `HarvesterCity` and `HarvesterZipCode` values are not explicitly imputed with 'Unknown' or '00000' as suggested in the Codebook, although rows with missing `harvestercounty` are dropped.

**Results and Outcomes:**

*   A consolidated `merged` dataset was successfully created, integrating harvest and package information, which forms the basis for the `harvestpackagemerge19-24` table.
*   Key columns were standardized in naming and converted to appropriate data types, making the data ready for quantitative analysis.
*   The `harvestercounty` column was significantly cleaned and normalized, enhancing the reliability of location-based analyses.
*   New analytical metrics, including `package_to_harvest_ratio` and `dry_to_wet_ratio`, were derived, providing valuable insights into product transformation and yield.
*   Aggregated summaries at both the item category and county levels were produced, offering high-level views of the data for strategic analysis.
*   The `county_summary` was exported to an Excel file, making the aggregated data readily available for further reporting and integration into other tools.
*   Visualizations were generated to illustrate trends in harvest pounds, package pounds, and package-to-harvest ratios across the top counties over time, facilitating data exploration and aiding in the identification of significant patterns or anomalies.
*   **Note on Data Quality:** While substantial cleaning was performed, particularly on geographic identifiers, the Python code does not explicitly address all the specific anomaly handling rules (e.g., correcting negative weights or out-of-range ratios) suggested in the Codebook's data quality sections. Therefore, the resulting `merged` and aggregated datasets may still contain these specific anomalies if they were present in the raw source files and were not converted to `NaN` during initial numeric parsing.






# Table: harvestpackagemerge23-24

### Overview Section

This dataset provides aggregated information related to cannabis harvest and packaging activities within the Track & Trace system, specifically covering the years 2023 and 2024. It aims to offer insights into the volume of cannabis processed by licensed harvesters, categorized by item type. Each row in the `harvestpackagemerge23-24` table represents an aggregated summary of harvest and package data for a specific harvester and item category within a given year. The overall data source is the Track & Trace system, with data collected during the 2023-2024 period. The exact extraction date is not specified.

**Assumptions:**
*   The table name `harvestpackagemerge23-24` indicates that the data covers activities from the years 2023 and 2024.
*   "Pounds" is the implied unit for all weight-related columns (`TotalPackagePounds`, `TotalHarvestPounds`, `TotalHarvestWetPounds`).
*   Harvester information (License Number, Facility Type, City, Zip Code, County) pertains to the entity responsible for the harvest and packaging activities.

### Table Inventory

*   **harvestpackagemerge23-24:** This table summarizes cannabis harvest and packaging metrics, including total pounds, unique harvest batches, and harvester details, aggregated by year and item category.

## Table: harvestpackagemerge23-24

*   **Purpose:** To provide an aggregated view of cannabis harvest and packaging volumes, linked to specific harvesters and item categories over the 2023-2024 period.
*   **What one row represents:** An aggregated summary of harvest and package data for a specific harvester, item category, and year.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 11869 rows, 11 columns

*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                           | Allowed Values / Range         |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------|:--------|:--------|:----------------------------------------------------------------------|:-------------------------------|------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique license number of the cannabis harvester.                      |                                |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| HarvesterFacilityType  | object  |         | Type of facility operated by the harvester.                           |                                |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| HarvesterCity          | object  |         | City where the harvester's facility is located.                       |                                |         0.1 | Missing values present. Consider imputation or flagging if critical for geographic analysis.                                                                                                                                                                                                                                                                       |
| HarvesterZipCode       | float64 |         | Zip code of the harvester's facility.                                 | 4000.0 - 961503674.0           |         5.5 | Missing values present. Some zip codes appear to be unusually large (e.g., 961503674.0), suggesting potential data entry errors or concatenated values. Validate against standard zip code formats. Consider imputation or flagging.                                                                                                                               |
| HarvesterCounty        | object  |         | County where the harvester's facility is located.                     |                                |         0.1 | Missing values present. Consider imputation or flagging if critical for geographic analysis.                                                                                                                                                                                                                                                                       |
| Year                   | int64   | Year    | The calendar year of the harvest and packaging activities.            | 2023.0 - 2024.0                |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| ItemCategory           | object  |         | Category of the cannabis item (e.g., Flower).                         |                                |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| TotalPackagePounds     | float64 | Pounds  | Total weight in pounds of packaged cannabis.                          | 0.0 - 819416.794               |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches contributing to the aggregated data. | 1.0 - 1110.0                   |         0   |                                                                                                                                                                                                                                                                                                                                                                    |
| TotalHarvestPounds     | float64 | Pounds  | Total weight in pounds of harvested cannabis.                         | -380.53733377132 - 785406.9175 |         2.5 | Contains negative values, which are physically impossible for weight. These entries likely represent data errors or returns/adjustments not properly accounted for. Recommended handling: Flag negative values and investigate their source. For analysis, consider treating them as missing or imputing with 0 if they represent negligible quantities or errors. |
| TotalHarvestWetPounds  | float64 | Pounds  | Total wet weight in pounds of harvested cannabis.                     | 0.75 - 4440808.26822343        |         2.5 | Missing values present. Consider imputation or flagging.                                                                                                                                                                                                                                                                                                           |


### Data Quality & Anomalies Section

*   **Issue:** `TotalHarvestPounds` contains negative values.
    *   **Likely cause:** Data entry errors, system glitches, or an incorrect representation of returns/adjustments within the tracking system where negative values are used to decrement inventory.
    *   **Recommended handling rule:** Flag all rows where `TotalHarvestPounds` is negative. For quantitative analysis, these values should be treated as invalid. Options include:
        1.  Excluding these rows from calculations involving total harvest pounds.
        2.  Imputing them with 0, assuming they represent negligible or erroneous entries that should not contribute negatively to total weight.
        3.  Investigating the source system to understand the business logic behind negative values.

*   **Issue:** `HarvesterZipCode` contains unusually large numeric values (e.g., 961503674.0) and missing values.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or inclusion of non-standard postal codes. Missing values indicate incomplete address information.
    *   **Recommended handling rule:**
        1.  For unusually large values, attempt to parse or truncate to standard 5-digit or 9-digit (ZIP+4) formats. If parsing is not feasible, flag as invalid.
        2.  For missing values, consider imputation based on `HarvesterCity` or `HarvesterCounty` if a reliable mapping exists, or flag as unknown.

*   **Issue:** Missing values in `HarvesterCity`, `HarvesterCounty`, `TotalHarvestPounds`, and `TotalHarvestWetPounds`.
    *   **Likely cause:** Incomplete data entry during the collection process or data extraction issues.
    *   **Recommended handling rule:**
        1.  For `HarvesterCity` and `HarvesterCounty`, if geographic analysis is critical, consider imputation based on other location fields or external geographic data, or flag rows with missing values.
        2.  For `TotalHarvestPounds` and `TotalHarvestWetPounds`, missing values should be handled based on the analytical context. Common approaches include exclusion, mean/median imputation, or more sophisticated methods if the missingness is not random.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Pounds:** Identify and flag all rows where `TotalHarvestPounds` is less than zero. For analytical purposes, replace these negative values with `NaN` or `0` to prevent erroneous calculations, depending on the downstream use case.
2.  **Validate and Clean Zip Codes:** Convert `HarvesterZipCode` to a string type. For values exceeding standard zip code lengths (e.g., 5 or 9 digits), attempt to extract the first 5 digits or flag as invalid. For missing zip codes, consider using `HarvesterCity` or `HarvesterCounty` to infer a plausible zip code if a lookup table is available, otherwise, leave as `NaN`.
3.  **Handle Missing Geographic Data:** For `HarvesterCity` and `HarvesterCounty` missing values, if these fields are critical for analysis, consider imputing them using the most frequent value within the same `HarvesterLicenseNumber` or leaving them as `NaN` and accounting for missingness in analysis.
4.  **Handle Missing Weight Data:** For missing values in `TotalHarvestPounds` (after addressing negative values) and `TotalHarvestWetPounds`, decide on an imputation strategy (e.g., mean, median, or zero) or exclude rows with missing values, based on the specific analytical requirements and tolerance for data loss.
5.  **Standardize Categorical Fields:** Review `HarvesterFacilityType` and `ItemCategory` for consistent capitalization and spelling to ensure accurate grouping and analysis.

### Limitations & Trust Section

*   **Geographic Data Incompleteness:** `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty` have missing values and potential inconsistencies (e.g., malformed zip codes). This limits the reliability of granular geographic analysis without further validation against external geographic datasets.
*   **Negative Harvest Pounds:** The presence of negative values in `TotalHarvestPounds` indicates a significant data quality issue that impacts the accuracy of total harvest volume calculations. Without understanding the root cause from the source system, any handling rule is an assumption.
*   **Data Aggregation Level:** The data is already aggregated by harvester, item category, and year. This limits the ability to perform analyses at a more granular level (e.g., individual transactions, specific harvest dates within a year).
*   **Lack of Primary Keys/Relationships:** The absence of explicit primary keys and relationships makes it challenging to confidently join this table with other potential datasets or to enforce data integrity rules.

To validate these elements, it would be beneficial to:
*   Consult with the data source owners to understand the meaning of negative `TotalHarvestPounds` and the data entry practices for geographic information.
*   Obtain a data dictionary or schema from the Track & Trace system for definitive column definitions, units, and expected value ranges.
*   Access raw, unaggregated data if available, to verify aggregation logic and investigate anomalies at a finer granularity.

### Appendix: Quick Reference

*   **Negative `TotalHarvestPounds`:** Flag and treat as invalid; consider replacing with 0 or `NaN` for analysis.
*   **Malformed `HarvesterZipCode`:** Validate and clean zip codes to standard formats; truncate or flag invalid entries.
*   **Missing Geographic Data:** Impute `HarvesterCity` and `HarvesterCounty` cautiously or flag for exclusion in geographic analysis.
*   **Missing Weight Data:** Address missing `TotalHarvestPounds` and `TotalHarvestWetPounds` via imputation (e.g., median) or exclusion, based on analytical needs.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for validation before any numeric conversion.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions, units, and proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative `TotalHarvestPounds` and the strategy for cleaning `HarvesterZipCode`. Any additional context regarding the Track & Trace system's data collection practices or business rules would be invaluable for refining this codebook and ensuring the reproducibility of the cleaning plan.

---

# Work Documentation

## Table: harvestpackagemerge23-24

**Data Operations:**
The provided Python script generates and processes a dataset that aligns with the description of `harvestpackagemerge23-24`. This involved several key steps:

*   **Source Data Consolidation:** Raw harvest quantity data from multiple CSV files (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and combined into a single `harvest_df`. Similarly, package quantity data from `packageqty19-24.csv`, `packageqty23-24.csv`, and `packageqty25.csv` were consolidated into a `package_df`. These consolidated dataframes were then saved as `harvest.csv` and `package.csv` respectively for future use.
*   **Column Renaming and Type Conversion:** Columns in both the `harvest_df` and `package_df` were systematically renamed to a consistent lowercase format (e.g., `HarvesterLicenseNumber` became `harvesterlicensenumber`). Critical numeric columns such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted to a numeric data type, with any conversion errors resulting in missing values.
*   **Initial Data Merging:** The cleaned `package_df` and `harvest_df` were merged using a left join operation, based on `harvesterlicensenumber` and `year`. This merge created a comprehensive dataset (`merged`) that conceptually represents the `harvestpackagemerge23-24` table, containing both harvest and package metrics alongside harvester details.
*   **Geographic Data Normalization and Imputation:**
    *   The `harvestercounty` column in both `harvest_df` and `package_df` underwent cleaning, replacing "NA" and "UNDEFINED" strings with empty values.
    *   A predefined mapping was applied to standardize various county name formats (e.g., "Alameda County" was converted to "ALAMEDA").
    *   Rows with missing `harvestercounty` values were removed after the initial mapping.
    *   Whitespace was removed from county names, and empty strings were converted to `pd.NA` (missing value indicator).
    *   The suffix "County" was removed from `harvestercounty` values to ensure consistency.
    *   In the merged dataset, the `harvestercounty` column was resolved by prioritizing the county information from the harvest data and falling back to the package data if the harvest county was missing.
    *   Further cleaning steps were applied to the `harvestercounty` column in the `merged` dataframe, replacing empty strings, "NA", and "nan" with `pd.NA`, followed by dropping any remaining rows with missing county information.
*   **Ratio Calculation:** Several new derived metrics were computed within the `merged` dataset to provide insights into processing efficiency:
    *   `package_to_harvest_ratio`: Calculated as the `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: Also calculated as `totalpackagepounds` divided by `totalharvestpounds`.
*   **Data Aggregation:** The `merged` dataset was further aggregated into two summary tables:
    *   **Category-level summary (`category_summary`):** This table was created by grouping the `merged` data by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, the first `totalharvestpounds` was taken, and the mean `package_to_harvest_ratio` was calculated.
    *   **County-level summary (`county_summary`):** This table was created by grouping the `merged` data by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, and the first `totalharvestpounds` was taken. A `package_to_harvest_ratio` was then calculated specifically for this aggregated table.
*   **Output Generation:** The final `county_summary` table was exported to an Excel file named `harvest_package_ratios.xlsx`.
*   **Exploratory Visualization:** The script also included steps to identify the top 10 counties based on total harvest pounds. For these top counties, bar plots were generated for each year to visualize trends in total harvest pounds, total package pounds, and the package-to-harvest ratio.

**Variables Affected:**
*   **Modified/Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `PkgYear` (renamed to `year`), `TotalHarvestPounds`, `TotalHarvestWetPounds`, `ItemCategory`, `TotalPackagePounds`, `UniqueHarvestBatches`. All these columns were consistently renamed to lowercase. The values within `HarvesterCounty` were standardized and cleaned across the dataset.
*   **Created:** New calculated fields include `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`. Additionally, aggregated versions of `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` were created in the `category_summary` and `county_summary` tables.

**Logic and Methodology:**
The overarching goal of these operations was to transform raw, disparate harvest and package data into a clean, standardized, and aggregated format suitable for analysis, mirroring the structure and content described for `harvestpackagemerge23-24`. The methodology involved:
*   **Data Integration:** Combining multiple years and types of data (harvest and package) into unified dataframes.
*   **Standardization:** Ensuring consistency in column names and, critically, in geographic identifiers like county names, which often suffer from varied spellings or formats in raw data.
*   **Data Cleansing:** Handling missing values and potential inconsistencies in geographic data to improve data quality and reliability for location-based analysis.
*   **Feature Engineering:** Deriving new metrics (ratios) that provide deeper insights into the efficiency of cannabis processing from harvest to final package.
*   **Aggregation:** Summarizing the data at different levels (item category and county) to support both granular and high-level analytical perspectives.
*   **Reporting and Visualization:** Generating structured outputs and visual summaries to facilitate understanding of key trends and comparisons across counties and years.

**Validation and Verification:**
*   Data type conversions were implemented with error coercion, which automatically handles non-numeric entries by converting them to `NaN`, preventing script failures due to unexpected data types.
*   Missing values in the `harvestercounty` column were explicitly addressed through multiple steps of replacement and row removal, ensuring that subsequent analyses rely on complete geographic information.
*   While the merge operation for `package_df` and `harvest_df` did not explicitly use a `validate` argument, the `how="left"` strategy ensures that all package records are retained, with harvest-related fields potentially becoming missing if no match is found.
*   No explicit data validation checks (e.g., range checks for weight values, consistency checks between related fields) were observed in the provided code snippets for the `harvestpackagemerge23-24` related processing, beyond the handling of missing or malformed county names and the numeric conversions.

**Results and Outcomes:**
The data work resulted in:
*   A consolidated and cleaned dataset that effectively represents the `harvestpackagemerge23-24` table, ready for detailed analysis.
*   Standardized and more reliable geographic information for harvesters, enhancing the accuracy of location-based insights.
*   The creation of new, insightful metrics such as `package_to_harvest_ratio` and `dry_to_wet_ratio`, which are crucial for evaluating operational efficiency.
*   The generation of aggregated summary tables at both the item category and county levels, providing a structured overview of the cannabis market.
*   An Excel report (`harvest_package_ratios.xlsx`) containing county-level summaries, serving as a direct output for stakeholders.
*   A series of visualizations that highlight key trends in harvest and package volumes, as well as processing ratios, across top-performing counties over time.






# Table: harvestpackagemerge25

### Overview Section

This dataset provides a detailed view into the "Track & Trace" project, focusing on the journey of cannabis products from harvest to packaging. It primarily captures information related to packaged products, their originating harvests, and the licensed harvesters involved. Each row in the `harvestpackagemerge25` table represents a specific package or a record associated with a package, detailing its characteristics, the harvester's location, and metrics related to the harvest from which it originated. The overall data source, collection period, and extraction date are not explicitly provided in the current summary.

**Assumptions:**
*   The `PkgYear` field indicating '2025' suggests this dataset might represent future projections, planned activities, or a specific reporting period for the year 2025, rather than historical data.
*   The data is intended for analysis of harvest-to-package yields and harvester performance.

### Table Inventory

*   **harvestpackagemerge25:** This table consolidates information about packaged products, linking them to their originating harvests and providing details about the harvester.

### Table: harvestpackagemerge25

*   **Purpose:** To track and analyze the packaging of harvested cannabis products, including harvester details and yield metrics.
*   **What one row represents:** One record of a packaged product derived from a harvest, including associated harvester and yield information.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 4125 rows, 14 columns

*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                                                                | Allowed Values / Range                 |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                               |
|:-----------------------|:--------|:--------|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------|------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique license number of the harvester facility.                                                           |                                        |         0   |                                                                                                                                                                                                                                                                                                                                |
| HarvesterFacilityType  | object  |         | Type of facility operated by the harvester (e.g., Microbusiness License).                                  |                                        |         0   |                                                                                                                                                                                                                                                                                                                                |
| HarvesterCity          | object  |         | City where the harvester facility is located.                                                              |                                        |         0   |                                                                                                                                                                                                                                                                                                                                |
| HarvesterZipCode       | float64 |         | Zip code of the harvester facility.                                                                        | 89019.0 - 960679768.0                  |         3.2 | 3.2% missing values. Consider imputation or flagging for analysis requiring complete location data. The upper range value 960679768.0 appears to be an outlier or data entry error, as zip codes are typically 5 digits.                                                                                                       |
| HarvesterCounty        | object  |         | County where the harvester facility is located.                                                            |                                        |         0   |                                                                                                                                                                                                                                                                                                                                |
| PkgYear                | int64   | Year    | The year associated with the package.                                                                      | 2025.0 - 2025.0                        |         0   | All values are '2025'. This suggests the data may be for a future period, a projection, or a placeholder. Verify the intended meaning of this field with data owners.                                                                                                                                                          |
| ItemCategory           | object  |         | Category of the packaged item (e.g., Flower).                                                              |                                        |         0   |                                                                                                                                                                                                                                                                                                                                |
| TotalPackagePounds     | float64 | Pounds  | Total weight of the package in pounds.                                                                     | 0.0004188786398349 - 282901.024047837  |         0   |                                                                                                                                                                                                                                                                                                                                |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches contributing to this package.                                             | 1.0 - 478.0                            |         0   |                                                                                                                                                                                                                                                                                                                                |
| TotalHarvestPounds     | float64 | Pounds  | Total dry weight from harvest associated with this package.                                                | 0.0022 - 282901.024047837              |         0   |                                                                                                                                                                                                                                                                                                                                |
| TotalHarvestWetPounds  | float64 | Pounds  | Total wet weight from harvest associated with this package.                                                | 1.4625 - 2500998.83340094              |         0   |                                                                                                                                                                                                                                                                                                                                |
| dryshare               | float64 | Ratio   | Ratio of TotalHarvestPounds to TotalHarvestWetPounds (dry weight / wet weight).                            | 1.62150769302827e-05 - 3.262834        |         0   | Values exceeding 1.0 (e.g., 3.26) suggest potential data entry errors or miscalculation, as dry weight should not exceed wet weight. Investigate records where dryshare > 1.0.                                                                                                                                                 |
| pkgsharedry            | float64 | Ratio   | Share of package pounds relative to total dry harvest pounds (TotalPackagePounds / TotalHarvestPounds).    | 1.86714224365046e-07 - 1.0059936674625 |         0   | Values slightly exceeding 1.0 (e.g., 1.00599) indicate that the package weight is marginally greater than the total dry harvest pounds it's attributed to. This could be due to rounding, minor data discrepancies, or measurement inaccuracies. Flag these for review or consider capping at 1.0 if appropriate for analysis. |
| pkgsharewet            | float64 | Ratio   | Share of package pounds relative to total wet harvest pounds (TotalPackagePounds / TotalHarvestWetPounds). | 3.36485567872677e-08 - 2.2928          |         0   | Values exceeding 1.0 (e.g., 2.2928) suggest a package weight greater than the total wet harvest pounds it's attributed to, which is physically impossible. Investigate these records for data entry errors or miscalculations.                                                                                                 |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestpackagemerge25` table.

*   **Issue:** Missing `HarvesterZipCode` values.
    *   **Likely cause:** Incomplete data entry or optional field during data collection.
    *   **Recommended handling rule:** For analyses requiring complete location data, rows with missing zip codes can be excluded or the zip code can be imputed based on `HarvesterCity` and `HarvesterCounty` if a reliable mapping exists. Otherwise, flag these records.
*   **Issue:** Anomalous `HarvesterZipCode` range.
    *   **Likely cause:** Data entry error or incorrect data type conversion. The upper range value `960679768.0` is not a valid 5-digit zip code.
    *   **Recommended handling rule:** Identify and correct or remove records with non-standard zip codes. Convert `HarvesterZipCode` to string type to preserve leading zeros and handle non-numeric entries more robustly.
*   **Issue:** `PkgYear` exclusively '2025'.
    *   **Likely cause:** The dataset represents future projections, planned data, or a specific reporting period for the year 2025. It is unlikely to be historical data if collected prior to 2025.
    *   **Recommended handling rule:** Confirm the intended meaning of this field with data stakeholders. If it's a projection, clearly document this assumption in any analysis. If it's a placeholder, investigate the actual intended year.
*   **Issue:** `dryshare` values greater than 1.0.
    *   **Likely cause:** Miscalculation or data entry error, as dry weight should not exceed wet weight.
    *   **Recommended handling rule:** Flag records where `dryshare > 1.0`. Investigate the source data for these records. For analysis, these values may need to be capped at 1.0 or excluded if the discrepancy is significant.
*   **Issue:** `pkgsharedry` values slightly greater than 1.0.
    *   **Likely cause:** Minor rounding errors, measurement inaccuracies, or slight discrepancies between reported package weight and harvest weight.
    *   **Recommended handling rule:** For practical purposes, values marginally above 1.0 can often be capped at 1.0, assuming they represent 100% allocation. Flag these records for potential review if high precision is critical.
*   **Issue:** `pkgsharewet` values greater than 1.0.
    *   **Likely cause:** Significant data entry error or miscalculation, as package weight cannot exceed the total wet harvest weight it originated from.
    *   **Recommended handling rule:** Flag records where `pkgsharewet > 1.0`. These are strong indicators of erroneous data and should be investigated thoroughly. Depending on the severity, these records may need to be excluded or corrected.

### Reproducible Cleaning Plan

1.  **Standardize Harvester Zip Codes:** Convert `HarvesterZipCode` to a string type to preserve leading zeros and handle non-numeric entries. Identify and flag or correct zip codes that are not 5-digit numeric values (e.g., `960679768.0`).
2.  **Address Missing Zip Codes:** For records with missing `HarvesterZipCode`, either impute based on `HarvesterCity` and `HarvesterCounty` using a lookup table if available, or flag these records for exclusion from analyses requiring complete location data.
3.  **Validate `PkgYear`:** Confirm the intended meaning of the `PkgYear` field with data owners. If it represents a future projection, document this clearly. No direct cleaning action is proposed without further clarification.
4.  **Correct `dryshare` Anomalies:** Identify and flag all records where `dryshare` is greater than 1.0. Investigate these records for potential data entry errors or miscalculations. For analytical purposes, consider capping these values at 1.0 or excluding them if the discrepancy is substantial.
5.  **Handle `pkgsharedry` Overages:** For `pkgsharedry` values slightly exceeding 1.0, cap these values at 1.0 to ensure logical consistency (package weight cannot exceed total harvest weight). Flag these records for potential review.
6.  **Address `pkgsharewet` Anomalies:** Identify and flag all records where `pkgsharewet` is greater than 1.0. These represent significant data inconsistencies and should be investigated thoroughly. Exclude these records from analyses or correct them if the true values can be ascertained.

### Limitations & Trust Section

The reliability of this dataset is subject to several limitations:

*   **`PkgYear` Discrepancy:** The uniform `PkgYear` of '2025' raises questions about whether this data represents actual historical events, future projections, or a placeholder. This significantly impacts the interpretability and trustworthiness of any time-series analysis or historical reporting. Validation with the data source is crucial.
*   **Missing and Anomalous `HarvesterZipCode`:** The presence of missing values and an extremely anomalous upper range for `HarvesterZipCode` indicates potential data entry issues or inconsistent data collection practices. This limits the accuracy of geographical analysis based solely on this field.
*   **Inconsistent Weight Ratios (`dryshare`, `pkgsharedry`, `pkgsharewet`):** Values in `dryshare`, `pkgsharedry`, and `pkgsharewet` that exceed logical bounds (e.g., dry weight > wet weight, package weight > total harvest weight) suggest underlying data quality issues, potentially from measurement errors, calculation errors, or incorrect data linkages. These inconsistencies reduce the trust in yield and allocation metrics.
*   **Lack of Primary Keys and Relationships:** The absence of identified primary keys and explicit relationship definitions makes it challenging to ensure data integrity and accurately join this table with other potential datasets within the Track & Trace ecosystem.

To validate these elements, it is essential to:
*   Consult with the data engineering or source system team to understand the origin and intended meaning of `PkgYear`.
*   Review data entry procedures for `HarvesterZipCode` and implement validation rules at the point of data capture.
*   Investigate the calculation logic for `dryshare`, `pkgsharedry`, and `pkgsharewet` and cross-reference with raw harvest and package weight data where available.
*   Obtain a comprehensive data model or schema diagram to understand primary keys and relationships across all Track & Trace tables.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Convert `HarvesterZipCode` to string; validate and correct non-standard 5-digit entries.
*   **Missing Data Handling:** Flag or impute missing `HarvesterZipCode` based on analysis needs.
*   **`PkgYear` Verification:** Confirm '2025' meaning with data owners; document as projection if applicable.
*   **`dryshare` Validation:** Flag records where `dryshare > 1.0`; investigate and potentially cap at 1.0.
*   **`pkgsharedry` Adjustment:** Cap `pkgsharedry` values slightly above 1.0 to 1.0.
*   **`pkgsharewet` Correction:** Flag and investigate records where `pkgsharewet > 1.0`; exclude or correct as necessary.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of column descriptions and inferred purposes, especially for calculated fields like `dryshare`, `pkgsharedry`, and `pkgsharewet`. Particular attention should be paid to the proposed handling rules for anomalies, such as the `PkgYear` being exclusively '2025' and the various ratio fields exceeding logical bounds. Confirmation from data owners regarding the intended meaning and acceptable ranges for these fields would greatly enhance the reproducibility and reliability of any subsequent data analysis.

# Work Documentation

## Table: harvestpackagemerge25

**Data Operations:**
The `harvestpackagemerge25` table, as described in the codebook, is conceptually represented by a `merged` DataFrame in the provided Python scripts. This DataFrame is constructed by combining data from multiple source files related to cannabis harvest and package quantities.

Specifically, the process involved:
1.  **Source Data Consolidation:** Separate CSV files containing harvest data (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and concatenated into a single `harvest_df`. Similarly, package data (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were consolidated into a `package_df`. These consolidated dataframes were then saved to intermediate CSV files (`harvest.csv` and `package.csv`) and reloaded.
2.  **Column Renaming and Type Conversion:** Key columns in both `harvest_df` and `package_df` were renamed for standardization (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`). Numeric fields such as `year`, `totalharvestpounds`, `totalharvestwetpounds`, and `totalpackagepounds` were converted to appropriate numeric types, with errors coerced to missing values.
3.  **Geographical Data Cleaning and Standardization:** The `HarvesterCounty` column in both `harvest_df` and `package_df` underwent extensive cleaning. This included replacing "NA" and "UNDEFINED" values with empty strings, mapping full county names (e.g., "Alameda County") to their standardized uppercase abbreviations (e.g., "ALAMEDA") using a predefined dictionary, stripping leading/trailing whitespace, replacing empty strings with proper missing value indicators (`pd.NA`), and removing the "County" suffix. Rows with resulting missing `harvestercounty` values were subsequently dropped.
4.  **Data Integration (Merge):** The cleaned `package_df` and `harvest_df` were merged using a left join operation. The merge was performed on `harvesterlicensenumber` and `year`, with suffixes `_pkg` and `_harv` applied to distinguish columns originating from each source. A unified `harvestercounty` column was then created, prioritizing the value from the harvest data (`harvestercounty_harv`) if available, otherwise using the package data (`harvestercounty_pkg`). Further cleaning and dropping of missing `harvestercounty` values were applied to the merged dataset.
5.  **Derived Metric Calculation:** Several new ratio variables were calculated:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. This corresponds to the `pkgsharedry` column in the codebook.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`. This corresponds to the `dryshare` column in the codebook.
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. This appears to be a duplicate calculation of `package_to_harvest_ratio`.
6.  **Aggregation and Export:** The `merged` DataFrame was used to create aggregated summaries:
    *   `category_summary`: Grouped by `harvestercounty`, `year`, and `itemcategory`, summing `totalpackagepounds` and averaging `package_to_harvest_ratio`.
    *   `county_summary`: Grouped by `harvestercounty` and `year`, summing `totalpackagepounds` and calculating `package_to_harvest_ratio` at the county level.
    The `county_summary` was then exported to an Excel file named `harvest_package_ratios.xlsx`.
7.  **Data Visualization:** The processed data was used to generate various plots, including bar charts illustrating total harvest pounds, total package pounds, and package-to-harvest ratios for the top 10 counties across different years.

**Variables Affected:**
*   **Modified/Renamed:** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype_pkg`/`_harv`), `HarvesterCity` (to `harvestercity_pkg`/`_harv`), `HarvesterZipCode` (to `harvesterzipcode_pkg`/`_harv`), `HarvesterCounty` (standardized and unified to `harvestercounty`), `PkgYear` (to `year`), `ItemCategory` (to `itemcategory`), `TotalPackagePounds` (to `totalpackagepounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches_pkg`/`_harv`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`).
*   **Created:**
    *   `package_to_harvest_ratio` (corresponds to codebook's `pkgsharedry`).
    *   `dry_to_wet_ratio` (corresponds to codebook's `dryshare`).
    *   `category_share` (a duplicate calculation of `package_to_harvest_ratio`).
*   **Not explicitly created/addressed:** The codebook's `pkgsharewet` (TotalPackagePounds / TotalHarvestWetPounds) is not calculated in the provided Python script.
*   **Validated/Cleaned:** `year`, `totalharvestpounds`, `totalharvestwetpounds`, `totalpackagepounds` (via numeric conversion with error coercion), `harvestercounty` (via extensive standardization and removal of missing values).

**Logic and Methodology:**
The overarching goal of these operations is to prepare a comprehensive dataset for analyzing the flow of cannabis products from harvest to packaging, focusing on yield metrics and harvester performance. The methodology involves:
*   **Data Integration:** Combining disparate harvest and package records into a single, coherent view to enable cross-source analysis.
*   **Data Standardization:** Ensuring consistency in column names, data types, and categorical values (especially for `harvestercounty`) to facilitate accurate aggregation and comparison.
*   **Feature Engineering:** Deriving new ratio variables (`package_to_harvest_ratio`, `dry_to_wet_ratio`) to quantify key performance indicators related to processing efficiency and yield.
*   **Aggregation:** Summarizing data at different granularities (category-level, county-level) to identify trends and patterns.
*   **Exploratory Visualization:** Generating plots to visually inspect the data, highlight top performers, and understand temporal changes in key metrics.

It is important to note a discrepancy with the codebook's description of `PkgYear`. While the codebook states `PkgYear` is exclusively '2025', the Python script processes data spanning multiple years (2019-2025), providing a broader historical context for analysis.

**Validation and Verification:**
Data validation steps observed in the script include:
*   **Type Coercion:** Numeric conversions (`pd.to_numeric`) use `errors='coerce'`, which automatically handles non-numeric entries by converting them to `NaN`, preventing script crashes and implicitly flagging problematic values.
*   **Missing Value Handling:** Rows with missing `harvestercounty` values are explicitly dropped at multiple stages, indicating a strict requirement for complete geographical information for analysis.
*   **Lookup-based Standardization:** The `county_map` serves as a form of data validation and standardization for county names, ensuring consistency across records.
*   **Merge Integrity:** While the merge operation for `harvestpackagemerge25` (the `merged` DataFrame) does not explicitly use a `validate` argument, the `how="left"` merge strategy ensures that all package records are retained, and harvest information is added where a match exists.

Crucially, the Python script *does not implement* the explicit validation or correction rules suggested in the codebook's "Reproducible Cleaning Plan" for ratio values like `dryshare` (now `dry_to_wet_ratio`) and `pkgsharedry` (now `package_to_harvest_ratio`) that exceed logical bounds (e.g., capping at 1.0 or flagging for investigation). The `pkgsharewet` ratio, also noted for potential anomalies in the codebook, is not calculated at all in the provided script.

**Results and Outcomes:**
The data work results in a refined and integrated dataset that serves as the foundation for further analysis. Key outcomes include:
*   A consolidated `merged` DataFrame (representing `harvestpackagemerge25`) containing harmonized harvest and package data from 2019 to 2025.
*   Cleaned and standardized geographical data, improving the reliability of location-based analysis.
*   New, analytically useful ratio metrics (`package_to_harvest_ratio`, `dry_to_wet_ratio`) that quantify yield and conversion rates.
*   Aggregated summaries at the category and county levels, providing high-level insights into market dynamics.
*   An exported Excel file (`harvest_package_ratios.xlsx`) containing county-level summary data.
*   A series of visualizations that offer immediate insights into trends and performance across different counties and years.

While the processing addresses several data quality issues identified in the codebook, particularly regarding `HarvesterCounty` standardization and the expansion of the `PkgYear` range, the script does not implement the recommended anomaly handling for ratio values exceeding logical bounds, which remains a pending data quality concern for the derived metrics.






# Table: harvestqty19-24

### Overview Section

This dataset, part of the Track & Trace project, provides aggregated harvest quantity data for licensed cannabis harvesters. Each row in the `harvestqty19-24` table represents a summary of harvest activities for a specific harvester, identified by their license number, within a given packaging year. The overall data source, collection period, and extraction date are currently unknown.

*   **Assumptions:**
    *   One row in `harvestqty19-24` represents aggregated harvest metrics for a unique harvester (`HarvesterLicenseNumber`) in a specific `PkgYear`.

### Table Inventory

*   `harvestqty19-24`: Contains aggregated harvest quantity data, including total harvest pounds, wet pounds, and unique batch counts, for licensed harvesters between 2019 and 2024.

## Table: harvestqty19-24

*   **Purpose:** To track and summarize harvest quantities and activities by licensed harvesters over several years.
*   **What one row represents:** Aggregated harvest metrics for a specific harvester (`HarvesterLicenseNumber`) during a particular `PkgYear`.
*   **Primary key(s):** Inferred composite key: `HarvesterLicenseNumber`, `PkgYear`.
*   **Relationships:** Unknown.
*   **Number of rows and columns:** 27719 rows, 9 columns.
*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                               | Allowed Values / Range                 |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------|:--------|:--------|:----------------------------------------------------------|:---------------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique identifier for the licensed harvester.             |                                        |         0   |                                                                                                                                                                                                                                                                                                                                                                                                    |
| HarvesterFacilityType  | object  |         | Type of facility associated with the harvester's license. |                                        |         0   |                                                                                                                                                                                                                                                                                                                                                                                                    |
| HarvesterCity          | object  |         | City where the harvester's facility is located.           |                                        |         0.2 | Missing values (0.2%) should be investigated. Consider imputation with a common value or flagging for review if critical for analysis.                                                                                                                                                                                                                                                             |
| HarvesterZipCode       | float64 |         | Zip code of the harvester's facility.                     | [4000.0, 961503674.0]                  |         8   | Missing values (8.0%) should be addressed. The upper range value (961503674.0) is highly anomalous for a US zip code; likely a data entry error or concatenation. Values outside the typical 5-digit or 9-digit US zip code format should be flagged or set to null. Consider imputation for missing values if geographic analysis is required, or use HarvesterCity for broader location context. |
| HarvesterCounty        | object  |         | County where the harvester's facility is located.         |                                        |         1.3 | Missing values (1.3%) should be investigated. Consider imputation or flagging.                                                                                                                                                                                                                                                                                                                     |
| PkgYear                | int64   | Year    | The year in which the harvest was packaged.               | [2019.0, 2024.0]                       |         0   |                                                                                                                                                                                                                                                                                                                                                                                                    |
| TotalHarvestPounds     | float64 | Pounds  | Total weight of harvested product in pounds.              | [-358.596995537842, 911433642.960996]  |         0   | Contains negative values, which are physically impossible for harvest quantities. These should be flagged, investigated, and potentially set to null or zero, or excluded from calculations. The upper range also appears extremely high, suggesting potential outliers or data entry errors.                                                                                                      |
| TotalHarvestWetPounds  | float64 | Pounds  | Total wet weight of harvested product in pounds.          | [0.0002204624420183, 1371869133.03903] |         0   | The upper range appears extremely high, suggesting potential outliers or data entry errors.                                                                                                                                                                                                                                                                                                        |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches recorded.                | [1.0, 8875.0]                          |         0   |                                                                                                                                                                                                                                                                                                                                                                                                    |


### Data Quality & Anomalies Section

*   **Issue:** Negative `TotalHarvestPounds`.
    *   **Likely cause:** Data entry error, system bug, or a representation of returns/adjustments without proper flagging. Physically impossible for a harvest quantity.
    *   **Recommended handling rule:** Flag these records for investigation. For analytical purposes, treat negative values as invalid: either set to `NULL`, `0`, or exclude from calculations involving sums/averages.
*   **Issue:** Anomalous `HarvesterZipCode` values.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or inclusion of non-standard codes. The upper range value (961503674.0) is not a valid US zip code format.
    *   **Recommended handling rule:** Validate `HarvesterZipCode` against a standard US zip code format (5 or 9 digits). Flag or set to `NULL` any values that do not conform.
*   **Issue:** Extremely large values in `TotalHarvestPounds` and `TotalHarvestWetPounds`.
    *   **Likely cause:** Potential data entry errors, unit conversion mistakes, or genuine but extreme outliers.
    *   **Recommended handling rule:** Investigate these extreme values. Consider winsorization or capping if they are deemed genuine but disproportionately influence analysis, or flag as outliers for further review.
*   **Issue:** Missing values in `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`.
    *   **Likely cause:** Incomplete data entry or optional fields.
    *   **Recommended handling rule:** For `HarvesterZipCode`, address after handling anomalous values. For all, consider imputation if location data is critical (e.g., using mode for categorical fields) or exclude records with missing critical location data for specific analyses.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Quantities:** Identify all records where `TotalHarvestPounds` is negative. For analytical purposes, these values will be set to `NULL` or `0` and flagged for further investigation into their origin.
2.  **Validate Zip Codes:** Filter `HarvesterZipCode` values. Any values that are not 5-digit or 9-digit numeric strings (after converting to string) will be flagged as invalid and set to `NULL`.
3.  **Handle Missing Location Data:** For `HarvesterCity`, `HarvesterZipCode` (after validation), and `HarvesterCounty`, records with missing values will be flagged. Depending on the analysis, these may be imputed (e.g., using the mode for categorical fields) or excluded.
4.  **Review Outlier Harvest Quantities:** Identify and flag records where `TotalHarvestPounds` or `TotalHarvestWetPounds` exceed a reasonable upper bound (e.g., 99th percentile + 3*IQR or a domain-specific threshold) for further review.

### Limitations & Trust Section

The dataset's reliability is impacted by several factors. The absence of explicit primary keys and relationships makes data integration and integrity validation challenging. The presence of negative harvest quantities and anomalous zip codes indicates potential data entry or system errors, requiring careful cleaning and validation. The overall data source, collection period, and extraction date are unknown, which limits the ability to fully contextualize and trust the data's recency and provenance. Validation against external licensing or harvest records would be needed to confirm the accuracy of harvester details and reported quantities.

### Appendix: Quick Reference

*   Negative `TotalHarvestPounds` values are invalid and set to `NULL` or `0`.
*   `HarvesterZipCode` values are validated for 5 or 9-digit numeric format; invalid entries are set to `NULL`.
*   Missing `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty` values are flagged.
*   Extreme outliers in `TotalHarvestPounds` and `TotalHarvestWetPounds` are flagged for review.
*   Inferred composite primary key: `HarvesterLicenseNumber`, `PkgYear`.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for negative harvest quantities and anomalous zip codes. Specific attention should be paid to the interpretation of "what one row represents" and the inferred primary key, as these are critical for data integrity and analysis. Additionally, any domain-specific knowledge regarding typical harvest quantities or zip code formats would be valuable to refine outlier detection thresholds and validation rules.

# Work Documentation

## Table: harvestqty19-24

**Data Operations:**
The data described conceptually as `harvestqty19-24` in the codebook was processed through several steps. Initially, multiple CSV files (`harvestqty19-24.csv`, `harvestqty23-24.csv`, `harvestqty25.csv`) were loaded and concatenated into a single dataframe named `harvest_df`. This consolidated dataframe was then saved to `Data/Track and Trace Data/Harvest/harvest.csv` and subsequently re-loaded for further processing.

Column names were standardized to a consistent lowercase format (e.g., `HarvesterLicenseNumber` was renamed to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`). The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric data types, with any non-convertible values being coerced to `NaN` (Not a Number).

The `harvestercounty` column underwent extensive cleaning and normalization. Initial string replacements converted "NA" and "UNDEFINED" values to empty strings. A predefined mapping was then applied to standardize county names (e.g., "Alameda County" was mapped to "ALAMEDA"). Rows where `harvestercounty` remained missing after this initial cleaning were removed. Further cleaning involved stripping leading/trailing whitespace, replacing empty strings with `pd.NA`, and removing the " County" suffix from all values. Any rows with `harvestercounty` values still identified as missing after these steps were subsequently dropped.

This cleaned `harvest_df` was then merged with a `package_df` (derived from separate `packageqty` files) using `harvesterlicensenumber` and `year` as keys, resulting in a `merged` dataframe. During this merge, the `harvestercounty` column was consolidated, prioritizing values from the `harvest_df` if available. New ratio-based metrics were calculated within the `merged` dataframe: `package_to_harvest_ratio` (total packaged pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total wet harvest pounds), and `category_share` (total packaged pounds divided by total harvest pounds). The `harvestercounty` column in the `merged` dataframe received additional cleaning, replacing empty strings, "<NA>", and "nan" with `pd.NA`, followed by dropping any remaining rows with missing county values.

Finally, the `merged` dataframe was used to create aggregated summaries. `category_summary` was generated by grouping data by `harvestercounty`, `year`, and `itemcategory`, calculating the sum of `totalpackagepounds` and the mean `package_to_harvest_ratio`. `county_summary` was created by grouping by `harvestercounty` and `year`, summing `totalpackagepounds`, and then calculating the `package_to_harvest_ratio` at the county level. The `county_summary` was exported to an Excel file named `harvest_package_ratios.xlsx`. Subsequent code snippets utilized this `county_summary` for generating various plots to visualize harvest and package pound trends, as well as package-to-harvest ratios across the top 10 counties by year.

**Variables Affected:**
*   `HarvesterLicenseNumber`: Renamed to `harvesterlicensenumber`.
*   `HarvesterFacilityType`: Renamed to `harvesterfacilitytype`.
*   `HarvesterCity`: Renamed to `harvestercity`.
*   `HarvesterZipCode`: Renamed to `harvesterzipcode`.
*   `HarvesterCounty`: Renamed to `harvestercounty`, extensively cleaned, normalized, and used for filtering.
*   `PkgYear`: Renamed to `year`, converted to numeric.
*   `TotalHarvestPounds`: Renamed to `totalharvestpounds`, converted to numeric, and used in ratio calculations.
*   `TotalHarvestWetPounds`: Renamed to `totalharvestwetpounds`, converted to numeric, and used in ratio calculations.
*   `UniqueHarvestBatches`: Renamed to `uniqueharvestbatches`.
*   *New variables created:* `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
The data work followed a systematic approach to prepare the harvest quantity data for analysis.
1.  **Data Consolidation:** Multiple annual harvest quantity files were combined to create a comprehensive dataset, ensuring a complete time-series view of harvest activities. This addresses the fragmented nature of the raw data.
2.  **Standardization:** Column names were converted to a consistent lowercase format to improve readability and facilitate programmatic access across different datasets.
3.  **Type Conversion:** Key quantitative and temporal columns were explicitly converted to numeric data types. This is crucial for enabling accurate mathematical operations and time-series analysis, with error coercion to `NaN` allowing for identification of problematic entries.
4.  **Geographic Data Cleaning and Normalization:** The `HarvesterCounty` column, critical for location-based analysis, underwent rigorous cleaning. This involved replacing inconsistent string values ("NA", "UNDEFINED"), standardizing county names using a predefined mapping, and removing the " County" suffix. Records with unresolvable missing county information were removed to ensure the integrity of geographic analyses.
5.  **Data Integration:** The cleaned harvest data was merged with package data. This integration is fundamental for comparative analysis, allowing for the calculation of ratios that reflect the efficiency of product flow from harvest to packaging.
6.  **Ratio Calculation:** New derived metrics, such as `package_to_harvest_ratio` and `dry_to_wet_ratio`, were introduced to provide insights into operational efficiency and product transformation. `category_share` was also calculated to understand the distribution of packaged product by category relative to total harvest.
7.  **Aggregation:** Data was aggregated at both category and county levels to provide summarized views. This enables high-level trend analysis and comparison across different segments and geographic regions.
8.  **Visualization Preparation:** The aggregated data was specifically prepared for visualization, allowing for graphical representation of trends and distributions of harvest and package quantities and their ratios across top counties and years.

**Validation and Verification:**
*   The use of `pd.to_numeric(errors="coerce")` for numeric conversions implicitly handles non-numeric values by converting them to `NaN`, which can then be explicitly addressed or investigated.
*   Multiple `dropna(subset=["harvestercounty"])` calls were strategically placed after cleaning steps to ensure that subsequent analyses are performed on records with valid and standardized county information.
*   The merge operation between `harvest_df` and `package_df` used a `left` join, preserving all records from the harvest data while incorporating matching package data.
*   Conditional logic (`if "harvestercounty_harv" in merged.columns`) was used during the consolidation of county columns in the `merged` dataframe, demonstrating a defensive programming approach to handle potential variations in column availability.

**Results and Outcomes:**
*   A consolidated and cleaned `harvest_df` was successfully created, providing a robust foundation for subsequent analysis.
*   Standardized column names and appropriate data types were established, ensuring consistency and facilitating accurate data processing.
*   The quality of geographic data in the `harvestercounty` column was significantly improved, leading to more reliable location-based insights.
*   A `merged` dataset integrating harvest and package information was generated, enabling the calculation of key performance ratios that track product flow.
*   Aggregated summaries at the category and county levels were produced, offering high-level insights into harvest and packaging trends.
*   An Excel file (`harvest_package_ratios.xlsx`) containing county-level summaries was generated, providing a structured output for further review and reporting.
*   A series of visualizations were created to illustrate harvest and package quantity trends and their ratios for top counties over time, aiding in the rapid identification of patterns, outliers, and operational efficiencies.






# Table: harvestqty23-24

### Overview Section

This dataset provides a summary of cannabis harvest quantities reported by licensed harvesters within the Track & Trace system. It offers insights into the volume of cannabis harvested, categorized by harvester details and year. Each row in the `harvestqty23-24` table represents a unique harvest record for a specific licensed harvester within a given year, detailing their reported harvest quantities. The data is sourced from the Track & Trace project, covering the collection period of 2023-2024. The extraction date is not available.

**Assumptions:**
*   Data reflects reported quantities as submitted to the Track & Trace system.
*   "Pounds" refer to avoirdupois pounds.

### Table Inventory

*   **harvestqty23-24**: Contains aggregated harvest quantity data for licensed harvesters for the years 2023 and 2024.

## Table: harvestqty23-24

*   **Purpose:** To track and summarize the total dry and wet harvest quantities, along with the number of unique harvest batches, for individual licensed cannabis harvesters over the years 2023 and 2024.
*   **What one row represents:** One aggregated harvest record for a specific licensed harvester (`HarvesterLicenseNumber`) in a particular `Year`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `Year` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 7500 rows, 9 columns

### Column Dictionary


| Column Name            | Type    | Units   | Description                                                                                        | Allowed Values / Range                    |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                |
|:-----------------------|:--------|:--------|:---------------------------------------------------------------------------------------------------|:------------------------------------------|------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | string  |         | Unique identifier for the harvester's license.                                                     | Example: C12-0000002-LIC                  |         0   |                                                                                                                                                                                                                                                                                                                                                 |
| HarvesterFacilityType  | string  |         | Type of facility associated with the harvester's license (e.g., Cannabis - Microbusiness License). | Example: Cannabis - Microbusiness License |         0   |                                                                                                                                                                                                                                                                                                                                                 |
| HarvesterCity          | string  |         | City where the harvester facility is located.                                                      | Example: SOUTH LAKE TAHOE                 |         0.1 | Missing values present. Consider imputation or flagging for records without a city.                                                                                                                                                                                                                                                             |
| HarvesterZipCode       | numeric |         | Zip code of the harvester facility.                                                                | Range: [4000.0, 961503674.0]              |         5.5 | Missing values present. The upper range value (961503674.0) appears to be an invalid zip code format, suggesting potential data entry errors or concatenated values. Recommend validating against standard 5-digit or 9-digit zip code formats and correcting or flagging anomalies.                                                            |
| HarvesterCounty        | string  |         | County where the harvester facility is located.                                                    | Example: EL DORADO                        |         0.1 | Missing values present. Consider imputation or flagging for records without a county.                                                                                                                                                                                                                                                           |
| Year                   | integer |         | Year of the harvest record.                                                                        | Range: [2023.0, 2024.0]                   |         0   |                                                                                                                                                                                                                                                                                                                                                 |
| TotalHarvestPounds     | numeric | pounds  | Total dry weight of harvested cannabis in pounds.                                                  | Range: [-380.53733377132, 785406.9175]    |         0   | Contains negative values. These are physically impossible for harvest quantities and likely represent data entry errors, returns, or adjustments not properly recorded. Recommend flagging these records and treating negative values as zero for aggregate analysis, or excluding them if the context requires strictly positive harvest data. |
| TotalHarvestWetPounds  | numeric | pounds  | Total wet weight of harvested cannabis in pounds.                                                  | Range: [0.75, 4440808.26822343]           |         0   |                                                                                                                                                                                                                                                                                                                                                 |
| UniqueHarvestBatches   | integer | batches | Number of unique harvest batches recorded.                                                         | Range: [1.0, 1360.0]                      |         0   |                                                                                                                                                                                                                                                                                                                                                 |


### Data Quality & Anomalies Section

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry errors, misinterpretation of returns/adjustments, or system glitches allowing negative quantities to be recorded. Physically, a harvest quantity cannot be negative.
    *   **Recommended handling rule:** Flag records where `TotalHarvestPounds` is negative. For analytical purposes, these values should be treated as zero or excluded, depending on the specific analysis. Further investigation into the source system or business rules for returns/adjustments is recommended.
*   **Issue:** Anomalously large `HarvesterZipCode` values.
    *   **Likely cause:** Data entry errors, concatenation of multiple numbers, or incorrect data type mapping during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Flag zip codes that exceed the standard 5 or 9-digit format. Attempt to parse or correct these values if a clear pattern for error is identified (e.g., leading zeros removed, concatenated values). Otherwise, treat as invalid or missing.
*   **Issue:** Missing values in `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty`.
    *   **Likely cause:** Incomplete data entry during registration or reporting.
    *   **Recommended handling rule:** Flag records with missing geographical information. For analysis requiring complete location data, these records may need to be excluded or imputed if a reliable method (e.g., using other known location data for the license) is available.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Quantities:** Identify all records where `TotalHarvestPounds` is less than zero. Create a new flag column, `is_negative_harvest_pounds`, set to `TRUE` for these records. For subsequent analysis, replace negative `TotalHarvestPounds` values with `0`.
2.  **Validate Zip Codes:** For `HarvesterZipCode`, convert to string format and identify values that do not conform to 5-digit or 9-digit (e.g., 'XXXXX-XXXX') US zip code patterns. Create a flag column, `is_invalid_zip_code`, for these records. Consider setting non-conforming zip codes to `NULL` for consistency.
3.  **Handle Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, identify records with missing values. Create flag columns, `is_missing_city` and `is_missing_county`, respectively. These records should be noted for potential bias in location-based analyses.

### Limitations & Trust Section

*   **Negative `TotalHarvestPounds`:** The presence of negative harvest quantities significantly impacts the reliability of total harvest volume calculations. Without clarification from the data source, these values are untrustworthy for direct summation and require specific handling. Validation is needed to understand the business logic behind such entries.
*   **Invalid `HarvesterZipCode`:** The range of `HarvesterZipCode` suggests potential data quality issues beyond simple missingness. The extremely large values indicate a need for external validation against a comprehensive list of valid zip codes or direct consultation with the data source to understand the input format.
*   **Missing Geographical Data:** The small percentage of missing `HarvesterCity` and `HarvesterCounty` values could lead to minor inaccuracies in geographically segmented analyses. Validation would involve cross-referencing with other license information or external geographical databases.

### Appendix: Quick Reference

*   **Negative Harvest Pounds:** Treat as `0` for aggregate analysis; flag original values for investigation.
*   **Invalid Zip Codes:** Flag non-standard zip codes; consider nullifying or correcting based on validation.
*   **Missing City/County:** Flag records with missing geographical data; exclude from location-specific analyses if imputation is not feasible.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for pattern matching before any numeric operations.
*   **Primary Key:** `HarvesterLicenseNumber` and `Year` form the composite primary key for unique identification of harvest records.
*   **Data Type Consistency:** Ensure `HarvesterZipCode` is handled as a string for pattern matching before any numeric operations.
*   **Primary Key:** `HarvesterLicenseNumber` and `Year` form the composite primary key for unique identification of harvest records.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies, especially concerning the negative `TotalHarvestPounds` and the anomalous `HarvesterZipCode` values. Confirmation of the primary key assumption (`HarvesterLicenseNumber`, `Year`) is also crucial. Additionally, any insights into the business context that might explain the observed data quality issues would be highly valuable for refining the cleaning plan and enhancing data trust.

# Work Documentation

## Table: harvestqty23-24

**Data Operations:**
The `harvestqty23-24` dataset was integrated with other harvest quantity files (`harvestqty19-24.csv` and `harvestqty25.csv`) to create a comprehensive `harvest_df`. This combined dataset was then saved as `Data/Track and Trace Data/Harvest/harvest.csv`. Subsequent operations were performed on this consolidated `harvest_df`.

The following transformations were applied:
*   **Column Renaming:** Original column names were standardized to lowercase (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` to `year`, `TotalHarvestPounds` to `totalharvestpounds`).
*   **Data Type Conversion:** The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric data types, with any conversion errors resulting in missing values.
*   **Geographical Data Normalization:** The `harvestercounty` column underwent extensive cleaning. This involved replacing "NA" and "UNDEFINED" strings with empty strings, standardizing various county name formats (e.g., "Alameda County") to a consistent uppercase format (e.g., "ALAMEDA") using a predefined mapping, stripping leading/trailing whitespace, and removing " County" suffixes (case-insensitively).
*   **Missing Value Handling:** Rows with missing values in `harvestercounty` were dropped at multiple stages of the cleaning process to ensure data completeness for geographical analysis.
*   **Data Merging:** The processed `harvest_df` was left-merged with a `package_df` (derived from `packageqty` files, which also underwent similar cleaning) using `harvesterlicensenumber` and `year` as keys.
*   **County Resolution Post-Merge:** A unified `harvestercounty` column was established in the merged dataset. Values from the harvest data (`harvestercounty_harv`) were prioritized, falling back to package data (`harvestercounty_pkg`) if harvest data was missing.
*   **Ratio Calculation:** Several new analytical variables were computed:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds` (this variable's specific use in aggregation suggests it might represent a share within a category).
*   **Aggregation:** The merged data was aggregated at two distinct levels:
    *   **Category-level Summary:** Grouped by `harvestercounty`, `year`, and `itemcategory` to sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`.
    *   **County-level Summary:** Grouped by `harvestercounty` and `year` to sum `totalpackagepounds` and calculate the `package_to_harvest_ratio`.
*   **Output Generation:** The county-level summary was exported to an Excel file named `Data/Results/harvest_package_ratios.xlsx`.
*   **Visualization Preparation:** The county-level summary was utilized to identify the top 10 counties based on total harvest pounds. Time-series bar plots were then generated to visualize trends in total harvest pounds, total package pounds, and package-to-harvest ratios for these top counties across different years.

**Variables Affected:**
*   **Renamed:** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype`), `HarvesterCity` (to `harvestercity`), `HarvesterZipCode` (to `harvesterzipcode`), `HarvesterCounty` (to `harvestercounty`), `PkgYear` (to `year`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches`).
*   **Modified/Cleaned:** `year` (converted to numeric), `totalharvestpounds` (converted to numeric), `totalharvestwetpounds` (converted to numeric), `harvestercounty` (normalized, missing values handled, unified post-merge).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Aggregated:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (in `category_summary` and `county_summary`).

**Logic and Methodology:**
The core methodology involved consolidating harvest data from various periods, standardizing key identifiers, and enriching it by integrating package data. The intent was to create a robust dataset suitable for analyzing the flow of cannabis from harvest to packaging. Standardization of column names and data types ensured consistency, while extensive geographical data normalization addressed inconsistencies critical for location-based analysis. Merging with package data enabled the calculation of efficiency metrics like package-to-harvest and dry-to-wet ratios. Aggregations at both category and county levels were performed to facilitate macro-level insights into market dynamics and regional performance. The iterative cleaning of geographical data, including dropping rows with missing values, indicates a preference for complete and accurate location information in the final analytical outputs.

**Validation and Verification:**
*   Data type conversions for numeric fields (`year`, `totalharvestpounds`, `totalharvestwetpounds`) used an `errors="coerce"` argument, which automatically converted unparseable values to `NaN`, implicitly flagging data quality issues.
*   Explicit dropping of rows with missing `harvestercounty` values at multiple stages served as a form of data validation, ensuring that subsequent analyses are based on records with complete geographical information.
*   The calculation of ratios (`package_to_harvest_ratio`, `dry_to_wet_ratio`) implicitly relies on non-zero denominators, which would highlight potential issues if division by zero occurred (though not explicitly handled in the provided snippets).
*   The final visualization steps, which plot aggregated data for top counties, provide a high-level visual verification of the processed data's trends and distributions.

**Results and Outcomes:**
The data work resulted in a consolidated and cleaned dataset of cannabis harvest and package quantities. Key outcomes include:
*   A unified `harvest.csv` file, combining harvest data from 2019-2025.
*   Standardized and cleaned geographical information, particularly for `harvestercounty`, enhancing the reliability of location-based analyses.
*   A merged dataset (`merged`) that links harvest and package records, enriched with calculated ratios providing insights into processing efficiency.
*   Aggregated summary tables at both category and county levels, offering a structured view of harvest and package volumes and their interrelationships.
*   An Excel export (`harvest_package_ratios.xlsx`) containing county-level summaries, ready for further reporting.
*   A series of visualizations depicting trends in harvest pounds, package pounds, and package-to-harvest ratios for the top 10 counties, facilitating quick insights into regional performance.






# Table: harvestqty25

### Overview Section

This dataset provides a summary of harvest quantities within the Track & Trace system, focusing on cannabis cultivation and processing. It details harvest metrics such as total pounds, wet pounds, and unique batches, associated with specific licensed harvesters for a given year. Each row in the `harvestqty25` table represents an aggregated summary of harvest activities for a particular harvester license within the specified packaging year. The overall data source is the Track & Trace system, with data extracted for the year 2025. The exact collection period and extraction date are not specified in the provided metadata.

**Assumptions:**
*   The `PkgYear` field accurately reflects the year of packaging or harvest aggregation.
*   `TotalHarvestPounds` refers to dried, processed cannabis weight.
*   `TotalHarvestWetPounds` refers to the initial, undried weight of harvested cannabis.

### Table Inventory

*   **harvestqty25:** This table summarizes harvest quantities and batch counts for licensed harvesters in the year 2025.

### Table: harvestqty25

*   **Purpose:** To provide an aggregated view of harvest output, including total dry and wet weights, and the number of unique harvest batches, associated with individual licensed harvesters for the year 2025.
*   **What one row represents:** An aggregated summary of harvest activities for a specific harvester license within the year 2025.
*   **Primary key(s):** HarvesterLicenseNumber, PkgYear (inferred composite key)
*   **Relationships:** None explicitly known.
*   **Number of rows and columns:** 2717 rows, 9 columns

*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                     | Allowed Values / Range                    |   Missing % | Cleaning / Notes                                                                                                                                                       |
|:-----------------------|:--------|:--------|:----------------------------------------------------------------|:------------------------------------------|------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique identifier for the licensed cannabis harvester.          | Example: C12-0000002-LIC                  |         0   |                                                                                                                                                                        |
| HarvesterFacilityType  | object  |         | Type of facility associated with the harvester license.         | Example: Cannabis - Microbusiness License |         0   |                                                                                                                                                                        |
| HarvesterCity          | object  |         | City where the harvester facility is located.                   | Example: SOUTH LAKE TAHOE                 |         0.1 | Small percentage of missing values; consider imputation or flagging if critical for location-based analysis.                                                           |
| HarvesterZipCode       | float64 |         | Zip code of the harvester facility.                             | Range: [89019.0, 960679768.0]             |         3.1 | Contains an anomalous maximum value (960679768.0) which is not a valid US zip code format. This indicates data entry error or corruption. Missing values also present. |
| HarvesterCounty        | object  |         | County where the harvester facility is located.                 | Example: EL DORADO                        |         0   |                                                                                                                                                                        |
| PkgYear                | int64   | Year    | The year in which the harvest was packaged or aggregated.       | Range: [2025.0, 2025.0]                   |         0   | All values are '2025', indicating the dataset is specific to this year.                                                                                                |
| TotalHarvestPounds     | float64 | Pounds  | Total dry weight of harvested cannabis in pounds.               | Range: [0.0022, 282901.024047837]         |         0   | Minimum value is very small (0.0022), which might represent trace amounts or rounding. Review if values close to zero are meaningful or noise.                         |
| TotalHarvestWetPounds  | float64 | Pounds  | Total wet weight of harvested cannabis in pounds.               | Range: [1.4625, 2500998.83340094]         |         0   |                                                                                                                                                                        |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches associated with the harvester. | Range: [1.0, 556.0]                       |         0   |                                                                                                                                                                        |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `harvestqty25` table.

*   **Issue:** Anomalous `HarvesterZipCode` values.
    *   **Likely cause:** Data entry error, system malfunction, or incorrect data type conversion during extraction. The maximum value `960679768.0` is clearly not a valid 5-digit or 9-digit US zip code.
    *   **Recommended handling rule:** Flag invalid zip codes. For analysis requiring valid geographical data, these rows should be excluded or the zip codes imputed if a reliable source (e.g., `HarvesterCity`, `HarvesterCounty`) is available for cross-referencing.
*   **Issue:** Missing `HarvesterCity` values (0.1% missing).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** For analyses dependent on city information, these rows may need to be excluded or the city imputed based on `HarvesterZipCode` (after cleaning) or `HarvesterCounty` if a mapping is available.
*   **Issue:** Missing `HarvesterZipCode` values (3.1% missing).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** Impute missing zip codes based on `HarvesterCity` and `HarvesterCounty` if a reliable lookup table is available. Otherwise, flag these rows and exclude them from analyses requiring complete geographical data.
*   **Issue:** Very small `TotalHarvestPounds` values (minimum 0.0022).
    *   **Likely cause:** Precision issues, rounding, or recording of trace amounts.
    *   **Recommended handling rule:** Evaluate if values below a certain threshold (e.g., 0.01 pounds) should be considered noise and potentially rounded to zero or excluded, depending on the analytical objective.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to string type to handle potential leading zeros and non-numeric representations.
2.  **Validate `HarvesterZipCode`:** Identify and flag `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit US zip code formats. For invalid entries, attempt to correct them using `HarvesterCity` and `HarvesterCounty` as references if a lookup table is available; otherwise, set them to `NULL` or a designated "invalid" value.
3.  **Handle Missing `HarvesterZipCode`:** Impute missing `HarvesterZipCode` values using a lookup based on `HarvesterCity` and `HarvesterCounty` where possible. If imputation is not feasible, flag these rows for potential exclusion in location-sensitive analyses.
4.  **Handle Missing `HarvesterCity`:** Impute missing `HarvesterCity` values using a lookup based on `HarvesterZipCode` (after cleaning) or `HarvesterCounty`. If imputation is not feasible, flag these rows.
5.  **Review `TotalHarvestPounds`:** Analyze the distribution of `TotalHarvestPounds` to determine if a threshold for "trace amounts" is necessary. If values below a certain threshold are deemed insignificant, consider rounding them to zero or excluding them from aggregate calculations.

### Limitations & Trust Section

The reliability of geographical data (`HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`) is impacted by missing values and the identified anomaly in `HarvesterZipCode`. Specifically, the presence of an extremely large, invalid zip code value (`960679768.0`) suggests potential data corruption or significant data entry errors that could affect any analysis relying on accurate location information. Validation against an external, authoritative source for zip codes and city/county mappings is needed to ensure the accuracy of these fields. The dataset is limited to `PkgYear` 2025, which restricts temporal analysis to a single year.

### Appendix: Quick Reference

*   **Zip Code Validation:** Flag and potentially nullify `HarvesterZipCode` values that are not valid 5-digit or 9-digit US zip codes.
*   **Missing Geographical Data:** Impute `HarvesterCity` and `HarvesterZipCode` using cross-referencing where possible; otherwise, flag for exclusion in location-dependent analyses.
*   **Data Scope:** All data pertains to `PkgYear` 2025.
*   **Trace Amounts:** Review `TotalHarvestPounds` for values near zero to determine if a minimum threshold for significance is required.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `harvestqty25` and confirm that the proposed handling rules for the `HarvesterZipCode` anomaly and missing geographical data align with project requirements for data integrity and analytical use cases. Specific attention should be paid to the implications of the `PkgYear` being exclusively 2025 for any time-series or comparative analyses.

# Work Documentation

## Table: harvestqty25

**Data Operations:**
The `harvestqty25` dataset, along with `harvestqty19-24.csv` and `harvestqty23-24.csv`, was loaded from CSV files, with all columns initially read as strings to preserve original formatting and prevent default `NaN` conversions. These individual datasets were then concatenated into a single, comprehensive `harvest_df` DataFrame. This combined DataFrame was subsequently saved to `Data/Track and Trace Data/Harvest/harvest.csv` and reloaded for further processing.

Key operations performed on `harvest_df` include:
1.  **Column Renaming:** Original column names (e.g., `HarvesterLicenseNumber`, `PkgYear`, `TotalHarvestPounds`) were standardized to a consistent lowercase snake_case format (e.g., `harvesterlicensenumber`, `year`, `totalharvestpounds`).
2.  **Data Type Conversion:** The `year`, `totalharvestpounds`, and `totalharvestwetpounds` columns were converted to numeric types, with errors coerced to `NaN` to handle non-numeric entries gracefully.
3.  **Geographical Data Cleaning and Normalization (`harvestercounty`):**
    *   Initial string replacements were performed to convert "NA" and "UNDEFINED" values to empty strings.
    *   A comprehensive mapping dictionary was applied to standardize various county name formats (e.g., "Alameda County") to a consistent uppercase format (e.g., "ALAMEDA").
    *   Rows with missing `harvestercounty` values were dropped after initial cleaning.
    *   The `harvestercounty` column was converted to string type, stripped of leading/trailing whitespace, and then any resulting empty strings were converted to `pd.NA`.
    *   A regular expression was used to remove " County" suffixes (case-insensitive) from county names, followed by another whitespace strip.
    *   Finally, rows with any remaining missing `harvestercounty` values were dropped.
4.  **Data Integration:** The processed `harvest_df` was left-merged with a similarly prepared `package_df` (derived from `packageqty` files) on `harvesterlicensenumber` and `year` to create a `merged` DataFrame.
5.  **Consolidating County Information:** In the `merged` DataFrame, a new `harvestercounty` column was created, prioritizing the county information from the harvest data (`harvestercounty_harv`) and falling back to the package data (`harvestercounty_pkg`) if the harvest data was missing.
6.  **Feature Engineering:** Several ratio-based variables were calculated:
    *   `package_to_harvest_ratio`: `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: `totalharvestpounds` divided by `totalharvestwetpounds`.
    *   `category_share`: `totalpackagepounds` divided by `totalharvestpounds` (this appears to be a re-calculation or redundant with `package_to_harvest_ratio`).
7.  **Final Geographical Data Refinement:** The `harvestercounty` column in the `merged` DataFrame underwent further cleaning, replacing empty strings, `<NA>`, and "nan" with `pd.NA`, followed by dropping rows with missing values.
8.  **Aggregation:**
    *   `category_summary`: Aggregated the `merged` data by `harvestercounty`, `year`, and `itemcategory` to sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`. `totalharvestpounds` was taken as the first value within each group.
    *   `county_summary`: Aggregated the `merged` data by `harvestercounty` and `year` to sum `totalpackagepounds` and take the first `totalharvestpounds`. A `package_to_harvest_ratio` was then calculated at this county-year level.
9.  **Output and Visualization:** The `county_summary` DataFrame was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Subsequently, the top 10 counties based on total harvest pounds were identified, and a series of bar plots were generated for each year, visualizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for these top counties.

**Variables Affected:**
*   **Original Columns (renamed):** `HarvesterLicenseNumber` (to `harvesterlicensenumber`), `HarvesterFacilityType` (to `harvesterfacilitytype`), `HarvesterCity` (to `harvestercity`), `HarvesterZipCode` (to `harvesterzipcode`), `HarvesterCounty` (to `harvestercounty`), `PkgYear` (to `year`), `TotalHarvestPounds` (to `totalharvestpounds`), `TotalHarvestWetPounds` (to `totalharvestwetpounds`), `UniqueHarvestBatches` (to `uniqueharvestbatches`).
*   **Transformed Columns:** `year`, `totalharvestpounds`, `totalharvestwetpounds` (data type changed to numeric). `harvestercounty` (values standardized and cleaned).
*   **New Derived Variables:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
The primary intent behind these operations was to consolidate harvest data across multiple years, standardize its format, clean critical geographical information, and then integrate it with packaging data to derive key performance indicators. Reading all initial data as strings ensures consistency and prevents premature type inference issues. Renaming columns to snake_case improves readability and programmatic access. Converting numeric fields allows for calculations. The extensive cleaning and normalization of `harvestercounty` are crucial for accurate geographical analysis, addressing inconsistencies and missing values. Merging with `package_df` enables the calculation of ratios that provide insights into the efficiency of converting harvested material into packaged products. The subsequent aggregations summarize these metrics at different granularities (category and county levels), facilitating high-level analysis and visualization of trends over time and across regions. The visualizations aim to highlight top-performing counties and their trends in harvest, packaging, and conversion ratios.

**Validation and Verification:**
*   Initial loading used `dtype=str` and `keep_default_na=False` to control how data was read, preventing implicit type conversions and `NaN` handling.
*   `errors="coerce"` was used during numeric type conversions for `year`, `totalharvestpounds`, and `totalharvestwetpounds` to identify and handle values that could not be converted.
*   `dropna(subset=["harvestercounty"])` was applied multiple times during the cleaning process to explicitly remove records with unresolvable missing county information, ensuring that subsequent analyses rely on complete geographical data.
*   The `merge` operation used `how="left"` to retain all harvest records and `validate="many_to_one"` (though this was used in a different merge operation, not the harvest-package merge) to ensure expected cardinality.
*   The `county_map` provides a form of data validation by standardizing county names, ensuring consistency.

**Results and Outcomes:**
The data work resulted in a cleaned, integrated dataset (`merged`) containing both harvest and package information, enriched with calculated ratios. This dataset was then used to produce:
*   `harvest_package_ratios.xlsx`: An Excel file summarizing `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` aggregated by `harvestercounty` and `year`.
*   A series of visualizations (bar plots) illustrating `totalharvestpounds`, `totalpackagepounds`, and `package_to_harvest_ratio` for the top 10 counties across different years, providing a clear overview of harvest and packaging trends and efficiency.
The cleaned `harvestercounty` column and the derived ratios are critical for geographical and operational performance analysis within the cannabis cultivation and packaging sector.






# Table: packageqty19-24

### Overview Section

This dataset provides aggregated package quantity information related to the Track & Trace project, likely within the regulated cannabis industry. It summarizes package data from licensed harvesters over several years. Each row in the `packageqty19-24` table represents the total package pounds and unique harvest batches for a specific harvester, item category, and year. The overall data source, collection period, and extraction date are not specified in the provided metadata.

**Assumptions:**
*   The data pertains to the regulated cannabis supply chain, given the "HarvesterLicenseNumber" and "Flower" item category.
*   "Pounds" refers to avoirdupois pounds.

### Table Inventory

*   **packageqty19-24**: Contains aggregated package quantity data from harvesters, categorized by item type and year.

## Table: packageqty19-24

*   **Purpose:** To provide a summary of package quantities processed by harvesters, broken down by item category and year, enabling analysis of production trends and volumes.
*   **What one row represents:** One row represents the aggregated total package pounds and unique harvest batches for a distinct combination of `HarvesterLicenseNumber`, `ItemCategory`, and `PkgYear`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` (composite key, inferred).
*   **Relationships:**
*   **Number of rows and columns:** 43827 rows, 9 columns.
*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                                          | Allowed Values / Range                    |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-----------------------|:--------|:--------|:-------------------------------------------------------------------------------------|:------------------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | string  |         | Unique identifier for the licensed cannabis harvester.                               | Example: C12-0000002-LIC                  |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HarvesterFacilityType  | string  |         | Type of license or facility operated by the harvester (e.g., Microbusiness License). | Example: Cannabis - Microbusiness License |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HarvesterCity          | string  |         | City where the harvester's facility is located.                                      | Example: SOUTH LAKE TAHOE                 |         0.2 | Small percentage of missing values. Consider imputation or flagging.                                                                                                                                                                                                                                                                                                                                                             |
| HarvesterZipCode       | float   |         | Zip code of the harvester's facility.                                                | [4000.0, 961503674.0]                     |         7.7 | High missing percentage. The upper range value (961503674.0) is highly suspicious and likely indicates data entry errors or concatenated values, as it does not conform to standard US zip code formats. Investigate and validate against known zip code patterns; flag or nullify invalid entries. For missing values, consider imputation based on HarvesterCity/HarvesterCounty if a reliable mapping exists, otherwise flag. |
| HarvesterCounty        | string  |         | County where the harvester's facility is located.                                    | Example: EL DORADO                        |         1.7 | Small percentage of missing values. Consider imputation or flagging.                                                                                                                                                                                                                                                                                                                                                             |
| ItemCategory           | string  |         | Category of the cannabis item (e.g., Flower, Edible).                                | Example: Flower                           |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PkgYear                | integer | Year    | Year the package quantity data pertains to.                                          | [2019.0, 2024.0]                          |         0   | Ensure values are within the expected range of years.                                                                                                                                                                                                                                                                                                                                                                            |
| TotalPackagePounds     | float   | Pounds  | Total weight of packages in pounds for the given category, harvester, and year.      | [2.20462442018378e-07, 911433262.960458]  |         0   | The upper range value (911,433,262.96 pounds) is extremely large and highly suspicious, suggesting potential outliers or data entry errors. Investigate values exceeding a reasonable threshold (e.g., 99th percentile + 3*IQR) and consider flagging or capping extreme outliers. Ensure all values are non-negative.                                                                                                           |
| UniqueHarvestBatches   | integer | Count   | Number of unique harvest batches contributing to the total package pounds.           | [1.0, 8875.0]                             |         0   | Ensure values are positive integers.                                                                                                                                                                                                                                                                                                                                                                                             |


### Data Quality & Anomalies Section

*   **Issue:** `HarvesterZipCode` contains values outside of standard US zip code ranges and has a high missing percentage (7.7%).
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or non-standard formatting during data collection.
    *   **Recommended handling rule:** Validate `HarvesterZipCode` against a regex pattern for 5-digit or 5+4 digit US zip codes. Invalid entries should be flagged and potentially nullified. Missing values should be imputed based on `HarvesterCity` or `HarvesterCounty` if a reliable lookup table is available, otherwise flagged as 'Unknown' or left null.
*   **Issue:** `TotalPackagePounds` has an extremely large maximum value (over 900 million pounds).
    *   **Likely cause:** Data entry error, incorrect unit conversion, or an aggregation error during data generation.
    *   **Recommended handling rule:** Identify and investigate extreme outliers. Values significantly exceeding a statistically derived upper bound (e.g., 99th percentile + 3 times the interquartile range) should be flagged for review, potentially capped, or excluded from aggregate calculations if deemed erroneous.
*   **Issue:** Missing values in `HarvesterCity` (0.2%) and `HarvesterCounty` (1.7%).
    *   **Likely cause:** Incomplete data entry.
    *   **Recommended handling rule:** For these relatively small percentages, consider imputing with a placeholder like "Unknown" or "Not Provided" to maintain row integrity, or flag rows for further investigation if location data is critical.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to string type. Validate values against a standard US zip code pattern (e.g., `^\d{5}(-\d{4})?$`). For values that do not match, replace them with `NULL` and flag the row.
2.  **Handle Missing `HarvesterZipCode`:** For `HarvesterZipCode` values that are `NULL` (either originally missing or invalidated in step 1), attempt to impute using a reliable mapping from `HarvesterCity` and `HarvesterCounty` if available. If imputation is not possible, leave as `NULL` and flag the row for missing zip code.
3.  **Address Missing Location Data:** For missing values in `HarvesterCity` and `HarvesterCounty`, impute with the string "Unknown" to ensure consistency and prevent errors in downstream analysis.
4.  **Review `TotalPackagePounds` Outliers:** Identify and flag rows where `TotalPackagePounds` exceeds a statistically determined upper threshold (e.g., 99th percentile + 3*IQR). These flagged rows should be reviewed manually or excluded from analyses sensitive to extreme values.
5.  **Validate `TotalPackagePounds` Non-Negativity:** Ensure all `TotalPackagePounds` values are greater than or equal to zero. If any negative values are found, flag them as erroneous and replace with `NULL` or `0`.
6.  **Validate `UniqueHarvestBatches`:** Ensure all `UniqueHarvestBatches` values are positive integers. If any non-positive or non-integer values are found, flag them as erroneous and replace with `NULL`.

### Limitations & Trust Section

The reliability of geographical analysis based on `HarvesterZipCode` is limited due to the high percentage of missing values and the presence of invalid entries. The extreme upper range observed in `TotalPackagePounds` suggests potential data entry errors or anomalies that could skew aggregate statistics; trust in these maximum values is low without further investigation. The absence of explicit primary key definitions and relationships requires inference, which could lead to incorrect assumptions about data uniqueness and join capabilities. The lack of overall data source, collection period, and extraction date limits the ability to assess data freshness and context.

### Appendix: Quick Reference

*   **Zip Code Validation:** `HarvesterZipCode` values are validated against standard US zip code patterns; invalid entries are nullified.
*   **Missing Zip Codes:** Missing `HarvesterZipCode` values are imputed if possible via city/county, otherwise flagged.
*   **Location Imputation:** Missing `HarvesterCity` and `HarvesterCounty` values are replaced with "Unknown".
*   **Outlier Flagging:** Extreme `TotalPackagePounds` values are flagged for review.
*   **Non-Negative Checks:** `TotalPackagePounds` and `UniqueHarvestBatches` are validated to be non-negative.
*   **Inferred Keys:** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` are assumed to form a unique composite key.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary keys and relationships, as these were not explicitly provided in the source metadata. Particular attention should be paid to the proposed handling rules for `HarvesterZipCode` and `TotalPackagePounds` anomalies, ensuring they align with business requirements and data integrity standards. Additionally, confirmation of the data source, collection period, and extraction date would enhance the completeness and context of this codebook.

# Work Documentation

## Table: packageqty19-24

**Data Operations:**
*   **Data Ingestion and Concatenation:** Multiple CSV files (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`) were read into pandas DataFrames, treating all columns as strings to preserve original formatting. These were then concatenated into a single `package_df` and saved as `package.csv` for consistent access.
*   **Column Renaming:** Original column names (e.g., `HarvesterLicenseNumber`, `PkgYear`) were standardized to lowercase snake_case (e.g., `harvesterlicensenumber`, `year`) for improved readability and consistency.
*   **Data Type Conversion:** The `year` and `totalpackagepounds` columns were converted to numeric data types. Any values that could not be converted were coerced to `NaN` (Not a Number).
*   **Geographical Data Normalization:** The `harvestercounty` column underwent a multi-step cleaning and standardization process:
    *   Specific string values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined mapping (`county_map`) was applied to standardize various county name formats (e.g., "Alameda County" to "ALAMEDA").
    *   Rows with missing `harvestercounty` values were dropped from the DataFrame.
    *   The column was stripped of leading/trailing whitespace, and empty strings were replaced with `pd.NA`.
    *   Further rows with `pd.NA` in `harvestercounty` were dropped to ensure data quality for geographical analysis.
*   **Data Integration (Merge):** The `package_df` was left-merged with a `harvest_df` (which was similarly prepared from harvest quantity files) using `harvesterlicensenumber` and `year` as common keys. This merge enriched the package data with corresponding harvest information.
*   **Post-Merge County Resolution:** After the merge, a new `harvestercounty` column was created in the `merged` DataFrame. This column prioritized the county information from the `harvest_df` (if available) over the `package_df`'s county information, using the `fillna` method.
*   **Ratio Calculation:** Three new analytical columns were computed:
    *   `package_to_harvest_ratio`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`.
    *   `dry_to_wet_ratio`: Calculated as `totalharvestpounds` divided by `totalharvestwetpounds` (from the `harvest_df`).
    *   `category_share`: Calculated as `totalpackagepounds` divided by `totalharvestpounds`. (Note: This calculation is identical to `package_to_harvest_ratio` in the provided script.)
*   **Final County Cleaning on Merged Data:** The `harvestercounty` column in the `merged` DataFrame underwent another round of cleaning, replacing empty strings, `<NA>`, and "nan" with `pd.NA`, followed by dropping rows with any remaining missing values in this column.
*   **Data Aggregation:**
    *   `category_summary`: The `merged` data was grouped by `harvestercounty`, `year`, and `itemcategory`. For each group, `totalpackagepounds` was summed, `package_to_harvest_ratio` was averaged, and `totalharvestpounds` was taken as the first observed value.
    *   `county_summary`: The `merged` data was grouped by `harvestercounty` and `year`. For each group, `totalpackagepounds` was summed, and `totalharvestpounds` was taken as the first observed value. A `package_to_harvest_ratio` was then calculated at this aggregated level (sum of package pounds / sum of harvest pounds).
*   **Export:** The `county_summary` DataFrame, containing aggregated package and harvest ratios by county and year, was exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Original Columns:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `PkgYear`, `TotalPackagePounds`, `UniqueHarvestBatches`.
*   **Renamed Columns:** `harvesterlicensenumber`, `harvesterfacilitytype`, `harvestercity`, `harvesterzipcode`, `harvestercounty`, `itemcategory`, `year`, `totalpackagepounds`, `uniqueharvestbatches`.
*   **Type-Converted Columns:** `year` (to numeric), `totalpackagepounds` (to numeric).
*   **Cleaned/Normalized Columns:** `harvestercounty` (standardized names, missing values handled).
*   **New Columns Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share` (in the `merged` DataFrame).
*   **Aggregated Columns:** `totalpackagepounds` (summed), `totalharvestpounds` (first value), `package_to_harvest_ratio` (mean or re-calculated sum/sum).

**Logic and Methodology:**
The overarching goal of these data operations is to prepare, integrate, and summarize package quantity data with harvest quantity data to facilitate analytical insights into the cannabis supply chain.
1.  **Data Consolidation:** Combining package data from various annual files into a single, comprehensive dataset (`package_df`) ensures a holistic view of package quantities across the entire period of interest.
2.  **Data Standardization:** Renaming columns to a consistent, machine-readable format and converting key metrics (`year`, `totalpackagepounds`) to appropriate numeric types are fundamental steps for enabling accurate and efficient data processing and analysis.
3.  **Geographical Data Quality Assurance:** The extensive cleaning and normalization of the `harvestercounty` column are critical. Inconsistent or missing geographical data can severely hinder spatial analysis. By standardizing names and systematically dropping records with unresolvable missing county information, the integrity of location-based analysis is maintained.
4.  **Data Enrichment and KPI Generation:** Merging package data with harvest data allows for the creation of new, insightful metrics such as `package_to_harvest_ratio` and `dry_to_wet_ratio`. These ratios serve as key performance indicators (KPIs) for evaluating processing efficiency, yield, and the transformation of raw harvested material into packaged products.
5.  **Hierarchical Aggregation:** Aggregating the data at both `category` and `county` levels provides summarized views that are essential for high-level reporting and trend identification. This allows stakeholders to quickly understand production volumes, processing efficiency, and market dynamics across different product types and geographical regions.

**Validation and Verification:**
*   **Data Type Coercion:** The use of `errors="coerce"` during numeric type conversion for `year` and `totalpackagepounds` ensures that the script does not fail due to non-numeric entries. However, this implicitly converts problematic values to `NaN`, which necessitates explicit handling (e.g., dropping or imputing) in subsequent steps if these `NaN`s are not acceptable.
*   **Missing Value Handling:** The script explicitly addresses missing `harvestercounty` values by dropping affected rows at multiple stages of processing. This ensures that analyses relying on county information are performed on complete records.
*   **Merge Strategy:** The `left` merge with `harvest_df` ensures that all records from the `package_df` are retained, even if no matching harvest data is found. The post-merge logic for `harvestercounty` prioritizes the `harvest_df`'s county information, suggesting a preference for its accuracy or completeness.
*   **Implicit Duplicate Handling:** While `pd.concat` does not explicitly drop duplicates, the subsequent aggregation steps (`groupby().agg()`) will correctly sum or average values for identical grouping keys, effectively handling any potential duplicate rows within the aggregated context.

**Results and Outcomes:**
The data processing pipeline yields a robust, cleaned, and integrated dataset suitable for in-depth analysis of cannabis package and harvest quantities.
*   A consolidated `package_df` is created, combining package quantity data from multiple years into a single, unified source.
*   A `merged` DataFrame is generated, which integrates package and harvest information, providing a comprehensive view of the supply chain. This DataFrame is enriched with calculated ratios that offer insights into processing efficiency and yield.
*   Two aggregated summary tables, `category_summary` and `county_summary`, are produced. These tables offer summarized views of package and harvest data by geographical location, year, and item category, facilitating high-level trend analysis.
*   The `county_summary` is exported to `harvest_package_ratios.xlsx`, serving as a primary output for further analytical tasks and visualizations. This output enables stakeholders to monitor production trends, assess processing efficiency, and understand market dynamics across different counties and years.






# Table: packageqty23-24

### Overview Section

This dataset provides aggregated package quantity and harvest batch information for licensed cannabis harvesters within the Track & Trace system. It offers insights into the volume of packaged cannabis products and the diversity of harvest batches associated with individual licensees. Each row in the `packageqty23-24` table represents the aggregated total package pounds and unique harvest batches for a specific harvester, item category, and year. The data is derived from a regulatory Track & Trace system, covering the period from 2023 to 2024. The exact extraction date is not available.

**Assumptions:**
*   Data is aggregated at the `HarvesterLicenseNumber`, `ItemCategory`, and `Year` level.
*   `TotalPackagePounds` represents the cumulative weight of all packages for the given aggregation keys.
*   `UniqueHarvestBatches` counts distinct harvest identifiers associated with the packages.

### Table Inventory

*   **`packageqty23-24`**: Contains aggregated data on total package pounds and unique harvest batches for licensed harvesters in 2023 and 2024.

## Table: packageqty23-24

*   **Purpose:** To provide an overview of the total packaged weight and the number of unique harvest batches associated with individual licensed cannabis harvesters for specific product categories and years.
*   **What one row represents:** One row represents the aggregated total package pounds and unique harvest batches for a specific `HarvesterLicenseNumber`, `ItemCategory`, and `Year`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `Year` (composite key).
*   **Relationships:** `HarvesterLicenseNumber` likely serves as a foreign key linking to a master table of licensed harvesters.
*   **Number of rows and columns:** 11869 rows, 9 columns.
*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                       | Allowed Values / Range                         |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                             |
|:-----------------------|:--------|:--------|:------------------------------------------------------------------|:-----------------------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique identifier for the licensed cannabis harvester.            | Example: C12-0000002-LIC                       |         0   |                                                                                                                                                                                                                                                                                                                                              |
| HarvesterFacilityType  | object  |         | Type of facility or license held by the harvester.                | Example: Cannabis - Microbusiness License      |         0   |                                                                                                                                                                                                                                                                                                                                              |
| HarvesterCity          | object  |         | City where the harvester's licensed facility is located.          | Example: SOUTH LAKE TAHOE                      |         0.1 | Small percentage of missing values. Consider imputation from HarvesterZipCode or HarvesterLicenseNumber if a master facility table is available, or flag for review.                                                                                                                                                                         |
| HarvesterZipCode       | float64 |         | Zip code of the harvester's licensed facility.                    | Range: [4000.0, 961503674.0]. Example: 96150.0 |         5.5 | Significant percentage of missing values. The maximum value (961503674.0) is an anomalous, non-standard zip code, likely a data entry error or concatenation. Values outside of standard 5-digit or 9-digit zip code formats should be flagged or set to null. Imputation from HarvesterCity or HarvesterLicenseNumber should be considered. |
| HarvesterCounty        | object  |         | County where the harvester's licensed facility is located.        | Example: EL DORADO                             |         0.1 | Small percentage of missing values. Consider imputation from HarvesterZipCode or HarvesterLicenseNumber if a master facility table is available, or flag for review.                                                                                                                                                                         |
| ItemCategory           | object  |         | Category of the cannabis product being packaged.                  | Example: Flower                                |         0   |                                                                                                                                                                                                                                                                                                                                              |
| Year                   | int64   |         | Calendar year for which the data is aggregated.                   | Range: [2023.0, 2024.0]                        |         0   |                                                                                                                                                                                                                                                                                                                                              |
| TotalPackagePounds     | float64 | pounds  | Total weight of all packages in pounds for the given aggregation. | Range: [0.0, 819416.794]                       |         0   | Values of 0.0 pounds may indicate no packages or data entry issues. Investigate if 0.0 is a valid state or an anomaly.                                                                                                                                                                                                                       |
| UniqueHarvestBatches   | int64   |         | Number of distinct harvest batches contributing to the packages.  | Range: [1.0, 1110.0]                           |         0   | Values of 0 or null would indicate an anomaly, but the current range starts at 1.0, suggesting all entries have at least one batch.                                                                                                                                                                                                          |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `packageqty23-24` table.

*   **Issue:** Missing `HarvesterCity` and `HarvesterCounty` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For the small percentage (0.1%) of missing values, consider imputation from other geographical identifiers (e.g., `HarvesterZipCode`) if a reliable mapping exists, or from a master facility table using `HarvesterLicenseNumber`. If imputation is not feasible or reliable, these rows should be flagged for review or excluded from analyses requiring complete location data.
*   **Issue:** Missing `HarvesterZipCode` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For the 5.5% missing values, imputation from `HarvesterCity` or `HarvesterCounty` (if available and reliable) or a master facility table is recommended. If imputation is not possible, flag these rows.
*   **Issue:** Anomalous `HarvesterZipCode` values (e.g., `961503674.0`).
    *   **Likely cause:** Data entry error, concatenation of multiple zip codes, or incorrect data type conversion during extraction. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Identify and flag or nullify `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit (ZIP+4) numeric formats. Further investigation may be needed to determine if these can be corrected or if they represent a systemic data entry problem.
*   **Issue:** `TotalPackagePounds` values of 0.0.
    *   **Likely cause:** Could represent periods of no packaging activity, or potentially data entry errors where a non-zero value should have been recorded.
    *   **Recommended handling rule:** Investigate the business context for 0.0 values. If 0.0 is a valid representation of no activity, no specific cleaning is required beyond understanding its meaning. If it indicates an error, these rows should be flagged or excluded from analyses where non-zero package quantities are expected.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to a string type to handle potential leading zeros and non-numeric entries. Identify and flag or nullify entries that do not conform to 5-digit or 9-digit numeric patterns (e.g., using regular expressions).
2.  **Impute Missing Location Data:** For missing `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty`, attempt to impute values using a hierarchical approach. Prioritize imputation from a master facility table using `HarvesterLicenseNumber` if available. Otherwise, use `HarvesterZipCode` to infer `HarvesterCity` and `HarvesterCounty`, or vice-versa, based on a reliable geographical lookup table.
3.  **Flag Imputed Values:** Create new boolean flag columns (e.g., `HarvesterCity_Imputed`, `HarvesterZipCode_Cleaned`) to indicate rows where data was imputed or corrected, allowing for transparency and traceability.
4.  **Review `TotalPackagePounds` = 0:** Analyze rows where `TotalPackagePounds` is 0.0 to understand if these represent legitimate zero activity or potential data errors. Depending on the finding, either document this as a valid state or flag these rows for further investigation or exclusion from specific analyses.

### Limitations & Trust Section

The reliability of geographical data (`HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`) is compromised by missing values and anomalous entries in `HarvesterZipCode`. This limits the ability to perform accurate location-based analyses without significant data cleaning and potential imputation. Validation of these fields would require cross-referencing with an authoritative master list of licensed facilities and their addresses, ideally provided by the regulatory body. Without such a master list, any imputation carries a degree of uncertainty. The interpretation of `TotalPackagePounds` values of 0.0 also requires further business context validation to ensure accurate representation of harvester activity.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Non-standard `HarvesterZipCode` values (e.g., > 5 or 9 digits, non-numeric) are flagged or nullified.
*   **Missing Location Imputation:** Missing `HarvesterCity`, `HarvesterZipCode`, and `HarvesterCounty` are imputed using available geographical data or a master facility list.
*   **Imputation Flags:** New columns are added to explicitly mark imputed or cleaned data points.
*   **Zero Package Pounds:** Rows with `TotalPackagePounds = 0.0` are reviewed for business context; flagged if anomalous.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies, particularly concerning the `HarvesterZipCode` and missing location data. Specific attention should be paid to the assumptions made regarding the aggregation level and the interpretation of `TotalPackagePounds`. Validation against source system documentation or subject matter experts is recommended to ensure the codebook accurately reflects the data's true nature and intended use.

# Work Documentation

## Table: packageqty23-24

**Data Operations:**
The `packageqty23-24` dataset was integrated as part of a broader data consolidation effort. Initially, multiple package quantity datasets, including `packageqty19-24.csv`, `packageqty23-24.csv`, and `packageqty25.csv`, were loaded and concatenated into a single master package dataframe. This consolidated dataset underwent several cleaning and transformation steps. Key columns such as `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, and `UniqueHarvestBatches` were systematically renamed to a consistent lowercase format. Data types for `Year` and `TotalPackagePounds` were converted from string to numeric, with a mechanism to coerce invalid entries to missing values.

A significant portion of the work focused on standardizing and cleaning the `harvestercounty` column. This involved applying a predefined mapping to normalize county names (e.g., converting "X County" to "X"), stripping extraneous whitespace, and replacing various representations of missing data (empty strings, "NA") with standard missing value indicators. Rows where `harvestercounty` remained missing after these initial cleaning steps were subsequently removed.

The cleaned package data was then integrated with a separate harvest dataset through a left merge operation, using `harvesterlicensenumber` and `year` as the common keys. This merge enriched the package data with corresponding harvest information. During this integration, a strategy was implemented to resolve potential discrepancies or missingness in the `harvestercounty` column, prioritizing the county information from the harvest dataset when available, and falling back to the package dataset's value otherwise.

Following the merge, new ratio-based metrics were calculated to provide deeper insights into the relationship between package and harvest quantities. These included `package_to_harvest_ratio` (total package pounds divided by total harvest pounds) and `category_share` (which was calculated identically to `package_to_harvest_ratio`). Further cleaning and dropping of rows with missing `harvestercounty` values were performed on the merged dataset to ensure data integrity for subsequent aggregations.

Finally, the integrated data was aggregated at two distinct levels: a category-level summary (grouped by `harvestercounty`, `year`, and `itemcategory`) and a county-level summary (grouped by `harvestercounty` and `year`). These aggregations involved summing `totalpackagepounds` and calculating the mean or recalculating `package_to_harvest_ratio`. The resulting county-level summary was then exported to an Excel file for further analysis and visualization.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, `UniqueHarvestBatches` were all renamed to their lowercase equivalents. The data types of `Year` and `TotalPackagePounds` were converted to numeric. The values within `HarvesterCounty` were standardized and cleaned, and rows with missing `harvestercounty` were removed.
*   **Created:** New variables `package_to_harvest_ratio` and `category_share` were computed. The `dry_to_wet_ratio` was also created, though it primarily utilized variables from the merged harvest dataset. Aggregated columns such as summed `totalpackagepounds` and mean/recalculated `package_to_harvest_ratio` were generated in the summary tables.
*   **Validated/Filtered:** Rows containing missing or inconsistent `harvestercounty` values were identified and removed at multiple stages of the data processing pipeline.

**Logic and Methodology:**
The overarching objective of the data work was to create a robust and analytically ready dataset by consolidating package quantity information across different years and integrating it with relevant harvest data. The methodology involved a systematic approach to data cleaning, standardization, and transformation. Column renaming ensured consistency and ease of use. Explicit data type conversions, with error handling, were crucial for enabling accurate numerical computations.

The extensive cleaning of the `harvestercounty` variable was a critical step, addressing known data quality issues related to geographical identifiers. This iterative cleaning process, including mapping, stripping, and dropping missing values, aimed to maximize the reliability of location-based analyses. The integration with harvest data through a left merge was fundamental to deriving new, insightful metrics that link packaging output to cultivation input. The conflict resolution strategy for `harvestercounty` during the merge aimed to preserve the most reliable geographical information.

The creation of ratio-based features like `package_to_harvest_ratio` was designed to provide a normalized view of packaging efficiency, allowing for comparisons across different harvesters, categories, and years. The final aggregation steps were performed to summarize these key metrics at meaningful geographical and categorical levels, preparing the data for higher-level reporting, trend analysis, and visualization.

**Validation and Verification:**
Data type conversions included error coercion, which implicitly validates input by converting unparseable values to `NaN`, preventing downstream computational errors. The repeated application of `dropna` on the `harvestercounty` column served as an explicit validation step, ensuring that all records used in subsequent analyses had complete geographical information. While the merge operation for `package_df` did not explicitly use the `validate` argument, the careful handling of `harvestercounty` conflicts post-merge indicates an awareness of potential data integrity issues. The consistency of county names was enforced through a mapping dictionary, providing a form of lookup-based validation.

**Results and Outcomes:**
The data work resulted in a comprehensive and cleaned dataset that combines package quantity and harvest information across multiple years. This integrated dataset is suitable for analyzing trends in packaging activity, assessing the efficiency of converting harvested material into packaged products, and understanding market dynamics at various geographical and categorical levels. Specifically, the creation of `package_to_harvest_ratio` and aggregated summary tables provides valuable metrics for performance evaluation and strategic decision-making. The final export of the county-level summary to an Excel file facilitates direct use in reports and dashboards, enabling stakeholders to easily access and interpret key insights.






# Table: packageqty25

### Overview Section

This dataset provides summarized information related to cannabis packaging quantities within the Track & Trace project. It aggregates data concerning licensed harvesters, their facility types, locations, and the categories and volumes of cannabis items packaged. The dataset aims to offer insights into the distribution of packaged cannabis products across different harvesters and item categories for a specific year.

One row in the `packageqty25` table represents the total packaged pounds and the count of unique harvest batches for a specific harvester, item category, and year.

The overall data source is the Track & Trace system. The collection period and extraction date are not explicitly provided, but the `PkgYear` column indicates the data pertains to the year 2025.

**Assumptions:**
*   The `packageqty25` table name implies a specific aggregation level or version of package quantity data.
*   The `PkgYear` being uniformly '2025' suggests this dataset might be a projection, a specific annual report, or a limited snapshot.

### Table Inventory

*   **packageqty25:** Summarizes packaged cannabis quantities, aggregated by harvester, item category, and year.

## Table: packageqty25

*   **Purpose:** To provide an aggregated view of cannabis packaging activities, detailing total packaged pounds and unique harvest batches per harvester, item category, and year.
*   **What one row represents:** One row represents the total packaged pounds and unique harvest batches associated with a specific harvester (identified by `HarvesterLicenseNumber`), for a particular `ItemCategory`, during the `PkgYear`.
*   **Primary key(s):** `HarvesterLicenseNumber`, `ItemCategory`, `PkgYear` (composite key, inferred)
*   **Relationships:** Not explicitly defined.
*   **Number of rows and columns:** 4125 rows, 9 columns

*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                             | Allowed Values / Range                        |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                            |
|:-----------------------|:--------|:--------|:------------------------------------------------------------------------|:----------------------------------------------|------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique identifier for the cannabis harvester's license.                 | Example: C12-0000002-LIC                      |         0   |                                                                                                                                                                                                                                                                                                             |
| HarvesterFacilityType  | object  |         | Type of facility associated with the harvester's license.               | Example: Cannabis - Microbusiness License     |         0   |                                                                                                                                                                                                                                                                                                             |
| HarvesterCity          | object  |         | City where the harvester's facility is located.                         | Example: SOUTH LAKE TAHOE                     |         0   |                                                                                                                                                                                                                                                                                                             |
| HarvesterZipCode       | float64 |         | Zip code of the harvester's facility.                                   | Range: [89019.0, 960679768.0]                 |         3.2 | Range includes values (e.g., 960679768.0) that are not valid 5-digit or 9-digit US zip codes. These likely represent data entry errors or concatenated values. Proposed handling: Flag invalid zip codes, attempt to correct based on city/county, or set to null if uncorrectable. Convert to string type. |
| HarvesterCounty        | object  |         | County where the harvester's facility is located.                       | Example: EL DORADO                            |         0   |                                                                                                                                                                                                                                                                                                             |
| ItemCategory           | object  |         | Category of the cannabis item (e.g., Flower, Edible).                   | Example: Flower                               |         0   |                                                                                                                                                                                                                                                                                                             |
| PkgYear                | int64   | Year    | Year of packaging.                                                      | Range: [2025.0, 2025.0]                       |         0   | All values are '2025', indicating the dataset may be limited to a specific year or a future projection.                                                                                                                                                                                                     |
| TotalPackagePounds     | float64 | Pounds  | Total weight of packaged cannabis in pounds.                            | Range: [0.0004188786398349, 282901.024047837] |         0   |                                                                                                                                                                                                                                                                                                             |
| UniqueHarvestBatches   | int64   | Count   | Number of unique harvest batches contributing to the packaged quantity. | Range: [1.0, 478.0]                           |         0   |                                                                                                                                                                                                                                                                                                             |


### Data Quality & Anomalies Section

*   **Issue:** Invalid `HarvesterZipCode` values and incorrect data type.
    *   **Likely cause:** Data entry errors, concatenation of multiple zip codes, or incorrect data type conversion (storing zip codes as `float64` instead of string or integer). The presence of values like `960679768.0` strongly suggests data corruption or misinterpretation.
    *   **Recommended handling rule:** Convert `HarvesterZipCode` to a string type. Validate all `HarvesterZipCode` entries against standard 5-digit or 9-digit US zip code formats. For invalid entries, attempt to correct using `HarvesterCity` and `HarvesterCounty` information. If correction is not feasible, set the `HarvesterZipCode` to NULL to indicate missing or unrecoverable data.
*   **Issue:** `PkgYear` contains only a single value (2025).
    *   **Likely cause:** The dataset might be a specific snapshot, a projection, or intentionally limited to a single year's data. It could also indicate an incomplete data extract if broader historical data is expected.
    *   **Recommended handling rule:** Document this limitation and seek clarification on the intended temporal scope of the dataset. No direct cleaning is needed unless the data is confirmed to be incomplete.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode` Data Type:** Convert the `HarvesterZipCode` column from `float64` to a `string` data type to ensure proper handling of leading zeros and non-numeric characters if they were to appear.
2.  **Validate `HarvesterZipCode` Format:** Implement a validation check to identify `HarvesterZipCode` values that do not conform to standard 5-digit or 9-digit US zip code patterns.
3.  **Address Invalid `HarvesterZipCode` Entries:** For any `HarvesterZipCode` identified as invalid, attempt to correct the value by cross-referencing with `HarvesterCity` and `HarvesterCounty` using external geographic data if available. If a valid correction cannot be determined, replace the invalid entry with a NULL value.
4.  **Document `PkgYear` Scope:** Add a metadata flag or note indicating that the `PkgYear` column exclusively contains the value '2025', highlighting the dataset's specific temporal focus.

### Limitations & Trust Section

*   **`HarvesterZipCode` Reliability:** The `HarvesterZipCode` column exhibits significant data quality issues, including an inappropriate `float64` data type and values outside the valid range for US zip codes (e.g., `960679768.0`). This compromises the accuracy of geographic analysis. Validation against a comprehensive list of US zip codes and cross-referencing with `HarvesterCity` and `HarvesterCounty` is critically needed to improve trust in location-based data.
*   **`PkgYear` Temporal Scope:** The `PkgYear` column exclusively containing '2025' limits the dataset's utility for historical trend analysis or multi-year comparisons. Clarification is required to determine if this is a future projection, a specific annual snapshot, or an incomplete data extract.
*   **Lack of Explicit Primary Keys and Relationships:** The absence of explicitly defined primary keys and foreign key relationships within the provided table summary limits the ability to confidently ensure data integrity, prevent duplicate records, and understand how this table relates to other potential tables in the Track & Trace system. This requires inferring keys, which introduces potential for error.

### Appendix: Quick Reference

*   Convert `HarvesterZipCode` to string type.
*   Validate `HarvesterZipCode` against 5-digit and 9-digit US zip code formats.
*   Nullify `HarvesterZipCode` entries that cannot be corrected or are clearly invalid.
*   Acknowledge that `PkgYear` is uniformly '2025' and represents a specific temporal scope.
*   Note the inferred composite primary key for `packageqty25` as (`HarvesterLicenseNumber`, `ItemCategory`, `PkgYear`).

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred primary key for the `packageqty25` table and to confirm the proposed handling rules for the `HarvesterZipCode` anomalies. Additionally, any further context regarding the `PkgYear` (e.g., if this is a projection or a specific annual report) would be valuable for enhancing the dataset's documentation and ensuring its appropriate use. Please also confirm if any relationships to other tables are known.

# Work Documentation

## Table: packageqty25

**Data Operations:**
The data originating from `packageqty25.csv` is integrated into a broader dataset encompassing multiple years of package quantity data. Initially, `packageqty25.csv` is concatenated with `packageqty19-24.csv` and `packageqty23-24.csv` to form a comprehensive `package_df`. This combined dataset is then saved as `package.csv` and reloaded for further processing.

Key transformations include:
1.  **Column Renaming:** Several columns are renamed for consistency, converting PascalCase to snake_case (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`, `PkgYear` (from the original CSV `Year`) to `year`, `TotalPackagePounds` to `totalpackagepounds`). The `HarvesterZipCode` column is read as a string type during initial data loading, addressing the data type anomaly noted in the codebook.
2.  **Data Type Conversion:** The `year` and `totalpackagepounds` columns are converted to numeric data types, with any conversion errors being coerced to missing values.
3.  **Geographic Data Cleaning and Normalization:** The `harvestercounty` column undergoes extensive cleaning. This involves replacing "NA" and "UNDEFINED" values with empty strings, stripping leading/trailing whitespace, and then mapping various county name formats (e.g., "Alameda County") to a standardized uppercase format (e.g., "ALAMEDA") using a predefined mapping. After normalization, any remaining empty strings are converted to `pd.NA`, and rows with missing `harvestercounty` values are removed.
4.  **Data Integration (Merge):** The processed `package_df` is left-merged with a similarly processed `harvest_df` (containing harvest quantity data from multiple years) using `harvesterlicensenumber` and `year` as keys. This merge combines packaging and harvest information for each harvester and year.
5.  **Post-Merge County Resolution:** In the merged dataset, a unified `harvestercounty` column is created, prioritizing the county information from the harvest data (`harvestercounty_harv`) and falling back to the package data (`harvestercounty_pkg`) if the harvest county is missing.
6.  **Ratio Calculation:** New analytical columns are derived: `package_to_harvest_ratio` (total package pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), and `category_share` (which is calculated identically to `package_to_harvest_ratio`).
7.  **Final County Cleaning:** The `harvestercounty` column in the merged dataset undergoes another round of cleaning, replacing empty strings, "NA", and "nan" with `pd.NA`, followed by dropping rows with missing county values.
8.  **Aggregation:** The merged data is aggregated to create `category_summary` (by `harvestercounty`, `year`, `itemcategory`) and `county_summary` (by `harvestercounty`, `year`). These aggregations sum `totalpackagepounds` and calculate the mean `package_to_harvest_ratio`. The `county_summary` is then exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Modified:** `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`), `HarvesterFacilityType` (renamed to `harvesterfacilitytype`), `HarvesterCity` (renamed to `harvestercity`), `HarvesterZipCode` (renamed to `harvesterzipcode`, data type handled as string), `HarvesterCounty` (renamed to `harvestercounty`, values normalized and cleaned), `ItemCategory` (renamed to `itemcategory`), `PkgYear` (from original CSV `Year`, renamed to `year`, converted to numeric), `TotalPackagePounds` (renamed to `totalpackagepounds`, converted to numeric), `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.
*   **Used in Aggregation:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (for mean calculation).

**Logic and Methodology:**
The primary intent of these operations is to prepare a comprehensive dataset for analyzing cannabis packaging and harvest activities across multiple years and geographic regions. By combining `packageqty` data from various years, the project aims to overcome the single-year limitation noted in the codebook for `packageqty25`. Renaming columns standardizes the dataset for easier programmatic access. Converting key metrics to numeric types enables quantitative analysis. The extensive cleaning and normalization of `harvestercounty` are crucial for accurate geographic segmentation and analysis, addressing inconsistencies in the raw data. Merging with harvest data allows for the calculation of important ratios, providing insights into the efficiency and relationship between harvest and packaging volumes. The final aggregations summarize these insights at different granularities (county, year, item category), facilitating higher-level reporting and visualization. The repeated cleaning steps for `harvestercounty` indicate a robust effort to ensure data quality for this critical categorical variable.

**Validation and Verification:**
The code includes several implicit validation steps:
*   **Data Type Handling:** The `HarvesterZipCode` column is explicitly read as a string type (`dtype=str`) during the initial loading of the CSV files. This prevents the `float64` data type issue identified in the codebook, ensuring zip codes are treated as categorical strings rather than numerical values. However, explicit validation of zip code formats (e.g., 5-digit or 9-digit US zip codes) and subsequent correction or nullification of invalid entries, as recommended in the codebook's "Reproducible Cleaning Plan," are not observed in the provided Python snippets.
*   **Data Type Coercion:** `pd.to_numeric(errors="coerce")` handles non-numeric values gracefully by converting them to `NaN`, which can then be identified and managed.
*   **Missing Value Handling:** Explicit `dropna(subset=[...])` calls are used after cleaning and merging steps to remove records where critical identifiers or geographic information (`harvestercounty`) are missing or unrecoverable.
*   **County Normalization:** The use of a `county_map` and subsequent stripping/replacement of empty strings serves as a form of data validation and standardization, ensuring consistency in county names.
*   **Merge Validation:** The `how="left"` merge ensures that all package records are retained, and `suffixes` help identify the origin of columns, which is useful for debugging and understanding data lineage.

**Results and Outcomes:**
The processing results in a cleaned, integrated, and enriched dataset (`merged`) that combines package and harvest quantities over several years. This dataset is then used to generate aggregated summaries (`category_summary` and `county_summary`), which are exported for further analysis and visualization. Specifically, `county_summary` is saved as `harvest_package_ratios.xlsx`, providing county- and year-level insights into total harvest pounds, total package pounds, and the package-to-harvest ratio. This prepared data forms the foundation for subsequent analyses, such as market concentration (HHI) calculations and trend visualizations, as seen in other parts of the provided Python code. The `packageqty25` data, originally a single-year snapshot, is now part of a multi-year, harmonized dataset, significantly expanding its analytical utility.




## Distribution





# Table: Distribution_cleaned

### Overview Section

This dataset provides a comprehensive record of distribution events within the Track & Trace system, detailing the movement of items between various facilities. It is designed to offer insights into supply chain logistics, item categories, and associated quantities and wholesale prices. Each row in the `Distribution_cleaned` table represents a single distribution event or shipment of items from an origin facility to a destination facility. The overall data source is the Track & Trace system, with the collection period and extraction date not explicitly specified in the provided metadata.

**Assumptions:**
*   The `_cleaned` suffix in the table name `Distribution_cleaned` implies that some level of data preprocessing and cleaning has already been performed. However, the specifics of these cleaning steps are not detailed.
*   Quantity values (e.g., `shipped_quantity`, `received_quantity`) are assumed to be in weight-based units (e.g., grams, pounds) given their float data type and typical use in supply chain tracking for bulk goods.
*   Price values are assumed to be in a standard currency unit.

### Table Inventory

*   **Distribution_cleaned:** This table records individual distribution events, tracking items shipped and received between various facilities within the supply chain.

## Table: Distribution_cleaned

*   **Purpose:** To track the movement of items, including their quantities and wholesale prices, between various facilities within the supply chain.
*   **What one row represents:** One distinct distribution event or shipment of a specific item category from an origin facility to a destination facility.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 2,268,507 rows, 14 columns.
*   **Column Dictionary**


| Column Name               | Type    | Units                              | Description                                                 | Allowed Values / Range   |   Missing % | Cleaning / Notes                                                                                                                                                            |
|:--------------------------|:--------|:-----------------------------------|:------------------------------------------------------------|:-------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| origin_facility_type      | object  |                                    | The type of the facility from which items were shipped.     | Example: A-Large Indoor  |           0 |                                                                                                                                                                             |
| origin_city               | object  |                                    | The city where the originating facility is located.         | Example: Cathedral City  |           0 |                                                                                                                                                                             |
| origin_county             | object  |                                    | The county where the originating facility is located.       | Example: Riverside       |           0 |                                                                                                                                                                             |
| destination_facility_type | object  |                                    | The type of the facility to which items were shipped.       | Example: A-Processor     |           0 |                                                                                                                                                                             |
| destination_city          | object  |                                    | The city where the destination facility is located.         | Example: Lancaster       |           0 |                                                                                                                                                                             |
| destination_county        | object  |                                    | The county where the destination facility is located.       | Example: Los Angeles     |           0 |                                                                                                                                                                             |
| item_category             | object  |                                    | The category of the item being distributed.                 | Example: Flower          |           0 |                                                                                                                                                                             |
| item_quantity_type        | object  |                                    | The method or type of quantity measurement for the item.    | Example: WeightBased     |           0 |                                                                                                                                                                             |
| month                     | object  |                                    | The month in which the distribution event occurred.         | Example: December        |           0 |                                                                                                                                                                             |
| year                      | int64   |                                    | The year in which the distribution event occurred.          | [2022.0, 2025.0]         |           0 |                                                                                                                                                                             |
| shipped_quantity          | float64 | weight units (e.g., grams, pounds) | The quantity of items shipped from the origin facility.     | [-100.0, 4198361791.36]  |           0 | Contains negative values, which may indicate returns, adjustments, or data entry errors. Requires investigation and specific handling to ensure accurate quantity tracking. |
| shipped_wholesale_price   | float64 | currency units                     | The wholesale price associated with the shipped quantity.   | [0.0, 144364409.32]      |           0 |                                                                                                                                                                             |
| received_quantity         | float64 | weight units (e.g., grams, pounds) | The quantity of items received at the destination facility. | [0.0, 4198361791.36]     |           0 |                                                                                                                                                                             |
| received_wholesale_price  | float64 | currency units                     | The wholesale price associated with the received quantity.  | [0.0, 144364409.32]      |           0 |                                                                                                                                                                             |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the dataset.

*   **Issue:** Negative values observed in `shipped_quantity`.
*   **Likely cause:** Negative quantities typically do not represent physical shipments. This could be due to:
    *   **Returns or Adjustments:** The system might record returns or inventory adjustments as negative shipments.
    *   **Data Entry Errors:** Incorrect manual input or system glitches.
    *   **Specific Business Logic:** An undocumented business rule that uses negative values for certain types of transactions.
*   **Recommended handling rule:**
    1.  **Flag:** Identify and flag all rows where `shipped_quantity` is negative.
    2.  **Investigate:** Consult with domain experts to understand the true meaning of negative quantities.
    3.  **Conditional Exclusion/Imputation:** If negative values represent invalid data, exclude these rows from analyses involving total quantities. If they represent returns, consider treating them as a separate transaction type or adjusting inventory levels accordingly rather than summing them directly with positive shipments. If imputation is necessary, replace with 0 or a contextually appropriate value after investigation.

### Reproducible Cleaning Plan

1.  **Identify Negative Shipments:** Create a new boolean column, `is_negative_shipment`, in the `Distribution_cleaned` table. This column will be `TRUE` for rows where `shipped_quantity` is less than 0 and `FALSE` otherwise.
2.  **Analyze Negative Shipments:** Perform a preliminary analysis on the flagged rows to understand their frequency, magnitude, and correlation with other columns (e.g., `item_category`, `facility_type`). This step aims to provide context for the anomaly.
3.  **Consult for Business Rules:** Engage with data owners or business stakeholders to clarify the meaning and intended handling of negative `shipped_quantity` values.
4.  **Apply Handling Rule:** Based on the consultation, either filter out these rows for analyses requiring positive quantities, adjust them to zero if they are errors, or process them as returns if that is their intended meaning. For example, if they represent returns, they might be excluded from "total outbound volume" calculations but included in "net movement" calculations.

### Limitations & Trust Section

*   **Undefined Primary Keys and Relationships:** The dataset lacks explicit primary key definitions and relationships between tables (though only one table is provided). This limits the ability to uniquely identify records or integrate this data with other datasets without further investigation.
*   **Ambiguous Units:** While units for quantity and price have been inferred, they are not explicitly stated. This could lead to misinterpretation if the actual units (e.g., grams vs. kilograms, USD vs. CAD) differ from assumptions.
*   **"Cleaned" Status:** The `_cleaned` suffix implies prior data processing, but the specific cleaning steps, transformations, and assumptions made during that process are unknown. This opacity reduces trust in the data's current state without further documentation of the cleaning pipeline.
*   **Negative `shipped_quantity`:** The presence of negative values in `shipped_quantity` indicates an unresolved data quality issue or an undocumented business rule that requires validation to ensure accurate interpretation of distribution volumes.

To validate these elements, it is necessary to:
*   Obtain the full data dictionary from the source system.
*   Consult with the data engineering team or data owners regarding the `_cleaned` process.
*   Clarify business rules for `shipped_quantity` with negative values.

### Appendix: Quick Reference

*   **Negative `shipped_quantity`:** Flag and investigate. Do not sum directly with positive quantities without understanding their meaning (e.g., returns vs. errors).
*   **Units:** Assume `shipped_quantity` and `received_quantity` are in weight units (e.g., grams, pounds) and prices are in currency units, but verify with data owners.
*   **Data Source:** Data originates from the Track & Trace system; specific collection period and extraction date are not provided.
*   **Table `_cleaned` suffix:** Indicates prior processing; details of cleaning steps are not available and should be requested.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of column descriptions and inferred units. Particular attention should be paid to the proposed handling rule for negative `shipped_quantity` values, ensuring it aligns with business requirements and data integrity standards. Additionally, any missing information, such as primary keys, relationships, or the specifics of the `_cleaned` process, should be highlighted for further investigation to ensure the codebook is complete and the data is fully reproducible and trustworthy.

# Work Documentation

## Table: Distribution_cleaned

**Data Operations:**
The `Distribution_cleaned` table, initially loaded from `TransferSummary2.csv`, underwent several cleaning and transformation steps. A new column, `Difference`, was calculated as the difference between `ShippedQuantity` and `ReceivedQuantity`. A comprehensive unit standardization process was applied to `ItemUnitWeight`, `ItemUnitVolume`, `ShippedQuantity`, and `ReceivedQuantity`, converting values to a consistent base unit (e.g., grams for weight, milliliters for volume) based on their respective Unit of Measure (UOM) columns. The results were rounded to two decimal places, and the original UOM columns (`ItemUnitWeightUOM`, `ItemUnitVolumeUOM`, `ShippedUOM`, `ReceivedUOM`) were subsequently removed.

Geographic data for both destination and origin facilities was imputed. Missing values in `DestinationZipCode`, `DestinationCounty`, `DestinationCity`, `OriginZipCode`, `OriginCounty`, and `OriginCity` were filled using a rule-based approach that leveraged existing complete records to infer missing components. Specifically, if two of the three geographic identifiers (city, zip, county) were present, the third was populated from a lookup. A targeted rule also filled missing zip codes if the corresponding city was available.

Rows with incomplete critical information were removed. This included records missing values in `DestinationFacilityType`, `DestinationCity`, `DestinationZipCode`, `DestinationCounty`, `ItemCategory`, `ItemQuantityType`, `OriginZipCode`, or `OriginCounty`. All column names were then standardized to a snake_case format for consistency. Categorical text fields, specifically `origin_city`, `destination_city`, `origin_county`, and `destination_county`, underwent extensive standardization. This involved correcting common misspellings and variations using predefined mapping dictionaries, removing the "County" suffix from county names, and converting all city and county names to title case. Finally, several columns deemed redundant or unnecessary for the current analysis (`item_unit_volume`, `item_unit_weight`, `manifest_count`, `destination_zip_code`, `origin_zip_code`) were dropped. The `month` column, originally text-based, was converted to a numerical representation (1-12).

**Variables Affected:**
*   **Created:**
    *   `Difference`: A numerical column representing the difference between shipped and received quantities.
*   **Modified:**
    *   `ItemUnitWeight`, `ItemUnitVolume`, `ShippedQuantity`, `ReceivedQuantity`: Values were updated to reflect standardized units and rounding.
    *   `DestinationCity`, `DestinationZipCode`, `DestinationCounty`, `OriginCity`, `OriginZipCode`, `OriginCounty`: Missing values were imputed, and categorical text values were standardized (corrected spellings, consistent casing).
    *   All column names: Converted to snake_case.
    *   `month`: Converted from object (text) to numerical (integer).
*   **Removed:**
    *   `ItemUnitWeightUOM`, `ItemUnitVolumeUOM`, `ShippedUOM`, `ReceivedUOM`: Original unit of measure columns.
    *   `item_unit_volume`, `item_unit_weight`, `manifest_count`, `destination_zip_code`, `origin_zip_code`: Columns identified as unnecessary.

**Logic and Methodology:**
The data cleaning and transformation methodology focused on enhancing data consistency, completeness, and usability. Unit conversion was critical to ensure that all quantity and volume measurements were comparable, preventing aggregation errors due to mixed units. The geographic imputation strategy aimed to recover missing location data by leveraging existing, complete records, thereby maximizing the utility of location-based analysis. This hierarchical approach prioritized data integrity by inferring values from the most reliable available information. Filtering out rows with critical missing data ensured that subsequent analyses would be based on sufficiently complete records. Standardization of column names and categorical text values (cities, counties) was performed to improve data readability, facilitate programmatic access, and ensure accurate grouping and aggregation in analytical tasks. The removal of redundant columns streamlined the dataset, reducing its size and complexity, while the conversion of the `month` column to a numerical format enabled proper chronological ordering and time-series analysis.

**Validation and Verification:**
Throughout the data processing, several validation and verification steps were implicitly or explicitly performed. Null value counts were regularly checked (`df.isnull().sum()`, `null_summary`) to monitor the impact of imputation and filtering operations. Descriptive statistics (`df.describe()`, `df.describe(include='object')`) provided insights into the distributions and ranges of numerical and categorical columns, helping to identify anomalies or unexpected changes. Value counts (`df[col].value_counts().head(15)`) were used to inspect the frequency of unique values in categorical fields, which was crucial for identifying and confirming the effectiveness of text standardization. String similarity checks (`difflib.SequenceMatcher`) were employed to detect and guide the correction of similar but not identical categorical entries. Various visualizations, including histograms for the `Difference` column and numerous plots for trends and distributions, served as visual checks to confirm the logical consistency and expected outcomes of the transformations.

**Results and Outcomes:**
As a result of the performed data work, the `Distribution_cleaned` table is significantly more robust and prepared for analysis. The creation of the `Difference` column provides immediate insight into shipment discrepancies. The standardization of quantity and volume units ensures that all measurements are consistent and comparable. Geographic data is more complete and accurate, with fewer missing values and standardized naming conventions, which will improve the reliability of spatial analysis. Column names are uniformly in snake_case, enhancing readability and ease of use for data consumers. Categorical fields like city and county names are cleaned, reducing data entry errors and variations, leading to more precise aggregations. The conversion of the `month` column to a numerical format enables straightforward temporal analysis. Overall, these transformations have improved the data quality, consistency, and analytical readiness of the `Distribution_cleaned` dataset.






# Table: Distribution_source

### Overview Section

This dataset provides a comprehensive record of product distribution events within the Track & Trace project, detailing the movement of items between various facility types. It serves as a critical component for understanding supply chain logistics, inventory flow, and compliance monitoring. Each row in the `Distribution_source` table represents a single distribution event or shipment, documenting the transfer of a specific item category and quantity from an origin facility to a destination facility. The overall data source is the Track & Trace project's operational logs. The collection period spans from 2022 to 2025, based on the `Year` column. The exact data extraction date is not available.

**Assumptions:**
*   The `Distribution_source` table primarily captures outbound shipments or transfers from an origin facility to a destination facility.
*   "Wholesale Price" columns represent the price at the point of shipment or receipt, not necessarily the final retail price.

### Table Inventory

*   **Distribution_source:** Tracks the movement of items between different facility types, including origin and destination details, item specifics, and quantities.

### Table: Distribution_source

*   **Purpose:** To record and track individual distribution events, including details about the origin, destination, item, quantity, and associated wholesale prices for each shipment.
*   **What one row represents:** A single distribution event or shipment of a specific item category from an origin facility to a destination facility.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 3,219,101 rows, 23 columns.
*   **Column Dictionary**


| Column Name             | Type    | Units                       | Description                                                                    | Allowed Values / Range            |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                     |
|:------------------------|:--------|:----------------------------|:-------------------------------------------------------------------------------|:----------------------------------|------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OriginFacilityType      | object  |                             | The type of the facility from which the item was shipped.                      | e.g., A-Large Indoor, A-Processor |         0   |                                                                                                                                                                                                                                                                                      |
| OriginCity              | object  |                             | The city of the originating facility.                                          | e.g., Cathedral City              |         0   |                                                                                                                                                                                                                                                                                      |
| OriginZipCode           | object  |                             | The zip code of the originating facility.                                      | e.g., 92234.0                     |         0.2 | Small percentage of missing values. Consider imputation or flagging if critical for geographic analysis.                                                                                                                                                                             |
| OriginCounty            | object  |                             | The county of the originating facility.                                        | e.g., Riverside County            |        27.3 | Significant percentage of missing values. Investigate the cause of missingness. May require imputation from ZipCode or external data sources, or exclusion from analyses requiring county-level detail.                                                                              |
| DestinationFacilityType | object  |                             | The type of the facility to which the item was shipped.                        | e.g., A-Processor                 |         0   |                                                                                                                                                                                                                                                                                      |
| DestinationCity         | object  |                             | The city of the destination facility.                                          | e.g., Lancaster                   |         0   |                                                                                                                                                                                                                                                                                      |
| DestinationZipCode      | object  |                             | The zip code of the destination facility.                                      | e.g., 93534                       |         0.2 | Small percentage of missing values. Consider imputation or flagging if critical for geographic analysis.                                                                                                                                                                             |
| DestinationCounty       | object  |                             | The county of the destination facility.                                        | e.g., Los Angeles County          |        27.5 | Significant percentage of missing values. Investigate the cause of missingness. May require imputation from ZipCode or external data sources, or exclusion from analyses requiring county-level detail.                                                                              |
| ItemCategory            | object  |                             | The category of the item being distributed.                                    | e.g., Flower                      |         0   |                                                                                                                                                                                                                                                                                      |
| ItemQuantityType        | object  |                             | The type of quantity measurement for the item (e.g., WeightBased, CountBased). | e.g., WeightBased                 |         0   |                                                                                                                                                                                                                                                                                      |
| ItemUnitWeightUOM       | object  |                             | Unit of Measure (UOM) for the item's unit weight.                              | e.g., Grams                       |        18.2 | High percentage of missing values. Investigate if this is expected for items not measured by weight or if it's a data entry issue. Imputation may be challenging without clear rules; consider flagging or excluding records where UOM is critical.                                  |
| ItemUnitVolumeUOM       | object  |                             | Unit of Measure (UOM) for the item's unit volume.                              | e.g., Milliliters                 |        90.7 | Very high percentage of missing values. This suggests that most items are not measured by volume, or volume data is rarely captured. Consider if this column is useful for analysis given its sparsity, or if it should be excluded.                                                 |
| ShippedUOM              | object  |                             | Unit of Measure (UOM) for the total quantity shipped.                          | e.g., Pounds                      |         0   |                                                                                                                                                                                                                                                                                      |
| ReceivedUOM             | object  |                             | Unit of Measure (UOM) for the total quantity received.                         | e.g., Pounds                      |         0   |                                                                                                                                                                                                                                                                                      |
| month                   | object  |                             | The month in which the distribution event occurred.                            | e.g., October                     |         0   |                                                                                                                                                                                                                                                                                      |
| Year                    | int64   |                             | The year in which the distribution event occurred.                             | 2022.0 to 2025.0                  |         0   |                                                                                                                                                                                                                                                                                      |
| ManifestCount           | int64   | count                       | The number of manifests associated with this distribution event.               | 1.0 to 3587.0                     |         0   |                                                                                                                                                                                                                                                                                      |
| ItemUnitWeight          | float64 | Varies by ItemUnitWeightUOM | The weight of a single unit of the item.                                       | 0.0 to 1008056.4                  |         0   | Values of 0.0 may indicate items not measured by weight or data entry issues. Investigate if 0.0 is a valid representation for certain item types.                                                                                                                                   |
| ItemUnitVolume          | float64 | Varies by ItemUnitVolumeUOM | The volume of a single unit of the item.                                       | 0.0 to 190387.0                   |         0   | Values of 0.0 may indicate items not measured by volume or data entry issues. Investigate if 0.0 is a valid representation for certain item types.                                                                                                                                   |
| ShippedQuantity         | float64 | Varies by ShippedUOM        | The total quantity of the item shipped.                                        | -8191.8295 to 269905305.4149      |         0   | Contains negative values. These likely represent returns or adjustments. It is recommended to flag these records for further investigation or to convert them to positive values in a separate 'Returns' column, or exclude them from analyses focused solely on outbound shipments. |
| ShippedWholesalePrice   | float64 | Currency                    | The wholesale price of the total quantity shipped.                             | 0.0 to 144364409.32               |         0   | Values of 0.0 may indicate free samples, internal transfers, or missing price data. Investigate the business context for zero prices.                                                                                                                                                |
| ReceivedQuantity        | float64 | Varies by ReceivedUOM       | The total quantity of the item received at the destination.                    | 0.0 to 269905305.4149             |         0   | Values of 0.0 may indicate discrepancies or data entry issues. Investigate the business context for zero received quantities.                                                                                                                                                        |
| ReceivedWholesalePrice  | float64 | Currency                    | The wholesale price of the total quantity received.                            | 0.0 to 144364409.32               |         0   | Values of 0.0 may indicate free samples, internal transfers, or missing price data. Investigate the business context for zero prices.                                                                                                                                                |


### Data Quality & Anomalies Section

*   **Issue:** Negative values in `ShippedQuantity`.
    *   **Likely cause:** These values likely represent returns, adjustments, or cancellations rather than actual outbound shipments. They could also be data entry errors.
    *   **Recommended handling rule:** Flag records with negative `ShippedQuantity` for separate analysis or exclusion from standard shipment volume calculations. Consider creating a new column, e.g., `IsReturn`, and converting negative values to positive in a `ReturnQuantity` column, or setting `ShippedQuantity` to 0 for these records if the focus is only on positive shipments.

*   **Issue:** High percentage of missing values in `OriginCounty` (27.3%) and `DestinationCounty` (27.5%).
    *   **Likely cause:** Incomplete data entry during facility registration or shipment logging, or the county information was not mandatory for all facilities.
    *   **Recommended handling rule:** For analyses requiring county-level granularity, consider imputing missing values using `OriginZipCode`/`DestinationZipCode` and an external zip-to-county mapping dataset. Alternatively, exclude records with missing county information from such analyses, or flag them as 'Unknown County'.

*   **Issue:** High percentage of missing values in `ItemUnitWeightUOM` (18.2%) and `ItemUnitVolumeUOM` (90.7%).
    *   **Likely cause:** Many items may not be measured by weight or volume, or the unit of measure was not consistently recorded. The very high missing percentage for `ItemUnitVolumeUOM` suggests volume is rarely a primary metric.
    *   **Recommended handling rule:** For `ItemUnitWeightUOM`, investigate if missing values correlate with `ItemQuantityType` (e.g., 'CountBased' items). For `ItemUnitVolumeUOM`, given its high missing rate, consider if the column is sufficiently populated to be useful for analysis; if not, it may be best to exclude it or use it only for specific item categories where volume is relevant.

*   **Issue:** Zero values in `ItemUnitWeight`, `ItemUnitVolume`, `ShippedWholesalePrice`, `ReceivedQuantity`, and `ReceivedWholesalePrice`.
    *   **Likely cause:** These could represent items not measured by weight/volume, free samples, internal transfers with no monetary value, or discrepancies where items were shipped but not officially received (or vice versa).
    *   **Recommended handling rule:** Investigate the business context for each instance of zero values. For `ItemUnitWeight` and `ItemUnitVolume`, cross-reference with `ItemQuantityType` and `ItemCategory`. For prices, determine if zero indicates a non-commercial transaction or missing data. For `ReceivedQuantity`, investigate potential discrepancies between shipped and received. Flag these records for specific handling based on business rules.

### Reproducible Cleaning Plan

1.  **Address Negative Shipped Quantities:** Identify all records where `ShippedQuantity` is negative. Create a new boolean column `IsReturn` set to `True` for these records and `False` otherwise. Convert the negative `ShippedQuantity` values to their absolute positive equivalent in a new `ReturnQuantity` column, or set `ShippedQuantity` to 0 for these records if the analysis focuses solely on outbound shipments.
2.  **Impute Missing County Data:** For `OriginCounty` and `DestinationCounty`, attempt to impute missing values using a reliable external dataset that maps zip codes to counties. If imputation is not feasible or accurate, flag these records as having 'Unknown County' for geographic analyses.
3.  **Handle Missing Unit of Measure (UOM) Data:** For `ItemUnitWeightUOM`, investigate if missing values align with `ItemQuantityType` (e.g., 'CountBased' items might not have a weight UOM). For `ItemUnitVolumeUOM`, given its high missing rate, consider if it's necessary for analysis; if not, it may be excluded or used only for specific, volume-centric item categories.
4.  **Investigate Zero Values:** Systematically review records where `ItemUnitWeight`, `ItemUnitVolume`, `ShippedWholesalePrice`, `ReceivedQuantity`, or `ReceivedWholesalePrice` are zero. Based on business context, determine if these represent valid scenarios (e.g., free samples, non-weight-based items) or data errors, and apply appropriate flags or transformations.
5.  **Standardize Zip Codes:** Ensure `OriginZipCode` and `DestinationZipCode` are consistently formatted (e.g., as 5-digit strings) by removing any decimal points or converting to string type.

### Limitations & Trust Section

*   **Missing County Data:** The high percentage of missing values in `OriginCounty` and `DestinationCounty` (approx. 27%) limits the ability to perform comprehensive county-level geographic analysis without significant imputation efforts. Validation requires cross-referencing with facility master data or external geographic datasets.
*   **Missing Item Unit of Measure Data:** The substantial missingness in `ItemUnitWeightUOM` (18.2%) and `ItemUnitVolumeUOM` (90.7%) impacts the ability to accurately interpret `ItemUnitWeight` and `ItemUnitVolume` for a significant portion of the data. Trust in these specific unit measurements is low without further investigation into the cause of missingness. Validation requires understanding item categorization and standard measurement practices.
*   **Negative Shipped Quantities:** The presence of negative `ShippedQuantity` values indicates that the column may represent more than just outbound shipments (e.g., returns). Without clear documentation, interpreting these values solely as shipments can lead to inaccurate volume calculations. Validation requires business clarification on how returns and adjustments are recorded.
*   **Zero Values in Key Metrics:** The occurrence of zero values in `ItemUnitWeight`, `ItemUnitVolume`, `ShippedWholesalePrice`, `ReceivedQuantity`, and `ReceivedWholesalePrice` requires careful interpretation. These could be valid (e.g., free items, non-measured items) or indicative of missing/erroneous data. Trust in these values is conditional on understanding their specific business context. Validation requires business rule clarification for zero-value scenarios.

### Appendix: Quick Reference

*   **Negative ShippedQuantity:** Flag as `IsReturn=True`; consider converting to positive `ReturnQuantity`.
*   **Missing County Data:** Impute from ZipCode if possible, otherwise flag as 'Unknown County'.
*   **Missing Item UOMs:** Investigate `ItemUnitWeightUOM` for correlation with `ItemQuantityType`; `ItemUnitVolumeUOM` may be too sparse for general use.
*   **Zero Values:** Investigate business context for `ItemUnitWeight`, `ItemUnitVolume`, `ShippedWholesalePrice`, `ReceivedQuantity`, `ReceivedWholesalePrice`.
*   **Zip Code Formatting:** Standardize `OriginZipCode` and `DestinationZipCode` to string format.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the column descriptions and the proposed handling rules for anomalies, particularly concerning the interpretation of negative `ShippedQuantity` and the high percentage of missing county and unit of measure data. Specific attention should be paid to whether the recommended cleaning steps align with business requirements for data usage and reporting, ensuring reproducibility and consistency with the Track & Trace project's objectives.

---

# Work Documentation

## Table: Distribution_source

**Data Operations:**
The data work for the `Distribution_source` table began with initial loading and exploratory data analysis to understand its structure and content. A new column, `difference`, was engineered by calculating the discrepancy between `shipped_quantity` and `received_quantity`. A significant transformation involved standardizing `item_unit_weight`, `item_unit_volume`, `shipped_quantity`, and `received_quantity` by converting their values to a common base unit, based on their respective Unit of Measure (UOM) columns. During this process, any missing values in these numeric columns were treated as zero. Following standardization, the original UOM columns (`item_unit_weight_uom`, `item_unit_volume_uom`, `shipped_uom`, `received_uom`) were removed.

Missing geographic information for both destination (`destination_city`, `destination_zip_code`, `destination_county`) and origin (`origin_city`, `origin_zip_code`, `origin_county`) facilities was addressed through an imputation process. This involved creating internal consistency rules from existing complete records within the dataset to fill in missing components. After imputation attempts, rows that still contained missing values in critical destination-related columns (`destination_facility_type`, `destination_city`, `destination_zip_code`, `destination_county`, `item_category`, `item_quantity_type`) or origin-related columns (`origin_zip_code`, `origin_county`) were removed to ensure data quality.

All column names were standardized to snake_case for consistency. Extensive text cleaning and standardization were performed on `origin_city` and `destination_city` columns to correct typos, variations in capitalization, and abbreviations. Similarly, the "County" suffix was removed from `origin_county` and `destination_county`, and their case was standardized. Several columns, including `item_unit_volume`, `item_unit_weight`, `manifest_count`, `destination_zip_code`, and `origin_zip_code`, were dropped to streamline the dataset. Finally, the `month` column, originally containing month names, was mapped to numerical representations. The cleaned data was then saved as `cleaned.csv`.

Subsequent to cleaning, various descriptive statistics and visualizations were generated. These included analyses of quantity differences, monthly shipment trends, comparisons of shipped versus received quantities by item category, distributions of wholesale prices, and geographic flow patterns between cities and counties.

**Variables Affected:**
*   **Created:** A new column, `difference`, was created to quantify the discrepancy between shipped and received quantities.
*   **Modified:**
    *   `item_unit_weight`, `item_unit_volume`, `shipped_quantity`, and `received_quantity` had their values converted to a standardized unit based on their original UOMs.
    *   `origin_city`, `destination_city`, `origin_county`, and `destination_county` underwent text standardization (e.g., typo correction, case standardization) and had missing values imputed.
    *   The `month` column was converted from textual month names to numerical representations.
    *   All column names were modified to adhere to a snake_case convention.
*   **Removed:** The columns `item_unit_weight_uom`, `item_unit_volume_uom`, `shipped_uom`, `received_uom`, `manifest_count`, `destination_zip_code`, and `origin_zip_code` were removed from the dataset.
*   **Validated/Checked:** Key data elements such as `shipped_quantity`, `received_quantity`, `item_category`, `origin_facility_type`, `destination_facility_type`, `origin_city`, `destination_city`, `origin_zip_code`, `destination_zip_code`, `origin_county`, and `destination_county` were subject to validation and quality checks throughout the cleaning process.

**Logic and Methodology:**
*   **Quantity Difference Calculation:** A straightforward subtraction of `received_quantity` from `shipped_quantity` was performed to create the `difference` column. This metric serves to immediately highlight potential discrepancies, which could indicate losses, gains, or data recording errors in the supply chain.
*   **Unit Standardization:** A custom function was implemented to convert diverse units of measure (e.g., grams, pounds, milliliters) into a single, consistent base unit. This ensures that all quantity and weight/volume measurements are directly comparable, enabling accurate aggregation and analysis regardless of the original unit. Missing UOMs or numeric values were assigned a zero value during conversion, implying either non-applicability or absence of data.
*   **Geographic Imputation:** Missing city, zip code, and county information for both origin and destination facilities was addressed by building a mapping from existing complete records within the dataset. This mapping was then used to infer and fill missing geographic components in other records, assuming internal consistency of geographic identifiers. This method leverages the dataset's own structure to improve data completeness.
*   **Critical Data Row Removal:** Rows with persistent missing values in essential identifying or categorical columns (e.g., facility types, item categories, and core geographic identifiers) were removed. This decision prioritizes the integrity and reliability of the core data for analysis, ensuring that subsequent operations are performed on a dataset with robust foundational information.
*   **Text Standardization:** Fuzzy matching algorithms and predefined replacement dictionaries were utilized to identify and correct common data entry errors, variations in spelling, and inconsistent capitalization in city and county names. This systematic approach ensures uniformity in categorical text data, which is vital for accurate grouping and aggregation in analytical tasks. The "County" suffix was also programmatically removed from county names for a cleaner, standardized representation.
*   **Column Management:** Columns identified as redundant (e.g., original UOMs after conversion), less critical for primary analysis (e.g., `manifest_count`), or superseded by other data (e.g., `zip_code` after county imputation) were systematically dropped. This process streamlines the dataset, reduces computational overhead, and focuses the data on the most relevant attributes.

**Validation and Verification:**
*   Initial data quality was assessed through `df.info()` and `df.describe()` calls, providing insights into data types, non-null counts, and statistical distributions.
*   The `difference` column's descriptive statistics and histogram were explicitly analyzed to understand the distribution of quantity discrepancies, confirming the prevalence of exact matches and identifying outliers.
*   Null value summaries (`df.isnull().sum() / len(df)`) were generated at various stages of the cleaning process to quantitatively track the impact of imputation and row-dropping operations on missing data percentages.
*   `value_counts().head(15)` was employed to inspect the most frequent values in categorical columns, which helped in identifying inconsistencies and verifying the effectiveness of text standardization.
*   Fuzzy matching (`difflib.SequenceMatcher`) was used to programmatically identify and report potential typos and variations in categorical text fields (e.g., city names) prior to applying corrections.
*   A dedicated `check_city_based_fills` function was utilized to report potential conflicts or successful fills during the geographic imputation process, providing an audit trail for the imputation logic.
*   Post-cleaning, the `df.columns` attribute was inspected to confirm the successful conversion to snake_case and the removal of specified columns.
*   A comprehensive suite of visualizations (histograms, bar plots, line plots, heatmaps, box plots, violin plots) was generated to visually inspect data distributions, trends, and relationships. These visual checks served as a critical validation step for the cleaning and transformation outcomes, for example, confirming the impact of unit standardization on quantity comparisons.

**Results and Outcomes:**
*   The `Distribution_source` dataset now features standardized quantity and weight/volume measurements, enabling accurate and consistent comparisons and aggregations across all items and shipments.
*   The completeness of geographic information for both origin and destination facilities has been significantly improved through internal imputation, thereby enhancing the dataset's utility for location-based analyses.
*   Textual inconsistencies, typos, and variations in city and county names have been largely resolved, leading to more reliable categorical groupings and analyses.
*   The dataset's structure has been optimized with consistent snake_case column names and the removal of redundant or less informative columns, resulting in a more streamlined and efficient data model.
*   The newly introduced `difference` column provides immediate and quantifiable insight into discrepancies between shipped and received quantities, facilitating anomaly detection and further investigation into supply chain efficiency.
*   The data is now robustly prepared for advanced analytical tasks, as evidenced by the extensive exploratory data analysis and visualization performed. These analyses have already revealed significant patterns in shipment quantities, pricing, and geographic distribution flows, providing a solid foundation for deeper insights. The cleaned and transformed data has been successfully saved as `cleaned.csv`, ready for subsequent analytical phases.




## Harvest





# Table: harvest

### Overview Section

This dataset provides a summary of cannabis harvest activities within the Track & Trace system. It aggregates information related to licensed harvesters, their locations, and the quantities of cannabis harvested over specific periods. The data aims to offer insights into production volumes and geographical distribution of harvesting operations. Each row in the `harvest` table represents a summarized record of harvest activities, likely aggregated by harvester license and year, providing key metrics such as total harvest pounds and unique batch counts. The overall data source is the Track & Trace system, with specific collection periods and extraction dates not explicitly provided in this summary.

**Assumptions:**
*   Data pertains to the regulated cannabis industry.
*   Units for harvest quantities are in pounds, unless otherwise specified.
*   Geographical information (City, Zip Code, County) refers to the harvester's location.

### Table Inventory

*   **harvest:** Contains aggregated information about cannabis harvesting activities, including harvester details, location, and total harvest quantities.

## Table: harvest

*   **Purpose:** To provide a summarized view of cannabis harvesting operations, detailing quantities harvested and associated harvester information.
*   **What one row represents:** One aggregated harvest record, likely unique per harvester license and a specific time period (e.g., year).
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 37936 rows, 10 columns

*   **Column Dictionary**


| Column Name            | Type    | Units          | Description                                               | Allowed Values / Range                        |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                  |
|:-----------------------|:--------|:---------------|:----------------------------------------------------------|:----------------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  | License Number | Unique identifier for the licensed cannabis harvester.    | Example: C12-0000002-LIC                      |         0   |                                                                                                                                                                                                                                                                                                                                   |
| HarvesterFacilityType  | object  | Facility Type  | Type of facility associated with the harvester's license. | Example: Cannabis - Microbusiness License     |         0   |                                                                                                                                                                                                                                                                                                                                   |
| HarvesterCity          | object  | City Name      | City where the harvester's facility is located.           | Example: SOUTH LAKE TAHOE                     |         0.2 | Minor missing values; consider imputation with 'Unknown' or based on Zip Code/County if available.                                                                                                                                                                                                                                |
| HarvesterZipCode       | float64 | Zip Code       | Zip code of the harvester's facility.                     | Range: [4000.0, 961503674.0]                  |         7.2 | The upper range value (961503674.0) is an invalid US zip code, indicating potential data entry errors or corruption. Values outside the standard 5-digit US zip code range (e.g., 00000-99999) should be flagged or corrected. Missing values can be imputed or flagged.                                                          |
| HarvesterCounty        | object  | County Name    | County where the harvester's facility is located.         | Example: EL DORADO                            |         1   | Minor missing values; consider imputation with 'Unknown' or based on City/Zip Code if available.                                                                                                                                                                                                                                  |
| PkgYear                | float64 | Year           | Year associated with the harvest packaging or record.     | Range: [2019.0, 2025.0]                       |        19.8 | Significant missing values. This column may be redundant with 'Year' or represent a different aspect of the harvest timeline. Investigate relationship with 'Year' column. Missing values may need imputation or rows with missing values may need to be excluded if 'Year' is also missing.                                      |
| TotalHarvestPounds     | float64 | Pounds         | Total weight of harvested cannabis in pounds.             | Range: [-380.53733377132, 911433642.960996]   |         0   | Contains negative values, which are physically impossible for harvest weight. These values likely represent data entry errors, returns, or system anomalies. Negative values should be investigated and potentially set to zero or null, or the entire row flagged for review.                                                    |
| TotalHarvestWetPounds  | float64 | Pounds         | Total wet weight of harvested cannabis in pounds.         | Range: [0.0002204624420183, 1371869133.03903] |         0   | Values are generally positive, which is expected for wet weight. The upper range is very large, suggesting potential outliers or large-scale operations.                                                                                                                                                                          |
| UniqueHarvestBatches   | int64   | Count          | Number of unique harvest batches recorded.                | Range: [1.0, 8875.0]                          |         0   |                                                                                                                                                                                                                                                                                                                                   |
| Year                   | float64 | Year           | Year of the harvest record.                               | Range: [2023.0, 2024.0]                       |        80.2 | Extremely high percentage of missing values. This column's utility is severely limited. Investigate if 'PkgYear' can serve as a primary year indicator or if 'Year' is intended for a different purpose. Consider dropping this column if 'PkgYear' is more reliable and complete, or imputing based on 'PkgYear' if appropriate. |


### Data Quality & Anomalies Section

*   **Issue:** Negative values in `TotalHarvestPounds`.
    *   **Likely cause:** Data entry errors, system glitches, or misinterpretation of return/adjustment entries. Physically, harvest weight cannot be negative.
    *   **Recommended handling rule:** Investigate the source of negative values. For analysis, consider setting negative values to `0` or `NaN` (Not a Number) and flagging the corresponding rows for further review. If these represent adjustments, a separate column for adjustments might be needed.

*   **Issue:** Invalid `HarvesterZipCode` values, specifically the upper range `961503674.0`.
    *   **Likely cause:** Typographical errors during data entry, concatenation of multiple numbers, or incorrect data type conversion. Standard US zip codes are 5 digits.
    *   **Recommended handling rule:** Filter out or correct zip codes that are not 5-digit numeric values. For values outside the standard range, consider setting them to `NaN` or flagging them as invalid. Impute missing or invalid zip codes using `HarvesterCity` or `HarvesterCounty` if possible, or mark as 'Unknown'.

*   **Issue:** High percentage of missing values in `Year` (80.2%) and significant missing values in `PkgYear` (19.8%).
    *   **Likely cause:** Inconsistent data capture, different reporting standards over time, or `Year` being a derived field that was not consistently populated.
    *   **Recommended handling rule:** Prioritize `PkgYear` as the primary year indicator due to its lower missing rate. Investigate the relationship between `PkgYear` and `Year`. If `Year` is largely redundant or unreliably populated, consider dropping it. For missing `PkgYear` values, if `Year` is present and valid, use it for imputation; otherwise, rows with missing year information may need to be excluded from time-series analyses or flagged.

### Reproducible Cleaning Plan

1.  **Address Negative Harvest Pounds:** Identify all records where `TotalHarvestPounds` is less than zero. Set these values to `0` and create a new boolean flag column, `is_harvest_pounds_adjusted`, to indicate rows where this adjustment was made.
2.  **Clean Harvester Zip Codes:** Validate `HarvesterZipCode` values. Convert to integer type. For any zip code that is not a 5-digit number (e.g., values > 99999 or < 10000), set the value to `NaN` and create a flag column, `is_zip_code_invalid`, to mark these records.
3.  **Handle Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, impute missing values with a placeholder string like "UNKNOWN" to ensure consistency and prevent issues with categorical analysis.
4.  **Consolidate Year Information:** Evaluate the `PkgYear` and `Year` columns. If `Year` is predominantly missing and `PkgYear` is more reliable, consider dropping the `Year` column. For remaining missing values in `PkgYear`, if no other reliable year information is available, these rows may need to be excluded from time-based analyses.
5.  **Standardize Data Types:** Ensure all numerical columns (`TotalHarvestPounds`, `TotalHarvestWetPounds`, `UniqueHarvestBatches`, `PkgYear`, `HarvesterZipCode`) are cast to appropriate numeric types (e.g., `float64` or `int64`) after cleaning, and categorical columns (`HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterCounty`) are cast to `category` type for efficiency.

### Limitations & Trust Section

*   **HarvesterZipCode:** The presence of extremely large, invalid zip codes significantly reduces the trustworthiness of this field for precise geographical analysis without extensive cleaning and validation against a known zip code directory.
*   **TotalHarvestPounds:** The existence of negative values indicates potential issues with data capture or reporting logic, requiring careful interpretation of total harvest figures. Without understanding the root cause, aggregated sums may be skewed.
*   **Year Information (PkgYear & Year):** The high percentage of missing values in `Year` and significant missingness in `PkgYear` limits the ability to perform robust time-series analysis or accurately track trends over time. The relationship and intended use of these two year columns are unclear, potentially leading to misinterpretation.
*   **Missing Geographical Data:** While minor, missing `HarvesterCity` and `HarvesterCounty` values can slightly impact geographical distribution analyses. Validation against external geographical data sources would be needed to fully trust these fields.

### Appendix: Quick Reference

*   **Negative Harvest Pounds:** Set to 0; flag rows as `is_harvest_pounds_adjusted`.
*   **Invalid Zip Codes:** Set to `NaN` if not 5-digit numeric; flag rows as `is_zip_code_invalid`.
*   **Missing City/County:** Impute with "UNKNOWN".
*   **Year Column:** Prioritize `PkgYear` due to lower missingness; consider dropping `Year` if redundant.
*   **Data Type Conversion:** Ensure numeric fields are `float64`/`int64` and categorical fields are `category`.
*   **Outlier Check:** Review extremely large values in `TotalHarvestPounds` and `TotalHarvestWetPounds` for plausibility, though no specific anomaly was noted beyond the range.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for anomalies, particularly the treatment of negative `TotalHarvestPounds` and invalid `HarvesterZipCode` values, to ensure they align with business requirements and analytical goals. Special attention should be paid to the decision regarding the `Year` and `PkgYear` columns, confirming that the chosen approach for handling missingness and potential redundancy is appropriate for downstream analysis. Additionally, the inferred units and descriptions for each column should be cross-referenced with domain experts for accuracy.

# Work Documentation

## Table: harvest

**Data Operations:**
The `harvest` table underwent several data operations, including consolidation, cleaning, standardization, integration, feature engineering, and aggregation. Initially, multiple CSV files containing harvest data from different periods (2019-2024, 2023-2024, 2025) were loaded and concatenated into a single comprehensive DataFrame. This combined dataset was then saved to a new CSV file (`Data/Track and Trace Data/Harvest/harvest.csv`) and subsequently re-loaded for further processing.

Column names were standardized by converting them to a consistent lowercase snake_case format (e.g., `HarvesterLicenseNumber` became `harvesterlicensenumber`, `PkgYear` became `year`). Key numerical columns, specifically `year`, `totalharvestpounds`, and `totalharvestwetpounds`, were converted to appropriate numeric data types, with errors coerced to missing values.

Extensive cleaning was performed on the `harvestercounty` column. This involved replacing "NA" and "UNDEFINED" string values with empty strings, followed by a mapping process to standardize various county name representations (e.g., "Alameda County" to "ALAMEDA"). The column values were then stripped of leading/trailing whitespace, and any remaining empty strings or "nan" representations were converted to proper missing values. Rows with unresolved missing `harvestercounty` information were subsequently removed from the dataset.

The cleaned `harvest` data was then integrated with a `package` dataset (which underwent similar cleaning and standardization) using a left merge operation, based on `harvesterlicensenumber` and `year`. This merge enriched the harvest data with related packaging information. Following the merge, new analytical features were engineered, including `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`, to derive insights into the efficiency of cannabis processing. Further cleaning of the `harvestercounty` column was applied to the merged dataset, including replacing empty strings, `<NA>`, and "nan" with missing values, and dropping rows where `harvestercounty` remained missing.

Finally, the integrated data was aggregated at both category and county levels to summarize key metrics. The county-level summary, which included the derived ratios, was exported to an Excel file (`Data/Results/harvest_package_ratios.xlsx`). Visualizations were also generated to explore trends in harvest pounds, package pounds, and package-to-harvest ratios for the top 10 counties over time.

**Variables Affected:**
- `HarvesterLicenseNumber` (renamed to `harvesterlicensenumber`)
- `HarvesterFacilityType` (renamed to `harvesterfacilitytype`)
- `HarvesterCity` (renamed to `harvestercity`)
- `HarvesterZipCode` (renamed to `harvesterzipcode`)
- `HarvesterCounty` (renamed to `harvestercounty`)
- `PkgYear` (renamed to `year`)
- `TotalHarvestPounds` (renamed to `totalharvestpounds`)
- `TotalHarvestWetPounds` (renamed to `totalharvestwetpounds`)
- `UniqueHarvestBatches` (renamed to `uniqueharvestbatches`)
- New derived variables: `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`.

**Logic and Methodology:**
- **Data Consolidation:** Multiple CSV files containing harvest data from different periods were combined to create a comprehensive dataset, ensuring all available records were included for analysis.
- **Standardization:** Column names were standardized to a consistent lowercase snake_case format, improving readability and programmatic access. Data types were enforced for numerical columns to ensure accurate calculations and prevent errors during analysis. The `PkgYear` column was explicitly chosen and renamed to `year`, effectively prioritizing it as the primary year indicator, aligning with the data cleaning plan's recommendation due to its lower missingness compared to the original `Year` column.
- **Geographical Data Cleaning:** The `harvestercounty` column underwent extensive cleaning to correct inconsistencies, standardize naming conventions (e.g., mapping "Alameda County" to "ALAMEDA"), and handle missing values. This involved replacing various representations of missing or undefined values, stripping whitespace, and removing rows with unresolvable missing county information to enhance the reliability of geographical analysis.
- **Data Integration:** The cleaned harvest data was integrated with a `package` dataset using a left merge operation on `harvesterlicensenumber` and `year`. This step was crucial for combining related information from different stages of the cannabis production pipeline, enabling a holistic view.
- **Feature Engineering:** New ratio metrics, such as `package_to_harvest_ratio` (total package pounds divided by total harvest pounds) and `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), were calculated. These ratios provide key performance indicators for understanding the efficiency of converting harvested cannabis into packaged products and the wet-to-dry weight conversion process.
- **Aggregation and Summarization:** The integrated data was aggregated at both category and county levels to summarize key metrics, facilitating higher-level analysis of harvest and package quantities and their relationships.
- **Exploratory Visualization:** Visualizations were generated to explore trends and distributions of harvest and package data, as well as the derived ratios, across top counties and over time. This aids in identifying patterns, outliers, and key insights.

**Validation and Verification:**
- Data type conversions for numerical columns included an `errors="coerce"` argument, which automatically converted unparseable values into `NaN`. This implicitly flagged problematic entries for review, rather than causing the script to fail.
- Explicit `dropna` calls were used on the `harvestercounty` column at multiple stages of cleaning to remove records with unresolvable missing geographical information, serving as a direct validation step to ensure data quality for location-based analysis.
- The `county_map` provided a predefined lookup for standardizing county names, ensuring consistency across the dataset.
- The creation of ratio metrics inherently involved division operations. While explicit checks for division by zero were not observed, the use of numeric data types would result in `inf` or `NaN` values for such cases, which would then be handled by subsequent aggregation or visualization steps.

**Results and Outcomes:**
- A unified and cleaned `harvest` dataset was successfully created, combining data from multiple source files into a single `harvest.csv`.
- The `harvestercounty` column was significantly improved in terms of consistency and completeness, making it more reliable for geographical analysis and reporting.
- Key numerical columns (`year`, `totalharvestpounds`, `totalharvestwetpounds`) were correctly typed, enabling accurate calculations and preventing data type-related errors. The `PkgYear` column was effectively utilized as the primary year indicator, aligning with the recommended data cleaning strategy.
- The `harvest` data was successfully integrated with packaging data, creating a more comprehensive view of the cannabis production pipeline and enabling cross-functional analysis.
- New analytical features (`package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share`) were derived, offering deeper insights into harvest and packaging efficiency and relationships within the cannabis industry.
- Summarized data at county and category levels was generated and exported to `harvest_package_ratios.xlsx`, providing aggregated views suitable for reporting and further in-depth analysis.
- Visualizations were produced to highlight trends in harvest and packaging volumes and ratios across key geographical areas and years, aiding in data exploration, understanding, and communication of findings.




## Package





# Table: package

### Overview Section

This dataset provides information related to the "Track & Trace" project, which aims to monitor and record the movement of specific items or packages through a supply chain. The data primarily focuses on package-level details, including information about the harvester, item category, and package weight. Each row in the `package` table represents a unique package record, detailing its attributes and origin. The overall data source is from the Track & Trace system. Specific collection periods and extraction dates are not provided in the current summary.

**Assumptions:**
*   The `HarvesterLicenseNumber` uniquely identifies a harvester.
*   `TotalPackagePounds` represents the weight of the package in avoirdupois pounds.

### Table Inventory

*   **package:** Contains detailed records for individual packages, including harvester information, item category, and package weight.

## Table: package

*   **Purpose:** To track individual packages, their contents, and associated harvester details within the Track & Trace system.
*   **What one row represents:** One unique package record.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 59821 rows, 10 columns

*   **Column Dictionary**


| Column Name            | Type    | Units   | Description                                                   | Allowed Values / Range                    |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                |
|:-----------------------|:--------|:--------|:--------------------------------------------------------------|:------------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HarvesterLicenseNumber | object  |         | Unique identifier for the harvester's license.                | Example: C12-0000002-LIC                  |         0   |                                                                                                                                                                                                                                                                                                                                                                 |
| HarvesterFacilityType  | object  |         | Type of facility operated by the harvester.                   | Example: Cannabis - Microbusiness License |         0   |                                                                                                                                                                                                                                                                                                                                                                 |
| HarvesterCity          | object  |         | City where the harvester facility is located.                 | Example: SOUTH LAKE TAHOE                 |         0.2 | Missing values present. Consider imputation or flagging if critical for analysis.                                                                                                                                                                                                                                                                               |
| HarvesterZipCode       | float64 |         | Zip code of the harvester facility.                           | Range: [4000.0, 961503674.0]              |         7   | Significant missing values. Data type is float64, suggesting potential issues with leading zeros or non-standard formats. The upper range value (961503674.0) is anomalous for a standard US zip code (typically 5 or 9 digits). Values outside of typical 5-digit or 9-digit zip code formats should be investigated and potentially corrected or flagged.     |
| HarvesterCounty        | object  |         | County where the harvester facility is located.               | Example: EL DORADO                        |         1.3 | Missing values present. Consider imputation or flagging if critical for analysis.                                                                                                                                                                                                                                                                               |
| ItemCategory           | object  |         | Category of the item contained within the package.            | Example: Flower                           |         0   |                                                                                                                                                                                                                                                                                                                                                                 |
| PkgYear                | float64 | year    | Year the package was created or recorded.                     | Range: [2019.0, 2025.0]                   |        19.8 | High percentage of missing values. Data type is float64, which should be converted to integer if representing a year. Missing values need to be addressed, potentially by imputation or exclusion depending on analytical requirements.                                                                                                                         |
| TotalPackagePounds     | float64 | pounds  | Total weight of the package in pounds.                        | Range: [0.0, 911433262.960458]            |         0   | The maximum value (911,433,262.96 pounds) is extremely large and warrants investigation for potential data entry errors or unit conversion issues. Values of 0.0 pounds may represent empty packages or data anomalies.                                                                                                                                         |
| UniqueHarvestBatches   | int64   | count   | Number of unique harvest batches contributing to the package. | Range: [1.0, 8875.0]                      |         0   |                                                                                                                                                                                                                                                                                                                                                                 |
| Year                   | float64 | year    | General year associated with the package record.              | Range: [2023.0, 2024.0]                   |        80.2 | Extremely high percentage of missing values. This column is largely incomplete and may not be suitable for direct analysis without significant imputation or external data sources. Data type is float64, which should be converted to integer if representing a year. Consider if this column is redundant with 'PkgYear' or if it serves a different purpose. |


### Data Quality & Anomalies Section

*   **Issue:** High percentage of missing values in `Year` (80.2%) and `PkgYear` (19.8%).
    *   **Likely cause:** Incomplete data entry, data extraction issues, or the field was not consistently mandatory.
    *   **Recommended handling rule:** For `Year`, due to extreme missingness, consider excluding it from most analyses or using it only where non-missing. For `PkgYear`, impute missing values if a reasonable method (e.g., mode, nearest valid date) can be determined, or flag records with missing values for exclusion in time-series analyses.
*   **Issue:** Anomalous `HarvesterZipCode` values, specifically the maximum value (961503674.0) and float64 data type.
    *   **Likely cause:** Data entry errors, incorrect data type conversion during extraction, or inclusion of non-standard zip code formats.
    *   **Recommended handling rule:** Convert `HarvesterZipCode` to string/object type to preserve leading zeros. Filter out or flag zip codes that do not conform to standard 5-digit or 9-digit (ZIP+4) US formats. Investigate the extremely large values for potential misinterpretation or corruption.
*   **Issue:** Missing values in `HarvesterCity` (0.2%) and `HarvesterCounty` (1.3%).
    *   **Likely cause:** Minor data entry omissions.
    *   **Recommended handling rule:** For `HarvesterCity` and `HarvesterCounty`, consider imputing missing values based on `HarvesterZipCode` (if cleaned) or `HarvesterLicenseNumber` if a consistent mapping exists. Alternatively, flag these records or exclude them from analyses requiring complete geographical information.
*   **Issue:** Extremely large `TotalPackagePounds` value (911,433,262.96 pounds).
    *   **Likely cause:** Data entry error, unit conversion mistake (e.g., grams entered as pounds), or an outlier representing an aggregation rather than a single package.
    *   **Recommended handling rule:** Investigate the source of this extreme outlier. If it's an error, correct it or exclude the record. If it represents a valid, albeit unusual, aggregation, document its meaning and consider winsorization or transformation for statistical analyses to mitigate its impact.

### Reproducible Cleaning Plan

1.  **Standardize `HarvesterZipCode`:** Convert `HarvesterZipCode` to a string data type to preserve leading zeros. Identify and flag or remove entries that do not conform to standard 5-digit or 9-digit US zip code formats, especially the anomalous large values.
2.  **Address Missing Geographical Data:** For `HarvesterCity` and `HarvesterCounty`, attempt to impute missing values using a lookup table based on the cleaned `HarvesterZipCode` or `HarvesterLicenseNumber`. If imputation is not feasible or reliable, flag these records.
3.  **Clean `PkgYear` and `Year`:** Convert `PkgYear` and `Year` to integer data types. For `PkgYear`, impute missing values using a suitable method (e.g., mode, or a derived value if a date column is available). For `Year`, given its high missingness, evaluate its utility; if not critical, consider dropping the column or using it only for records where it is present.
4.  **Investigate `TotalPackagePounds` Outliers:** Review records with `TotalPackagePounds` exceeding a reasonable threshold (e.g., several standard deviations above the mean or a domain-specific maximum). Correct identified data entry errors or flag these records for special handling in analyses.
5.  **Validate `TotalPackagePounds` Zero Values:** Investigate records where `TotalPackagePounds` is 0.0 to determine if these represent empty packages, errors, or specific operational states.

### Limitations & Trust Section

The reliability of the `Year` column is severely compromised due to over 80% missing values, making it unsuitable for most analytical purposes without extensive imputation or external validation. The `HarvesterZipCode` column contains anomalous values and an incorrect data type, requiring significant cleaning to ensure geographical accuracy. The extreme outlier in `TotalPackagePounds` raises concerns about data entry accuracy or unit consistency, necessitating validation against source systems or domain experts. Trust in analyses relying heavily on these specific fields should be tempered until these data quality issues are thoroughly addressed and validated.

### Appendix: Quick Reference

*   **Zip Code Cleaning:** Convert `HarvesterZipCode` to string; validate against 5/9-digit US formats.
*   **Year Imputation:** Impute `PkgYear` missing values; `Year` column has high missingness, use with caution.
*   **Outlier Detection:** Investigate extreme `TotalPackagePounds` values for data entry errors.
*   **Geographical Imputation:** Use `HarvesterZipCode` to impute `HarvesterCity` and `HarvesterCounty` where possible.
*   **Data Type Correction:** Convert `PkgYear` and `Year` from float64 to integer.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions and proposed cleaning rules, particularly for `HarvesterZipCode` and `TotalPackagePounds` where anomalies were identified. Specific attention should be paid to the handling of missing values in `PkgYear` and `Year` to ensure that the proposed approach aligns with analytical objectives. Validation of the assumed units for `TotalPackagePounds` and the interpretation of `PkgYear` vs. `Year` is also crucial.

# Work Documentation

## Table: package

**Data Operations:**
The `package` table data was sourced from multiple CSV files (`packageqty19-24.csv`, `packageqty23-24.csv`, `packageqty25.csv`), which were concatenated into a single dataframe. This combined dataset was then saved as `package.csv` and re-loaded for processing. Initial loading treated all columns as strings to preserve original formats.

Key cleaning and transformation steps included:
*   **Column Renaming:** Original column names were converted to a consistent lowercase snake_case format (e.g., `HarvesterLicenseNumber` to `harvesterlicensenumber`).
*   **Data Type Conversion:** The `Year` and `TotalPackagePounds` columns were converted to numeric data types. Non-numeric values encountered during this conversion were coerced to missing values (NaN).
*   **Geographical Data Normalization:** The `harvestercounty` column underwent a standardization process using a predefined mapping (`county_map`) to ensure consistency in county names.
*   **Missing Value Handling:** Rows with missing values in the `harvestercounty` column were removed from the dataset at multiple stages of processing. Empty strings, "NA", and "nan" values in `harvestercounty` were explicitly replaced with `pd.NA` before dropping rows.
*   **Data Integration:** The `package` data was left-merged with a `harvest_df` (harvest data) using `harvesterlicensenumber` and `year` as keys. This enriched the package records with corresponding harvest information.
*   **Consolidation of Geographical Data:** After merging, the `harvestercounty` column was consolidated, prioritizing the county information from the harvest data if available, otherwise defaulting to the package data's county.
*   **Feature Engineering:** Several new ratio metrics were calculated: `package_to_harvest_ratio` (total package pounds divided by total harvest pounds), `dry_to_wet_ratio` (total harvest pounds divided by total harvest wet pounds), and `category_share` (total package pounds divided by total harvest pounds).
*   **Aggregation:** The processed data was aggregated into two summary tables: `category_summary` (grouped by `harvestercounty`, `year`, and `itemcategory`) and `county_summary` (grouped by `harvestercounty` and `year`). These aggregations involved summing `totalpackagepounds`, taking the first `totalharvestpounds` value, and calculating the mean `package_to_harvest_ratio` for `category_summary`, and summing `totalpackagepounds` and taking the first `totalharvestpounds` for `county_summary` with a re-calculated `package_to_harvest_ratio`.
*   **Export:** The `county_summary` dataframe was exported to an Excel file named `harvest_package_ratios.xlsx`.

**Variables Affected:**
*   **Renamed:** `HarvesterLicenseNumber`, `HarvesterFacilityType`, `HarvesterCity`, `HarvesterZipCode`, `HarvesterCounty`, `ItemCategory`, `Year`, `TotalPackagePounds`, `UniqueHarvestBatches` were all renamed to their lowercase snake_case equivalents.
*   **Data Type Changed:** `year` (from string to numeric), `totalpackagepounds` (from string to numeric).
*   **Modified/Cleaned:** `harvestercounty` (values normalized, missing values handled).
*   **Created:** `package_to_harvest_ratio`, `dry_to_wet_ratio`, `category_share` (new calculated metrics).
*   **Aggregated:** `totalharvestpounds`, `totalpackagepounds`, `package_to_harvest_ratio` (in the `category_summary` and `county_summary` tables).

**Logic and Methodology:**
The data work on the `package` table aimed to consolidate raw package data from various periods, standardize its structure, and integrate it with related harvest information. The initial loading as strings ensured no data loss due to incorrect type inference. Renaming columns provided consistency, while converting `year` and `totalpackagepounds` to numeric types enabled quantitative analysis. The `errors='coerce'` argument in numeric conversions is a pragmatic approach to handle data quality issues by converting problematic entries to `NaN` rather than halting execution.

A significant part of the methodology focused on cleaning and standardizing geographical data (`harvestercounty`) to ensure accurate spatial analysis and consistent aggregation. The repeated dropping of rows with missing county information indicates a strong requirement for complete geographical context for downstream analysis.

Merging with harvest data was crucial for enriching the package records and enabling the calculation of derived metrics like `package_to_harvest_ratio`, which provides insights into the efficiency of converting harvested material into packaged products. The aggregation steps were designed to summarize key metrics at different levels of granularity (county, year, item category), facilitating high-level reporting and trend analysis. The final export of the `county_summary` table makes this aggregated data readily available for further use.

**Validation and Verification:**
*   **Data Type Validation:** Explicit conversion of `year` and `totalpackagepounds` to numeric types, using `errors='coerce'`, serves as a form of validation, identifying and isolating non-conforming entries as `NaN`.
*   **Missing Data Handling:** The repeated use of `dropna(subset=["harvestercounty"])` and replacement of various missing value representations (`""`, "NA", "nan", "<NA>") with `pd.NA` demonstrates a consistent approach to managing and verifying the completeness of critical geographical data.
*   **Lookup-based Standardization:** The application of a `county_map` to `harvestercounty` acts as a lookup-based validation, ensuring that county names conform to a predefined set of standardized values.
*   **Merge Integrity:** While the `validate` argument was not explicitly used in the `package_df` merge, the choice of a left merge implies that all package records are retained, and harvest data is added where a match exists, preserving the primary focus on package information.

**Results and Outcomes:**
The data work resulted in a clean, standardized, and enriched `package` dataset.
*   The `package_df` is now a consolidated source of package information across multiple years, with consistent column names and appropriate data types for `year` and `totalpackagepounds`.
*   The `harvestercounty` column is standardized and free of missing values, enabling reliable geographical analysis.
*   The `merged` dataframe provides a comprehensive view by integrating package details with harvest data, allowing for a more holistic understanding of the supply chain.
*   New analytical features, such as `package_to_harvest_ratio`, `dry_to_wet_ratio`, and `category_share`, are available for deeper insights into operational efficiency and product flow.
*   Two aggregated summary tables (`category_summary` and `county_summary`) are generated, offering pre-computed metrics for high-level analysis and reporting.
*   A final Excel output (`harvest_package_ratios.xlsx`) provides a ready-to-use summary of package-to-harvest ratios by county and year.




## Retail





# Table: sales18

### Overview Section

This dataset, part of the Track & Trace project, provides aggregated sales information for licensed cannabis retailers. It aims to offer insights into sales performance by retailer, item category, and time period. Each row in the `sales18` table represents the aggregated monthly sales data for a specific item category sold by a particular licensed retailer. The overall data source is likely a regulatory or commercial cannabis tracking system, with the collection period inferred to be around 2018 (based on table name `sales18` and `Date` column example "11-2018"). The extraction date is not specified.

**Assumptions:**
*   The `sales18` table contains monthly aggregated sales data.
*   "Track & Trace" refers to a regulatory system for cannabis products.
*   The `Date` column represents the month and year of the sales aggregation.

### Table Inventory

*   **sales18:** Contains aggregated monthly sales data for various item categories by licensed cannabis retailers.

### Table: sales18

*   **Purpose:** To provide a summary of monthly sales performance, broken down by retailer and item category.
*   **What one row represents:** One row represents the total sales and mean price for a specific item category sold by a particular licensed retailer within a given month.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 21 rows, 9 columns
*   **Column Dictionary**


| Column Name           | Type    | Units                | Description                                                                                | Allowed Values / Range                     |   Missing % | Cleaning / Notes                                                                                                                                               |
|:----------------------|:--------|:---------------------|:-------------------------------------------------------------------------------------------|:-------------------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                      | Unique identifier for the licensed cannabis retailer.                                      | Example: C10-0000004-LIC                   |           0 |                                                                                                                                                                |
| RetailerFacilityType  | object  |                      | Type of facility operated by the retailer.                                                 | Example: Cannabis - Retailer License       |           0 |                                                                                                                                                                |
| RetailerCity          | object  |                      | City where the retailer facility is located.                                               | Example: PALM SPRINGS                      |           0 |                                                                                                                                                                |
| RetailerZipCode       | int64   |                      | Zip code of the retailer facility.                                                         | 922624021                                  |           0 | The provided range indicates all observed values are identical (922624021). This may suggest a limited dataset scope or a specific focus on a single zip code. |
| RetailerCounty        | float64 |                      | County where the retailer facility is located.                                             |                                            |         100 | This column is entirely missing (100% missing values). It should be either removed or investigated for potential data source issues.                           |
| ItemCategory          | object  |                      | Category of the cannabis item sold.                                                        | Example: Other Concentrate (weight - each) |           0 |                                                                                                                                                                |
| Date                  | object  |                      | Month and year of the sales aggregation.                                                   | Example: 11-2018                           |           0 | This column is currently an object type. It should be converted to a datetime format for proper temporal analysis.                                             |
| totalsales            | float64 | Currency (e.g., USD) | Total sales amount for the specified item category by the retailer in the given month.     | 29.5 to 47451.82                           |           0 |                                                                                                                                                                |
| meanprice             | float64 | Currency per unit    | Average price per unit for the specified item category by the retailer in the given month. | 11.4811993069528 to 54.6266666666667       |           0 |                                                                                                                                                                |


### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column is 100% missing.
    *   **Likely cause:** Data was either not collected for this field, or it was lost during extraction/processing.
    *   **Recommended handling rule:** Exclude the column from analysis due to complete lack of data. If county-level analysis is critical, investigate original data sources for recovery.
*   **Issue:** `Date` column is of `object` (string) data type.
    *   **Likely cause:** Dates were stored or extracted as strings.
    *   **Recommended handling rule:** Convert to a proper datetime format for accurate temporal sorting and analysis.
*   **Issue:** `RetailerZipCode` shows a single unique value in the provided range, despite being an `int64`.
    *   **Likely cause:** The provided data sample (21 rows) might originate from a single zip code, or the data extraction was limited to a specific geographic area.
    *   **Recommended handling rule:** No immediate cleaning is required, but this observation should be noted when interpreting geographical insights. Verify with a larger dataset if this pattern holds.

### Reproducible Cleaning Plan

1.  **Convert `Date` column to datetime:** Transform the `Date` column from its current `object` type to a standard datetime format (e.g., YYYY-MM-DD, assuming the first day of the month for aggregation). This enables proper time-series analysis.
2.  **Handle `RetailerCounty` column:** Due to 100% missing values, drop the `RetailerCounty` column from the dataset.
3.  **Validate `RetailerZipCode` consistency:** While not requiring cleaning, document the observation that `RetailerZipCode` appears to be uniform across the current dataset. This step ensures awareness of potential data scope limitations.

### Limitations & Trust Section

*   **`RetailerCounty`:** This column is entirely missing, making any county-level analysis impossible with the current dataset. Validation would require accessing the original data source to determine if this information was ever collected or if it can be recovered.
*   **Geographic Scope:** The `RetailerZipCode` showing a single value suggests a potentially limited geographic scope for the provided data. Trust in broader geographic insights should be tempered until a more diverse dataset is available or the sampling methodology is understood.
*   **Data Source & Collection Period:** The exact data source, comprehensive collection period, and extraction date are not explicitly provided. This limits the ability to fully understand the data's provenance and timeliness.

### Appendix: Quick Reference

*   Convert `Date` column to datetime objects.
*   Drop `RetailerCounty` due to 100% missing values.
*   Note `RetailerZipCode` uniformity; investigate if broader geographic representation is needed.
*   Assume `totalsales` and `meanprice` are in currency (e.g., USD).
*   Recognize `sales18` as monthly aggregated data.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `sales18` and confirm that the proposed handling rules for missing data and data type conversions align with project requirements and data governance policies. Particular attention should be paid to the interpretation of `RetailerZipCode`'s uniformity and whether the assumed geographic scope is acceptable. Additionally, any available information regarding the original data source, collection period, and extraction date should be cross-referenced to enhance the overview section.

# Work Documentation

## Table: sales18

**Data Operations:**
The `sales18` dataset was initially loaded as part of a broader collection of annual sales files, ranging from `sales18.csv` to `sales24.csv`. These individual files were concatenated to form a single, comprehensive sales dataframe (`sales_df`) for longitudinal analysis. During this initial loading and concatenation, the `meanprice` and `v1` columns were systematically dropped if present in any of the individual sales files.

Following concatenation, column names were standardized to a consistent lowercase format (e.g., `RetailerLicenseNumber` became `retailerlicensenumber`, `ItemCategory` became `itemcategory`, `Date` became `date`, and `totalsales` became `totalsales`). The combined sales data was then sorted by multiple key identifiers including retailer license number, county, facility type, city, zip code, date, item category, and total sales.

A crucial step involved enriching the sales data by merging it with an external license dataset (`parent_temp`), using `retailerlicensenumber` as the key. This merge introduced `primary_company` and `cannabiz_county` information. Missing values in the `retailercounty` column were addressed through a multi-stage process: first, "NA" and "UNDEFINED" string values were replaced with empty strings; then, attempts were made to populate empty `retailercounty` entries using the `cannabiz_county` from the merged license data. Several specific manual corrections were applied to `retailercounty` for identified retailer license numbers. The `retailercounty` column was further standardized by converting all values to uppercase and by merging with a pre-computed lookup table of `retailerlicensenumber` to `retailercounty` mappings.

To enhance geographic data, a 5-digit zip code (`zip5`) was extracted from `retailerzipcode`. This `zip5` was then used to merge the sales data with an external HUD ZIP-to-County mapping dataset (`zip_df`), allowing for additional imputation or correction of `retailercounty` values. Further manual county corrections were applied for specific retailer license numbers. An `Unnamed: 0` column, likely an artifact of previous processing, was dropped. All remaining columns were converted to string type, and any lingering missing values were filled with empty strings to ensure data consistency.

The extensively cleaned and enriched sales data was saved as an intermediate Stata file (`sales_w_parent_co_test.dta`) and subsequently reloaded for further processing. The `year` was extracted from the `date` column, and both `totalsales` and `year` were converted to numeric data types, with errors coerced to missing values.

The core analytical work involved calculating the Herfindahl-Hirschman Index (HHI) at various levels of aggregation:
1.  Overall statewide HHI based on individual retailer sales.
2.  Statewide HHI based on primary company sales.
3.  County-level HHI based on individual retailer sales.
4.  County-level HHI based on primary company sales.
These HHI calculations involved aggregating total sales by the respective grouping variables (retailer, primary company, county, year), computing market shares, and then squaring these shares to sum them for the HHI. The various HHI results were then combined and merged into a single `merged` dataframe. Additional `opacity` metrics, representing the relative sales contribution of counties, were calculated.

The `merged` dataframe was then used for several analytical and visualization tasks:
*   Data was filtered to years 2019-2025 for specific trend analyses.
*   Counties were clustered based on their HHI trends over time using KMeans.
*   Linear regression was applied to HHI values over time for each county to categorize them into "increasing," "decreasing," or "stable" HHI trajectories.
*   Year-over-year percentage change in HHI was calculated.
*   Top counties with the largest average HHI increases and decreases were identified.
*   A correlation matrix was computed to examine relationships between HHI, total sales, and county sales.
*   Finally, the processed sales data was re-read from the Stata file, and city-level sales were aggregated by date and city to analyze sales trends over time for the top 10 cities.

**Variables Affected:**
*   **Modified:**
    *   `RetailerLicenseNumber`: Renamed to `retailerlicensenumber`.
    *   `RetailerFacilityType`: Renamed to `retailerfacilitytype`.
    *   `RetailerCity`: Renamed to `retailercity`.
    *   `RetailerZipCode`: Renamed to `retailerzipcode`.
    *   `RetailerCounty`: Renamed to `retailercounty`, extensively cleaned, imputed, and standardized (uppercase).
    *   `ItemCategory`: Renamed to `itemcategory`.
    *   `Date`: Renamed to `date`, used to derive `year`.
    *   `totalsales`: Converted to numeric type, used in aggregations.
*   **Dropped:** `meanprice`, `v1`, `_merge` (temporary), `retailercounty_from_license_county` (temporary), `zip5` (temporary after merge), `retailercounty_from_zip` (temporary), `_merge_zip` (temporary), `Unnamed: 0`.
*   **Created:**
    *   `companyid` (from external license data)
    *   `statelicenseid` (from external license data)
    *   `multi_owner` (indicator for multiple company IDs)
    *   `primary_company` (extracted from `companyid` or `retailerlicensenumber`)
    *   `cannabiz_county` (from external license data)
    *   `zip5` (5-digit zip code extracted from `retailerzipcode`)
    *   `year` (extracted from `date`)
    *   `industry_sales` (total sales for a given year/county)
    *   `mkt_share` (market share of a retailer/company)
    *   `mkt_share2` (squared market share for HHI calculation)
    *   `mkt_share2_parent` (squared market share for parent company HHI)
    *   `totalsales_parent` (total sales for parent company)
    *   `county_sales` (total sales at county level)
    *   `county_sales_parent` (total parent company sales at county level)
    *   `opacity`, `opacity_parent` (metrics based on sales contribution)
    *   `cluster` (KMeans cluster assignment for counties)
    *   `hhi_change` (year-over-year percentage change in HHI)

**Logic and Methodology:**
The overarching objective of the data work was to construct a robust dataset for analyzing market concentration within the cannabis retail sector, specifically using the Herfindahl-Hirschman Index (HHI). This involved integrating sales data from multiple years and enriching it with external license and geographic information.

A key methodological decision was to combine annual sales files into a single longitudinal dataset, enabling time-series analysis of market dynamics. Extensive effort was dedicated to cleaning and imputing the `retailercounty` variable, which was initially entirely missing in the `sales18` table. This was achieved by systematically leveraging information from merged license data (which provided `cannabiz_county`), a ZIP-to-county mapping, and targeted manual corrections. This multi-pronged approach was critical to enable county-level market analysis.

To account for complex ownership structures, a `primary_company` identifier was derived, allowing for HHI calculations at both the individual retailer and the aggregated parent company levels. Market share was consistently defined as a retailer's or company's total sales relative to the total industry sales within a specific year and geographic scope (statewide or county). The HHI was then computed by summing the squares of these market shares, providing a quantitative measure of market concentration.

Beyond static HHI calculation, the methodology extended to dynamic analysis. Linear regression was employed to model HHI trends over time for each county, classifying them into categories of "increasing," "decreasing," or "stable" concentration. KMeans clustering was also applied to group counties exhibiting similar HHI trajectories. These analytical steps aimed to provide deeper insights into the evolution of market structure.

Finally, various visualization techniques were utilized to effectively communicate the findings, including line plots for HHI trends, bar plots for market share comparisons, and heatmaps for multi-dimensional views of market concentration.

**Validation and Verification:**
Data quality and consistency were maintained through several validation and verification steps:
*   **Missing Value Handling:** The `retailercounty` column, initially 100% missing, underwent rigorous imputation using multiple external data sources and manual review, with `value_counts(dropna=False)` used to monitor progress.
*   **Data Type Conversions:** Explicit type conversions (e.g., `pd.to_numeric` with `errors="coerce"`) were applied to `totalsales` and `year` to ensure accurate mathematical operations, gracefully handling any non-numeric entries.
*   **Column Renaming and Standardization:** Consistent lowercase column naming was enforced, improving readability and programmatic access.
*   **Merge Indicators:** The `indicator=True` argument in pandas merge operations provided `_merge` columns, which were used to verify the success and type of merges (e.g., `left_only`, `both`, `right_only`), although these temporary columns were subsequently dropped.
*   **Manual Review and Correction:** Specific manual fixes for `retailercounty` were applied based on identified discrepancies, indicating a level of human oversight in data quality.
*   **String Operations:** Extensive use of `astype(str)`, `str.strip()`, and `replace` functions ensured consistent string formatting and handling of empty strings or "NA" values across various text-based columns.
*   **Intermediate Saves:** Saving the processed data to a Stata file (`sales_w_parent_co_test.dta`) served as a checkpoint, allowing for verification of the data state before subsequent analytical steps.

**Results and Outcomes:**
The data work successfully transformed raw annual sales files into a clean, enriched, and analytically ready dataset. Key outcomes include:
*   **Comprehensive Sales Dataset:** A unified sales dataset spanning multiple years was created, providing a robust foundation for longitudinal market analysis.
*   **Populated Geographic Data:** The `retailercounty` column, which was entirely missing in the original `sales18` codebook, was substantially populated and standardized, enabling detailed county-level market concentration analysis.
*   **Market Concentration Metrics:** A comprehensive set of HHI metrics was computed at statewide and county levels, for both individual retailers and their primary companies, offering granular insights into market concentration dynamics over time.
*   **Market Trend Categorization:** Counties were effectively categorized into "increasing," "decreasing," or "stable" HHI trajectories, providing a dynamic understanding of market evolution.
*   **Visualizations and Insights:** A variety of plots and tables were generated, illustrating HHI trends, sales distributions, market share comparisons, and year-over-year changes, which are crucial for understanding competitive landscapes and informing strategic decisions.
*   **Exportable Results:** Key analytical outputs, such as HHI tables and summary statistics, were exported to CSV and Excel formats, making them readily available for reporting and further analysis.






# Table: sales19

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
*   **Column Dictionary**


| Column Name           | Type    | Units             | Description                                                             | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------------|:--------|:------------------|:------------------------------------------------------------------------|:-------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                   | Unique identifier for the retailer's license.                           | Example: C10-0000004-LIC             |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RetailerFacilityType  | object  |                   | Type of facility associated with the retailer license.                  | Example: Cannabis - Retailer License |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RetailerCity          | object  |                   | City where the retailer facility is located.                            | Example: PALM SPRINGS                |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RetailerZipCode       | int64   |                   | Zip code of the retailer facility.                                      | [90019.0, 961610393.0]               |           0 | The upper bound of the range (961610393.0) is highly anomalous for a standard zip code, suggesting potential data entry errors, concatenated values, or incorrect data type interpretation. Needs validation and potential truncation/correction to standard 5 or 9-digit zip codes.                                                                                                                                  |
| RetailerCounty        | float64 |                   | County where the retailer facility is located.                          |                                      |         100 | Entire column is missing. Consider dropping or attempting to impute from RetailerZipCode or RetailerCity if external mapping data is available.                                                                                                                                                                                                                                                                       |
| ItemCategory          | object  |                   | Category of the item sold.                                              | Example: Flower                      |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Date                  | object  |                   | Month and year of the sales data.                                       | Example: 01-2019                     |           0 | Currently stored as an object (string). Convert to a proper datetime format (e.g., YYYY-MM-DD, representing the first day of the month) for accurate time-series analysis.                                                                                                                                                                                                                                            |
| totalsales            | float64 | Currency          | Total sales amount for the given retailer, item category, and date.     | [-75.23, 1013321.09]                 |           0 | Contains negative values. These likely represent returns, refunds, or sales adjustments. For analyses focused on positive revenue, these values should be flagged and potentially treated as zero or excluded. For full financial reconciliation, they should be retained and understood.                                                                                                                             |
| meanprice             | float64 | Currency per unit | Average price per unit for the given retailer, item category, and date. | [-Infinity, Infinity]                |           0 | Contains negative and infinite values. Negative values could stem from negative total sales or calculation errors. Infinite values typically arise from division by zero (e.g., total sales divided by zero units sold). Flag these records for investigation. For analysis, infinite values should be converted to NaN, and negative values should be treated similarly to negative totalsales, or excluded/imputed. |


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






# Table: sales20

### Overview Section

This dataset provides a summary of cannabis sales transactions, likely aggregated monthly, from various licensed retailers. Each row in the `sales20` table represents a summarized sales record for a specific retailer, item category, and month. The data captures key details such as retailer identification, location, item category, total sales value, and mean item price. The overall data source is inferred to be the Track & Trace system, with a collection period likely encompassing at least January 2020, as indicated by the `Date` column. The extraction date is not specified.

**Assumptions:**
*   The `sales20` table contains monthly aggregated sales data.
*   `totalsales` and `meanprice` are expressed in a local currency (e.g., USD).
*   Negative values in `totalsales` and `meanprice` represent returns, adjustments, or data entry errors.
*   Infinite values in `meanprice` are likely due to division by zero.

### Table Inventory

*   **sales20:** Contains aggregated sales data for cannabis products from licensed retailers, including sales figures, item categories, and retailer location details.

## Table: sales20

*   **Purpose:** To track and analyze aggregated sales performance and product distribution across various licensed cannabis retailers.
*   **What one row represents:** One summarized sales record for a specific retailer, item category, and month.
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 169704 rows, 9 columns

*   **Column Dictionary**


| Column Name           | Type    | Units                | Description                                                                    | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------------|:--------|:---------------------|:-------------------------------------------------------------------------------|:-------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                      | Unique identifier for the licensed cannabis retailer.                          | Example: C10-0000122-LIC             |           0 |                                                                                                                                                                                                                                                                                                                                                                                         |
| RetailerFacilityType  | object  |                      | Type of facility operated by the retailer (e.g., Cannabis - Retailer License). | Example: Cannabis - Retailer License |           0 |                                                                                                                                                                                                                                                                                                                                                                                         |
| RetailerCity          | object  |                      | City where the retailer facility is located.                                   | Example: MARINA DL REY               |           0 |                                                                                                                                                                                                                                                                                                                                                                                         |
| RetailerZipCode       | object  |                      | Zip code of the retailer facility.                                             | Example: 902925618                   |           0 | May require formatting to a standard 5 or 9-digit zip code format for consistency.                                                                                                                                                                                                                                                                                                      |
| RetailerCounty        | float64 |                      | County where the retailer facility is located.                                 |                                      |         100 | This column is entirely missing. Consider removing it or attempting to impute from RetailerCity/ZipCode using external data sources if critical for analysis.                                                                                                                                                                                                                           |
| ItemCategory          | object  |                      | Category of the cannabis item sold (e.g., Pre-Roll Flower).                    | Example: Pre-Roll Flower             |           0 |                                                                                                                                                                                                                                                                                                                                                                                         |
| Date                  | object  |                      | Month and year of the sales record.                                            | Example: 01-2020                     |           0 | Convert to a datetime object for proper temporal analysis and filtering.                                                                                                                                                                                                                                                                                                                |
| totalsales            | float64 | Currency (e.g., USD) | Total sales amount for the given record.                                       | [-27161.03, 9408194.73]              |           0 | Contains negative values. These likely represent returns or sales adjustments. Flag these records for investigation. For analyses requiring positive sales, consider treating negative values as zero or excluding them.                                                                                                                                                                |
| meanprice             | float64 | Currency per unit    | Average price per unit for the items in the sales record.                      | [-Infinity, Infinity]                |           0 | Contains negative and infinite values. Negative values may indicate returns or calculation errors. Infinite values typically result from division by zero (e.g., zero quantity sold). Flag these records. For analysis, infinite values should be treated as missing (NaN) or excluded. Negative values should be investigated or treated as zero if only positive prices are relevant. |


### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column is 100% missing.
    *   **Likely cause:** Data was either not collected for this field or was not extracted/joined correctly.
    *   **Recommended handling rule:** If county-level analysis is not critical, the column can be dropped. If essential, attempt to impute county information using `RetailerCity` and `RetailerZipCode` with an external geographic lookup table.
*   **Issue:** `totalsales` contains negative values.
    *   **Likely cause:** These values typically represent product returns, sales adjustments, or credit memos rather than actual positive sales.
    *   **Recommended handling rule:** Flag these records for further investigation. For analyses focused on gross sales, these values could be excluded or converted to zero. For net sales, they should be retained.
*   **Issue:** `meanprice` contains negative values.
    *   **Likely cause:** Similar to `totalsales`, negative mean prices could result from returns where the return value exceeds the original sale price, or from calculation errors.
    *   **Recommended handling rule:** Flag these records. For analyses requiring positive prices, these values should be excluded or converted to zero.
*   **Issue:** `meanprice` contains infinite values.
    *   **Likely cause:** Infinite values often arise from division by zero, which could occur if the quantity sold for a particular item category in a given record was zero, leading to a `total_sales / 0` calculation for mean price.
    *   **Recommended handling rule:** Convert infinite values to `NaN` (Not a Number) to represent missing or undefined data. These records should then be excluded from calculations involving `meanprice` or imputed if appropriate.

### Reproducible Cleaning Plan

1.  **Handle Missing County Data:** Assess the necessity of the `RetailerCounty` column. If not critical, drop the column. If required, attempt to enrich the dataset by joining with an external geographic dataset using `RetailerCity` and `RetailerZipCode` to populate the county information.
2.  **Standardize Zip Code Format:** Inspect `RetailerZipCode` for variations (e.g., 5-digit vs. 9-digit) and standardize to a consistent format (e.g., 5-digit) to ensure uniformity.
3.  **Convert Date Column:** Transform the `Date` column from its current object type (e.g., "01-2020") into a proper datetime object to enable robust temporal filtering and analysis.
4.  **Address Negative Sales Values:** Identify and flag all records where `totalsales` is negative. For analyses requiring only positive sales, create a new column for 'positive_sales' where negative values are set to zero, or filter out these records.
5.  **Address Anomalous Mean Price Values:**
    *   Identify and flag records where `meanprice` is negative. For analyses requiring positive prices, these values should be treated as zero or excluded.
    *   Identify and convert all infinite values in `meanprice` to `NaN`. These records should then be excluded from calculations involving `meanprice` or imputed if appropriate.

### Limitations & Trust Section

*   **Missing `RetailerCounty` Data:** The complete absence of data in the `RetailerCounty` column significantly limits geographical analysis at the county level. Trust in any county-level insights derived from this dataset is low without external data enrichment.
*   **Ambiguous `totalsales` and `meanprice` Anomalies:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry issues, returns, or calculation errors. Without clear documentation on how these values are generated, the absolute reliability of these metrics for direct summation or averaging is reduced. Further validation with source system logic or business stakeholders is needed to fully understand their meaning and appropriate handling.
*   **Date Granularity:** The `Date` column appears to be at a monthly granularity ("MM-YYYY"). This limits analysis to monthly trends and prevents daily or weekly insights.

### Appendix: Quick Reference

*   **County Data:** `RetailerCounty` is 100% missing; consider dropping or external imputation.
*   **Zip Code:** Standardize `RetailerZipCode` to a consistent format.
*   **Date Conversion:** Convert `Date` column to datetime objects.
*   **Negative Sales:** Flag `totalsales < 0`; treat as zero or exclude for positive sales analysis.
*   **Negative Mean Price:** Flag `meanprice < 0`; treat as zero or exclude for positive price analysis.
*   **Infinite Mean Price:** Convert `meanprice` infinite values to `NaN`; exclude from calculations.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative and infinite values in `totalsales` and `meanprice`, ensuring that the recommended cleaning steps align with the intended analytical goals and business definitions. Additionally, the feasibility and necessity of imputing `RetailerCounty` should be discussed.

# Work Documentation

## Table: sales20

**Data Operations:**
The `sales20` dataset was integrated into a larger, comprehensive sales DataFrame by concatenating multiple yearly sales files (including `sales18.csv` through `sales24.csv`). During this initial processing, the `meanprice` column, along with an unnamed `v1` column, was explicitly dropped from the dataset. Several columns were renamed for consistency, such as `ItemCategory` to `itemcategory`, and `RetailerLicenseNumber`, `RetailerFacilityType`, `RetailerCity`, `RetailerZipCode`, `RetailerCounty`, and `Date` were converted to their lowercase counterparts. The combined dataset was then sorted by multiple key identifiers to ensure a consistent order.

The dataset was enriched by merging with an external `parent_df` (containing company ID and license information) using `retailerlicensenumber` as the key. This merge introduced `primary_company` and `cannabiz_county` information. Records from the `parent_df` that did not have a match in the sales data were excluded.

Extensive cleaning and imputation were performed on the `retailercounty` column due to its initial incompleteness. This involved:
1.  Replacing "NA" and "UNDEFINED" string values with empty strings.
2.  Attempting to fill empty `retailercounty` values using `cannabiz_county` obtained from the merged `parent_df`.
3.  Applying specific manual fixes for known license numbers with incorrect or missing county information.
4.  Standardizing all `retailercounty` names to uppercase.
5.  Creating a lookup table from existing, valid `retailerlicensenumber` and `retailercounty` pairs within the dataset, and then merging this back to further impute missing county values.
6.  Extracting a 5-digit zip code (`zip5`) from the `retailerzipcode` column.
7.  Merging with an external `zip_df` (a ZIP-to-county mapping for California) to fill any remaining missing `retailercounty` values based on the `zip5`.
8.  Applying additional manual fixes for specific license numbers that still had incorrect county assignments.
9.  Performing a final cleaning pass on `retailercounty` by stripping whitespace and replacing empty strings, "NA", and "nan" with proper missing value indicators (`pd.NA`), followed by dropping rows where `retailercounty` remained missing.

An `Unnamed: 0` column was dropped from the DataFrame. All columns were then converted to string type, with any remaining `NaN` values filled with empty strings. The processed data was saved to a Stata file named `sales_w_parent_co_test.dta` and subsequently reloaded for further analysis.

Further transformations included extracting the `year` from the `date` column and converting both `totalsales` and the newly derived `year` column to numeric data types, coercing any errors to `NaN`.

The core analytical work involved calculating the Herfindahl-Hirschman Index (HHI) to measure market concentration. This was performed at several levels:
*   Statewide HHI for individual retailers.
*   Statewide HHI for parent companies (where `primary_company` was used, defaulting to `retailerlicensenumber` if `primary_company` was missing).
*   County-level HHI for individual retailers.
*   County-level HHI for parent companies.
These calculations involved grouping data by relevant identifiers (retailer, parent company, county, year), summing `totalsales` to determine market size, calculating individual market shares, and then squaring and summing these shares to derive the HHI.

All calculated HHI results were combined into a single DataFrame. Additional metrics like `county_sales` and `county_sales_parent` were computed to provide context for market size. The data was filtered to include years from 2019 to 2025 for specific analyses.

Advanced analytical techniques were applied to the HHI data:
*   K-Means clustering was used to group counties based on their HHI trends over time.
*   Linear regression was performed on HHI values over time for each county to classify them into "increasing," "decreasing," or "stable" HHI trajectories based on the slope of the trend.
*   Year-over-year HHI percentage change was calculated for each county.
*   Correlation analysis was conducted between `mkt_share2` (HHI), `totalsales`, and `county_sales`.

Finally, numerous visualizations (line plots, bar plots, heatmaps, box plots, violin plots, scatter plots) were generated using `matplotlib`, `seaborn`, and `plotly` to illustrate HHI trends, distributions, and relationships. Key HHI summary tables were exported to CSV and Excel formats for reporting.

**Variables Affected:**
*   **Created:** `primary_company` (derived from `Company ID` in `parent_df`), `zip5` (5-digit zip code extracted from `retailerzipcode`), `year` (extracted from `date`), `multi_owner` (indicator for multiple owners in `companyid`), `mkt_share` (market share percentage), `mkt_share2` (squared market share, used for HHI), `industry_sales` (total sales for a given market), `county_sales` (total sales for a county), `county_sales_parent` (total parent company sales for a county), `opacity` and `opacity_parent` (metrics related to sales volume), `cluster` (K-Means cluster assignment), `hhi_change` (year-over-year HHI percentage change).
*   **Modified:**
    *   `RetailerLicenseNumber` was renamed to `retailerlicensenumber`.
    *   `RetailerFacilityType` was renamed to `retailerfacilitytype`.
    *   `RetailerCity` was renamed to `retailercity`.
    *   `RetailerZipCode` was renamed to `retailerzipcode` and used to derive `zip5`.
    *   `RetailerCounty` was renamed to `retailercounty` and underwent extensive cleaning, imputation, and standardization.
    *   `ItemCategory` was renamed to `itemcategory`.
    *   `Date` was renamed to `date` and used to derive `year`.
    *   `totalsales` was converted to a numeric data type and used extensively in HHI calculations.
*   **Dropped:** `meanprice` (explicitly removed), `v1` (an unnamed column), `_merge` (temporary column from merge operation), `retailercounty_from_license_county` (temporary column from county imputation), `_merge_lic_county` (temporary column for merge tracking), `retailercounty_from_zip` (temporary column from zip-based county imputation), `_merge_zip` (temporary column for merge tracking), `Unnamed: 0` (an unnamed column).

**Logic and Methodology:**
The overarching goal of the data work was to transform raw cannabis sales data into a structured format suitable for in-depth market concentration analysis using the Herfindahl-Hirschman Index (HHI). The methodology involved a systematic approach:
1.  **Data Consolidation:** Multiple annual sales files were combined to create a comprehensive dataset, enabling a broader temporal perspective for trend analysis. This ensured that market dynamics could be observed across several years.
2.  **Data Enrichment:** The sales data was augmented by merging with external license information. This critical step introduced `primary_company` identifiers, allowing for market concentration to be assessed not only at the individual retailer level but also at the parent company level, providing a more accurate view of corporate influence.
3.  **Geographic Data Standardization and Imputation:** Recognizing the initial deficiencies in the `RetailerCounty` column, a robust multi-stage cleaning and imputation strategy was implemented. This involved leveraging internal data consistency, external geographic lookup tables (ZIP-to-county), and targeted manual corrections. The aim was to maximize the completeness and accuracy of county assignments, which is fundamental for reliable county-level HHI analysis.
4.  **Data Type Conversion and Derivation:** Key columns representing sales values (`totalsales`) and temporal information (`date`, `year`) were converted to appropriate numeric and datetime data types. This facilitated accurate mathematical operations and time-series analysis. The `year` was explicitly derived to enable annual aggregations.
5.  **Market Concentration Calculation (HHI):** The HHI was calculated by first determining the market share of each entity (individual retailer or parent company) based on their `totalsales` within specific market definitions (statewide or county-level). These market shares were then squared and summed to produce the HHI, a standard economic indicator of market concentration.
6.  **Trend and Pattern Analysis:** To understand the evolution of market concentration, the calculated HHI values were subjected to further analysis. K-Means clustering was employed to group counties exhibiting similar HHI trajectories, while linear regression was used to quantify the rate of change in HHI over time for each county, categorizing them as having "increasing," "decreasing," or "stable" concentration trends.
7.  **Visualization and Reporting:** The results were extensively visualized using a variety of plotting libraries. These visualizations, along with exported summary tables, were designed to make complex market concentration trends, distributions, and relationships easily interpretable for stakeholders and to support formal reporting.

**Validation and Verification:**
Throughout the data processing, several steps were taken to ensure data quality and validate transformations:
*   The use of `indicator=True` during merge operations provided an audit trail for record matching, allowing for verification of successful joins and identification of unmatched records.
*   Explicit checks for `notna()` and non-empty strings were applied to filter out invalid license numbers, ensuring that merges were performed on clean keys.
*   `value_counts(dropna=False)` was frequently used to inspect the distribution of categorical columns like `itemcategory` and `retailercounty` before and after cleaning, serving as a check for data quality and the effectiveness of imputation steps.
*   The `errors='coerce'` argument in `pd.to_numeric` calls was utilized to gracefully handle non-numeric values, converting them to `NaN` for subsequent identification and handling.
*   Temporary columns like `_merge_lic_county` and `_merge_zip` were created to track the source and method of `retailercounty` imputation, providing transparency and an audit trail for the complex county assignment logic.
*   The final `retailercounty` column was rigorously inspected using `value_counts(dropna=False)` to confirm the successful outcome of the extensive cleaning and imputation efforts.
*   The HHI calculations inherently include internal consistency checks, as market shares within a defined market should sum to 100% (before squaring), providing a basis for validating the aggregation logic.
*   The generation of numerous visualizations served as a crucial visual validation step, allowing for quick identification of anomalies, unexpected trends, or inconsistencies in the processed data.

**Results and Outcomes:**
The data work successfully produced a robust, cleaned, and enriched dataset that enabled comprehensive market concentration analysis. Key outcomes include:
*   A consolidated and standardized sales dataset spanning multiple years (2018-2024), providing a reliable foundation for temporal analysis of market trends.
*   A significantly improved `retailercounty` column, which is now more complete and accurate, thereby enhancing the reliability of geographical analyses.
*   The successful integration of `primary_company` information, allowing for a nuanced understanding of market concentration at the corporate ownership level, beyond individual retail outlets.
*   The calculation of Herfindahl-Hirschman Index (HHI) values for both individual retailers and parent companies, at both statewide and county levels, providing quantitative measures of market concentration.
*   Identification of distinct HHI trends (increasing, decreasing, stable) across different counties, offering insights into evolving market structures.
*   Clustering of counties based on their HHI trajectories, revealing underlying patterns of market behavior and potentially identifying regions with similar competitive landscapes.
*   The generation of various analytical outputs (e.g., `hhi_by_county.csv`, `Cult_HHI_DeepDive.xlsx`) and interactive visualizations (e.g., HTML plots) that effectively communicate complex HHI trends, distributions, and correlations, making the findings accessible for further review, reporting, and strategic decision-making.
*   The problematic `meanprice` column, as identified in the codebook, was appropriately removed from the dataset, mitigating the risk of its use in potentially misleading analyses.






# Table: sales21

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
*   **Column Dictionary**


| Column Name           | Type    | Units        | Description                                                                                | Allowed Values / Range                    |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                                    |
|:----------------------|:--------|:-------------|:-------------------------------------------------------------------------------------------|:------------------------------------------|------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |              | Unique identifier for the retailer's license.                                              | Example: C12-0000233-LIC                  |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RetailerFacilityType  | object  |              | Type of facility operated by the retailer (e.g., Microbusiness License).                   | Example: Cannabis - Microbusiness License |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RetailerCity          | object  |              | City where the retailer's facility is located.                                             | Example: Maywood                          |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RetailerZipCode       | int64   |              | Zip code of the retailer's facility location.                                              | [90008.0, 961610393.0]                    |           0 | The upper bound of the range (961610393.0) appears unusually large for a standard 5-digit or 9-digit zip code. Investigate these values for potential data entry errors or concatenated data. Consider flagging or excluding values outside a plausible zip code range.                                                                                                                                             |
| RetailerCounty        | float64 |              | County where the retailer's facility is located.                                           |                                           |         100 | This column is entirely missing. It should be excluded from analysis or populated from an external source if county-level aggregation is required.                                                                                                                                                                                                                                                                  |
| ItemCategory          | object  |              | Category of the cannabis item sold (e.g., Pre-Roll Flower).                                | Example: Pre-Roll Flower                  |           0 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Date                  | object  |              | Month and year of the sales data.                                                          | Example: 01-2021                          |           0 | Convert to a proper datetime format for accurate temporal analysis and filtering.                                                                                                                                                                                                                                                                                                                                   |
| totalsales            | float64 | USD          | Total sales amount for the given item category by the retailer in the specified month.     | [-11837.69, 4268253.77]                   |           0 | Contains negative values. Sales amounts cannot be negative. These values may represent returns, adjustments, or data entry errors. Proposed handling: Flag these records for investigation. For analysis, consider treating them as zero or excluding them, depending on the business context (e.g., if negative sales are not meaningful for revenue calculations).                                                |
| meanprice             | float64 | USD per unit | Average price per unit for the given item category by the retailer in the specified month. | [-Infinity, Infinity]                     |           0 | Contains negative and infinite values. Negative prices are illogical. Infinite values likely result from division by zero (e.g., zero units sold). Proposed handling: Flag negative values for investigation and exclude them from price calculations. Replace infinite values with NaN or zero, or exclude records where meanprice is infinite, as they indicate an underlying data issue (e.g., no sales volume). |


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






# Table: sales22

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

*   **Column Dictionary**


| Column Name           | Type    | Units             | Description                                                                                  | Allowed Values / Range                             |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------------------|:--------|:------------------|:---------------------------------------------------------------------------------------------|:---------------------------------------------------|------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                   | Unique identifier for the retailer's license.                                                | Example: C9-0000034-LIC                            |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RetailerFacilityType  | object  |                   | Type of facility operated by the retailer (e.g., Cannabis - Retailer Nonstorefront License). | Example: Cannabis - Retailer Nonstorefront License |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RetailerCity          | object  |                   | City where the retailer is located.                                                          | Example: CULVER CITY                               |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RetailerZipCode       | int64   |                   | Zip code of the retailer's location.                                                         | Range: [90008.0, 961610393.0]                      |         0   | Some values appear to be concatenated ZIP+4 codes (e.g., 902306965). Standardize to 5-digit ZIP code for consistency and joinability.                                                                                                                                                                                                                                                                                              |
| RetailerCounty        | object  |                   | County where the retailer is located.                                                        | Example: LOS ANGELES                               |         9.7 | Approximately 9.7% of values are missing. Consider imputation using RetailerCity/ZipCode or flagging records with missing county for further investigation.                                                                                                                                                                                                                                                                        |
| ItemCategory          | object  |                   | Category of the item sold (e.g., Pre-Roll Flower).                                           | Example: Pre-Roll Flower                           |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| totalsales            | float64 | Currency          | Total sales amount for the aggregated record.                                                | Range: [-58292.28, 7820938.99]                     |         0   | Contains negative values. This likely indicates returns, refunds, or data entry errors. Recommend flagging these records and investigating their cause. For analysis, consider treating negative values as zero or excluding them, depending on the analytical objective.                                                                                                                                                          |
| meanprice             | float64 | Currency per unit | Average price per unit for the item within the aggregated record.                            | Range: [-Infinity, Infinity]                       |         0   | Contains negative and infinite values. Negative values likely indicate returns or calculation errors. Infinite values typically result from division by zero (e.g., total sales divided by zero quantity). Recommend flagging these records. For analysis, negative values could be treated as zero or excluded. Infinite values should be converted to NaN/null or excluded, as they are not meaningful for statistical analysis. |
| Date                  | object  |                   | Month and year of the sales record.                                                          | Example: 01-2022                                   |         0   | Currently stored as an object (string). Convert to a datetime format for proper temporal analysis and filtering.                                                                                                                                                                                                                                                                                                                   |


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






# Table: sales23

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
*   **Column Dictionary**


| Column Name           | Type    | Units        | Description                                                                                 | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                              |
|:----------------------|:--------|:-------------|:--------------------------------------------------------------------------------------------|:-------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |              | Unique identifier for the licensed cannabis retailer.                                       | Example: C10-0000633-LIC             |           0 |                                                                                                                                                                                                                                                                                                                                                                                               |
| RetailerFacilityType  | object  |              | Categorization of the retailer's licensed facility type.                                    | Example: Cannabis - Retailer License |           0 |                                                                                                                                                                                                                                                                                                                                                                                               |
| RetailerCity          | object  |              | City where the licensed retailer facility is located.                                       | Example: LONG BEACH                  |           0 |                                                                                                                                                                                                                                                                                                                                                                                               |
| RetailerZipCode       | int64   |              | Zip code of the retailer facility. May include 5-digit or 9-digit formats.                  | [90003.0, 961610393.0]               |           0 | Consider standardizing to a 5-digit format if consistency is required for geographical analysis or joins.                                                                                                                                                                                                                                                                                     |
| RetailerCounty        | object  |              | County where the licensed retailer facility is located.                                     | Example: LOS ANGELES                 |           8 | Significant missing values. Imputation strategy (e.g., based on RetailerZipCode or RetailerCity) or flagging for further investigation is recommended.                                                                                                                                                                                                                                        |
| ItemCategory          | object  |              | Category of the cannabis product sold.                                                      | Example: Extract (weight - each)     |           0 |                                                                                                                                                                                                                                                                                                                                                                                               |
| totalsales            | float64 | USD          | Total sales amount for the specified item category by the retailer during the given period. | [-29321.63, 9167140.17]              |           0 | Contains negative values. Likely cause: returns, refunds, or data entry errors. Proposed handling: Flag these rows for review, or exclude them from analyses requiring positive sales figures. Alternatively, treat as legitimate returns if context allows.                                                                                                                                  |
| meanprice             | float64 | USD per unit | Average price per unit for the specified item category.                                     | [-Infinity, Infinity]                |           0 | Contains negative and infinite values. Negative values are likely data entry errors. Infinite values suggest division by zero (e.g., zero quantity sold for a non-zero total sales, or zero total sales for zero quantity). Proposed handling: Flag these rows for review, or exclude them from analyses. Infinite values should be converted to NaN or null for proper numerical operations. |
| Date                  | object  |              | Month and year of the sales data.                                                           | Example: 01-2023                     |           0 | Convert to a datetime object for proper temporal analysis and filtering.                                                                                                                                                                                                                                                                                                                      |


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






# Table: sales23v2

### Overview Section

This dataset provides aggregated sales information related to the Track & Trace project, likely pertaining to cannabis sales within a regulated market. It captures various attributes of sales transactions, including retailer details, item categories, and sales figures. Each row in the `sales23v2` table represents an aggregated sales record for a specific item category by a retailer for a given month. The overall data source, collection period, and extraction date are not specified in the provided summary.

**Assumptions:**
*   One row in the `sales23v2` table represents a monthly aggregated sales record for a unique combination of retailer, item category, and date.
*   `totalsales` and `meanprice` are expressed in a currency, likely USD.

### Table Inventory

*   **sales23v2:** Contains aggregated sales data, including retailer information, item categories, total sales, and mean prices for specific periods.

## Table: sales23v2

*   **Purpose:** To provide a summary of sales transactions, detailing retailer characteristics, product categories, and key sales metrics over time.
*   **What one row represents:** An aggregated sales record for a specific item category by a retailer for a given month.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key inferred).
*   **Relationships:**
*   **Number of rows and columns:** 286938 rows, 9 columns.
*   **Column Dictionary**


| Column Name           | Type    | Units        | Description                                                                    | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                        |
|:----------------------|:--------|:-------------|:-------------------------------------------------------------------------------|:-------------------------------------|------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |              | Unique identifier for the licensed retailer.                                   | Example: C10-0000196-LIC             |         0   |                                                                                                                                                                                                                                                         |
| RetailerFacilityType  | object  |              | Type of facility operated by the retailer (e.g., Cannabis - Retailer License). | Example: Cannabis - Retailer License |         0   |                                                                                                                                                                                                                                                         |
| RetailerCity          | object  |              | City where the retailer's facility is located.                                 | Example: RIVERBANK                   |         0   |                                                                                                                                                                                                                                                         |
| RetailerZipCode       | float64 |              | Zip code of the retailer's location.                                           | Range: [90003.0, 961610393.0]        |         0.2 | Data type is float64 but should be string or integer. Investigate unusually large values (e.g., 961610393.0) which may indicate concatenated zip codes or data entry errors. Convert to string and validate format.                                     |
| RetailerCounty        | object  |              | County where the retailer's facility is located.                               | Example: STANISLAUS                  |         0.5 | High percentage of missing values (50%). Consider imputation from RetailerZipCode or RetailerCity if a reliable mapping exists, otherwise flag for awareness or exclude if critical for analysis.                                                       |
| ItemCategory          | object  |              | Category of the item sold (e.g., Flower, Edibles, Concentrates).               | Example: Flower (packaged - each)    |         0   |                                                                                                                                                                                                                                                         |
| totalsales            | float64 | USD          | Total sales amount for the given item category by the retailer for the period. | Range: [-29321.63, 9167140.17]       |         0   | Contains negative values, which are illogical for sales totals. These may represent returns or data entry errors. Flag these records; for analysis, consider excluding them or treating them as zero.                                                   |
| meanprice             | float64 | USD per unit | Average price per unit for the item category.                                  | Range: [-Infinity, Infinity]         |         0   | Contains negative and infinite values. Negative prices are illogical. Infinite values likely result from division by zero (e.g., total sales / zero quantity). Flag these records; exclude from price-related calculations or treat as missing/invalid. |
| Date                  | object  |              | Month and year of the sales record.                                            | Example: 01-2023                     |         0   | Convert to datetime object for proper temporal analysis and sorting.                                                                                                                                                                                    |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `sales23v2` table.

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Data entry errors, incorrect processing of returns, or system glitches where sales figures are recorded as negative.
    *   **Recommended handling rule:** Flag records with negative `totalsales`. For most analyses, these records should be excluded or their `totalsales` value set to zero, as negative sales are not a valid business outcome.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these are likely data entry errors or calculation errors, as a price cannot be negative.
    *   **Recommended handling rule:** Flag records with negative `meanprice`. Exclude these records from any price-related calculations or treat the `meanprice` as missing/invalid.
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** Division by zero, typically occurring when the quantity sold for an item category is zero, leading to `total_sales / 0`.
    *   **Recommended handling rule:** Flag records with infinite `meanprice`. Exclude these records from price-related calculations or treat the `meanprice` as missing/invalid.
*   **Issue:** High missing percentage (50%) for `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry, an optional field during data collection, or issues during data extraction.
    *   **Recommended handling rule:** Investigate if `RetailerCounty` can be reliably imputed from `RetailerZipCode` or `RetailerCity` using an external, validated lookup table. If imputation is not feasible or reliable, acknowledge this as a limitation and use the column with caution, or exclude records where county information is critical.
*   **Issue:** `RetailerZipCode` stored as `float64` with unusually large values.
    *   **Likely cause:** Data type mismatch (zip codes should be strings or integers), potential concatenation of multiple zip codes, or data entry errors. The large values (e.g., `961610393.0`) are not standard zip codes.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Validate values against known zip code formats. For anomalous large values, investigate their origin; they may need to be truncated, split, or flagged as invalid.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the 'Date' column from its current object type (e.g., "01-2023") to a proper datetime object to enable accurate temporal analysis and sorting.
2.  **Address `RetailerZipCode` Anomalies:** Convert the `RetailerZipCode` column to a string data type. Subsequently, identify and correct or flag entries with unusually large or non-standard values (e.g., `961610393.0`) to ensure all entries conform to valid zip code formats.
3.  **Handle Missing `RetailerCounty` Data:** Attempt to impute missing `RetailerCounty` values by leveraging a reliable external mapping from `RetailerZipCode` or `RetailerCity`; if a robust imputation method is not available, flag these records to indicate missing information.
4.  **Process Negative `totalsales`:** Identify all records where `totalsales` is negative and flag them. For subsequent analytical tasks, these records should either be excluded from calculations or their `totalsales` value should be set to zero, depending on the specific analytical objective regarding returns.
5.  **Process Negative and Infinite `meanprice`:** Identify all records where `meanprice` is negative or infinite and flag them. These values are considered invalid and should be excluded from any price-related calculations or treated as missing data.

### Limitations & Trust Section

The trustworthiness of this dataset is impacted by several factors. The absence of an explicit data source, collection period, and extraction date limits the ability to fully validate its provenance and timeliness. Significant data quality issues, such as negative sales and prices, infinite prices, and a high percentage of missing county data, suggest potential inaccuracies or inconsistencies in data collection or processing. The anomalous `RetailerZipCode` values also raise concerns about data integrity. To validate these elements, it is crucial to:
*   Obtain detailed metadata regarding the data source, collection methodology, and any pre-processing steps.
*   Consult with data owners or subject matter experts to understand the business rules for handling returns and pricing, and to clarify the expected format and range of `RetailerZipCode` and `RetailerCounty` values.
*   Cross-reference `RetailerZipCode` and `RetailerCounty` with external, authoritative geographic datasets.

### Appendix: Quick Reference

*   **Date Conversion:** Convert 'Date' to datetime objects.
*   **Zip Code Cleaning:** Convert 'RetailerZipCode' to string; validate and correct/flag non-standard or anomalous values.
*   **County Imputation:** Attempt to impute missing 'RetailerCounty' from zip codes/cities if reliable mapping exists; otherwise, flag.
*   **Sales Validation:** Flag negative 'totalsales'; exclude or set to zero for analysis.
*   **Price Validation:** Flag negative or infinite 'meanprice'; exclude from calculations.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred data descriptions, especially for "What one row represents" and "Primary key(s)," as these were not explicitly provided. Please also scrutinize the proposed cleaning rules for `RetailerZipCode`, `RetailerCounty`, `totalsales`, and `meanprice` to ensure they align with business requirements and analytical objectives. Specific attention should be paid to the handling of negative and infinite values to confirm that the recommended approach maintains data integrity and reproducibility for downstream analysis.

# Work Documentation

## Table: sales23v2

**Data Operations:**
The `sales23v2` dataset was integrated into a larger, consolidated sales dataset (`sales_df`) by concatenating it with several other annual sales files (from 2018 to 2024). During the initial loading of each individual sales file, the `meanprice` column and any `v1` column were dropped. Subsequently, column names were standardized to a consistent lowercase format (e.g., `RetailerLicenseNumber` became `retailerlicensenumber`, `ItemCategory` became `itemcategory`, `Date` became `date`, and `totalsales` became `totalsales`). The combined dataset was then sorted by multiple retailer and sales attributes to ensure a consistent order.

The dataset was enriched by a left merge with an external `parent_df` (containing license and company information), linking `primary_company` and `cannabiz_county` based on `retailerlicensenumber`. Missing `retailercounty` values were addressed through a multi-stage imputation process: initially replacing "NA" and "UNDEFINED" with empty strings, then imputing from `cannabiz_county` using a predefined mapping, followed by specific manual corrections for certain license numbers. All `retailercounty` values were then standardized to uppercase. Further imputation was performed by leveraging license-level aggregated county information and an external ZIP-to-County mapping (`zip_df`) after extracting a 5-digit zip code (`zip5`) from `retailerzipcode`. An `Unnamed: 0` column, likely an artifact from data export, was dropped.

After these cleaning steps, all columns in the dataframe were converted to string type, with any remaining NaN values filled with empty strings. A `year` column was extracted from the `date` column, and both `totalsales` and the new `year` column were converted to numeric types, coercing any conversion errors. The data was then aggregated by `retailerlicensenumber` and `year` to sum `totalsales` and retain the first `retailerzipcode` and `primary_company`. This aggregated data was used to calculate market share (`mkt_share`) and squared market share (`mkt_share2`) for Herfindahl-Hirschman Index (HHI) analysis at statewide and county levels, for both individual retailers and parent companies. The processed data and analytical results were exported to Stata and Excel files, and various visualizations were generated.

**Variables Affected:**
*   **Dropped:** `meanprice`, `v1` (if present in source files), `Unnamed: 0`.
*   **Renamed:** `RetailerLicenseNumber` to `retailerlicensenumber`, `RetailerFacilityType` to `retailerfacilitytype`, `RetailerCity` to `retailercity`, `RetailerZipCode` to `retailerzipcode`, `RetailerCounty` to `retailercounty`, `ItemCategory` to `itemcategory`, `Date` to `date`, `totalsales` to `totalsales`.
*   **Modified/Cleaned:** `retailercounty` (cleaned, imputed, standardized to uppercase), `retailerzipcode` (used to derive `zip5`).
*   **Type Converted:** `date` (used to derive `year`), `totalsales` (to numeric), `year` (to numeric), all columns (to string at one stage).
*   **New Variables Created:** `primary_company`, `cannabiz_county` (from merge), `zip5`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `_merge_lic_county`, `_merge_zip`, `opacity`, `opacity_parent`, `HHI`, `HHI_parent_level`, `hhi_change`, `cluster`.

**Logic and Methodology:**
The primary objective of the data work was to prepare a comprehensive sales dataset for market concentration analysis. This involved consolidating annual sales data, standardizing its structure, and enriching it with external company and geographic information. A multi-pronged approach was used for `retailercounty` imputation, prioritizing internal consistency (from existing license data) and then external validation (from a ZIP-to-County mapping) to maximize data completeness for geographic analysis. The extraction of a 5-digit zip code aimed to normalize the `retailerzipcode` for reliable lookups. The conversion of `totalsales` to a numeric type was essential for quantitative aggregations. The core analytical methodology involved calculating the Herfindahl-Hirschman Index (HHI) to measure market concentration, which was performed at various granularities (statewide vs. county, individual retailer vs. parent company). Further analysis included identifying HHI trends over time using linear regression and grouping counties with similar HHI trajectories through K-Means clustering, providing a deeper understanding of market dynamics.

**Validation and Verification:**
The data cleaning process directly addressed several data quality issues identified in the Codebook. The problematic `meanprice` column, which contained negative and infinite values, was entirely removed from the dataset, effectively resolving that anomaly. The `RetailerZipCode` issue, characterized by a `float64` type and unusually large values, was handled by converting the column to string and extracting a standardized 5-digit zip code (`zip5`), which was then used for reliable geographic lookups. The high percentage of missing `RetailerCounty` values was extensively mitigated through a series of imputation steps, including leveraging merged data, manual corrections, and an external ZIP-to-County mapping, aligning with the recommended handling rule. While `totalsales` was converted to numeric, the code did not explicitly implement the Codebook's recommendation to flag or exclude negative `totalsales` values, which may warrant further review. The `Date` column was successfully used to derive a `year` column, supporting temporal analysis. The numerous intermediate data manipulations and merges suggest an iterative process of data refinement.

**Results and Outcomes:**
The data work resulted in a robust, consolidated sales dataset spanning multiple years (2018-2024), significantly improved in terms of data quality and completeness, particularly for geographic attributes. The dataset is now enriched with parent company information, enabling more sophisticated market analysis. Key outcomes include the calculation of Herfindahl-Hirschman Index (HHI) values at both statewide and county levels, and for individual retailers and their parent companies, providing critical metrics for assessing market concentration. The analysis further categorized counties based on their HHI trends (increasing, decreasing, stable) and identified clusters of counties with similar HHI trajectories. A variety of visualizations were generated to illustrate these findings, including HHI trends over time, market share comparisons, and distributions of HHI. The final processed data and analytical results were exported to various file formats (Stata, Excel, CSV, HTML plots), making them accessible for further reporting and stakeholder review.






# Table: sales24

### Overview Section

This dataset provides aggregated sales information from the Track & Trace project, detailing monthly sales performance for various cannabis retailers across different item categories. Each row in the `sales24` table represents a monthly summary of sales for a specific item category by a particular retailer. The data source is the Track & Trace project, with the collection period inferred to be January 2024 based on the 'Date' column. The extraction date is not available.

**Assumptions:**
*   The 'Date' column represents the month and year for which the sales data is aggregated.
*   `totalsales` and `meanprice` are expressed in a standard currency (e.g., USD).

### Table Inventory

*   **sales24:** Contains aggregated monthly sales data for cannabis retailers, including retailer details, item categories, total sales, and mean prices.

## Table: sales24

*   **Purpose:** To provide a summary of monthly sales transactions, detailing sales performance by retailer and item category.
*   **What one row represents:** A monthly sales summary for a specific item category by a unique retailer.
*   **Primary key(s):** Likely composite key: `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 289765 rows, 9 columns
*   **Column Dictionary**


| Column Name           | Type    | Units             | Description                                                                             | Allowed Values / Range                  |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------|:--------|:------------------|:----------------------------------------------------------------------------------------|:----------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                   | Unique identifier for the retailer's license.                                           | Example: C10-0000007-LIC                |         0   |                                                                                                                                                                                                                                                                                                                                                                                   |
| RetailerFacilityType  | object  |                   | Type of facility operated by the licensed retailer.                                     | Example: Cannabis - Retailer License    |         0   |                                                                                                                                                                                                                                                                                                                                                                                   |
| RetailerCity          | object  |                   | City where the retailer's facility is located.                                          | Example: SAN ANDREAS                    |         0   |                                                                                                                                                                                                                                                                                                                                                                                   |
| RetailerZipCode       | float64 |                   | Zip code of the retailer's facility location.                                           | [90003.0, 961610393.0]                  |         0.2 | Convert to string to preserve leading zeros and handle non-numeric entries. Investigate unusually large values (e.g., 961610393.0) as they may indicate data entry errors or extended zip codes. Impute missing values based on RetailerCity/RetailerCounty if possible.                                                                                                          |
| RetailerCounty        | object  |                   | County where the retailer's facility is located.                                        | Example: CALAVERAS                      |         0.4 | Impute missing values based on RetailerCity/RetailerZipCode if a reliable mapping exists. Otherwise, flag as 'Unknown'.                                                                                                                                                                                                                                                           |
| ItemCategory          | object  |                   | Category of the cannabis item sold.                                                     | Example: Vape Cartridge (weight - each) |         0   |                                                                                                                                                                                                                                                                                                                                                                                   |
| totalsales            | float64 | Currency          | Total sales amount for the specified item category by the retailer for the given month. | [-154888.11, 1718788.33]                |         0   | Contains negative values. These likely represent returns, sales adjustments, or data entry errors. Flag these records for investigation. For analyses requiring positive sales, these values may be excluded or set to zero.                                                                                                                                                      |
| meanprice             | float64 | Currency per unit | Average price per unit for the specified item category.                                 | [-107.412004160888, Infinity]           |         0   | Contains negative and infinite values. Negative values likely due to returns/adjustments or calculation errors. Infinite values likely due to division by zero (e.g., zero units sold). Flag these records for investigation. For analyses requiring valid prices, these records should be excluded or imputed (e.g., with the median meanprice for the respective ItemCategory). |
| Date                  | object  | Month-Year        | Month and year of the sales data aggregation.                                           | Example: 01-2024                        |         0   | Convert to datetime object for proper temporal analysis.                                                                                                                                                                                                                                                                                                                          |


### Data Quality & Anomalies Section

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Returns, sales adjustments, or data entry errors where a net negative sales amount was recorded for an item category in a given month.
    *   **Recommended handling rule:** Flag these records for further investigation. For analyses focused on positive revenue generation, these values should be excluded or set to zero.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these could result from returns, adjustments, or calculation errors where the total sales or quantity sold was negative, leading to a negative average price.
    *   **Recommended handling rule:** Flag these records. For analyses requiring valid positive prices, exclude these records or impute them with a reasonable value (e.g., the median `meanprice` for the specific `ItemCategory`).
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** Division by zero during calculation, implying that zero units were sold for an `ItemCategory` in a given month, but a sales record still exists.
    *   **Recommended handling rule:** Flag these records. For analyses requiring valid prices, exclude these records or impute them with a reasonable value (e.g., the median `meanprice` for the specific `ItemCategory`).
*   **Issue:** `RetailerZipCode` is stored as `float64`, contains missing values (0.2%), and includes unusually large numeric values (e.g., 961610393.0).
    *   **Likely cause:** Data type mismatch during ingestion, potential inclusion of extended zip codes, or data entry errors. Missing values are common in geographical fields.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Investigate and validate values that do not conform to standard 5-digit or 9-digit zip code formats. Impute missing values using `RetailerCity` or `RetailerCounty` if a reliable mapping is available; otherwise, flag as 'Unknown'.
*   **Issue:** Missing `RetailerCounty` data (0.4%).
    *   **Likely cause:** Incomplete data entry or extraction processes.
    *   **Recommended handling rule:** Impute missing values using `RetailerZipCode` or `RetailerCity` if a reliable geographical lookup or mapping can be applied. Otherwise, flag these records as 'Unknown'.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from its current object type (e.g., '01-2024') to a proper datetime object to enable accurate temporal analysis.
2.  **Address Missing Geographical Data:** For `RetailerZipCode` and `RetailerCounty`, attempt to impute missing values by cross-referencing with other available geographical fields (e.g., using a city-to-zip code or zip code-to-county mapping). Any values that cannot be reliably imputed should be flagged as 'Unknown'.
3.  **Correct `RetailerZipCode` Data Type and Format:** Convert the `RetailerZipCode` column to a string data type to preserve leading zeros and accommodate potential non-numeric entries. Validate the format of all zip codes, flagging or correcting entries that do not conform to standard formats (e.g., 5-digit or 9-digit).
4.  **Handle Negative `totalsales`:** Identify and flag all records where `totalsales` is negative. For analyses focused on positive revenue, these values should be set to zero or excluded, depending on the specific analytical objective.
5.  **Address Negative and Infinite `meanprice`:** Identify and flag records where `meanprice` is negative or infinite. For analyses requiring valid positive prices, these records should be excluded or imputed (e.g., with the median `meanprice` for the respective `ItemCategory`) to prevent skewed results.

### Limitations & Trust Section

Several data elements require further validation to ensure full trustworthiness:
*   The missing `RetailerZipCode` (0.2%) and `RetailerCounty` (0.4%) data could impact the accuracy of geographical analyses. The proposed imputation strategy needs to be validated against an authoritative source.
*   The primary key for the `sales24` table is inferred as a composite of `RetailerLicenseNumber`, `ItemCategory`, and `Date`. This assumption requires confirmation from the data source owner to guarantee uniqueness and data integrity.
*   The interpretation of the 'Date' column as representing the month and year of sales aggregation needs explicit confirmation.
*   The `RetailerZipCode` column's `float64` type and the presence of unusually large numeric values suggest potential data quality issues that warrant further investigation and validation against a known zip code directory.

### Appendix: Quick Reference

*   `Date` column converted to datetime objects for temporal analysis.
*   Missing `RetailerZipCode` and `RetailerCounty` values are imputed where possible or flagged as 'Unknown'.
*   `RetailerZipCode` is converted to string type, and its format is validated.
*   Negative `totalsales` values are flagged and handled based on the specific analytical context (e.g., set to zero for revenue calculations).
*   Negative and infinite `meanprice` values are flagged and either excluded or imputed for price-sensitive analyses.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred primary key for the `sales24` table and confirm the interpretation of the 'Date' column. Additionally, please review the proposed handling rules for negative and infinite `totalsales` and `meanprice` values, as well as the strategy for addressing missing and anomalous geographical data, to ensure they align with project objectives and data governance standards. Your feedback on the completeness and clarity of the column descriptions and cleaning notes is also appreciated.

# Work Documentation

## Table: sales24

**Data Operations:**
The `sales24` dataset was integrated into a larger sales dataframe by concatenating it with other historical sales files. During this process, the `meanprice` and `v1` columns were removed from the dataset if they were present. Several columns were renamed for consistency, such as `RetailerLicenseNumber` to `retailerlicensenumber` and `RetailerCounty` to `retailercounty`. Data types were standardized, with `totalsales` and the extracted `year` (from `date`) converted to numeric types, and the `date` column itself converted to datetime objects for temporal analysis.

Extensive cleaning and imputation were performed on geographical data. `retailercounty` values like "NA" and "UNDEFINED" were standardized to empty strings. Missing `retailercounty` values were then imputed through a multi-step process: first, by merging with a separate licenses dataset (`parent_temp`) using `retailerlicensenumber`; second, by extracting a 5-digit zip code (`zip5`) from `retailerzipcode` and merging with a HUD zip-to-county mapping; and finally, by applying several manual corrections for specific `retailerlicensenumber`s. All `retailercounty` values were converted to uppercase, and any remaining empty strings, "NA", or "nan" values were treated as missing and subsequently dropped.

The dataset was enriched by integrating `primary_company` information, derived from the licenses dataset, to identify the primary owning entity for each retailer, especially in cases of multiple owners. This allowed for a more accurate representation of market structure.

Aggregations of `totalsales` were performed by `retailerlicensenumber` and `year`, and also by `primary_company` and `year`, at both statewide and county levels. These aggregations were used to calculate market share and the Herfindahl-Hirschman Index (HHI), a measure of market concentration, for both individual retailers and parent companies.

Further analytical operations included categorizing counties based on the trajectory of their HHI over time (increasing, decreasing, or stable concentration) using linear regression. K-Means clustering was also applied to group counties with similar HHI trends. Various visualizations were generated to illustrate sales trends and HHI dynamics across different dimensions.

**Variables Affected:**
*   `meanprice`: This column was removed from the dataset.
*   `v1`: This column was removed from the dataset.
*   `RetailerLicenseNumber`, `RetailerCounty`, `RetailerFacilityType`, `RetailerCity`, `RetailerZipCode`, `Date`, `ItemCategory`, `totalsales`: These columns were renamed to `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales`, respectively, for standardization.
*   `retailercounty`: Values were extensively cleaned, standardized, and imputed using multiple external data sources and manual corrections to improve data quality and completeness.
*   `retailerzipcode`: This column was used to derive a new `zip5` column, representing the first five digits of the zip code.
*   `date`: Converted from an object type to datetime objects, and a `year` column was extracted from it.
*   `totalsales`: Converted to a numeric type and used as the basis for various aggregations and market share calculations.
*   New variables created include: `primary_company` (identifying the primary owning entity), `zip5` (5-digit zip code), `industry_sales` (total sales for a given industry segment), `mkt_share` (market share percentage), `mkt_share2` (squared market share for HHI calculation), `county_sales` (total sales at the county level), `opacity` (a calculated metric related to sales volume), `cluster` (from K-Means clustering), and `hhi_change` (year-over-year HHI percentage change).

**Logic and Methodology:**
The overarching goal of the data work was to transform raw sales data, including `sales24`, into a robust dataset suitable for in-depth market concentration analysis. The methodology involved several key steps:
1.  **Data Integration:** Combining `sales24` with other sales files created a comprehensive historical sales record, enabling longitudinal analysis.
2.  **Data Standardization and Cleaning:** Column renaming ensured consistency, while rigorous cleaning of geographical data (`retailercounty`, `retailerzipcode`) addressed inconsistencies and missing values. This was critical for accurate location-based analysis. Imputation strategies prioritized reliable external sources (license data, HUD zip-to-county mapping) to fill gaps.
3.  **Enrichment with Ownership Information:** The integration of `primary_company` allowed for a more accurate assessment of market power by aggregating sales under ultimate parent entities rather than just individual licenses.
4.  **Market Concentration Measurement:** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for market concentration. Calculations were performed at multiple granularities (individual retailer vs. parent company, statewide vs. county) to provide a nuanced view of market structure.
5.  **Trend Analysis and Segmentation:** Linear regression was applied to HHI trends over time to classify counties into categories of increasing, decreasing, or stable market concentration. K-Means clustering further segmented counties based on their HHI trajectories, facilitating targeted insights.
6.  **Visualization and Reporting:** The results were visualized using various plotting techniques to effectively communicate complex market dynamics and trends to stakeholders.

**Validation and Verification:**
Throughout the data processing, several validation and verification steps were implicitly or explicitly performed:
*   **Error Handling in Conversions:** Numeric conversions for `totalsales` and `year` used `errors="coerce"`, which converts unparseable values to `NaN`, allowing for identification and handling of problematic entries.
*   **Merge Tracking:** The use of `indicator=True` in merge operations allowed for tracking the origin of records after joins, ensuring that merges were successful and identifying unmatched data.
*   **Manual Data Correction:** Specific manual fixes for known `retailercounty` inconsistencies demonstrated a commitment to data accuracy where automated methods were insufficient.
*   **Missing Value Inspection:** The `value_counts(dropna=False)` method was used to inspect the distribution of key categorical variables like `itemcategory` and `retailercounty` at various stages, confirming the impact of cleaning steps.
*   **Uniqueness Checks:** `drop_duplicates()` was applied to source dataframes like `parent_df` and `license_county` to ensure that mappings used for enrichment were unique and consistent.
*   **Post-Processing Checks:** The final `retailercounty` column was explicitly checked for empty strings, "NA", and "nan" values, which were then dropped to ensure that subsequent analyses were performed on clean geographical data.

**Results and Outcomes:**
The data work successfully produced a refined and enriched sales dataset, saved as `sales_w_parent_co_test.dta`, which is now suitable for advanced market analysis. This dataset includes crucial `primary_company` identification and standardized geographical information. The core outcome is a comprehensive set of HHI metrics, calculated for both individual retailers and parent companies, at statewide and county levels, offering detailed insights into market concentration dynamics over time. These HHI results were exported into several structured files, including `HHI_by_county_test.xlsx`, `hhi_by_county.csv`, and `hhi_by_county_parent.csv`. Furthermore, the analytical processes, including clustering and linear regression, provided a deeper understanding of market concentration trends and identified counties exhibiting distinct HHI trajectories. The generated visualizations effectively communicate these findings, highlighting sales distributions over time by city and correlations between HHI and sales metrics.






# Table: sales25

### Overview Section

This dataset provides aggregated sales information for licensed cannabis retailers within the Track & Trace project. Each row in the `sales25` table represents a summary of sales for a specific item category by a particular retailer during a given month. The data is intended to offer insights into retail sales performance and product distribution. The overall data source is the Track & Trace system, with the collection period and extraction date currently unspecified.

**Assumptions:**
*   The `sales25` table contains aggregated sales data, likely summarized monthly, given the `Date` column format.
*   `totalsales` represents the total revenue generated for the specified item category by the retailer in that period.
*   `meanprice` represents the average price per unit for the specified item category.

### Table Inventory

*   **sales25:** Contains aggregated monthly sales data for cannabis retailers, including retailer demographics, item categories, total sales, and mean prices.

## Table: sales25

*   **Purpose:** To provide a summarized view of sales performance for various item categories across different licensed cannabis retailers over time.
*   **What one row represents:** One row represents the aggregated sales data for a specific `ItemCategory` by a unique `RetailerLicenseNumber` for a particular `Date` (month).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key, inferred).
*   **Relationships:**
*   **Number of rows and columns:** 71102 rows, 9 columns.
*   **Column Dictionary**


| Column Name           | Type    | Units        | Description                                                                              | Allowed Values / Range                   |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------|:--------|:-------------|:-----------------------------------------------------------------------------------------|:-----------------------------------------|------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |              | Unique identifier for the licensed cannabis retailer.                                    | Example: C10-0000400-LIC                 |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RetailerFacilityType  | object  |              | Type of facility operated by the retailer.                                               | Example: Cannabis - Retailer License     |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RetailerCity          | object  |              | City where the retailer's facility is located.                                           | Example: SANTA ANA                       |         0.1 | Missing values should be investigated. Consider imputation if patterns are found, or flagging for exclusion if critical.                                                                                                                                                                                                                                                                                          |
| RetailerZipCode       | float64 |              | Zip code of the retailer's facility.                                                     | Range: [90003.0, 961610393.0]            |         0.3 | Missing values should be investigated. The range includes values that appear to be concatenated ZIP+4 codes or potentially erroneous entries (e.g., 961610393.0). These should be validated against a standard ZIP code directory and potentially truncated or corrected.                                                                                                                                         |
| RetailerCounty        | object  |              | County where the retailer's facility is located.                                         | Example: ORANGE                          |         0.5 | Missing values should be investigated. Consider imputation based on RetailerCity or flagging for exclusion.                                                                                                                                                                                                                                                                                                       |
| ItemCategory          | object  |              | Category of the cannabis product sold.                                                   | Example: Flower (packaged eighth - each) |         0   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| totalsales            | float64 | USD          | Total sales revenue for the specified item category by the retailer in the given period. | Range: [-27.0, 1154419.92]               |         0   | Contains negative values. Negative sales are anomalous and likely indicate returns, adjustments, or data entry errors. These should be investigated; consider setting to 0 or excluding from aggregate calculations, or flagging for further review.                                                                                                                                                              |
| meanprice             | float64 | USD per unit | Average price per unit for the specified item category.                                  | Range: [-Infinity, 388.51]               |         0   | Contains negative and infinite values. Negative prices are anomalous and likely indicate data errors. Infinite values typically arise from division by zero (e.g., total sales divided by zero units sold). Negative values should be investigated and potentially set to 0 or excluded. Infinite values should be handled by setting to null or 0, or excluding the row, as they represent invalid calculations. |
| Date                  | object  | Month-Year   | Month and year of the sales aggregation.                                                 | Example: 01-2025                         |         0   | Should be converted to a datetime object for proper temporal analysis.                                                                                                                                                                                                                                                                                                                                            |


### Data Quality & Anomalies Section

This section summarizes identified data quality issues and anomalies within the `sales25` table.

*   **Issue:** Negative `totalsales` values.
    *   **Likely cause:** Data entry errors, processing errors, or potentially legitimate (but unusual) returns/adjustments that result in a net negative for the period.
    *   **Recommended handling rule:** Investigate the business logic for negative sales. For analytical purposes, consider treating these as zero sales or excluding them from calculations of positive revenue. Flag these records for further review by data owners.
*   **Issue:** Negative `meanprice` values.
    *   **Likely cause:** Similar to `totalsales`, these are likely data entry or processing errors. A physical product cannot have a negative price.
    *   **Recommended handling rule:** Treat these as invalid. Set `meanprice` to `NULL` or `0` for these records, or exclude the entire row from analyses that rely on valid pricing. Flag for review.
*   **Issue:** Infinite `meanprice` values.
    *   **Likely cause:** This typically occurs when `totalsales` is divided by a quantity of zero (e.g., `total_sales / 0_units`). This suggests a record where sales revenue was reported but no units were sold, or the unit count was erroneously zero.
    *   **Recommended handling rule:** Treat these as invalid. Set `meanprice` to `NULL` or `0` for these records, or exclude the entire row from analyses. Flag for review.
*   **Issue:** Missing values in `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, attempt to impute based on `RetailerLicenseNumber` if historical data exists, or use a general 'Unknown' category. For `RetailerZipCode`, validate existing values and impute missing ones based on `RetailerCity` or `RetailerCounty` if possible, otherwise flag as unknown.
*   **Issue:** Anomalous `RetailerZipCode` values (e.g., `961610393.0`).
    *   **Likely cause:** Potential concatenation of ZIP+4 codes without proper formatting, or data entry errors.
    *   **Recommended handling rule:** Standardize `RetailerZipCode` to a 5-digit format. For values exceeding 5 digits, attempt to parse as ZIP+4 and retain only the 5-digit ZIP. Validate against a known list of valid 5-digit US zip codes. Flag or set to `NULL` any values that remain invalid after this process.

### Reproducible Cleaning Plan

1.  **Standardize Date Format:** Convert the `Date` column from `object` type (e.g., "01-2025") to a standard datetime format (e.g., `YYYY-MM-DD` representing the first day of the month) to enable proper temporal analysis.
2.  **Address Missing Geographic Data:** For `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`, identify and flag rows with missing values. Attempt to impute missing `RetailerCity` and `RetailerCounty` values using a lookup table based on `RetailerLicenseNumber` if available, or fill with 'Unknown'.
3.  **Clean RetailerZipCode:** Convert `RetailerZipCode` to string type. For values longer than 5 digits, attempt to extract the first 5 digits. Validate all zip codes against a list of valid 5-digit US zip codes. Flag or set to `NULL` any values that remain invalid after this process.
4.  **Handle Negative `totalsales`:** Identify all rows where `totalsales` is less than 0. For analytical purposes, these values will be set to 0, and a new flag column (`is_negative_sales_adjusted`) will be created to indicate these adjustments.
5.  **Handle Negative and Infinite `meanprice`:** Identify all rows where `meanprice` is less than 0 or is infinite. These values will be set to `NULL`, and a new flag column (`is_anomalous_price_adjusted`) will be created to indicate these adjustments.

### Limitations & Trust Section

The trustworthiness of the `sales25` dataset is impacted by several factors:

*   **Incomplete Geographic Data:** Missing values in `RetailerCity`, `RetailerZipCode`, and `RetailerCounty` reduce the ability to perform granular geographic analysis. Validation against an external, authoritative source of retailer addresses is needed.
*   **Anomalous Sales and Price Data:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry errors, processing issues, or unusual business events (e.g., large returns). Without further context or validation, these fields may not accurately reflect true sales performance. A clear understanding of the business rules for returns and adjustments is needed to validate these anomalies.
*   **Inferred Primary Key:** The primary key (`RetailerLicenseNumber`, `ItemCategory`, `Date`) is inferred. Confirmation from the data source owner is required to ensure uniqueness and integrity.
*   **Zip Code Accuracy:** The wide range and format of `RetailerZipCode` suggest potential inaccuracies or non-standard storage. Validation against a current, authoritative zip code database is crucial.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` column to datetime objects (e.g., `YYYY-MM-01`).
*   **Missing Geographic Data:** Impute or flag missing `RetailerCity`, `RetailerZipCode`, `RetailerCounty`.
*   **Zip Code Standardization:** Truncate `RetailerZipCode` to 5 digits and validate against known US zip codes.
*   **Negative Sales Handling:** Set `totalsales < 0` to `0` and flag.
*   **Anomalous Price Handling:** Set `meanprice < 0` or `meanprice = Infinity` to `NULL` and flag.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for the `sales25` table. Special attention should be paid to the proposed handling rules for negative and infinite `totalsales` and `meanprice` values, ensuring they align with business requirements for analysis. Additionally, the approach to standardizing and validating `RetailerZipCode` should be reviewed for robustness and accuracy against official geographic data sources. Confirmation of the data collection period and extraction date would also be beneficial.

# Work Documentation

## Table: sales25

**Data Operations:**
*   **Data Ingestion and Consolidation:** Multiple `sales*.csv` files (from 2018 to 2024) were loaded and concatenated into a single dataset. Notably, during this process, the `meanprice` and `v1` columns were explicitly dropped if present. This deviates from the Codebook's cleaning plan which specified handling for negative and infinite `meanprice` values.
*   **Column Renaming:** Column names were standardized to a consistent snake_case format (e.g., `ItemCategory` to `itemcategory`, `RetailerLicenseNumber` to `retailerlicensenumber`).
*   **Data Sorting:** The dataset was sorted by `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales`.
*   **External Data Integration (Parent Company Information):** The sales data was left-merged with an external "Cannabis Market Intelligence Platform Report - Licenses" dataset (`parent_temp`) using `retailerlicensenumber`. This introduced `primary_company` and `cannabiz_county` into the sales dataset.
*   **Geographic Data Cleaning and Imputation (`retailercounty`):**
    *   Initial cleanup: "NA" and "UNDEFINED" string values in `retailercounty` were replaced with empty strings.
    *   Imputation from Cannabiz data: Missing `retailercounty` values were filled using `cannabiz_county` from the merged parent company data, based on a predefined mapping.
    *   Manual corrections: Specific `retailercounty` values were manually updated for certain `retailerlicensenumber` entries.
    *   Standardization: `retailercounty` values were converted to uppercase.
    *   Self-imputation: A lookup table of unique `retailerlicensenumber`-`retailercounty` pairs was created from the existing data and used to fill further missing `retailercounty` values.
    *   Imputation from ZIP code data: The first five digits of `retailerzipcode` were extracted to create a `zip5` column. This `zip5` was then used to merge with an external HUD ZIP-to-County mapping (`zip_df`) to impute additional missing `retailercounty` values.
    *   Final manual corrections: Another set of specific `retailercounty` values were manually updated.
    *   Missing value handling: Remaining `NaN` values were filled with empty strings, and the entire dataframe was converted to string type before an intermediate save. The Codebook's plan to flag missing geographic values was not explicitly implemented; instead, imputation was prioritized.
*   **Date and Numeric Conversion:** The `date` column was used to extract a `year` column, and both `totalsales` and `year` were converted to numeric types for analysis. The `date` column itself was not consistently converted to a datetime object for the primary HHI calculation path, which partially deviates from the Codebook's recommendation.
*   **Market Concentration Analysis (Herfindahl-Hirschman Index - HHI):**
    *   Aggregated sales data by `retailerlicensenumber` (or `primary_company`), `year`, and `retailercounty`.
    *   Calculated `industry_sales` (total sales for a given year/county/grow type).
    *   Computed `mkt_share` (market share) and `mkt_share2` (squared market share).
    *   Aggregated `mkt_share2` to derive HHI values at statewide and county levels, for both individual retailers and parent companies.
    *   **Note on `totalsales`:** The Codebook's cleaning plan to set negative `totalsales` to 0 and flag them was not implemented; negative values were retained in the dataset for HHI calculations.
*   **Trend Analysis and Clustering:** HHI data was used for linear regression to identify increasing, decreasing, or stable HHI trends by county, and K-Means clustering was applied to group counties based on HHI trends.
*   **Visualization Data Preparation:** Data was prepared for various plots, including line plots of HHI over time, bar plots of HHI by county, and plots of HHI change.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales`.
*   **City-level Sales Analysis:** Monthly total sales were aggregated by `retailercity` and `date` to analyze sales trends for the top 10 cities.

**Variables Affected:**
*   **Modified:** `retailercounty`, `retailerzipcode` (used to derive `zip5`), `date` (used to derive `year`), `totalsales` (converted to numeric).
*   **Created:** `primary_company`, `cannabiz_county`, `zip5`, `_merge_lic_county`, `_merge_zip`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Dropped:** `meanprice`, `v1`.

**Logic and Methodology:**
*   The primary intent was to consolidate sales data, enrich it with retailer ownership and geographic information, and then analyze market concentration using the Herfindahl-Hirschman Index (HHI).
*   A robust imputation strategy was employed for `retailercounty`, leveraging multiple external and internal data sources (Cannabiz license data, HUD ZIP-to-County mapping, and internal consistency checks) to maximize geographic coverage and accuracy. Manual fixes addressed specific known data issues. The approach prioritized imputation over flagging missing values, which was a deviation from the Codebook's recommendation.
*   HHI calculations were performed at different granularities (statewide vs. county, individual retailer vs. parent company) to provide a comprehensive view of market concentration dynamics.
*   Trend analysis and clustering aimed to categorize counties based on their HHI evolution over time, providing insights into market stability or shifts.
*   The explicit dropping of the `meanprice` column suggests that this variable was either deemed unreliable or not relevant for the specific market concentration analysis being performed, despite its description and cleaning notes in the original Codebook. Similarly, the non-implementation of the negative `totalsales` handling suggests a different analytical approach or an oversight regarding data quality issues identified in the Codebook.

**Validation and Verification:**
*   Merge indicators (`_merge_lic_county`, `_merge_zip`) were used internally during the merging process to track the source of `retailercounty` values and identify records that were matched or updated.
*   `value_counts(dropna=False)` was used to inspect the distribution of `itemcategory` and `retailercounty` at various stages, indicating checks for completeness and consistency.
*   The `retailercounty` column was explicitly checked for `NA`, `UNDEFINED`, empty strings, and `nan` values at multiple points, with corresponding cleaning actions.
*   Numeric conversions (`pd.to_numeric`) used `errors="coerce"` to handle non-numeric values gracefully, converting them to `NaN`.
*   The final HHI results were rounded and converted to integer/string types for export, implying a final review of data types.
*   **Discrepancy Note:** It is important to note that the explicit validation and handling rules for negative `totalsales` and negative/infinite `meanprice` as outlined in the Codebook's "Reproducible Cleaning Plan" were not observed in the provided Python code. The `meanprice` column was dropped, and negative `totalsales` values were retained without adjustment or flagging.

**Results and Outcomes:**
*   A cleaned and enriched `sales` dataset (`sales_w_parent_co_test.dta`) was produced, containing standardized column names, imputed geographic information, and `primary_company` identifiers.
*   Comprehensive HHI metrics were calculated for various geographic and ownership levels, providing quantitative measures of market concentration.
*   Trend analysis identified counties with increasing, decreasing, or stable HHI trajectories.
*   Clustering grouped counties with similar HHI trends.
*   Several output files were generated (`Cult_HHI_DeepDive.xlsx`, `Cult_HHI_Summary.csv`, `Cult_Size_vs_HHI.csv`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`), containing the calculated HHI values and related metrics, ready for further reporting and visualization.
*   Various plots (Matplotlib, Plotly) were generated to visualize sales trends, HHI over time, and HHI changes, providing visual insights into market dynamics.






# Table: sales25q2

### Overview Section

This dataset provides detailed sales transaction records from the Track & Trace project, focusing on cannabis retail operations. It captures key information about retailers, product categories, and sales figures over a specified period. Each row in the `sales25q2` table represents a single sales record or aggregated sales entry for a specific item category at a retailer for a given period. The overall data source is the Track & Trace system, with the collection period inferred to be Q2 2025 based on table and date column names. The extraction date is not specified.

**Assumptions:**
*   The `sales25q2` table contains sales data specifically for the second quarter of 2025.
*   `totalsales` and `meanprice` are denominated in a local currency (e.g., USD).
*   `RetailerLicenseNumber` uniquely identifies a retailer.

### Table Inventory

*   **sales25q2:** Contains detailed sales transaction data, including retailer information, item categories, total sales, and mean prices for Q2 2025.

## Table: sales25q2

*   **Purpose:** To provide granular sales data for cannabis products, enabling analysis of retailer performance, product category trends, and pricing dynamics within the specified quarter.
*   **What one row represents:** One aggregated sales record for a specific item category at a particular retailer for a given period (likely monthly, given the 'Date' format).
*   **Primary key(s):**
*   **Relationships:**
*   **Number of rows and columns:** 72325 rows, 10 columns

### Column Dictionary


| Column Name           | Type    | Units             | Description                                                                      | Allowed Values / Range       | Missing %   | Cleaning / Notes                                                                                                                                                                                                                                                                                                   |
|:----------------------|:--------|:------------------|:---------------------------------------------------------------------------------|:-----------------------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                   | Unique identifier for the licensed cannabis retailer.                            |                              | 0.0%        |                                                                                                                                                                                                                                                                                                                    |
| RetailerFacilityType  | object  |                   | Type of facility operated by the retailer (e.g., 'Cannabis - Retailer License'). |                              | 0.0%        |                                                                                                                                                                                                                                                                                                                    |
| RetailerCity          | object  |                   | City where the retailer's facility is located.                                   |                              | 0.1%        | Missing values observed. Investigate cause; consider imputation or flagging for analysis.                                                                                                                                                                                                                          |
| RetailerZipCode       | float64 |                   | Zip code of the retailer's facility.                                             | 90003.0 - 961610393.0        | 0.3%        | Missing values observed. Investigate cause; consider imputation or flagging. Anomalous upper range value (961610393.0) suggests potential data entry errors or concatenated zip codes; validate against standard zip code formats.                                                                                 |
| RetailerCounty        | object  |                   | County where the retailer's facility is located.                                 |                              | 0.5%        | Missing values observed. Investigate cause; consider imputation or flagging for analysis.                                                                                                                                                                                                                          |
| ItemCategory          | object  |                   | Category of the cannabis item sold (e.g., 'Extract (weight - each)').            |                              | 0.0%        |                                                                                                                                                                                                                                                                                                                    |
| totalsales            | float64 | Currency          | Total sales amount for the item category.                                        | -4.78 - 3311600.34           | 0.0%        | Contains negative values. Likely cause: returns, refunds, or data entry errors. Proposed handling: Flag negative values for investigation; consider excluding from sum calculations or treating as zero if confirmed as returns.                                                                                   |
| meanprice             | float64 | Currency per unit | Average price per unit for the item category.                                    | -1.59333333333333 - Infinity | 0.0%        | Contains negative and infinite values. Negative values likely due to negative sales or returns. Infinite values suggest division by zero (e.g., quantity sold was zero). Proposed handling: Flag negative and infinite values; exclude from mean calculations or impute with a reasonable value if context allows. |
| Date                  | object  |                   | Month and year of the sales record.                                              | 04-2025                      | 0.0%        | Currently stored as an object; convert to datetime format for proper temporal analysis.                                                                                                                                                                                                                            |
| ItemGroup             | object  |                   | Broader grouping for item categories (e.g., 'Extract/Concentrate').              |                              | 0.0%        |                                                                                                                                                                                                                                                                                                                    |


### Data Quality & Anomalies Section

The dataset exhibits several data quality issues that require attention:

*   **Issue:** Negative values in `totalsales`.
    *   **Likely cause:** These typically indicate returns, refunds, or potential data entry errors where a credit was recorded as a negative sale.
    *   **Recommended handling rule:** Flag these records for further investigation. For aggregate analysis, consider excluding them from positive sales sums or treating them as zero if they represent legitimate returns.
*   **Issue:** Negative values in `meanprice`.
    *   **Likely cause:** Similar to `totalsales`, negative mean prices could result from returns or incorrect calculations based on negative sales figures.
    *   **Recommended handling rule:** Flag these records. Exclude them from average price calculations or treat as `NaN` to prevent skewing statistical measures.
*   **Issue:** Infinite values in `meanprice`.
    *   **Likely cause:** Infinite values usually arise from division by zero, implying that the quantity sold for a particular item category was zero while a sales value was recorded, or a calculation error occurred.
    *   **Recommended handling rule:** Flag these records. Replace infinite values with `NaN` or exclude them from calculations to maintain data integrity.
*   **Issue:** Missing values in `RetailerCity` (0.1%), `RetailerZipCode` (0.3%), and `RetailerCounty` (0.5%).
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, consider imputing based on `RetailerZipCode` if a reliable mapping exists, or flag records with missing geographical information for exclusion from location-based analyses. For `RetailerZipCode`, investigate if it can be inferred from other retailer details or if it's consistently missing for certain retailers.
*   **Issue:** Anomalous upper range for `RetailerZipCode` (e.g., `961610393.0`).
    *   **Likely cause:** Data entry error, concatenation of multiple zip codes, or inclusion of non-standard postal codes. Standard US zip codes are 5 or 9 digits.
    *   **Recommended handling rule:** Validate `RetailerZipCode` values against known zip code formats. Flag or correct values that fall outside expected ranges or formats.

### Reproducible Cleaning Plan

1.  **Convert Date Column:** Convert the `Date` column from object type to a datetime format (e.g., `YYYY-MM-DD` for the first day of the month) to enable proper temporal analysis.
2.  **Handle Missing Geographical Data:** For `RetailerCity`, `RetailerZipCode`, and `RetailerCounty`, identify and flag records with missing values. If possible, impute missing city/county based on a valid zip code mapping; otherwise, exclude these records from geographical analyses.
3.  **Validate RetailerZipCode:** Identify and flag `RetailerZipCode` values that are outside the standard 5-digit or 9-digit US zip code format. Investigate these anomalies for correction or exclusion.
4.  **Address Negative `totalsales`:** Flag all records where `totalsales` is negative. For analyses requiring positive sales, create a derived column `adjusted_totalsales` where negative values are set to 0 or `NaN`.
5.  **Address Negative and Infinite `meanprice`:** Flag all records where `meanprice` is negative or infinite. For analyses requiring valid mean prices, create a derived column `adjusted_meanprice` where these anomalous values are set to `NaN`.
6.  **Document Cleaning Actions:** Maintain a log of all cleaning steps, including the number of records affected and the rationale for each transformation.

### Limitations & Trust Section

The current dataset has several limitations that impact its trustworthiness and the scope of analysis:

*   **Missing Primary Keys and Relationships:** The absence of explicitly defined primary keys and foreign key relationships makes it difficult to ensure data uniqueness, integrity, and to confidently join this table with other potential datasets. Validation of `RetailerLicenseNumber` as a unique identifier is needed.
*   **Geographical Data Incompleteness:** Missing and potentially erroneous `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` values limit the accuracy of location-based analyses and regional aggregations. Validation against a master retailer list or geographical database is required.
*   **Anomalous Sales and Pricing Data:** The presence of negative and infinite values in `totalsales` and `meanprice` indicates potential data entry errors, system glitches, or unhandled business logic (e.g., returns). Without clear definitions or business rules for these scenarios, the accuracy of aggregated sales and pricing metrics is compromised.
*   **Data Source and Extraction Details:** The lack of specific data source documentation, exact collection period, and extraction date reduces the auditability and reproducibility of the data.

To validate these elements, access to the original Track & Trace system documentation, business rules for sales and returns, and a master list of retailer information (including validated addresses and license numbers) would be crucial.

### Appendix: Quick Reference

*   **Date Conversion:** Convert `Date` column to datetime objects for accurate time-series analysis.
*   **Geographical Data Validation:** Cross-reference `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` with a reliable geographical database.
*   **Handle Missing Geographicals:** Flag or impute missing `RetailerCity`, `RetailerZipCode`, and `RetailerCounty` values.
*   **Negative Sales Handling:** Flag negative `totalsales` values; consider excluding from positive sum calculations.
*   **Anomalous Price Handling:** Flag negative and infinite `meanprice` values; exclude from average price calculations.
*   **Zip Code Correction:** Identify and correct or flag non-standard `RetailerZipCode` entries.

### Notes for Reviewers

Reviewers are requested to verify the accuracy of the inferred column descriptions and proposed handling rules for anomalies. Particular attention should be paid to the interpretation of negative and infinite values in `totalsales` and `meanprice`, as their appropriate handling depends heavily on business context. Additionally, please confirm the assumptions made regarding the dataset's scope and currency. Feedback on potential primary keys or relationships with other Track & Trace tables would be highly valuable for enhancing data integrity.

# Work Documentation

## Table: sales25q2

**Data Operations:**
The provided Python code does not directly process a table named `sales25q2` or data specifically for Q2 2025. Instead, it processes a broader historical sales dataset (`sales_df`) covering years 2018-2024, which shares a similar structure and column names with the `sales25q2` table described in the Codebook. The following operations were performed on this `sales_df` and related datasets:

*   **Data Ingestion & Concatenation:** Multiple historical sales CSV files (from 2018 to 2024) were loaded and combined into a single DataFrame (`sales_df`). All columns were initially read as strings, and empty strings were preserved.
*   **Column Management:**
    *   Columns named `meanprice` and `v1` were removed from the `sales_df` if present.
    *   Several columns were consistently renamed for standardization (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `ItemCategory` to `itemcategory`, `Date` to `date`, `totalsales` to `totalsales`).
*   **Data Sorting:** The dataset was sorted by multiple key identifiers and temporal columns (`retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, `totalsales`) to ensure consistent ordering.
*   **External Data Integration:** The sales data was enriched by performing a left merge with a `parent_df` (derived from an external "Cannabis Market Intelligence Platform Report - Licenses" CSV) using `retailerlicensenumber` as the key. Records present only in the `parent_df` were excluded.
*   **Geographical Data Cleaning & Imputation:**
    *   Missing or undefined `retailercounty` values ("NA", "UNDEFINED", empty strings) were standardized.
    *   A predefined `county_map` was applied to normalize county names (e.g., "Alameda County" to "ALAMEDA"), primarily using `cannabiz_county` (from the merged `parent_df`) to fill in initially missing `retailercounty` values.
    *   Specific `retailerlicensenumber` values had their `retailercounty` manually corrected based on known data issues.
    *   All `retailercounty` values were converted to uppercase for consistency.
    *   Missing `retailercounty` values were further imputed by:
        1.  Leveraging existing `retailercounty` information associated with a `retailerlicensenumber` across the dataset.
        2.  Truncating `retailerzipcode` to 5 digits (`zip5`) and merging with an external `zip_df` (a HUD ZIP-to-County mapping) to fill in additional missing county information.
    *   More manual corrections were applied to `retailercounty` for specific `retailerlicensenumber` values.
    *   Finally, any remaining empty strings, "NA", or "nan" in `retailercounty` were converted to missing values (`pd.NA`), and rows with missing `retailercounty` were dropped to ensure data quality for geographical analysis.
*   **Data Type Conversion:** `totalsales` and `year` (extracted from the `date` column) were converted to numeric types, with errors coerced to `NaN` to prevent processing failures.
*   **Hierarchical HHI Calculation:** The Herfindahl-Hirschman Index (HHI) was calculated at multiple levels of aggregation:
    *   Overall (individual retailer) and Parent Company level.
    *   Statewide and County-level.
    *   This involved grouping data by `retailerlicensenumber` or `primary_company` (parent company ID), `retailercounty`, and `year`, summing `totalsales`, calculating market share, and then squaring and summing market shares.
    *   `primary_company` was imputed with `retailerlicensenumber` where it was missing to ensure all entities were accounted for in parent company analysis.
*   **Derived Metrics:** New columns such as `industry_sales`, `mkt_share`, `mkt_share2`, `county_sales`, `county_sales_parent`, `opacity`, and `opacity_parent` were created to support HHI analysis and visualization.
*   **Clustering and Trend Analysis:** K-Means clustering was applied to HHI trends over time to identify groups of counties with similar market concentration patterns. Linear regression was used to categorize counties into "increasing," "decreasing," or "stable" HHI trajectories based on the slope of HHI values over years (from 2019 onwards).
*   **Percentage Change Calculation:** Year-over-year percentage change in HHI was calculated to show dynamic shifts in market concentration.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales` to understand relationships between market concentration and sales volumes.
*   **Aggregation for Visualization:** Sales data was aggregated by `date` and `retailercity` to analyze sales trends over time for the top 10 cities by total sales.
*   **Output Generation:** Various intermediate and final results were exported to CSV and Excel files (e.g., `sales_w_parent_co_test.dta`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, `HHI_by_county_test.xlsx`). Numerous plots were generated and displayed using `matplotlib`, `seaborn`, and `plotly`, with some saved as HTML files for interactive viewing.

**Variables Affected:**
*   **Modified:** `meanprice` (dropped), `v1` (dropped), `ItemCategory` (renamed to `itemcategory`), `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, cleaned, imputed, normalized), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `Date` (renamed to `date`, converted to datetime, `year` extracted), `totalsales` (renamed to `totalsales`, converted to numeric), `primary_company` (imputed, converted to numeric).
*   **Created:** `companyid`, `county`, `statelicenseid`, `multi_owner`, `primary_company`, `licenseNumber`, `zip5`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Validated:** `retailercounty`, `retailerzipcode`, `totalsales`.

**Logic and Methodology:**
The primary objective of the data work was to prepare a comprehensive sales dataset for in-depth market concentration analysis using the Herfindahl-Hirschman Index (HHI). A multi-step data cleaning and imputation process was employed for geographical information (`retailercounty`, `retailerzipcode`) by leveraging internal data consistency, external mapping files (HUD ZIP-to-County), and targeted manual corrections. This meticulous approach aimed to maximize the completeness and accuracy of location data, which is critical for reliable county-level analysis. HHI was calculated at both individual retailer and parent company levels, and for both statewide and county-level scopes, to provide a granular view of market concentration dynamics. This involved standard market share calculations and subsequent aggregation. Time-series analysis was performed on HHI values to understand trends over years, including categorizing counties by their HHI trajectory (increasing, decreasing, stable) using linear regression. Clustering techniques were applied to group counties with similar HHI trend patterns, aiding in identifying distinct market dynamics. Sales data was aggregated and visualized to provide insights into overall market performance and city-level contributions.

**Validation and Verification:**
Data type conversions for numeric fields (`totalsales`, `year`) were performed with error coercion, indicating an awareness of potential data inconsistencies and a strategy to handle them gracefully. Merge indicators (`_merge`, `_merge_lic_county`, `_merge_zip`) were utilized during data integration steps to track the success and source of merged records, serving as an internal validation mechanism. Explicit dropping of rows with missing `retailercounty` after multiple imputation attempts suggests a commitment to a high standard of geographical data quality for subsequent analyses. The code includes steps to identify and handle empty strings, "NA", and "nan" values, demonstrating a focus on data completeness and consistency. The generation of numerous plots and summary tables serves as a visual and statistical verification of the transformations and calculations, allowing for quick identification of anomalies or unexpected results.

**Results and Outcomes:**
A cleaned, standardized, and enriched historical sales dataset (`sales_w_parent_co_test.dta`) was produced, suitable for advanced analytical tasks. Comprehensive HHI metrics were calculated across various geographical and organizational levels (statewide, county, retailer, parent company) and over time (2018-2024). Insights into market concentration trends were generated, including the identification of counties with increasing, decreasing, or stable HHI, and clusters of counties with similar HHI trajectories. Key summary tables and visualizations were created, providing a clear overview of sales performance, market concentration, and geographical dynamics. The analysis identified top-performing cities and counties, as well as those experiencing significant shifts in market concentration. The output files (CSV, Excel, HTML plots) provide actionable data and visualizations for further reporting and decision-making.






# Table: salesquantity18

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
*   **Column Dictionary**


| Column Name           | Type    | Units    | Description                                                              | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                 |
|:----------------------|:--------|:---------|:-------------------------------------------------------------------------|:-------------------------------------|------------:|:-------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier for the retailer's license.                            | Example: C10-0000004-LIC             |           0 |                                                                                                  |
| RetailerFacilityType  | object  |          | Type of facility associated with the retailer license.                   | Example: Cannabis - Retailer License |           0 |                                                                                                  |
| RetailerCity          | object  |          | City where the retailer facility is located.                             | Example: PALM SPRINGS                |           0 |                                                                                                  |
| RetailerZipCode       | int64   |          | Zip code of the retailer facility.                                       | [922624021.0, 922624021.0]           |           0 |                                                                                                  |
| RetailerCounty        | float64 |          | County where the retailer facility is located.                           |                                      |         100 | 100% missing values. This column is entirely empty.                                              |
| ItemCategory          | object  |          | Category of the cannabis item sold.                                      | Example: flowereighth                |           0 |                                                                                                  |
| Date                  | object  |          | Month and year of the aggregated sales data.                             | Example: 11-2018                     |           0 | Currently stored as a string (object). Should be converted to datetime for time-series analysis. |
| totalgrams            | float64 | grams    | Total grams sold for the given item category, retailer, and month.       | [21.0, 2432.5]                       |           0 |                                                                                                  |
| totalsales            | float64 | USD      | Total sales revenue for the given item category, retailer, and month.    | [201.85, 33892.26]                   |           0 |                                                                                                  |
| meanprice             | float64 | USD/gram | Average price per gram for the given item category, retailer, and month. | [48.7658417266187, 83.1406593406593] |           0 |                                                                                                  |


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






# Table: salesquantity19

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
*   **Column Dictionary**


| Column Name           | Type    | Units    | Description                                                                                     | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                      |
|:----------------------|:--------|:---------|:------------------------------------------------------------------------------------------------|:-------------------------------------|------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier for the licensed cannabis retailer.                                           | Example: C10-0000004-LIC             |           0 |                                                                                                                                                                                                       |
| RetailerFacilityType  | object  |          | Type of facility operated by the retailer.                                                      | Example: Cannabis - Retailer License |           0 |                                                                                                                                                                                                       |
| RetailerCity          | object  |          | City where the retailer's facility is located.                                                  | Example: PALM SPRINGS                |           0 |                                                                                                                                                                                                       |
| RetailerZipCode       | int64   |          | Zip code of the retailer's facility. May include ZIP+4 or be concatenated.                      | Range: [90021.0, 961610393.0]        |           0 | The range and example value (922624021) suggest this might be a concatenated ZIP+4 code or an improperly formatted string. Verification of format and potential truncation/splitting may be required. |
| RetailerCounty        | float64 |          | County where the retailer's facility is located.                                                |                                      |         100 | All values are missing. This column is unusable as is. Consider dropping or investigating if county data can be derived from other location fields.                                                   |
| ItemCategory          | object  |          | Category of the cannabis product sold.                                                          | Example: flowerquarter               |           0 |                                                                                                                                                                                                       |
| Date                  | object  |          | Month and year of the aggregated sales data.                                                    | Example: 01-2019                     |           0 | Currently stored as an object (string). Should be converted to a datetime format for proper temporal analysis.                                                                                        |
| totalgrams            | float64 | grams    | Total quantity of the item category sold in grams for the given month.                          | Range: [0.4819415, 116269.5]         |           0 | Values are non-negative, which is expected for quantities.                                                                                                                                            |
| totalsales            | float64 | USD      | Total sales revenue in USD for the item category sold in the given month.                       | Range: [0.99, 865567.25]             |           0 | Values are non-negative, which is expected for sales revenue.                                                                                                                                         |
| meanprice             | float64 | USD/gram | Average price per gram for the item category sold in the given month (totalsales / totalgrams). | Range: [0.8045, 248.0]               |           0 | Values are non-negative, which is expected for price. Division by zero is not observed as minimum totalgrams is > 0.                                                                                  |


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






# Table: salesquantity20

### Overview Section

This dataset provides detailed sales quantity and value information for cannabis products within the Track & Trace project. It captures transactional summaries at the retailer level, categorized by product type and reported for specific periods. Each row in the `salesquantity20` table represents the aggregated sales data for a particular item category at a specific licensed retailer for a given month. The overall data source is the Track & Trace system, with the collection period implied to be around 2020 based on the table name and date examples. The exact extraction date is not available.

**Assumptions:**
*   The `Date` column in `salesquantity20` represents a month-year period (MM-YYYY).
*   `totalsales` is denominated in USD.
*   `totalgrams` refers to the total weight in grams.

### Table Inventory

*   **salesquantity20:** Contains aggregated monthly sales quantities, total sales revenue, and mean prices for various cannabis product categories sold by licensed retailers.

## Table: salesquantity20

*   **Purpose:** To provide a summary of sales performance, including quantities sold, total revenue, and average pricing, for different cannabis product categories across various retailers.
*   **What one row represents:** One monthly sales record for a specific item category at a particular licensed retailer.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 38758 rows, 10 columns

### Column Dictionary


| Column Name           | Type    | Units    | Description                                                                                                         | Allowed Values / Range            |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                               |
|:----------------------|:--------|:---------|:--------------------------------------------------------------------------------------------------------------------|:----------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier for the licensed cannabis retailer.                                                               | e.g., C10-0000182-LIC             |         0   |                                                                                                                                                                                                                                                                |
| RetailerFacilityType  | object  |          | Type of facility operated by the retailer (e.g., Cannabis - Retailer License).                                      | e.g., Cannabis - Retailer License |         0   |                                                                                                                                                                                                                                                                |
| RetailerCity          | object  |          | City where the retailer's facility is located.                                                                      | e.g., REDWAY                      |         0   |                                                                                                                                                                                                                                                                |
| RetailerZipCode       | object  |          | Zip code of the retailer's facility.                                                                                | e.g., 95560                       |         0   |                                                                                                                                                                                                                                                                |
| RetailerCounty        | object  |          | County where the retailer's facility is located.                                                                    | e.g., TUOLUMNE                    |        99.9 | High percentage of missing values (99.9%). This column is largely unreliable for analysis. Consider imputation from RetailerZipCode or RetailerCity if a reliable mapping exists, otherwise flag as unreliable or exclude from analyses requiring county data. |
| ItemCategory          | object  |          | Category of the cannabis product sold (e.g., flower, edibles).                                                      | e.g., flowereighth                |         0   |                                                                                                                                                                                                                                                                |
| Date                  | object  |          | Month and year of the sales record.                                                                                 | e.g., 01-2020                     |         0   | Convert to datetime object for proper temporal analysis. Assumed format is MM-YYYY.                                                                                                                                                                            |
| totalgrams            | float64 | grams    | Total quantity of the item category sold in grams for the given period.                                             | [0.4819415, 478256.2]             |         0   | Values are non-negative, which is expected for quantities.                                                                                                                                                                                                     |
| totalsales            | float64 | USD      | Total sales revenue in USD for the item category for the given period.                                              | [0.63, 5803939.28]                |         0   | Values are non-negative, which is expected for sales revenue.                                                                                                                                                                                                  |
| meanprice             | float64 | USD/gram | Average price per gram for the item category for the given period, typically calculated as totalsales / totalgrams. | [0.5, 367.82]                     |         0   | Values are non-negative and within a plausible range for cannabis pricing.                                                                                                                                                                                     |


### Data Quality & Anomalies Section

*   **Issue:** `RetailerCounty` column has 99.9% missing values.
    *   **Likely cause:** Data was either not collected, not recorded, or failed to be extracted for this field during the data generation process.
    *   **Recommended handling rule:** Due to the overwhelming percentage of missing values, this column should be flagged as unreliable for direct analysis. If county-level analysis is critical, consider attempting to impute values based on `RetailerZipCode` or `RetailerCity` using an external, validated mapping dataset. Otherwise, exclude it from analyses requiring complete geographical information.

### Reproducible Cleaning Plan

1.  **Handle Missing County Data:** Evaluate the necessity of the `RetailerCounty` column for downstream analysis. If required, attempt to impute missing values using a reliable external mapping from `RetailerZipCode` or `RetailerCity`. If not critical or imputation is unreliable, exclude the column from the analytical dataset.
2.  **Standardize Date Format:** Convert the `Date` column from its current object (string) type to a proper datetime object (e.g., `YYYY-MM-DD` or `YYYY-MM-01` to represent the start of the month). This will enable accurate temporal filtering and aggregation.
3.  **Verify Numeric Data Types:** Confirm that `totalgrams`, `totalsales`, and `meanprice` are correctly interpreted as numeric (float64) types to prevent calculation errors.

### Limitations & Trust Section

The `RetailerCounty` column is highly unreliable due to 99.9% missing values. Any analysis relying on county-level granularity would be severely compromised or impossible without significant imputation efforts, which would introduce assumptions and potential inaccuracies. The interpretation of the `Date` column as representing a month-year period (MM-YYYY) is an assumption based on the example format; validation with the data source owner would confirm this. The absence of explicit primary key constraints or relationship definitions in the provided metadata means these were inferred and should be verified.

### Appendix: Quick Reference

*   **County Data:** `RetailerCounty` is 99.9% missing; do not use for direct analysis without imputation.
*   **Date Conversion:** Convert `Date` (MM-YYYY) to datetime objects for temporal analysis.
*   **Numeric Validation:** `totalgrams`, `totalsales`, `meanprice` are float64 and non-negative.
*   **Primary Key:** `RetailerLicenseNumber`, `ItemCategory`, `Date` is the inferred composite primary key.

### Notes for Reviewers

Reviewers should verify the accuracy of the inferred primary key for `salesquantity20` and confirm the assumed MM-YYYY format for the `Date` column. Additionally, any proposed imputation strategy for `RetailerCounty` should be thoroughly reviewed for its methodology and potential impact on data integrity and analytical outcomes. The descriptions and units for all columns should be cross-referenced with source system documentation if available.

# Work Documentation

## Table: salesquantity20

**Data Operations:**
*   **Data Ingestion & Consolidation:** Multiple annual sales CSV files (e.g., `sales18.csv` through `sales24.csv`) were loaded and concatenated into a single comprehensive sales dataset.
*   **Column Management:** The `meanprice` and `v1` columns were dropped from the dataset if present. Several columns were renamed to a consistent lowercase format (e.g., `RetailerLicenseNumber` to `retailerlicensenumber`, `Date` to `date`, `ItemCategory` to `itemcategory`, `totalsales` to `totalsales`).
*   **Data Sorting:** The dataset was sorted by `retailerlicensenumber`, `retailercounty`, `retailerfacilitytype`, `retailercity`, `retailerzipcode`, `date`, `itemcategory`, and `totalsales` for consistency.
*   **License Data Integration:** The sales data was left-merged with an external "Cannabis Market Intelligence Platform Report - Licenses" dataset (`parent_temp`) using `retailerlicensenumber`. This merge enriched the sales data with `primary_company` (parent company identifier) and `cannabiz_county` information. Rows that only existed in the license data after the merge were excluded.
*   **County Data Standardization & Imputation (Multi-stage):**
    *   Initial cleaning replaced "NA" and "UNDEFINED" values in `retailercounty` with empty strings.
    *   A predefined mapping (`county_map`) was used to standardize `cannabiz_county` values (e.g., "Alameda County" to "ALAMEDA").
    *   Missing `retailercounty` values were imputed using the `cannabiz_county` from the merged license data.
    *   Specific `retailerlicensenumber` values had their `retailercounty` manually corrected based on a predefined list.
    *   A consistent `retailercounty` was established for each `retailerlicensenumber` by creating a unique license-to-county mapping and applying it to fill remaining missing values.
    *   The `retailerzipcode` was truncated to a 5-digit `zip5` and merged with an external HUD ZIP-to-County mapping (`zip_df`). Missing `retailercounty` values were further imputed using this zip-code-based county information.
    *   Additional manual corrections were applied to `retailercounty` for specific `retailerlicensenumber` values.
    *   Finally, all `retailercounty` values were converted to uppercase, and any remaining empty strings or "NA" values were converted to `pd.NA` and subsequently dropped, ensuring a clean county column.
*   **Data Type Conversion:** `totalsales` was converted to a numeric type, and `year` (extracted from the `date` column) was also converted to numeric.
*   **Herfindahl-Hirschman Index (HHI) Calculation:**
    *   HHI was calculated at four levels of granularity: statewide based on individual retailer sales, statewide based on parent company sales (where `primary_company` was imputed from `retailerlicensenumber` if missing), county-level based on individual retailer sales, and county-level based on parent company sales.
    *   Calculations involved summing `totalsales` to determine `industry_sales` (per year/county), computing `mkt_share` (market share), and then `mkt_share2` (squared market share) for the HHI.
*   **Derived Metrics:** `county_sales`, `county_sales_parent`, `opacity`, and `opacity_parent` were calculated to provide context on sales volume relative to the statewide maximum.
*   **Temporal Analysis:** HHI data was filtered to focus on years 2019-2025 for trend analysis.
*   **Clustering Analysis:** K-Means clustering was applied to the HHI data (excluding 2018) to group counties with similar HHI trends.
*   **Trend Trajectory Analysis:** Linear regression was used to determine the slope of HHI change over time for each county, classifying them into "increasing," "decreasing," or "stable" categories based on predefined thresholds.
*   **Sales Trend Analysis:** Total sales over time were aggregated by `retailercity` for the top 10 cities.
*   **HHI Change Calculation:** Year-over-year percentage change in HHI was calculated for each county.
*   **Correlation Analysis:** A correlation matrix was computed for `mkt_share2`, `totalsales`, and `county_sales`.
*   **Data Export:** Various aggregated and processed datasets were exported to Stata (`.dta`), Excel (`.xlsx`), and CSV (`.csv`) formats, including `sales_w_parent_co_test.dta`, `hhi_by_county.csv`, `hhi_by_county_parent.csv`, and `HHI_by_county_test.xlsx`.
*   **Visualization Generation:** Numerous plots (line plots, bar plots, box plots, histograms, violin plots, heatmaps, scatter plots) were generated using Matplotlib, Seaborn, and Plotly to visualize HHI trends, distributions, and changes, both overall and by county/cluster. HTML files for interactive plots were also generated.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerFacilityType` (renamed to `retailerfacilitytype`), `RetailerCity` (renamed to `retailercity`), `RetailerZipCode` (renamed to `retailerzipcode`), `Date` (renamed to `date`, used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric, used in aggregations).
*   **Dropped:** `meanprice`, `v1`, `_merge`, `_merge_lic_county`, `_merge_zip`, `Unnamed: 0`, `retailercounty_from_zip`.
*   **Created:** `primary_company`, `cannabiz_county`, `zip5`, `year`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.
*   **Validated:** `retailercounty`, `totalsales`, `year`.

**Logic and Methodology:**
The primary objective of the data work was to prepare a comprehensive sales dataset for market concentration analysis using the Herfindahl-Hirschman Index (HHI). This involved integrating sales data from multiple years, enriching it with license and parent company information, and meticulously cleaning and imputing missing geographical data, particularly for the `retailercounty` column, which was noted as highly unreliable in the original codebook. The multi-stage imputation strategy for `retailercounty` leveraged information from the license dataset, manual corrections, and zip code mappings to maximize data completeness and accuracy. Once the data was prepared, HHI was calculated at various levels (statewide, county, overall, and parent company) to provide a granular view of market concentration. Further analysis involved identifying temporal trends in HHI, clustering counties based on their HHI trajectories, and visualizing these insights to understand market dynamics. The dropping of `meanprice` suggests a focus on total sales and market share rather than average pricing for the HHI analysis.

**Validation and Verification:**
Data validation was embedded throughout the cleaning process. Merge indicators (`_merge`, `_merge_lic_county`, `_merge_zip`) were used to track the success and nature of data joins. Explicit dropping of rows with missing `retailercounty` values after multiple imputation attempts ensured that only records with reliable county information were used for analysis. Data types were explicitly converted to numeric where appropriate, with error handling (`errors="coerce"`) to identify non-numeric values. The consistency of `retailercounty` was enforced by converting it to uppercase and standardizing values using a mapping. Visualizations (plots) were extensively used to inspect trends and distributions, serving as a form of qualitative validation for the calculated metrics and identified patterns.

**Results and Outcomes:**
The data work successfully produced a robust and enriched sales dataset suitable for market concentration analysis. Key outcomes include:
*   A consolidated sales dataset spanning multiple years with standardized and largely complete `retailercounty` information.
*   Integration of parent company identifiers, allowing for HHI calculations at both individual retailer and parent company levels.
*   Calculated HHI metrics for California statewide and for individual counties, providing quantitative measures of market concentration.
*   Identification of county clusters based on HHI trends and classification of counties into increasing, decreasing, or stable HHI trajectories.
*   Generation of numerous analytical outputs (CSV, Excel, Stata files) and comprehensive visualizations (plots) that illustrate market dynamics, HHI trends over time, and geographical variations in market concentration.
*   The work provides a foundation for understanding competitive landscapes within the cannabis market, addressing a critical data quality issue identified in the original codebook (`RetailerCounty`).






# Table: salesquantity21

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

### Column Dictionary


| Column Name           | Type    | Units            | Description                                                                                                   | Allowed Values / Range            |   Missing % | Cleaning / Notes                                                                                                                                                                                                                       |
|:----------------------|:--------|:-----------------|:--------------------------------------------------------------------------------------------------------------|:----------------------------------|------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  | License Number   | Unique identifier for the licensed cannabis retailer.                                                         | e.g., C10-0000638-LIC             |           0 |                                                                                                                                                                                                                                        |
| RetailerFacilityType  | object  | Facility Type    | Type of facility operated by the retailer (e.g., Cannabis - Retailer License).                                | e.g., Cannabis - Retailer License |           0 |                                                                                                                                                                                                                                        |
| RetailerCity          | object  | City Name        | City where the retailer facility is located.                                                                  | e.g., MODESTO                     |           0 |                                                                                                                                                                                                                                        |
| RetailerZipCode       | int64   | Zip Code         | Zip code of the retailer facility.                                                                            | [90008.0, 961610393.0]            |           0 | Investigate values like 961610393.0, which are not standard 5-digit US zip codes. This may represent ZIP+4 codes stored numerically or data entry errors. Convert to string type to preserve leading zeros and handle varying lengths. |
| RetailerCounty        | float64 | County Name      | County where the retailer facility is located.                                                                |                                   |         100 | This column is entirely missing. It should be excluded from analysis or imputed using an external mapping if county-level aggregation is required.                                                                                     |
| ItemCategory          | object  | Product Category | Category of the cannabis product sold (e.g., flower, edibles, concentrates).                                  | e.g., flowereighth                |           0 |                                                                                                                                                                                                                                        |
| Date                  | object  | Month-Year       | Month and year of the aggregated sales data.                                                                  | e.g., 01-2021                     |           0 | Convert to a proper datetime object for accurate time-series analysis.                                                                                                                                                                 |
| totalgrams            | float64 | grams            | Total grams of the item category sold by the retailer in the given month.                                     | [0.4819415, 481290.46]            |           0 |                                                                                                                                                                                                                                        |
| totalsales            | float64 | USD              | Total sales revenue for the item category by the retailer in the given month.                                 | [1.0, 4597238.18]                 |           0 |                                                                                                                                                                                                                                        |
| meanprice             | float64 | USD per unit     | Average price per unit (e.g., per gram or per item) for the item category by the retailer in the given month. | [0.817826086956522, 196.65]       |           0 |                                                                                                                                                                                                                                        |


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






# Table: salesquantity22

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
*   **Column Dictionary**


| Column Name           | Type    | Units        | Description                                                            | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                      |
|:----------------------|:--------|:-------------|:-----------------------------------------------------------------------|:-------------------------------------|------------:|:--------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |              | Unique identifier for the licensed cannabis retailer.                  | Example: C10-0000622-LIC             |           0 |                                                                                                                                       |
| RetailerFacilityType  | object  |              | Type of facility or license held by the retailer.                      | Example: Cannabis - Retailer License |           0 |                                                                                                                                       |
| RetailerCity          | object  |              | City where the retailer's facility is located.                         | Example: STOCKTON                    |           0 |                                                                                                                                       |
| RetailerZipCode       | int64   |              | Zip code of the retailer's facility.                                   | Range: [90008.0, 961610393.0]        |           0 | The wide range suggests potential inclusion of ZIP+4 codes or data entry errors. Standardization to 5-digit zip codes is recommended. |
| RetailerCounty        | object  |              | County where the retailer's facility is located.                       | Example: SAN JOAQUIN                 |          10 | 10% of values are missing. Imputation using RetailerZipCode or RetailerCity, if a reliable mapping exists, is recommended.            |
| ItemCategory          | object  |              | Category of the cannabis item sold.                                    | Example: flowereighth                |           0 |                                                                                                                                       |
| totalgrams            | float64 | grams        | Total quantity of the item category sold in grams for the given month. | Range: [0.4191, 622627.02]           |           0 |                                                                                                                                       |
| totalsales            | float64 | USD          | Total sales revenue for the item category in USD for the given month.  | Range: [0.5, 8184776.28]             |           0 |                                                                                                                                       |
| meanprice             | float64 | USD per gram | Average price per gram for the item category for the given month.      | Range: [0.5, 129.516666666667]       |           0 |                                                                                                                                       |
| Date                  | object  |              | Month and year of the aggregated sales data.                           | Example: 01-2022                     |           0 | Consider converting to a datetime format for easier temporal analysis.                                                                |


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






# Table: salesquantity23

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

*   **Column Dictionary**


| Column Name           | Type    | Units      | Description                                           | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                          |
|:----------------------|:--------|:-----------|:------------------------------------------------------|:-------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |            | Unique identifier for the licensed cannabis retailer. | Example: C10-0000908-LIC             |         0   |                                                                                                                                                                                                           |
| RetailerFacilityType  | object  |            | Type of facility operated by the retailer.            | Example: Cannabis - Retailer License |         0   |                                                                                                                                                                                                           |
| RetailerCity          | object  |            | City where the retailer's facility is located.        | Example: CHULA VISTA                 |         0   |                                                                                                                                                                                                           |
| RetailerZipCode       | int64   |            | Zip code of the retailer's facility.                  | Range: [90003.0, 961610393.0]        |         0   | The upper range of zip codes (961610393.0) appears unusually large and may indicate data entry errors or concatenated zip+4 values that need to be parsed or validated against standard zip code formats. |
| RetailerCounty        | object  |            | County where the retailer's facility is located.      | Example: CONTRA COSTA                |         8.1 | 8.1% of values are missing. Missing values should be investigated. Potential handling: Impute based on RetailerCity/ZipCode if a reliable mapping exists, or flag as unknown.                             |
| ItemCategory          | object  |            | Category of the cannabis item sold.                   | Example: flowereighth                |         0   |                                                                                                                                                                                                           |
| totalgrams            | float64 | grams      | Total quantity of the item category sold in grams.    | Range: [0.5, 960114.5]               |         0   | Values are expected to be non-negative. The current range confirms this.                                                                                                                                  |
| totalsales            | float64 | USD        | Total sales revenue for the item category.            | Range: [0.75, 6896017.44]            |         0   | Values are expected to be non-negative. The current range confirms this.                                                                                                                                  |
| meanprice             | float64 | USD/unit   | Average price per unit for the item category.         | Range: [0.6, 131.3375]               |         0   | Values are expected to be non-negative. The current range confirms this.                                                                                                                                  |
| Date                  | object  | Month-Year | Month and year of the aggregated sales data.          | Example: 01-2023                     |         0   | Consider converting to a datetime format for easier temporal analysis.                                                                                                                                    |


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






# Table: salesquantity23v2

### Overview Section

This dataset provides aggregated sales and quantity information for various cannabis item categories across licensed retailers within the Track & Trace project. It offers insights into market performance by tracking total grams sold, total sales revenue, and mean prices for specific item categories. Each row in the `salesquantity23v2` table represents the aggregated sales and quantity data for a unique combination of a retailer, an item category, and a specific month and year. The data originates from the Track & Trace system, covering sales activities during 2023 (based on the table name and `Date` column examples). The exact extraction date is not available.

**Assumptions:**
*   The `Date` column represents the month and year of the aggregated sales data.
*   `RetailerLicenseNumber` uniquely identifies a retailer.
*   `totalgrams` and `totalsales` are aggregated values for the specified `ItemCategory` and `Date`.

### Table Inventory

*   **salesquantity23v2:** Contains aggregated sales quantities, revenues, and mean prices for various cannabis item categories by retailer and month.

## Table: salesquantity23v2

*   **Purpose:** To provide a summary of sales performance, including total quantities sold, total sales revenue, and average prices, for different cannabis product categories across licensed retailers over time.
*   **What one row represents:** One row represents the aggregated sales quantity, total sales revenue, and mean price for a specific `ItemCategory` sold by a particular `RetailerLicenseNumber` during a given `Date` (month and year).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date`
*   **Relationships:**
*   **Number of rows and columns:** 58226 rows, 10 columns

### Column Dictionary


| Column Name           | Type    | Units    | Description                                                                    | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                           |
|:----------------------|:--------|:---------|:-------------------------------------------------------------------------------|:-------------------------------------|------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier assigned to the licensed cannabis retailer.                  | Example: C10-0000196-LIC             |         0   |                                                                                                                                                                                                                                                                                                            |
| RetailerFacilityType  | object  |          | Categorization of the retailer's licensed facility type.                       | Example: Cannabis - Retailer License |         0   |                                                                                                                                                                                                                                                                                                            |
| RetailerCity          | object  |          | City where the retailer's licensed facility is located.                        | Example: RIVERBANK                   |         0   |                                                                                                                                                                                                                                                                                                            |
| RetailerZipCode       | float64 |          | Zip code of the retailer's licensed facility.                                  | [90003.0, 961610393.0]               |         0.3 | Contains 0.3% missing values. Data type is float64, but zip codes are typically strings. Some values appear to be concatenated 5-digit zip codes (e.g., '953679611.0' likely represents '95367-9611'). Needs conversion to string and potential parsing/validation to standard 5-digit or 9-digit formats. |
| RetailerCounty        | object  |          | County where the retailer's licensed facility is located.                      | Example: STANISLAUS                  |         0.6 | Contains 0.6% missing values. These missing values may impact geographical analysis.                                                                                                                                                                                                                       |
| ItemCategory          | object  |          | Category of the cannabis item being sold.                                      | Example: flowereighth                |         0   |                                                                                                                                                                                                                                                                                                            |
| totalgrams            | float64 | grams    | Total quantity of the item category sold, measured in grams.                   | [0.5, 960114.5]                      |         0   |                                                                                                                                                                                                                                                                                                            |
| totalsales            | float64 | USD      | Total sales revenue generated from the item category, in US Dollars.           | [0.67, 6896017.44]                   |         0   |                                                                                                                                                                                                                                                                                                            |
| meanprice             | float64 | USD/unit | Average price per unit for the item category.                                  | [0.6, 131.3375]                      |         0   |                                                                                                                                                                                                                                                                                                            |
| Date                  | object  |          | Month and year representing the period for which the sales data is aggregated. | Example: 01-2023 (MM-YYYY format)    |         0   | Stored as an object (string); should be converted to a datetime format for proper temporal analysis and filtering.                                                                                                                                                                                         |


### Data Quality & Anomalies Section

*   **Issue:** Missing `RetailerZipCode` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For analytical purposes, rows with missing zip codes can be flagged. For geographical analysis requiring zip codes, these rows may need to be excluded or imputed if a reliable method is available (e.g., based on `RetailerCity` and `RetailerCounty`).
*   **Issue:** Missing `RetailerCounty` values.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** Similar to zip codes, flag rows with missing county information. For analyses requiring county-level aggregation, these rows should be excluded or imputed if a reliable mapping from city/zip to county exists.
*   **Issue:** `RetailerZipCode` stored as `float64` with potentially concatenated values.
    *   **Likely cause:** Data type mismatch during extraction or storage, and potential non-standard entry of zip+4 codes.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to string. Attempt to parse and standardize values into 5-digit or 9-digit (ZIP+4) formats. Values that cannot be standardized should be flagged or treated as invalid.
*   **Issue:** `Date` column stored as `object` (string).
    *   **Likely cause:** Default data type assignment during data ingestion.
    *   **Recommended handling rule:** Convert the `Date` column to a proper datetime format (e.g., `YYYY-MM-DD` representing the first day of the month) to enable robust temporal analysis.

### Reproducible Cleaning Plan

1.  **Standardize Date Column:** Convert the `Date` column from its current `object` type (MM-YYYY string) to a datetime object, representing the first day of each month (e.g., '01-2023' becomes '2023-01-01'). This ensures proper temporal sorting and analysis.
2.  **Clean RetailerZipCode:** Convert the `RetailerZipCode` column to a string type. Identify and parse any concatenated 9-digit zip codes (e.g., '953679611.0' to '95367-9611' or '95367'). Validate against standard zip code patterns and flag or nullify non-conforming entries.
3.  **Address Missing Geographical Data:** For rows with missing `RetailerZipCode` or `RetailerCounty`, consider the analytical context. If geographical precision is critical, these rows may be excluded from specific analyses. Otherwise, flag them for awareness and proceed with available data.
4.  **Validate Numeric Ranges:** Confirm that `totalgrams`, `totalsales`, and `meanprice` values fall within expected positive ranges, as indicated by their `Allowed Values / Range`. Flag any outliers or negative values if they appear in future data.

### Limitations & Trust Section

The reliability of geographical analysis is limited by the 0.3% missing values in `RetailerZipCode` and 0.6% missing values in `RetailerCounty`. Furthermore, the `RetailerZipCode` column's current `float64` type and observed concatenated values suggest potential data entry or processing inconsistencies that require careful cleaning and validation. The accuracy of `meanprice` relies on the correct aggregation of `totalgrams` and `totalsales`; any underlying issues in these base metrics would propagate. Validation of `RetailerZipCode` and `RetailerCounty` against an authoritative geographical dataset is needed to fully trust location-based insights.

### Appendix: Quick Reference

*   **Date Format:** Convert `Date` (MM-YYYY) to `YYYY-MM-DD` datetime objects.
*   **Zip Code Cleaning:** Convert `RetailerZipCode` to string, parse concatenated values, and validate format.
*   **Missing Geo Data:** Flag or exclude rows with missing `RetailerZipCode` or `RetailerCounty` for location-sensitive analyses.
*   **Data Types:** Ensure `RetailerZipCode` is treated as a string, not a float.
*   **Primary Key:** `(RetailerLicenseNumber, ItemCategory, Date)` forms the unique identifier for each record.

### Notes for Reviewers

Reviewers should verify the accuracy of the column descriptions and the proposed handling rules for anomalies, particularly concerning the `RetailerZipCode` and `RetailerCounty` fields. Confirmation of the inferred primary key and the interpretation of the `Date` column as month-year aggregation is also crucial. Any additional known data quality issues or business rules that might affect data interpretation should be highlighted.

# Work Documentation

## Table: salesquantity23v2

**Data Operations:**
The data originating from `salesquantity23v2.csv` was integrated with sales data from other years (2018-2024) into a single comprehensive dataset. During the initial loading of each sales file, columns named `meanprice` and `v1` were removed if present. All columns were initially read as string type to prevent unintended data type conversions.

Following concatenation, column names were standardized to a consistent lowercase format, including `RetailerLicenseNumber` to `retailerlicensenumber`, `RetailerFacilityType` to `retailerfacilitytype`, `RetailerCity` to `retailercity`, `RetailerZipCode` to `retailerzipcode`, `RetailerCounty` to `retailercounty`, `ItemCategory` to `itemcategory`, `Date` to `date`, and `totalsales` to `totalsales`. The combined dataset was then sorted by multiple key identifiers to ensure a consistent order.

The dataset was enriched by a left merge with an external license information dataset (`parent_temp`), using `retailerlicensenumber` as the key. This merge introduced `primary_company` and `cannabiz_county` information. Rows that existed only in the external license dataset were excluded.

Extensive cleaning and imputation were performed on the `retailercounty` field. Initial steps involved replacing "NA" and "UNDEFINED" string values with empty strings. Missing `retailercounty` values were then imputed using a predefined mapping from `cannabiz_county` (obtained from the merged license data). Further manual corrections were applied for specific `retailerlicensenumber` entries. All `retailercounty` values were converted to uppercase for standardization.

A `license_county` lookup table was dynamically created from existing non-empty `retailerlicensenumber` and `retailercounty` pairs within the dataset. This lookup was then used to fill any remaining missing `retailercounty` values. Additionally, a 5-digit zip code (`zip5`) was extracted from `retailerzipcode` and used to merge with an external HUD zip-to-county mapping (`zip_df`) to provide another layer of `retailercounty` imputation for previously missing entries. More manual fixes were applied to `retailercounty` for specific license numbers.

Finally, an `Unnamed: 0` column was dropped if it existed, all columns were explicitly converted to string type, and any remaining `NaN` values were replaced with empty strings to ensure data consistency. The processed dataset was then saved as a Stata `.dta` file named `sales_w_parent_co_test.dta`.

**Variables Affected:**
*   **Modified/Renamed:** `RetailerLicenseNumber` (to `retailerlicensenumber`), `RetailerFacilityType` (to `retailerfacilitytype`), `RetailerCity` (to `retailercity`), `RetailerZipCode` (to `retailerzipcode`), `RetailerCounty` (to `retailercounty`), `ItemCategory` (to `itemcategory`), `Date` (to `date`), `totalsales`. The `retailercounty` column underwent significant cleaning, standardization, and imputation.
*   **Created:** `primary_company` (from external merge), `cannabiz_county` (from external merge), `zip5` (derived from `retailerzipcode`), `_merge_lic_county` (internal tracking for county imputation), `_merge_zip` (internal tracking for zip-based county imputation).
*   **Dropped:** `meanprice`, `v1`, `Unnamed: 0`.

**Logic and Methodology:**
The core logic behind these operations was to create a unified, clean, and enriched sales dataset suitable for advanced analytical tasks, particularly market concentration (HHI) and geographical trend analysis. The initial concatenation addressed the need to combine sales data across multiple periods. The comprehensive renaming ensured consistency and ease of use. The multi-stage approach to cleaning and imputing `retailercounty` was critical due to its high missingness and varied formats, leveraging both internal data relationships and external authoritative sources to maximize accuracy and completeness. The integration of `primary_company` was designed to enable analysis at a corporate entity level, which is often more relevant for market structure studies than individual licenses. The final conversion to string type and handling of missing values ensured data integrity for subsequent processing.

**Validation and Verification:**
Several implicit and explicit validation steps were observed:
*   The use of `dtype=str` and `keep_default_na=False` during initial loading served as a preliminary validation by preventing automatic type inference that might misinterpret data.
*   The `indicator=True` argument during the initial merge with `parent_temp` allowed for tracking merge outcomes, ensuring that only records with a match in the sales data were retained.
*   Custom merge indicators (`_merge_lic_county`, `_merge_zip`) were created and mapped to descriptive labels ("Master only", "Matched", "Matched & updated") to provide transparency and track the source and impact of `retailercounty` imputations.
*   The `value_counts(dropna=False)` method was used on `itemcategory` and `retailercounty` at various points, indicating checks for data distribution and the presence of missing or unexpected values.
*   The explicit conversion of `retailercounty` to uppercase and the final `fillna("")` followed by `astype(str)` for all columns ensured a consistent and clean data state.

**Results and Outcomes:**
The data originating from `salesquantity23v2` (and other sales files) was successfully transformed into a robust and analytically ready dataset. The `retailercounty` field, initially plagued by missing values and inconsistencies, was significantly improved through a systematic cleaning and imputation process, making it reliable for geographical analysis. The addition of `primary_company` allows for a more nuanced understanding of market dynamics by aggregating data at the corporate level. The resulting `sales_w_parent_co_test.dta` file serves as a foundational dataset for subsequent market intelligence analyses, such as the calculation of Herfindahl-Hirschman Index (HHI) and the visualization of sales trends across different geographical and corporate levels.






# Table: salesquantity24

### Overview Section

This dataset provides aggregated sales and quantity data for cannabis products within the Track & Trace system. It captures transactional information at the retailer and item category level, offering insights into sales performance and product distribution. Each row in the `salesquantity24` table represents the aggregated sales quantity, total sales value, and mean price for a specific item category sold by a particular retailer on a given month. The data is derived from the Track & Trace system, with the `salesquantity24` table specifically covering the year 2024. The exact collection period and extraction date are not explicitly provided but are inferred from the table name and `Date` column.

**Assumptions:**
*   The `salesquantity24` table contains data exclusively for the year 2024.
*   `totalgrams` represents the total quantity sold in grams.
*   `totalsales` represents the total revenue in a local currency (e.g., USD).
*   `meanprice` represents the average price per gram.

### Table Inventory

*   **salesquantity24:** Contains aggregated monthly sales quantities, total sales, and mean prices for various cannabis item categories by individual retailers.

### Table: salesquantity24

*   **Purpose:** To provide a summary of sales performance for different cannabis product categories across various retailers, aggregated monthly.
*   **What one row represents:** One row represents the aggregated sales data (total grams sold, total sales value, and mean price per gram) for a specific `ItemCategory` by a unique `RetailerLicenseNumber` in a given `Date` (month-year).
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key)
*   **Relationships:**
*   **Number of rows and columns:** 60280 rows, 10 columns

*   **Column Dictionary**


| Column Name           | Type    | Units                          | Description                                                                                                   | Allowed Values / Range   |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                |
|:----------------------|:--------|:-------------------------------|:--------------------------------------------------------------------------------------------------------------|:-------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |                                | Unique identifier for the licensed cannabis retailer.                                                         |                          |         0   |                                                                                                                                                                                                                                                                                                                 |
| RetailerFacilityType  | object  |                                | Type of facility operated by the retailer (e.g., Microbusiness, Dispensary).                                  |                          |         0   |                                                                                                                                                                                                                                                                                                                 |
| RetailerCity          | object  |                                | City where the retailer's facility is located.                                                                |                          |         0   |                                                                                                                                                                                                                                                                                                                 |
| RetailerZipCode       | float64 |                                | Zip code of the retailer's facility. Appears to be stored as a float, potentially including ZIP+4 extensions. | 90003.0 - 961610393.0    |         0.3 | Contains missing values (0.3%). The data type 'float64' and large values (e.g., 902703447.0) suggest ZIP+4 codes might be concatenated and stored numerically, which can lead to issues with leading zeros and geographic analysis. Recommend converting to string and parsing into standard 5-digit ZIP codes. |
| RetailerCounty        | object  |                                | County where the retailer's facility is located.                                                              |                          |         0.4 | Contains missing values (0.4%). Missing values should be investigated; consider imputation based on RetailerCity or RetailerZipCode if a reliable mapping exists, or flag for exclusion if critical for analysis.                                                                                               |
| ItemCategory          | object  |                                | Category of the cannabis product sold (e.g., flowereighth).                                                   |                          |         0   |                                                                                                                                                                                                                                                                                                                 |
| totalgrams            | float64 | grams                          | Total quantity of the item category sold in grams.                                                            | 0.5 - 160733.51          |         0   |                                                                                                                                                                                                                                                                                                                 |
| totalsales            | float64 | currency (e.g., USD)           | Total sales value for the item category.                                                                      | 0.7 - 1346077.99         |         0   |                                                                                                                                                                                                                                                                                                                 |
| meanprice             | float64 | currency/gram (e.g., USD/gram) | Average price per gram for the item category.                                                                 | 0.57 - 112.941176470588  |         0   |                                                                                                                                                                                                                                                                                                                 |
| Date                  | object  |                                | Month and year of the sales data.                                                                             |                          |         0   | Stored as an object (string) in 'MM-YYYY' format. Recommend converting to a datetime object for proper temporal analysis.                                                                                                                                                                                       |


### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerZipCode`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For analysis requiring complete zip code information, rows with missing `RetailerZipCode` should be flagged or excluded. If possible, attempt to impute based on `RetailerCity` or `RetailerLicenseNumber` if a reliable mapping exists in an external reference table.
*   **Issue:** `RetailerZipCode` stored as `float64` with potentially concatenated ZIP+4 values.
    *   **Likely cause:** Data storage convention that combines the 5-digit ZIP code with its 4-digit extension into a single numeric field, then cast to float, losing leading zeros.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Extract the first 5 digits to represent the standard 5-digit ZIP code. This ensures proper handling of leading zeros and facilitates geographic analysis.
*   **Issue:** Missing values in `RetailerCounty`.
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** Similar to `RetailerZipCode`, rows with missing `RetailerCounty` should be flagged or excluded if county-level analysis is critical. Imputation could be considered if a reliable mapping from `RetailerCity` or `RetailerZipCode` to `RetailerCounty` is available from an external source.
*   **Issue:** `Date` column stored as an object (string).
    *   **Likely cause:** Default data type assignment during extraction or initial loading.
    *   **Recommended handling rule:** Convert the `Date` column to a proper datetime object for accurate temporal sorting, filtering, and aggregation.

### Reproducible Cleaning Plan

1.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column to a string type. Then, extract the first five characters to represent the standard 5-digit ZIP code, handling any potential leading zeros by padding if necessary.
2.  **Handle Missing `RetailerZipCode`:** For rows where `RetailerZipCode` remains missing after standardization, flag these rows for further investigation or exclude them from analyses requiring complete geographic information.
3.  **Handle Missing `RetailerCounty`:** For rows with missing `RetailerCounty`, flag them. If an external lookup table mapping `RetailerCity` or 5-digit `RetailerZipCode` to `RetailerCounty` is available, attempt to impute missing values. Otherwise, these rows should be excluded from county-level aggregations.
4.  **Convert `Date` Column:** Transform the `Date` column from its current string format (`MM-YYYY`) into a datetime object to enable robust time-series analysis.

### Limitations & Trust Section

The reliability of geographic analysis (city, zip code, county) is currently limited by missing values in `RetailerZipCode` (0.3%) and `RetailerCounty` (0.4%), as well as the non-standard format of `RetailerZipCode`. While `RetailerCity` is complete, its utility for precise geographic segmentation is reduced without complete and accurate zip code and county information. Validation is needed to confirm the accuracy of the `RetailerZipCode` parsing and the completeness of `RetailerCounty` data. An external, authoritative source for retailer addresses and their corresponding geographic identifiers would be beneficial to validate and impute missing or malformed entries.

### Appendix: Quick Reference

*   **ZIP Code Cleaning:** Convert `RetailerZipCode` to string, extract first 5 digits.
*   **Missing ZIP Codes:** Flag or exclude rows with missing `RetailerZipCode`.
*   **Missing Counties:** Flag or exclude rows with missing `RetailerCounty`; impute if external mapping is available.
*   **Date Conversion:** Convert `Date` column to datetime objects for temporal analysis.
*   **Primary Key:** `RetailerLicenseNumber`, `ItemCategory`, `Date` forms the composite primary key.

### Notes for Reviewers

Reviewers should verify the proposed handling rules for missing `RetailerZipCode` and `RetailerCounty` align with analytical requirements. Special attention should be paid to the `RetailerZipCode` conversion logic to ensure accurate extraction of 5-digit ZIP codes and proper handling of leading zeros. Additionally, confirm that the assumed primary key (`RetailerLicenseNumber`, `ItemCategory`, `Date`) accurately represents the uniqueness of each row for downstream analysis.

# Work Documentation

## Table: salesquantity24

**Data Operations:**
The `salesquantity24` table, representing aggregated sales data, was processed through a series of cleaning, transformation, and analytical steps. Initially, multiple sales CSV files (ranging from `sales18.csv` to `sales24.csv`) were loaded and concatenated into a single comprehensive sales DataFrame. During this initial load, columns such as `meanprice` and `v1` were dropped if present, and several columns were renamed for consistency (e.g., `ItemCategory` to `itemcategory`, `RetailerLicenseNumber` to `retailerlicensenumber`).

The sales data was then enriched by merging it with a `parent_df` (derived from a "Licenses" dataset), using `retailerlicensenumber` as the key. This merge incorporated information about primary companies and additional county details from an external source.

Extensive cleaning and imputation were performed on the `retailercounty` column. This involved replacing inconsistent values like "NA" and "UNDEFINED" with empty strings, applying a predefined `county_map` to standardize county names where `retailercounty` was missing, and implementing specific manual fixes for known license numbers. The `retailercounty` column was also converted to uppercase and stripped of whitespace to ensure uniformity. Further imputation was achieved by merging with a `license_county` lookup table and an external `zip_df` (HUD ZIP-County mapping) using a derived 5-digit ZIP code (`zip5`). After these steps, any remaining empty strings, "NA", or "nan" values in `retailercounty` were converted to `pd.NA`, and rows with persistent missing `retailercounty` values were dropped.

The `Date` column was used to extract the `year`, and both `totalsales` and the newly derived `year` column were converted to numeric data types.

The core analytical work involved calculating the Herfindahl-Hirschman Index (HHI) to measure market concentration. This was performed at both statewide and county levels, considering market shares based on total sales for individual retailers and their aggregated parent companies. The results were combined into a single DataFrame, and additional metrics like `opacity` (county sales relative to maximum sales) were calculated.

Finally, the processed data was used to generate various visualizations, including time-series plots of HHI by county. Counties were clustered based on their HHI trends using KMeans, and linear regression was applied to categorize counties into increasing, decreasing, or stable HHI trajectories. Year-over-year HHI percentage changes were calculated, and top counties with significant HHI shifts were identified. Several summary tables and the final processed data were exported to Excel and CSV files for reporting.

**Variables Affected:**
*   **Modified:** `RetailerLicenseNumber` (renamed to `retailerlicensenumber`), `RetailerCounty` (renamed to `retailercounty`, extensively cleaned, imputed, and standardized), `RetailerZipCode` (renamed to `retailerzipcode`, used to derive `zip5`), `Date` (renamed to `date`, used to derive `year`), `ItemCategory` (renamed to `itemcategory`), `totalsales` (converted to numeric, aggregated).
*   **Dropped:** `meanprice`, `v1` (if present in source files).
*   **Created:** `companyid`, `county` (renamed to `cannabiz_county`), `statelicenseid` (renamed to `retailerlicensenumber`), `multi_owner`, `primary_company`, `zip5`, `industry_sales`, `mkt_share`, `mkt_share2`, `mkt_share2_parent`, `totalsales_parent`, `county_sales`, `county_sales_parent`, `opacity`, `opacity_parent`, `cluster`, `hhi_change`.

**Logic and Methodology:**
The methodology focused on creating a robust dataset for market concentration analysis.
1.  **Data Integration and Harmonization:** Multiple years of sales data were combined, and then enriched with external license information to provide a comprehensive view of retailer and parent company structures. This ensured that all relevant attributes were available for analysis.
2.  **Geographic Data Standardization:** A multi-layered approach was implemented to clean and impute `retailercounty` data. This involved initial string replacements, application of a predefined mapping, and two stages of merging with external lookup tables (license-based and ZIP-code-based) to fill missing values. Manual corrections were applied for specific known data inconsistencies. This rigorous process aimed to maximize the accuracy and completeness of geographic identifiers, which are critical for county-level analysis.
3.  **Market Concentration Measurement:** The Herfindahl-Hirschman Index (HHI) was chosen as the primary metric for market concentration. HHI was calculated by summing the squares of market shares (based on total sales) for individual retailers and, separately, for their parent companies. This was performed at both statewide and county levels to provide granular insights into market structure.
4.  **Temporal Analysis and Trend Identification:** The `Date` column was transformed to extract `year`, enabling the analysis of HHI trends over time. Linear regression was applied to HHI values for each county to classify their market concentration trajectories as increasing, decreasing, or stable. K-Means clustering was also employed to group counties exhibiting similar HHI patterns, providing a data-driven categorization of market evolution.
5.  **Reporting and Visualization:** The results were aggregated into summary tables and visualized using various plot types (line plots, bar charts, heatmaps, scatter plots) to effectively communicate market dynamics, HHI distributions, and year-over-year changes. Key findings were exported to standard file formats for broader accessibility and further review.

**Validation and Verification:**
Data quality was addressed through several validation and verification steps:
*   **Type Coercion and Error Handling:** Columns were explicitly cast to appropriate data types (`str`, `numeric`, `datetime`), with `errors='coerce'` used during numeric conversions to handle non-convertible values gracefully.
*   **Missing Value Management:** A systematic approach to handling missing `retailercounty` values was implemented, involving multiple imputation sources and subsequent dropping of rows where imputation was not possible. This ensured that analyses were performed on complete geographic data.
*   **Duplicate Handling:** Duplicates in auxiliary dataframes (e.g., `parent_df`) were removed prior to merging to prevent data inflation.
*   **Merge Integrity:** Merge operations (`how='left'`, `indicator=True`) were used to monitor the success of joins and identify unmatched records, allowing for targeted investigation and filtering.
*   **Data Standardization:** Consistent string operations (e.g., `.str.upper()`, `.str.strip()`, `.replace()`) were applied to standardize categorical text fields, particularly `retailercounty`, to ensure accurate grouping and analysis.
*   **Visual Inspection:** The generation of numerous plots served as a visual validation step, allowing for quick identification of outliers, unexpected trends, or data inconsistencies that might not be apparent in raw tabular data.

**Results and Outcomes:**
The data work resulted in a refined and analytically ready dataset derived from the original sales data.
*   A comprehensive sales dataset was created, spanning multiple years and enriched with critical retailer and parent company information.
*   Standardized and largely complete geographic information (`retailercounty`, `zip5`) was established, significantly improving the reliability of location-based analyses.
*   Detailed Herfindahl-Hirschman Index (HHI) metrics were calculated, providing a quantitative measure of market concentration at statewide and county levels for both individual retailers and parent companies.
*   Counties were successfully categorized into groups based on their HHI trends (increasing, decreasing, stable), offering actionable insights into market evolution.
*   Key summary tables and visualizations were produced, effectively communicating market structure, sales performance, and HHI dynamics over time. These outputs are suitable for inclusion in formal reports and presentations.
*   Insights into year-over-year HHI changes and the identification of counties experiencing the most significant shifts in market concentration were generated, supporting strategic decision-making.






# Table: salesquantity25

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

*   **Column Dictionary**


| Column Name           | Type    | Units    | Description                                                          | Allowed Values / Range               |   Missing % | Cleaning / Notes                                                                                                                                                                                                                                                                                                                                    |
|:----------------------|:--------|:---------|:---------------------------------------------------------------------|:-------------------------------------|------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier for the retailer's license.                        | Example: C10-0001030-LIC             |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| RetailerFacilityType  | object  |          | Type of facility operated by the retailer.                           | Example: Cannabis - Retailer License |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| RetailerCity          | object  |          | City where the retailer's facility is located.                       | Example: WILMINGTON                  |         0.1 | Missing values should be investigated. Potential for imputation based on RetailerZipCode or RetailerCounty if a reliable mapping exists.                                                                                                                                                                                                            |
| RetailerZipCode       | float64 |          | Zip code of the retailer's facility.                                 | Range: [90003.0, 961610393.0]        |         0.3 | Contains non-standard zip code formats (e.g., 907442424.0, 961610393.0). These values are likely erroneous or concatenated. Investigate and attempt to parse into standard 5-digit US zip codes. Invalid entries should be flagged or set to null. Missing values should be handled, potentially by imputation from RetailerCity or RetailerCounty. |
| RetailerCounty        | object  |          | County where the retailer's facility is located.                     | Example: LOS ANGELES                 |         0.5 | Missing values should be investigated. Potential for imputation based on RetailerCity or RetailerZipCode if a reliable mapping exists.                                                                                                                                                                                                              |
| ItemCategory          | object  |          | Category of the cannabis item sold.                                  | Example: flowereighth                |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| totalgrams            | float64 | grams    | Total grams of the item category sold in the given month.            | Range: [0.5, 94407.74]               |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| totalsales            | float64 | USD      | Total sales revenue in USD for the item category in the given month. | Range: [1.3, 1310200.93]             |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| meanprice             | float64 | USD/unit | Average price per unit for the item category in the given month.     | Range: [0.716, 146.33]               |         0   |                                                                                                                                                                                                                                                                                                                                                     |
| Date                  | object  |          | Month and year of the sales data.                                    | Example: 01-2025                     |         0   | Currently stored as an object (string). Needs to be converted to a proper datetime format for temporal analysis.                                                                                                                                                                                                                                    |


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






# Table: salesquantity25q2

### Overview Section

This dataset provides aggregated sales and quantity data from the Track & Trace system, which monitors cannabis product movement within a regulated market. It offers insights into retailer performance, product categories, and sales trends over time. Each row in the `salesquantity25q2` table represents an aggregated sales record for a specific retailer, item category, and month. The overall data source is the Track & Trace system, with a collection period covering Q2 2025. The extraction date is not specified in the provided metadata.

**Assumptions:**
*   The `Date` column represents the month and year of the sales aggregation.
*   Currency values (e.g., `totalsales`, `meanprice`) are denominated in USD.
*   `totalgrams` refers to the total quantity sold in grams.

### Table Inventory

*   **salesquantity25q2:** Contains aggregated sales quantities, total sales values, and mean prices for various item categories by retailer and month.

### Table: salesquantity25q2

*   **Purpose:** To provide a summary of sales performance, including quantities sold, total revenue, and average pricing, for different cannabis product categories across various retailers within a specific period.
*   **What one row represents:** One aggregated sales record for a unique combination of `RetailerLicenseNumber`, `ItemCategory`, and `Date`.
*   **Primary key(s):** `RetailerLicenseNumber`, `ItemCategory`, `Date` (composite key).
*   **Relationships:**
*   **Number of rows and columns:** 14698 rows, 10 columns.
*   **Column Dictionary**


| Column Name           | Type    | Units    | Description                                        | Allowed Values / Range               | Missing %   | Cleaning / Notes                                                                                                                                                                                                                                                                         |
|:----------------------|:--------|:---------|:---------------------------------------------------|:-------------------------------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RetailerLicenseNumber | object  |          | Unique identifier for the retailer's license.      | Example: C10-0000092-LIC             | 0%          |                                                                                                                                                                                                                                                                                          |
| RetailerFacilityType  | object  |          | Type of facility operated by the retailer.         | Example: Cannabis - Retailer License | 0%          |                                                                                                                                                                                                                                                                                          |
| RetailerCity          | object  |          | City where the retailer's facility is located.     | Example: Perris                      | 0.1%        | Missing values observed. Consider imputation or flagging for analysis.                                                                                                                                                                                                                   |
| RetailerZipCode       | float64 |          | Zip code of the retailer's facility.               | [90003.0, 961610393.0]               | 0.3%        | Stored as float64, should ideally be string or integer. Anomalously large maximum value (961610393.0) suggests data entry errors or non-standard zip codes. Missing values observed. Convert to string and validate against standard zip code formats; flag or correct anomalous values. |
| RetailerCounty        | object  |          | County where the retailer's facility is located.   | Example: RIVERSIDE                   | 0.5%        | Missing values observed. Consider imputation or flagging for analysis.                                                                                                                                                                                                                   |
| ItemCategory          | object  |          | Category of the cannabis item sold.                | Example: flowereighth                | 0%          |                                                                                                                                                                                                                                                                                          |
| totalgrams            | float64 | grams    | Total quantity of the item category sold in grams. | [0.5, 457446.38]                     | 0%          | Minimum value of 0.5 suggests no zero or negative quantities, which is expected for sales.                                                                                                                                                                                               |
| totalsales            | float64 | USD      | Total sales revenue for the item category.         | [0.5, 3494699.4]                     | 0%          | Minimum value of 0.5 suggests no zero or negative sales, which is expected for revenue.                                                                                                                                                                                                  |
| meanprice             | float64 | USD/unit | Average price per unit for the item category.      | [0.5, 157.75]                        | 0%          | Minimum value of 0.5 suggests no zero or negative prices, which is expected.                                                                                                                                                                                                             |
| Date                  | object  |          | Month and year of the sales aggregation.           | Example: 04-2025                     | 0%          | Stored as object, should be converted to a datetime format for proper temporal analysis.                                                                                                                                                                                                 |


### Data Quality & Anomalies Section

*   **Issue:** Missing values in `RetailerCity` (0.1%), `RetailerZipCode` (0.3%), and `RetailerCounty` (0.5%).
    *   **Likely cause:** Incomplete data entry or data extraction issues.
    *   **Recommended handling rule:** For `RetailerCity` and `RetailerCounty`, consider imputing with the most frequent value within the same `RetailerLicenseNumber` if available, or flag as 'Unknown'. For `RetailerZipCode`, imputation might be less reliable; consider flagging or excluding rows if the missingness is critical for analysis.
*   **Issue:** `RetailerZipCode` is stored as `float64` and contains an anomalously large maximum value (961610393.0).
    *   **Likely cause:** Incorrect data type assignment during extraction or processing, and potential data entry errors for the anomalous value. Standard US zip codes are 5-digit integers.
    *   **Recommended handling rule:** Convert `RetailerZipCode` to a string type. Validate values to ensure they conform to standard 5-digit (or 9-digit) zip code formats. Flag or remove rows with non-standard or clearly erroneous zip codes like 961610393.0.
*   **Issue:** `Date` column is of `object` type.
    *   **Likely cause:** Default data type inference during data loading.
    *   **Recommended handling rule:** Convert `Date` to a proper datetime object for accurate temporal analysis and filtering.

### Reproducible Cleaning Plan

1.  **Convert `Date` to Datetime:** Parse the `Date` column from its 'MM-YYYY' object format into a standard datetime object to enable proper time-series analysis.
2.  **Standardize `RetailerZipCode`:** Convert the `RetailerZipCode` column from `float64` to a string type. Remove the `.0` suffix if present.
3.  **Validate `RetailerZipCode` Values:** Identify and flag or remove `RetailerZipCode` values that do not conform to standard 5-digit or 9-digit US zip code patterns, including the anomalous `961610393.0`.
4.  **Address Missing Location Data:** For `RetailerCity` and `RetailerCounty`, impute missing values using the most frequent value associated with the respective `RetailerLicenseNumber` if a clear majority exists, otherwise, flag these records as having 'Unknown' location data.
5.  **Review Sales and Quantity Ranges:** Verify that `totalgrams`, `totalsales`, and `meanprice` values remain within plausible business ranges after initial data loading, although the current ranges appear reasonable.

### Limitations & Trust Section

The reliability of geographical analysis based on `RetailerZipCode`, `RetailerCity`, and `RetailerCounty` is limited due to missing values and the data quality issues identified in `RetailerZipCode`. Specifically, the `float64` type and the presence of an extremely large zip code value in `RetailerZipCode` suggest potential data entry or processing errors that require validation against an authoritative source of retailer location data. The `Date` column, while present, requires type conversion to be fully trustworthy for temporal analysis. Validation of these fields against an external retailer master data file would significantly improve data trust.

### Appendix: Quick Reference

*   **Date Conversion:** Convert 'MM-YYYY' string to datetime objects.
*   **Zip Code Type:** Convert `RetailerZipCode` from float to string.
*   **Zip Code Validation:** Flag or remove non-standard `RetailerZipCode` values (e.g., `961610393.0`).
*   **Missing Location:** Impute or flag missing `RetailerCity` and `RetailerCounty` values.
*   **No Negative Sales/Quantities:** Confirm `totalgrams`, `totalsales`, `meanprice` are non-negative.

### Notes for Reviewers

Reviewers should verify the accuracy of the proposed data types and cleaning rules, especially for `RetailerZipCode` and `Date` columns. Particular attention should be paid to the handling of missing location data and the validation of the anomalous zip code value. Confirmation of the assumed currency (USD) and units (grams) for sales and quantity metrics is also crucial for accurate interpretation.

# Work Documentation

## Table: salesquantity25q2

**Data Operations:**
The provided Python scripts do not directly process a table explicitly named `salesquantity25q2`, which is described as covering Q2 2025. However, the scripts perform extensive data cleaning, transformation, and aggregation on a broader `sales_df` dataset, which comprises historical sales data from 2018 to 2024, sourced from the same "Track and Trace Data/Retail" system. The operations performed on this `sales_df` are highly relevant and analogous to the cleaning notes and data quality issues identified for `salesquantity25q2` in the Codebook.

The key data operations performed include:
1.  **Data Loading and Concatenation:** Multiple CSV files containing sales data (e.g., `sales18.csv` through `sales24.csv`) were loaded and combined into a single `sales_df`. During this process, columns like `meanprice` and `v1` were dropped if present.
2.  **Column Renaming:** Standardized column names were applied, mapping original names such as `RetailerLicenseNumber`, `RetailerCounty`, `RetailerZipCode`, `Date`, `ItemCategory`, and `totalsales` to a consistent lowercase format (e.g., `retailerlicensenumber`, `retailercounty`, `retailerzipcode`, `date`, `itemcategory`, `totalsales`).
3.  **Parent Company Integration:** An external `parent_df` (containing license and company information) was loaded, cleaned, and used to derive `primary_company` identifiers. This `parent_df` was then merged with the `sales_df` using `retailerlicensenumber` to enrich sales records with parent company information.
4.  **Location Data Cleaning and Imputation:**
    *   `retailercounty` values like "NA" and "UNDEFINED" were replaced with empty strings.
    *   A predefined `county_map` was used to standardize county names (e.g., "Alameda County" to "ALAMEDA").
    *   Missing `retailercounty` values were imputed using information from the merged `parent_df` (`cannabiz_county`) and a `zip_df` (containing ZIP code to county mappings).
    *   Specific manual fixes were applied to `retailercounty` for certain `retailerlicensenumber` values.
    *   `retailercounty` values were converted to uppercase for consistency.
5.  **Zip Code Standardization:** The `retailerzipcode` column was processed to extract the first five digits, creating a `zip5` column. This `zip5` was then used to merge with an external `zip_df` (from HUD data) to further validate and impute `retailercounty` where missing.
6.  **Date and Numeric Type Conversion:** The `date` column (originally 'MM-YYYY' object type) was used to extract a `year` column, which was then converted to a numeric type. The `totalsales` column was also converted to a numeric type, coercing errors.
7.  **Market Concentration (HHI) Calculation:** The cleaned sales data was used to calculate the Herfindahl-Hirschman Index (HHI) at various levels:
    *   Statewide and county-level HHI based on individual retailer sales.
    *   Statewide and county-level HHI based on parent company sales.
    *   These calculations involved grouping data by retailer/parent company and year, summing `totalsales`, calculating market share, and then squaring market shares to derive the HHI.
8.  **Trend Analysis and Clustering:** HHI values were analyzed over time (2019-2024) to identify trends (increasing, decreasing, stable) using linear regression and to group counties into clusters based on their HHI trajectories using KMeans clustering.
9.  **Aggregations and Visualizations:** Various aggregations were performed to summarize sales and HHI metrics. Numerous plots (line plots, bar plots, box plots, histograms, violin plots) were generated to visualize sales trends, HHI distributions, and changes over time.
10. **Data Export:** Intermediate and final processed dataframes, including HHI results, were exported to Stata (`.dta`) and Excel (`.xlsx`) files for further analysis and reporting.

**Variables Affected:**
*   `RetailerLicenseNumber` (renamed to `retailerlicensenumber`): Used as a key for merging and grouping.
*   `RetailerFacilityType` (renamed to `retailerfacilitytype`): Retained.
*   `RetailerCity` (renamed to `retailercity`): Retained.
*   `RetailerZipCode` (renamed to `retailerzipcode`): Standardized, `zip5` extracted.
*   `RetailerCounty` (renamed to `retailercounty`): Cleaned, standardized, and imputed.
*   `ItemCategory` (renamed to `itemcategory`): Retained.
*   `totalsales`: Converted to numeric, aggregated for HHI calculations.
*   `Date` (renamed to `date`): Used to derive `year`, converted to datetime for plotting.
*   `primary_company`: New variable created from `parent_df` to identify ultimate parent entities.
*   `year`: New numeric variable extracted from `date`.
*   `industry_sales`: New variable representing total sales for a given year/county.
*   `mkt_share`: New variable representing market share.
*   `mkt_share2`: New variable representing squared market share (HHI component).
*   `HHI`, `HHI_parent_level`: New variables representing the calculated HHI metrics.
*   `opacity`, `opacity_parent`: New variables indicating relative sales volume.
*   `hhi_change`: New variable for year-over-year HHI percentage change.
*   `cluster`: New variable for HHI trend clusters.

**Logic and Methodology:**
The primary intent behind these transformations is to prepare raw sales data for robust market concentration analysis and trend identification.
*   **Standardization and Imputation:** The extensive cleaning of `RetailerCounty` and `RetailerZipCode` aims to resolve inconsistencies and missingness in geographical identifiers, which are critical for accurate county-level analysis. By leveraging external master data (parent company licenses, HUD zip-to-county mappings) and internal consistency checks (license-to-county mappings), the project sought to create reliable location data.
*   **Date Conversion:** Converting the `Date` column to a proper datetime format and extracting `year` enables accurate temporal analysis, allowing for the study of trends and changes over time.
*   **Parent Company Identification:** Deriving `primary_company` is crucial for understanding market concentration beyond individual licenses, reflecting the true economic entities operating in the market.
*   **HHI Calculation:** The HHI is a standard economic measure of market concentration. Calculating it at both individual retailer and parent company levels, and across statewide and county geographies, provides a comprehensive view of market structure and competition. The use of squared market shares ensures that larger entities contribute disproportionately more to the index, reflecting their greater market power.
*   **Trend Analysis and Clustering:** Applying linear regression to HHI trends and KMeans clustering helps categorize counties based on their market dynamics, facilitating targeted policy or business insights.

**Validation and Verification:**
Several steps were taken to validate and verify the data:
*   **Merge Indicators:** The use of `indicator=True` during merges with `parent_df` and `zip_df` allowed for tracking the source of merged data and identifying records that did not find a match, providing transparency into the imputation process.
*   **Manual Fixes:** Specific manual overrides for known license-to-county discrepancies indicate a level of human review and correction for critical data points.
*   **Data Type Coercion:** Using `errors='coerce'` during numeric conversions for `totalsales` and `year` allowed for identifying and handling non-numeric values gracefully, converting them to `NaN` for subsequent handling.
*   **Missing Value Handling:** Explicitly replacing "NA", "UNDEFINED", and empty strings with `pd.NA` (or `np.nan`) and then dropping rows with missing critical values (e.g., `harvestercounty` in other scripts, or `totalsales` and `date` in sales analysis) ensures that calculations are performed on complete and valid records.
*   **Visualizations:** The generation of various plots (line plots, bar charts, heatmaps, box plots, histograms, violin plots) serves as a visual validation step, allowing for quick identification of outliers, unexpected trends, or data distribution issues.

**Results and Outcomes:**
The data work resulted in a cleaned, standardized, and enriched sales dataset suitable for advanced economic analysis.
*   **Enhanced Data Quality:** Significant improvements were made to the `RetailerCounty` and `RetailerZipCode` fields, addressing critical data quality issues identified in the Codebook. The `Date` column was prepared for temporal analysis.
*   **Market Concentration Metrics:** Comprehensive HHI metrics were computed for various geographical levels (statewide, county) and entity levels (individual retailer, parent company), providing quantitative measures of market concentration.
*   **Trend Insights:** The analysis identified counties with increasing, decreasing, or stable HHI trends, offering insights into evolving market dynamics. Clustering further grouped counties with similar HHI trajectories.
*   **Analytical Outputs:** Several aggregated datasets and visualizations were produced, including HHI summaries, sales over time by city, and detailed HHI trends by county, which are valuable for reporting and further research. These outputs were saved to Stata and Excel files, ready for consumption by analysts and stakeholders.
*   **Foundation for Future Analysis:** The established cleaning and transformation pipeline provides a robust framework for processing future sales data, such as the `salesquantity25q2` dataset, ensuring consistency and reliability in ongoing market intelligence efforts.

