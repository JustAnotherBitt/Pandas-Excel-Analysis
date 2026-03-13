###### Imports #######

import pandas as pd
from pathlib import Path

###### Functions #######   

def filter_data(data):
    column_name = input("Enter the column name to filter by: ")
    value = input("Enter the value to filter by: ")
    
    try:
        filtered_data = data.loc[data[column_name]==value]
        print(filtered_data)
    except KeyError:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
        

def update_row(data):
    print(f'This is your table: \n{data}\n')
    index = int(input('Type the index number of the row you want to modify: '))
    row_content = data.iloc[index]
    print(f'\n====== Row content ====== \n{row_content}')
    
    modify = input('Do you want to modify this row? (y/n): ')
    
    if modify.lower() == 'y':
        modify_row(data, index, row_content)           
    elif modify.lower() == 'n':
        modify_another_row = input("Row will not be modified.\nDo you want to modify another row? (y/n): ")
        if modify_another_row.lower() == 'y':
            modify_row(data, index, row_content)
        else:
            print("No changes will be made to the data.")


def modify_row(data, index, row_content):
    for column in row_content.index:
        new_value = input(f'Enter new value for {column} (current value: {row_content[column]}): ')
        
        if new_value:
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

            
def modify_column(data):     
    print(f'This is your table: \n{data}\n')
    column_name = input("Type the column name you want to modify exactly as it appears in the data: ")
    
    if column_name not in data.columns: #* data.columns is the Index which contains all the column names 
        print("Column not found.")
        return #* Exit the function if the column name is not found in the data
    
    unique_values = data[column_name].unique()
    #* Display the unique values in the column, transforming them to strings and joining them with a comma and a space
    print("Current values:", ", ".join(str(v) for v in unique_values))

    old_value = input("Which value do you want to change? ")
    new_value = input("Enter the new value: ")
    
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
        
    data.to_excel(f"{file_name}.xlsx")       
    print(f"Updated file saved as {file_name}.xlsx")
    
    
def calculate_mean(data):
    column_name = input("Enter the column name to calculate the mean: ")
    if column_name not in data.columns:
        print("Column name not found.")
        return
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Mean can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        mean_value = data[column_name].mean()
        print(f"The mean of {column_name} is: {mean_value}")
        

def calculate_median(data):
    column_name = input("Enter the column name to calculate the median: ")
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Median can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        median_value = data[column_name].median()
        print(f"The median of {column_name} is: {median_value}")
        
        
def calculate_mode(data):
    column_name = input("Enter the column name to calculate the mode: ")
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Mode can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        mode_value = data[column_name].mode()[0]
        print(f"The mode of {column_name} is: {mode_value}")
        
        
def calculate_std(data):
    column_name = input("Enter the column name to calculate the standard deviation: ")
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Standard deviation can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        std_value = data[column_name].std()
        print(f"The standard deviation of {column_name} is: {std_value}")
        
def calculate_max(data):
    column_name = input("Enter the column name to calculate the maximum: ")
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Maximum can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        max_value = data[column_name].max()
        print(f"The maximum of {column_name} is: {max_value}")
        

def calculate_min(data):
    column_name = input("Enter the column name to calculate the minimum: ")
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print("Minimum can only be calculated for numeric columns. Please check the column name and try again.")
        return
    elif column_name not in data.columns:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
        return
    else:
        min_value = data[column_name].min()
        print(f"The minimum of {column_name} is: {min_value}")
    