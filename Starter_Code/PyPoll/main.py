import csv
import os
# Set CSV path and output txt path
election_csv = os.path.join("Resources", "election_data.csv")
output_path = "election_analysis.txt"

# Declare variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read CSV file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip first row (Header)
    csv_header = next(csv_file)
    # Read through each row (minus the header)
    for row in csv_reader:
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Print results!
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})\n")
        
    # Check for the winner
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Print winner
print("-------------------------\n")
print(f"Winner: {winner['name']}\n")
print("-------------------------\n")

# Export results! (same but to output)
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes
    
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner['name']}\n")
    txtfile.write("-------------------------\n")