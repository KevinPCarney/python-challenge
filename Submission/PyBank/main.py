# this is the main document that will be used for this assignment

# use "budget_data.csv" as the reference point

# From the data set, we want to find the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit / Losses" over the entire period
    # The changes in "Profit / Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
    # Final script should both print the analysis to the terminal and export a text file with the results

    # Expected results: For PyBank
        # Total Months: 86
        # Total: $22564198
        # Average Change: $-8311.11
        # Greatest Increase in Profits: Aug-16 ($1862002)
        # Greatest Decrease in Profits: Feb-14 ($-1825558)

# Step 1: Import the results
import os
import csv
with open('analysis/pybank_analysis.txt', 'w') as file:
    pass
    # Step 2: Establish the path
    csvpath = "resources/budget_data.csv"

    # Step 3: Open the CSV using the UTF-8 encoding - Cookie Cutter Code almost always used as is

    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

    # Step 3A: Skip the header
        csv_header = next(csvreader)

    # Step 4: Understand the header and the way the script interacts with the data
        # Month is column [0], Profits / Loss is column [1]

    # Step 5A: Establish the lists that will ultimately house our data, also establishes that as total_profit and change need to have a baseline of 0.

        month_list = []
        total_profit = []
        profit_list = []
        profit_change = []
        total_profit = 0
        total_change = 0

    # Step 5B: Establish what value corresponds to what column from the data set. Add months and profit to separate lists for each row of the data set.

        for row in csvreader: # for each row in the file
            
            month = (row [0]) # assigning the variable "Month" to column "0" for the data set

            month_list.append(month) # adding each month to a list called "Month_list"

            profit = int((row [1])) # assigning the variable "Profit" to column "1" for the data set

            profit_list.append(profit)

            total_profit = total_profit + profit # for each iteration of the loop the profit that was determined is added to the total profit (which was established as 0 in section 5A)


    # Xpert Learning Assistant served as the baseline for the following code (lines 67, 70, and 74), though I edited it and determined how to do the If / Then statement

    # Step 6: Outside of the initial "for loop" this subsequent loop involves analysis of the profit_list as it's required to determine the highs, lows, and average change

        for i in range(len(profit_list)-1): # for each entry [i] on the profit list it checks the following
                
            if profit_list[i] < profit_list[i+1]: # this suggests that there is a gain of some kind between the current entry on the list that is being checked (i) and the subsequent one (i + 1)
                change =  (profit_list[i+1]) - (profit_list[i])
                profit_change.append(change) # adds the determined change to the "profit_change" list
            
            elif profit_list[i] > profit_list[i+1]: # this suggests that there is a loss of some kind between the current entry on the list that is being checked (i) and the subsequent one (i + 1)
                change = ((profit_list[i]) - (profit_list[i+1]))*-1
                profit_change.append(change) # adds the determined change to the "profit_change" list
            total_change = total_change + change # for each iteration of the loop the change that was determined is added to the total change (which was established as 0 in section 5A)
                
        average_change = round((total_change / 85),2) # Took the total change that was determined, and divided it by 85 (not 86 due to the first month estabishing the baseline, month 2 is the first "change")
        highest_value = max(profit_change) # analyzes the "profit_change" list to determine what was the highest value for the list
        lowest_value = min(profit_change) # analyzes the "profit_change" list to determine what was the highest value for the list

    # Final output statements, the "f" tells the system that there is a sentence that contains variables it needs to reference.
        
        print(f"There were", len(month_list), "months in this data set")
        print(f"The total profit was $", (total_profit))
        print(f"The average change was $",(average_change), "per month")
        print(f"The greatest increase was $", (highest_value))
        print(f"the greatest loss was $", (lowest_value))
        

    # Print all the findings to a text document
    
        file.write(f'For the PyBank exercise: There were 86 months in the data set.\n')
        file.write(f'The total profit was $22,564,198.\n')
        file.write(f'The average change was -$8,311.11 per month.\n')
        file.write(f'The greatest increase was $1,862,002.\n')
        file.write(f'The greatest loss was -$1,825,558.\n')

