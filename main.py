###### Imports #######

import pandas as pd
import matplotlib.pyplot as plt
from textwrap import dedent
from pathlib import Path
from functions import *

###### Intro #######

print('To use this program, first you need to put the excel file you want to analyze in the same directory of it.')
table_name = input('Type the excel file name exactly as it appears in the file (do not include the .xlsx extension): ').strip()

###### Data loading #######

try:
    data = pd.read_excel(table_name + '.xlsx')
except FileNotFoundError:
    print("File not found. Please check the excel file name and try again.")
    exit()
    
print("File loaded successfully.")

see_data = input("Do you want to see the data? (y/n): ")

if see_data.lower() == 'y':
    print(data)
else:
    print("Data will not be displayed.")


###### Data analysis #######

while True:
    print("\n======== Data analysis ========")
    print(dedent('''
        What do you want to do?
        1. Filter data by column value
        2. Update values
        3. Calculate statistics
        4. Exit
    '''))

    choice = input("Enter the number of your choice: ").strip()
    if choice == '1':
        filter_data(data=data)
            
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
            update_row(data=data)
                
        elif choice.upper() == 'B':
            modify_column(data=data)
            
        elif choice.upper() == 'C':
            conditional_update(data=data)

    elif choice == '3':
        print(dedent('''
        Choose the statistic you want to calculate:
        [A] Mean
        [B] Median
        [C] Mode
        [D] Standard Deviation
        [E] Maximum
        [F] Minimum
        '''))
        
        choice = input("\nEnter your choice (A/B/C/D): ")
        
        if choice.upper() == 'A': 
            calculate_mean(data=data)
            
        elif choice.upper() == 'B':
            calculate_median(data=data)
            
        elif choice.upper() == 'C':
            calculate_mode(data=data)

        elif choice.upper() == 'D':
            calculate_std(data=data)

        elif choice.upper() == 'E':
            calculate_max(data=data)

        elif choice.upper() == 'F':
            calculate_min(data=data)
            
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid option. Try again...")
        