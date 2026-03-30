# Pandas Excel Analysis

A simple command-line tool built with **Python** and **Pandas** to analyze and modify Excel spreadsheets.

The goal of this project is to practice working with **Pandas DataFrames**, performing data manipulation, and automating common operations on Excel files.

## Features

- Data Loading
- Data Exploration
  - Filter rows by specific column values
  - Quickly inspect table contents from the CLI
- Data Modification
  - Update values in a specific row
  - Modify an entire column
  - Perform conditional updates (e.g., update values in rows that match a condition)
- Calculate statistics:
  - Mean
  - Median
  - Mode
  - Standard Deviation
  - Min / Max
- Save modified Excel files
- Automatically rename output files if a name already exists

## Requirements

1. Python 3
2. pandas
3. openpyxl

- Create and activate virtual enviroment:

```
python3 -m venv venv
```
- Linux:
```
source venv/bin/activate
``` 
- Windows:
```
venv/Scripts/activate
``` 

## Install dependencies:

```bash
pip install pandas matplotlib calamine
```

## Usage

- Run the program:

```
python main.py
```

- Follow the prompts in the terminal to analyze or modify the Excel data. ;)
- Obs: there's a table included with the project that you can use for testing.

### Author
https://github.com/JustAnotherBitt :D
