###### Imports #######

import pandas as pd
from pathlib import Path
from constants import *
import os

###### Functions #######   

def convert_xlsx_to_csv(xlsx_file: str, csv_file: str) -> None:
    print("Converting XLSX to CSV (this may take a moment)...")
    
    df = pd.read_excel(xlsx_file, engine='calamine')
    df.to_csv(csv_file, index=False)
    
    print(f"Conversion complete! Saved as: {csv_file}")
    
    
def load_data(table_name: str):    
    xlsx_file = table_name + ".xlsx"
    csv_file = table_name + ".csv"
    
    # --- Prefers CSV if it exists ---
    if os.path.exists(csv_file):
        print(f"CSV file found ({csv_file}). Reading directly...")
        return pd.read_csv(csv_file)

    # --- Verifies if the XLSX file exists ---
    if not os.path.exists(xlsx_file):
        raise FileNotFoundError("File not found. Please check the file name and try again.")

    convert_xlsx_to_csv(xlsx_file, csv_file)
    return pd.read_csv(csv_file)


def filter_data(data):
    column_name = input("Enter the column name to filter by: ")
    value = input("Enter the value to filter by: ")
    
    try:
        filtered_data = data.loc[data[column_name]==value]
        print(filtered_data)
    except KeyError:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
        

def update_row(data):   #TODO: to fix update_row() func to work better with larger files
    while True:
        try:
            user_input = input("Enter the index of the row you want to modify (or type 'exit' to quit): ").strip()
            if user_input == 'exit':
                print("No changes will be made to the data.")
                return
            index = int(user_input)
            if index < 0 or index >= len(data):
                print("Index out of range. Please enter a valid index.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")
    
    row_content = data.iloc[index]
    print(f'\n====== Row content ====== \n{row_content}')
    
    modify = input('Do you want to modify this row? (y/n): ')
    
    if modify.lower() == 'y':
        modify_row(data, index, row_content)           
    elif modify.lower() == 'n':
        modify_another_row = input("Row will not be modified.\nDo you want to modify another row? (y/n): ").strip()
        if modify_another_row.lower() == 'y':
            modify_row(data, index, row_content)
        else:
            print("No changes will be made to the data.")


def modify_row(data, index, row_content):
    for column in row_content.index:
        new_value = input(f'Enter new value for {column} (current value: {row_content[column]}) (or type \'exit\' to quit): ').strip()
        
        if new_value:
            if new_value == 'exit':
                print("No changes will be made to the data.")
                return
            if data[column].dtype == 'int64':
                new_value = int(new_value)
                data.at[index, column] = new_value
            elif data[column].dtype == 'float64':
                new_value = float(new_value)
                data.at[index, column] = new_value
            else:
                data.at[index, column] = new_value
            print("Row modified successfully.")
        else:
            print("No changes made to this row.")
            
    update_file(data=data)

            
def modify_column(data):    #TODO: instead of asking for the column name to update values, ask for the column index
    print(f'\n\nThis is your table: \n{data}\n')
    
    while True:
        column_name = input("Type the column name you want to modify exactly as it appears in the data (or type 'exit' to quit): ").strip()
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns: #* data.columns is the Index which contains all the column names
            print("Column not found. Please check the column name and try again.")
            continue
        break
        
    
    unique_values = data[column_name].unique()
    #* Display the unique values in the column, transforming them to strings and joining them with a comma and a space
    print("Current values:", ", ".join(str(v) for v in unique_values))

    while True:
        old_value = input("Which value do you want to change? ").strip()
        if old_value not in unique_values:
            print("Value not found. Please check the value and try again.")
            continue
        break

    new_value = input("Enter the new value: ").strip()
    
    if new_value == "":
            print("No changes made.")
            return

    #* Convert type automatically
    if pd.api.types.is_integer_dtype(data[column_name]):
        new_value = int(new_value)
    elif pd.api.types.is_float_dtype(data[column_name]):
        new_value = float(new_value)

    data.loc[data[column_name] == old_value, column_name] = new_value

    print("Column modified successfully.")
         
    update_file(data)
    

def update_file(data):
    file_name = input('Type a name for the updated excel file (without .xlsx extension): ').strip()
    
    if file_name == "":
        file_name = "updated_data"
        print("No name provided. Updated file will be saved as updated_data.xlsx")
        #* Check if file already exists and add a number to the end of the file name if it does
    base_name = file_name
    counter = 1
    
    while Path(f"{file_name}.xlsx").exists():
        file_name = f"{base_name}_{counter}"
        counter += 1
        
    data.to_excel(f"{file_name}.xlsx", index=False)       
    print(f"Updated file saved as {file_name}.xlsx")


def conditional_update(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()    
    
    while True:
        condition_column = input("Enter the column name for the condition: ").strip()
        if condition_column not in data.columns:
            print("Condition column not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        else:
            break
    
    while True:
        condition_value = input("Enter the value for the condition: ").strip()
        if condition_value not in data[condition_column].values:
            print("Condition value not found. Please check the value and try again.")
        else:
            break

    while True:
        target_column = input("Enter the column name you want to update: ").strip()
        if target_column not in data.columns:
            print("Target column not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        else:
            break 
    
    new_value = input("Enter the new value: ").strip()
    
    if new_value == "":
        print("No changes made.")
    else:
        data.loc[data[condition_column] == condition_value, target_column] = new_value
        print("Conditional update applied successfully.")
        update_file(data)
    
    
def calculate_mean(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()    
    
    while True:
        column_name = input("Enter the column name to calculate the mean (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns:
            print("Column name not found.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Mean can only be calculated for numeric columns. Please check the column name and try again.")
            continue

        mean_value = data[column_name].mean()
        print(f"The mean of {column_name} is: {mean_value}")
        break
        

def calculate_median(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()    
    
    
    while True:
        column_name = input("Enter the column name to calculate the median (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return  
        if column_name not in data.columns:
            print("Column not found.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Column is not numeric.")
            continue
        
        median_value = data[column_name].median()
        print(f"The median of {column_name} is: {median_value}")
        break
        
        
def calculate_mode(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()     
    
    while True:
        column_name = input("Enter the column name to calculate the mode (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns:
            print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Mode can only be calculated for numeric columns. Please check the column name and try again.")
            continue

        mode_value = data[column_name].mode()[0]
        print(f"The mode of {column_name} is: {mode_value}")
        break
        
        
def calculate_std(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()      
    
    while True:
        column_name = input("Enter the column name to calculate the standard deviation (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns:
            print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Standard deviation can only be calculated for numeric columns. Please check the column name and try again.")
            continue

        std_value = data[column_name].std()
        print(f"The standard deviation of {column_name} is: {std_value}")
        break
        
        
def calculate_max(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()     
    
    while True:
        column_name = input("Enter the column name to calculate the maximum (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns:
            print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Maximum can only be calculated for numeric columns. Please check the column name and try again.")
            continue

        max_value = data[column_name].max()
        print(f"The maximum of {column_name} is: {max_value}")
        break
        

def calculate_min(data):
    print("\nTable columns:")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
    print()       
    
    while True:
        column_name = input("Enter the column name to calculate the minimum (or type 'exit' to quit): ").strip()
        
        if column_name.lower() == 'exit':
            print("No changes will be made to the data.")
            return
        if column_name not in data.columns:
            print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
            continue
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            print("Minimum can only be calculated for numeric columns. Please check the column name and try again.")
            continue

        min_value = data[column_name].min()
        print(f"The minimum of {column_name} is: {min_value}")
        break
    