#PyBank
#import libraries
import os
import csv

#path to collect data
budget_csv = os.path.join('..','Resources', 'budget_data.csv')
budget_analysis_output = os.path.join("budget_analysis.txt")

#Define initial variables
total_months = 0
total_revenue = 0
month_change = []
list_changes = []
first_increase = 0
first_decrease = 1000000000
increases = ["",first_increase]
decreases = ["",first_decrease]


#read CSV
with open (budget_csv,'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #read header
    header = next(csvreader)

#get values in row 1 (exclufing header)
    row1 = next(csvreader)
    total_months = total_months + 1
    total_revenue = total_revenue + int(row1[1])
    prevoious_revenue = int(row1[1])

    for row in csvreader:
        #Recalculate totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        revenuew_change = int(row[1]) - prevoious_revenue
        prevoious_revenue = int(row[1])
        list_changes.append(revenuew_change)

        #Determine greatest increase
        if revenuew_change > increases [1]:
            increases[0] = row[0]
            increases[1] = revenuew_change

        #Determine greatest decrease
        if revenuew_change < decreases [1]:
            decreases[0] = row[0]
            decreases[1] = revenuew_change

#average changes
avg_changes = sum(list_changes)/len(list_changes)
total_revenue = "${:,.1f}".format(total_revenue)
avg_changes = "${:,.1f}".format(avg_changes)

#pritn in terminal
print(f"Financial Analysis")
print(f"----------------------------------")
print(f"Total months: {total_months}")
print(f"Total revenue: {total_revenue}")
print(f"Average Change: {avg_changes}")
print(f"Greatest Increase in Profit {increases[0]} (${float(increases[1])})")
print(f"Greatest Decrease in Profit {decreases[0]} (${float(decreases[1])})")

#extract results in a new file
export = (
    f"\nFinancial Analysis\n"
    f"----------------------------------\n"
    f"Total months: {total_months}\n"
    f"Total revenue: {total_revenue}\n"
    f"Average Change: {avg_changes}\n"
    f"Greatest Increase in Profit {increases[0]} (${float(increases[1])})\n"
    f"Greatest Decrease in Profit {decreases[0]} (${float(decreases[1])})\n"    
)

with open (budget_analysis_output, "w") as analysis_txt:
    analysis_txt.write(export)