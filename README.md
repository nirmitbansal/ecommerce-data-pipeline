# E-commerce Orders Data Pipeline (Beginner Data Engineering Project)

This project is a complete **end-to-end ETL pipeline** built for beginners who want hands-on experience in **data engineering**, using only **Python, Pandas, and SQLite**.

It takes raw e-commerce order data (CSV), cleans and transforms it, loads it into a database, and runs analytical SQL queries.

This project demonstrates:
- 🗂️ Data extraction from CSV  
- 🧹 Data cleaning & transformation using Pandas  
- 🗄️ Loading data into a SQLite database  
- 📊 Running SQL-based analytics  
- 🧱 Modular project structure  
- 🔄 How to run ETL pipelines locally

**Data Pipeline Workflow**

Extraction

  Reads raw order data from CSV files in the data/ folder.

Transformation

  Cleans nulls and inconsistent values

  Standardizes formats

  Derives additional fields where needed

Loading

  Writes cleaned tables into a SQLite database file

  Ensures tables are indexed for performance

