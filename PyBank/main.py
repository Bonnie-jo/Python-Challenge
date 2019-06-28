# Import
import os
import csv

# File Path
budget_data = os.path.join('..', 'PyBank', 'budget-data.csv' )

# Setting variables
total_months = 0
total_pl = 0
value = 0
change = 0

# Creating Lists
dates = []
profit = []

# Open and Read the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read header row
    csv_header = next(csvreader)

    # Read first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    # Reading each row after header & first row 
    for row in csvreader:
        # Looking at the dates
        dates.append(row[0])
        
        # Calculating change, then add to list of changes
        change = int(row[1])-value
        profit.append(change)
        value = int(row[1])
        
        # Total number of months
        total_months += 1

        # Total amount of "Profit/Loss"
        total_pl = total_pl + int(row[1])

    # Greatest increase in profit
    greatest_increase = max(profit)
    greatest_index = profit.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease (lowest increase) in profit 
    greatest_decrease = min(profit)
    worst_index = profit.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Loss between months"
    avg_change = sum(profit)/len(profit)
    
# Print 
print("---------------------")
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total Revenue: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profit: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profit: {worst_date} (${str(greatest_decrease)})")
print("---------------------")

# Exporting to .txt file
pyBanktextfile = open("pyBanktextfile.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total Revenue: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profit: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profit: {worst_date} (${str(greatest_decrease)})")
pyBanktextfile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))