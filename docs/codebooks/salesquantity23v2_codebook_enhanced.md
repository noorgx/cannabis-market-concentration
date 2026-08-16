# Track & Trace Data Codebook

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

### Column Dictionary (in JSON format)

```json
[
  {
    "Column Name": "RetailerLicenseNumber",
    "Type": "object",
    "Units": "",
    "Description": "Unique identifier assigned to the licensed cannabis retailer.",
    "Allowed Values / Range": "Example: C10-0000196-LIC",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "Categorization of the retailer's licensed facility type.",
    "Allowed Values / Range": "Example: Cannabis - Retailer License",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerCity",
    "Type": "object",
    "Units": "",
    "Description": "City where the retailer's licensed facility is located.",
    "Allowed Values / Range": "Example: RIVERBANK",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "RetailerZipCode",
    "Type": "float64",
    "Units": "",
    "Description": "Zip code of the retailer's licensed facility.",
    "Allowed Values / Range": "[90003.0, 961610393.0]",
    "Missing %": 0.3,
    "Cleaning / Notes": "Contains 0.3% missing values. Data type is float64, but zip codes are typically strings. Some values appear to be concatenated 5-digit zip codes (e.g., '953679611.0' likely represents '95367-9611'). Needs conversion to string and potential parsing/validation to standard 5-digit or 9-digit formats."
  },
  {
    "Column Name": "RetailerCounty",
    "Type": "object",
    "Units": "",
    "Description": "County where the retailer's licensed facility is located.",
    "Allowed Values / Range": "Example: STANISLAUS",
    "Missing %": 0.6,
    "Cleaning / Notes": "Contains 0.6% missing values. These missing values may impact geographical analysis."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "Category of the cannabis item being sold.",
    "Allowed Values / Range": "Example: flowereighth",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalgrams",
    "Type": "float64",
    "Units": "grams",
    "Description": "Total quantity of the item category sold, measured in grams.",
    "Allowed Values / Range": "[0.5, 960114.5]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "totalsales",
    "Type": "float64",
    "Units": "USD",
    "Description": "Total sales revenue generated from the item category, in US Dollars.",
    "Allowed Values / Range": "[0.67, 6896017.44]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "meanprice",
    "Type": "float64",
    "Units": "USD/unit",
    "Description": "Average price per unit for the item category.",
    "Allowed Values / Range": "[0.6, 131.3375]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Date",
    "Type": "object",
    "Units": "",
    "Description": "Month and year representing the period for which the sales data is aggregated.",
    "Allowed Values / Range": "Example: 01-2023 (MM-YYYY format)",
    "Missing %": 0.0,
    "Cleaning / Notes": "Stored as an object (string); should be converted to a datetime format for proper temporal analysis and filtering."
  }
]
```

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