# Track & Trace Data Codebook

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
*   **Column Dictionary (in JSON format)**

```json
[
  {
    "Column Name": "origin_facility_type",
    "Type": "object",
    "Units": "",
    "Description": "The type of the facility from which items were shipped.",
    "Allowed Values / Range": "Example: A-Large Indoor",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "origin_city",
    "Type": "object",
    "Units": "",
    "Description": "The city where the originating facility is located.",
    "Allowed Values / Range": "Example: Cathedral City",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "origin_county",
    "Type": "object",
    "Units": "",
    "Description": "The county where the originating facility is located.",
    "Allowed Values / Range": "Example: Riverside",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "destination_facility_type",
    "Type": "object",
    "Units": "",
    "Description": "The type of the facility to which items were shipped.",
    "Allowed Values / Range": "Example: A-Processor",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "destination_city",
    "Type": "object",
    "Units": "",
    "Description": "The city where the destination facility is located.",
    "Allowed Values / Range": "Example: Lancaster",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "destination_county",
    "Type": "object",
    "Units": "",
    "Description": "The county where the destination facility is located.",
    "Allowed Values / Range": "Example: Los Angeles",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "item_category",
    "Type": "object",
    "Units": "",
    "Description": "The category of the item being distributed.",
    "Allowed Values / Range": "Example: Flower",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "item_quantity_type",
    "Type": "object",
    "Units": "",
    "Description": "The method or type of quantity measurement for the item.",
    "Allowed Values / Range": "Example: WeightBased",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "month",
    "Type": "object",
    "Units": "",
    "Description": "The month in which the distribution event occurred.",
    "Allowed Values / Range": "Example: December",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "year",
    "Type": "int64",
    "Units": "",
    "Description": "The year in which the distribution event occurred.",
    "Allowed Values / Range": "[2022.0, 2025.0]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "shipped_quantity",
    "Type": "float64",
    "Units": "weight units (e.g., grams, pounds)",
    "Description": "The quantity of items shipped from the origin facility.",
    "Allowed Values / Range": "[-100.0, 4198361791.36]",
    "Missing %": 0.0,
    "Cleaning / Notes": "Contains negative values, which may indicate returns, adjustments, or data entry errors. Requires investigation and specific handling to ensure accurate quantity tracking."
  },
  {
    "Column Name": "shipped_wholesale_price",
    "Type": "float64",
    "Units": "currency units",
    "Description": "The wholesale price associated with the shipped quantity.",
    "Allowed Values / Range": "[0.0, 144364409.32]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "received_quantity",
    "Type": "float64",
    "Units": "weight units (e.g., grams, pounds)",
    "Description": "The quantity of items received at the destination facility.",
    "Allowed Values / Range": "[0.0, 4198361791.36]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  },
  {
    "Column Name": "received_wholesale_price",
    "Type": "float64",
    "Units": "currency units",
    "Description": "The wholesale price associated with the received quantity.",
    "Allowed Values / Range": "[0.0, 144364409.32]",
    "Missing %": 0.0,
    "Cleaning / Notes": ""
  }
]
```

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