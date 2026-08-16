# Track & Trace Data Codebook

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
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "OriginFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "The type of the facility from which the item was shipped.",
    "Allowed Values / Range": "e.g., A-Large Indoor, A-Processor",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "OriginCity",
    "Type": "object",
    "Units": "",
    "Description": "The city of the originating facility.",
    "Allowed Values / Range": "e.g., Cathedral City",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "OriginZipCode",
    "Type": "object",
    "Units": "",
    "Description": "The zip code of the originating facility.",
    "Allowed Values / Range": "e.g., 92234.0",
    "Missing %": "0.2",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation or flagging if critical for geographic analysis."
  },
  {
    "Column Name": "OriginCounty",
    "Type": "object",
    "Units": "",
    "Description": "The county of the originating facility.",
    "Allowed Values / Range": "e.g., Riverside County",
    "Missing %": "27.3",
    "Cleaning / Notes": "Significant percentage of missing values. Investigate the cause of missingness. May require imputation from ZipCode or external data sources, or exclusion from analyses requiring county-level detail."
  },
  {
    "Column Name": "DestinationFacilityType",
    "Type": "object",
    "Units": "",
    "Description": "The type of the facility to which the item was shipped.",
    "Allowed Values / Range": "e.g., A-Processor",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "DestinationCity",
    "Type": "object",
    "Units": "",
    "Description": "The city of the destination facility.",
    "Allowed Values / Range": "e.g., Lancaster",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "DestinationZipCode",
    "Type": "object",
    "Units": "",
    "Description": "The zip code of the destination facility.",
    "Allowed Values / Range": "e.g., 93534",
    "Missing %": "0.2",
    "Cleaning / Notes": "Small percentage of missing values. Consider imputation or flagging if critical for geographic analysis."
  },
  {
    "Column Name": "DestinationCounty",
    "Type": "object",
    "Units": "",
    "Description": "The county of the destination facility.",
    "Allowed Values / Range": "e.g., Los Angeles County",
    "Missing %": "27.5",
    "Cleaning / Notes": "Significant percentage of missing values. Investigate the cause of missingness. May require imputation from ZipCode or external data sources, or exclusion from analyses requiring county-level detail."
  },
  {
    "Column Name": "ItemCategory",
    "Type": "object",
    "Units": "",
    "Description": "The category of the item being distributed.",
    "Allowed Values / Range": "e.g., Flower",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemQuantityType",
    "Type": "object",
    "Units": "",
    "Description": "The type of quantity measurement for the item (e.g., WeightBased, CountBased).",
    "Allowed Values / Range": "e.g., WeightBased",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemUnitWeightUOM",
    "Type": "object",
    "Units": "",
    "Description": "Unit of Measure (UOM) for the item's unit weight.",
    "Allowed Values / Range": "e.g., Grams",
    "Missing %": "18.2",
    "Cleaning / Notes": "High percentage of missing values. Investigate if this is expected for items not measured by weight or if it's a data entry issue. Imputation may be challenging without clear rules; consider flagging or excluding records where UOM is critical."
  },
  {
    "Column Name": "ItemUnitVolumeUOM",
    "Type": "object",
    "Units": "",
    "Description": "Unit of Measure (UOM) for the item's unit volume.",
    "Allowed Values / Range": "e.g., Milliliters",
    "Missing %": "90.7",
    "Cleaning / Notes": "Very high percentage of missing values. This suggests that most items are not measured by volume, or volume data is rarely captured. Consider if this column is useful for analysis given its sparsity, or if it should be excluded."
  },
  {
    "Column Name": "ShippedUOM",
    "Type": "object",
    "Units": "",
    "Description": "Unit of Measure (UOM) for the total quantity shipped.",
    "Allowed Values / Range": "e.g., Pounds",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ReceivedUOM",
    "Type": "object",
    "Units": "",
    "Description": "Unit of Measure (UOM) for the total quantity received.",
    "Allowed Values / Range": "e.g., Pounds",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "month",
    "Type": "object",
    "Units": "",
    "Description": "The month in which the distribution event occurred.",
    "Allowed Values / Range": "e.g., October",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "Year",
    "Type": "int64",
    "Units": "",
    "Description": "The year in which the distribution event occurred.",
    "Allowed Values / Range": "2022.0 to 2025.0",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ManifestCount",
    "Type": "int64",
    "Units": "count",
    "Description": "The number of manifests associated with this distribution event.",
    "Allowed Values / Range": "1.0 to 3587.0",
    "Missing %": "0.0",
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "ItemUnitWeight",
    "Type": "float64",
    "Units": "Varies by ItemUnitWeightUOM",
    "Description": "The weight of a single unit of the item.",
    "Allowed Values / Range": "0.0 to 1008056.4",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 may indicate items not measured by weight or data entry issues. Investigate if 0.0 is a valid representation for certain item types."
  },
  {
    "Column Name": "ItemUnitVolume",
    "Type": "float64",
    "Units": "Varies by ItemUnitVolumeUOM",
    "Description": "The volume of a single unit of the item.",
    "Allowed Values / Range": "0.0 to 190387.0",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 may indicate items not measured by volume or data entry issues. Investigate if 0.0 is a valid representation for certain item types."
  },
  {
    "Column Name": "ShippedQuantity",
    "Type": "float64",
    "Units": "Varies by ShippedUOM",
    "Description": "The total quantity of the item shipped.",
    "Allowed Values / Range": "-8191.8295 to 269905305.4149",
    "Missing %": "0.0",
    "Cleaning / Notes": "Contains negative values. These likely represent returns or adjustments. It is recommended to flag these records for further investigation or to convert them to positive values in a separate 'Returns' column, or exclude them from analyses focused solely on outbound shipments."
  },
  {
    "Column Name": "ShippedWholesalePrice",
    "Type": "float64",
    "Units": "Currency",
    "Description": "The wholesale price of the total quantity shipped.",
    "Allowed Values / Range": "0.0 to 144364409.32",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 may indicate free samples, internal transfers, or missing price data. Investigate the business context for zero prices."
  },
  {
    "Column Name": "ReceivedQuantity",
    "Type": "float64",
    "Units": "Varies by ReceivedUOM",
    "Description": "The total quantity of the item received at the destination.",
    "Allowed Values / Range": "0.0 to 269905305.4149",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 may indicate discrepancies or data entry issues. Investigate the business context for zero received quantities."
  },
  {
    "Column Name": "ReceivedWholesalePrice",
    "Type": "float64",
    "Units": "Currency",
    "Description": "The wholesale price of the total quantity received.",
    "Allowed Values / Range": "0.0 to 144364409.32",
    "Missing %": "0.0",
    "Cleaning / Notes": "Values of 0.0 may indicate free samples, internal transfers, or missing price data. Investigate the business context for zero prices."
  }
]
```

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