# Track & Trace Data Codebook

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

*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000122-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Type of facility operated by the retailer (e.g., Cannabis - Retailer License).",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer facility is located.",
    "Allowed Values / Range": "Example: MARINA DL REY",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "object",
    "Units": "",
    "Description": "Zip code of the retailer facility.",
    "Allowed Values / Range": "Example: 902925618",
    "Missing %": 0.0,
    "Cleaning / Notes": "May require formatting to a standard 5 or 9-digit zip code format for consistency."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "float64",
    "Units": "",
    "Description": "County where the retailer facility is located.",
    "Allowed Values / Range": "",
    "Missing %": 100.0,
    "Cleaning / Notes": "This column is entirely missing. Consider removing it or attempting to impute from RetailerCity/ZipCode using external data sources if critical for analysis."
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
    "Description": "Month and year of the sales record.",
    "Allowed Values / Range": "Example: 01-2020",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to a datetime object for proper temporal analysis and filtering."
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "Currency (e.g., USD)",
    "Description": "Total sales amount for the given record.",
    "Allowed Values / Range": "[-27161.03, 9408194.73]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values. These likely represent returns or sales adjustments. Flag these records for investigation. For analyses requiring positive sales, consider treating negative values as zero or excluding them."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "Currency per unit",
    "Description": "Average price per unit for the items in the sales record.",
    "Allowed Values / Range": "[-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative values may indicate returns or calculation errors. Infinite values typically result from division by zero (e.g., zero quantity sold). Flag these records. For analysis, infinite values should be treated as missing (NaN) or excluded. Negative values should be investigated or treated as zero if only positive prices are relevant."
  }
]
```

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