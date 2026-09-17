# Web Scraper and Analysis Pipeline

This capstone project implements an automated ETL, (Extract, Transform, Load) and analysis pipeline for web-scraped global weather data using Python, SQLite, Pandas, and Matplotlib.

Here are some summaries for each program and what it is does:
  - scrape.py: Scrapes weather data and outputs raw_weather_data.csv
  - clean.py: Cleans raw data and saves cleaned_weather_data.csv
  - database.py: Loads both CSVs into weather_data.db via to_sql
  - analysis.py: Generates summary stats and saves weather_summary_plot.png

## 1: scrape.py (Extract)
  - Requests live data from timeanddate.com/weather
  - Parses structured HTML elements to extract cities, weather conditions, raw temperatures, and additional parameters
  - Exports the extracted dataset to raw_weather_data.csv

## 2: clean.py (Transform)
  - Reads raw_weather_data.csv
  - Cleans numeric temperature values by stripping units and special characters
  - Handles missing values, deduplicates rows, and formats data types
  - Saves the cleaned dataset to cleaned_weather_data.csv

## 3: database.py (Load)
  - Connects to a local SQLite database (weather_data.db)
  - Ingests both raw_weather_data.csv and cleaned_weather_data.csv into database tables (raw_weather) and cleaned_weather) using Pandas to_sql

## 4: analysis.py (Analysis & Visualize)
  - Queries weather_data.db using SQL
  - Generates summary statistics
  - Creates and exports a bar chart visualization (weather_summary_plot.png)

# Environment & Requirements
  - Python Version: 3.x
  - Dependencies:
      - requests
      - beautifulsoup4
      - pandas
      - matplotlib

# Installation
  - pip install requests beautifulsoup4 pandas matplotlib

# How to Run the Pipeline
  - Execute the scripts sequentially in your terminal:
      - scrape live data: python scrape.py
      - Clean and format raw datasets: clean.py
      - Ingest cleaned data into SQLite database: python database.py
      - Generate statistics and visualization plots: python analysis.py
   
# Generated Artifacts
  - raw_weather_data.csv - unprocessed scraped data
  - cleaned_weather_data.csv - Sanitized dataset ready for analysis
  - weather_data.db - SQLite database housing raw and cleaned tables
  - weather_summary_plot.png - Visualization summary chart
  

