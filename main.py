###### Imports #######
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import dedent

###### Intro #######
print('To use this program, first you need to put the excel file you want to analyze in the same directory of it.')
table_name = input('Type the excel file name exactly as it appears in the file: ')

###### Data loading #######
try:
    data = pd.read_excel(table_name)
except FileNotFoundError:
    print("File not found. Please check the excel file name and try again.")
    exit()
print("File loaded successfully.")

see_data = input("Do you want to see the data? (y/n): ")
if see_data.lower() == 'y':
    print(data)
else:
    print("Data will not be displayed.")

###### Functions #######   

def modify_row():
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
    file_name = input('Type a name for the updated excel file (without .xlsx extension): ')
    data.to_excel(f"{file_name}.xlsx")       
    print(f"Updated file saved as {file_name}.xlsx")
            

def modify_column():     
    column_name = input("Type the column name you want to modify exactly as it appears in the data: ")
    if column_name in data.columns:
        print(f"Current values: {", ".join(str(item) for item in data[column_name].unique())}")
        for item in data[column_name]:
            new_value = input(f'Enter new value for {item}: ')            
            if new_value:
                if data[column_name].dtype == 'int64':
                    new_value = int(new_value)
                    data[column_name] = new_value
                elif data[column_name].dtype == 'float64':
                    new_value = float(new_value)
                    data[column_name] = new_value
                else:
                    data[column_name] = new_value
                print("Column modified successfully.")
            else:
                print("No changes made to this column.")
        file_name = input('Type a name for the updated excel file (without .xlsx extension): ').strip
        if file_name == "":
            file_name = "updated_data"
            print("No name provided. Updated file will be saved as updated_data.xlsx")
            
        data.to_excel(f"{file_name}.xlsx")       
        print(f"Updated file saved as {file_name}.xlsx")
    
###### Data analysis #######
print("\n======== Data analysis ========")
print(dedent('''
    What do you want to do?
    1. Filter data by column value
    2. Update values
    3. Calculate statistics'''))

choice = input("Enter the number of your choice: ")
if choice == '1':
    try:
        column_name = input("Enter the column name to filter by: ")
        value = input("Enter the value to filter by: ")
        filtered_data = data.loc[data[column_name]==value]
        print(filtered_data)
    except KeyError:
        print("Column name not found. Please check the column name and try again. Type it exactly as it appears in the data.")
elif choice == '2':
    print(dedent('''
    Choose what you want to update:
    [A] Row
    [B] Column
    [C] Conditional update'''))

    print("\nExample of conditional update:")
    print('Modify the "Tax Multiplier" in every row where the "Type" column is "Service" to 1.5')
    choice = input("\nEnter your choice (A/B/C): ")
    if choice.upper() == 'A':
        print(f'This is your table: \n{data}\n')
        index = int(input('Type the index number of the row you want to modify: '))
        row_content = data.iloc[index]
        print(f'\n====== Row content ====== \n{row_content}')
        
        modify = input('Do you want to modify this row? (y/n): ')
        if modify.lower() == 'y':
            modify_row()           
        elif modify.lower() == 'n':
            modify_another_row = input("Row will not be modified.\nDo you want to modify another row? (y/n): ")
            if modify_another_row.lower() == 'y':
                modify_row()
            else:
                print("No changes will be made to the data.")
            
    elif choice.upper() == 'B':
        print(f'This is your table: \n{data}\n')
        modify_column()
        
    elif choice.upper() == 'C':
        pass
