import csv
import os
# Set CSV path and output txt path
budget_csv = os.path.join("Resources", "budget_data.csv")
output_path = "budget_analysis.txt"

# Declare variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read CSV file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip first row (Header)
    csv_header = next(csv_file)
    # Read through each row (minus the header)
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss
        
        # Calculate profit/loss change and store the date
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            dates.append(date)
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / (total_months - 1)
# Find best increase/decrease
best_increase = max(profit_loss_changes)
best_increase_date = dates[profit_loss_changes.index(best_increase)]
best_decrease = min(profit_loss_changes)
best_decrease_date = dates[profit_loss_changes.index(best_decrease)]

# Print results!
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {best_increase_date} (${best_increase})")
print(f"Greatest Decrease in Profits: {best_decrease_date} (${best_decrease})")

# Export results!
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {best_increase_date} (${best_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {best_decrease_date} (${best_decrease})\n")