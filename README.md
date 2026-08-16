# Restaurant-Sales-Dirty-Data-for-Cleaning-Training

A data cleaning and exploratory data analysis (EDA) project using Python and Pandas to process raw restaurant order data, fix data quality issues, and extract actionable insights.

Key Steps & Data Cleaning Performed:
 - Text Normalization: Applied string methods (.str.strip(), .str.lower()) to eliminate trailing spaces and case inconsistencies in menu item names.

 - Data Type Handling: Resolved data type mismatches, successfully handled numeric columns, and converted quantities into appropriate integer formats.

 - Missing Value Management: Detected and processed missing values/zeros to ensure reliable metric aggregations.

 - Logical Ordering: Configured categorical data ordering for days of the week to ensure correct chronological sorting (Monday - Sunday) instead of default alphabetical order.

 - Aggregation & Insights: Grouped and analyzed data to find top-selling items, revenue patterns, and sales distribution across weekdays.

Tech Stack:

Python

Pandas
