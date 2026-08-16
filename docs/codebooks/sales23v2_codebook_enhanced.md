# Track & Trace Data Codebook

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
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier for the licensed retailer.",
    "Allowed Values / Range": "Example: C10-0000196-LIC",
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
    "Description": "City where the retailer's facility is located.",
    "Allowed Values / Range": "Example: RIVERBANK",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's location.",
    "Allowed Values / Range": "Range: [90003.0, 961610393.0]",
    "Missing %": 0.2,
    "Cleaning / Notes": "Data type is float64 but should be string or integer. Investigate unusually large values (e.g., 961610393.0) which may indicate concatenated zip codes or data entry errors. Convert to string and validate format."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's facility is located.",
    "Allowed Values / Range": "Example: STANISLAUS",
    "Missing %": 0.5,
    "Cleaning / Notes": "High percentage of missing values (50%). Consider imputation from RetailerZipCode or RetailerCity if a reliable mapping exists, otherwise flag for awareness or exclude if critical for analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the item sold (e.g., Flower, Edibles, Concentrates).",
    "Allowed Values / Range": "Example: Flower (packaged - each)",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales amount for the given item category by the retailer for the period.",
    "Allowed Values / Range": "Range: [-29321.63, 9167140.17]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values, which are illogical for sales totals. These may represent returns or data entry errors. Flag these records; for analysis, consider excluding them or treating them as zero."
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD per unit",
    "Description": "Average price per unit for the item category.",
    "Allowed Values / Range": "Range: [-Infinity, Infinity]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative and infinite values. Negative prices are illogical. Infinite values likely result from division by zero (e.g., total sales / zero quantity). Flag these records; exclude from price-related calculations or treat as missing/invalid."
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year of the sales record.",
    "Allowed Values / Range": "Example: 01-2023",
    "Missing %": 0.0,
    "Cleaning / Notes": "Convert to datetime object for proper temporal analysis and sorting."
  }
]
```

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