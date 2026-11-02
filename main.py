
import csv
from pathlib import Path

file = Path("expenses.csv")

print("Welcome to Smart Expense Tracker!")

while True:
    category = input("\nExpense category: ")

    try:
        amount = float(input("Amount in rupees: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if amount <= 0:
        print("Amount must be greater than zero.")
        continue

    new_file = not file.exists()

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)

        if new_file:
            writer.writerow(["Category", "Amount"])

        writer.writerow([category, amount])

    print("Expense saved successfully!")

    choice = input("Add another expense? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nAll expenses saved. Goodbye!")
