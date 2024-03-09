# Otodom.pl Scraper

A Python scraper for extracting real estate data from **otodom.pl**, a popular Polish real estate service.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Data Analysis Query](#example-data-analysis-query)

## Introduction

Otodom Scraper is a Python tool designed to extract real estate data from the **otodom.pl** website. With this scraper, users can gather information about available properties, including details such as building ownership, price, currency, number of rooms, construction status, floor, rent price, parking availability, heating type, and city. The scraped data is then saved into a PostgreSQL database for further analysis and usage.

## Features

- Retrieves information such as building ownership, price, currency, number of rooms, construction status, floor, rent price, parking availability, heating type etc.
- Allows users to select the city they want to scrape data from
- Saves data into a PostgreSQL database

## Requirements

- Python 3.x
- PostgreSQL 16 database
- Pip 21.3.1

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Kiranchai/otodom-scraper.git
```

The `config/schema.sql` file contains a template for creating the PostgreSQL table where the scraped data will be stored. You can use this schema to create the appropriate table in your PostgreSQL database before running the scraper.

To create the table, you can execute the SQL commands in the `schema.sql` file using a PostgreSQL client or command-line interface.

```sql
psql -U your_username -d your_database_name -a -f config/schema.sql
```

## Usage

To use the scraper and save data into a PostgreSQL database, follow these steps:

1. Set up your PostgreSQL database and ensure you have the necessary credentials.

2. Modify the .env file to include your PostgreSQL database connection details.

3. Run the main.py script:

```bash
python main.py
```

4. You will see a menu where you can choose the city you want to scrape data from.

5. Once you select a city, the scraper will gather the data.

6. Once all of the listings from the site were scraped, the script will stop running.

## Example Data Analysis Query

Here's an example of a SQL query that you can use to perform data analysis on the scraped data stored in your PostgreSQL database:

```sql
SELECT city, AVG(price / square_footage) AS average_square_meter_price
FROM property_details
WHERE price_currency = 'PLN'
GROUP BY city;
```

This query calculates the average price per square meter for flats in each city. You can execute this query using a PostgreSQL client or command-line interface after you've scraped and stored the data.

**Make sure to replace `property_details` with the name of your table if it's different.**
