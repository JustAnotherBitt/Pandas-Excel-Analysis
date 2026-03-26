###### Imports #######

import pandas as pd
import matplotlib.pyplot as plt
import time
from textwrap import dedent
from pathlib import Path
from functions import *
from openpyxl import load_workbook

###### Data loading #######

print('To use this program, first you need to put the excel file you want to analyze in the same directory of it.')

table_name = input('Type the name of the Excel file you want to analyze (without the .xlsx extension): ').strip()
data = load_data(table_name=table_name)

print(f"\nFile loaded successfully! [{data.shape[0]} rows x {data.shape[1]} columns]")

see_data = input("\nDo you want to see the data? (y/n): ")
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
        4. See data
        5. Exit
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
        
        
        while choice.upper() not in ['A', 'B', 'C']:
            choice = input("\nEnter your choice (A/B/C) or type 'exit' to quit: ").strip()
        
            if choice.upper() == 'A':
                update_row(data=data)
                break
                    
            elif choice.upper() == 'B':
                modify_column(data=data)
                break
                
            elif choice.upper() == 'C':
                conditional_update(data=data)
                break
            
            elif choice.lower() == 'exit':
                print("Exiting the update menu.")
                break
            
            else:
                print("Invalid option. Try again...")

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
        
        while choice.upper() not in ['A', 'B', 'C', 'D', 'E', 'F']:
            
            choice = input("\nEnter your choice (A/B/C/D): ")
            
            if choice.upper() == 'A': 
                calculate_mean(data=data)
                break
                
            elif choice.upper() == 'B':
                calculate_median(data=data)
                break
                
            elif choice.upper() == 'C':
                calculate_mode(data=data)
                break

            elif choice.upper() == 'D':
                calculate_std(data=data)
                break

            elif choice.upper() == 'E':
                calculate_max(data=data)
                break

            elif choice.upper() == 'F':
                calculate_min(data=data)
                break
                        
            else:
                print("Invalid option. Try again...")
            
        
    elif choice == '4':
        print(data)
            
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid option. Try again...")
        