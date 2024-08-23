import os
import csv

# Initialize lists and variables
months = []
profits = []
changes = []
max_change = 0
min_change = 0

# Read the CSV file and extract data
csvpath=os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # Skip the header
    for row in csv_reader:
        months.append(row[0])
        profits.append(int(row[1]))

# Calculate changes in profit and track the greatest increase and decrease
for i in range(1, len(profits)):
    change = profits[i] - profits[i - 1]
    changes.append(change)
   
    if change > max_change:
        max_change = change
        max_month = months[i]
   
    if change < min_change:
        min_change = change
        min_month = months[i]

# Calculate average change
average_change = round(sum(changes) / len(changes), 2)

# Saving results in variable
results = (
    "Financial Analysis\n"
    + "-" * 25 +"\n"
    f"Total Months: {len(months)}\n"
    f"Total: ${sum(profits)}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})"
)

# Print the results
print(results)


# Define the path for the output text file
output_path = os.path.join('analysis', 'analysis.txt')

# Write the result to text file 
with open(output_path, 'w') as file:
    file.write(results) 

