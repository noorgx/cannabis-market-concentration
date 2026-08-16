```markdown
# Track & Trace Data Codebook

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
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "licenseNumber",
    "Type": "string",
    "Units": "",
    "Description": "Unique identifier assigned to each cultivation license.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "id",
    "Type": "integer",
    "Units": "",
    "Description": "A unique identifier for each record in the table.",
    "Allowed Values / Range": "1 to 19543",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "licenseStatus",
    "Type": "string",
    "Units": "",
    "Description": "The current administrative status of the license (e.g., 'Active', 'Expired', 'Suspended').",
    "Allowed Values / Range": "e.g., 'Expired', 'Active', 'Provisional'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "licenseTerm",
    "Type": "string",
    "Units": "",
    "Description": "The duration or type of the license term (e.g., 'Annual', 'Provisional').",
    "Allowed Values / Range": "e.g., 'Annual'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "licenseType",
    "Type": "string",
    "Units": "",
    "Description": "The specific category of cultivation license (e.g., 'Medium Outdoor', 'Small Indoor').",
    "Allowed Values / Range": "e.g., 'Cultivation - Medium Outdoor'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "licenseDesignation",
    "Type": "string",
    "Units": "",
    "Description": "The designation of the license, indicating its allowed market (e.g., 'Adult-Use', 'Medicinal').",
    "Allowed Values / Range": "e.g., 'Adult-Use'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "issueDate",
    "Type": "date",
    "Units": "",
    "Description": "The date the license was initially issued.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for analysis."
  },
  {
    "Column Name": "expirationDate",
    "Type": "date",
    "Units": "",
    "Description": "The date the license is set to expire.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for analysis."
  },
  {
    "Column Name": "businessLegalName",
    "Type": "string",
    "Units": "",
    "Description": "The full legal name of the business holding the license.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "businessDbaName",
    "Type": "string",
    "Units": "",
    "Description": "The 'Doing Business As' name of the licensed entity, if different from the legal name.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains 'Data Not Available' strings, which should be treated as missing values (NaN)."
  },
  {
    "Column Name": "businessOwnerName",
    "Type": "string",
    "Units": "",
    "Description": "The name of the primary owner or contact for the business.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "businessStructure",
    "Type": "string",
    "Units": "",
    "Description": "The legal organizational structure of the business (e.g., 'Corporation', 'Sole Proprietorship').",
    "Allowed Values / Range": "e.g., 'Corporation'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "premiseCounty",
    "Type": "string",
    "Units": "",
    "Description": "The county where the licensed cultivation premise is physically located.",
    "Allowed Values / Range": "e.g., 'Humboldt'",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "businessEmail",
    "Type": "string",
    "Units": "",
    "Description": "The primary email address for business contact.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Standardize to lowercase."
  },
  {
    "Column Name": "businessPhone",
    "Type": "string",
    "Units": "",
    "Description": "The primary phone number for business contact.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Standardize phone number format if needed for consistency."
  },
  {
    "Column Name": "panel_month",
    "Type": "date",
    "Units": "",
    "Description": "The first day of the month to which the panel data corresponds.",
    "Allowed Values / Range": "",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for analysis."
  },
  {
    "Column Name": "Active",
    "Type": "binary",
    "Units": "",
    "Description": "Indicator if the license was active during the `panel_month` (1 = Active).",
    "Allowed Values / Range": "1",
    "Missing %": 0.0,
    "Cleaning / Notes": "Verify if this column is always 1, suggesting the dataset is pre-filtered for active licenses."
  },
  {
    "Column Name": "Canopy.Size",
    "Type": "numeric",
    "Units": "square feet",
    "Description": "The reported cultivation canopy size for the license during the `panel_month`.",
    "Allowed Values / Range": "0.0 to 1736868.0",
    "Missing %": 7.4,
    "Cleaning / Notes": "Missing values (7.4%) should be investigated. Consider imputation (e.g., median, zero) or exclusion based on analysis goals. Negative values are not expected, but 0 is possible for inactive or new licenses."
  }
]
```

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
```