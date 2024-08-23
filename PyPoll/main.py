import os
import csv

# Initialize variables
total_votes = 0
candidate_votes = {}


# Read the CSV file and extract data
csvpath=os.path.join('Resources', 'election_data.csv')
# Read CSV file
with open(csvpath) as file:
    csvreader = csv.reader(file, delimiter=",")
    next(csvreader)  # Skip header
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Initialize variables for determining the winner
max_votes = 0
winner = ""

# Find the winner using a dictionary
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Saving results in variables
result1 = ( 
            "\nElection Results\n"
            + "\n"+'-' * 25 + "\n"
            f"\nTotal Votes: {total_votes}\n"
            + "\n"+'-' * 25 + "\n"

        )

result2 = ( 
            "\n"+'-' * 25 + "\n"
            f"\nWinner: {winner}\n"
            + "\n" +'-' * 25 + "\n" 
)    

# Print results
print(result1)

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})\n')

print(result2)

# Define the path for the output text file
output_path = os.path.join('analysis', 'analysis.txt')

# Write the result to text file 
with open(output_path, 'w') as file:
    file.write(result1)
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f'\n{candidate}: {percentage:.3f}% ({votes})\n')
    file.write(result2)