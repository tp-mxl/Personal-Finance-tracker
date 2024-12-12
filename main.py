import csv
from reports import generate_report

TRANSACTION_FILE = 'transactions.csv'

# Function to add a new transaction
def add_transaction(date, description, amount, category):
    with open(TRANSACTION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])
    print("Transaction added successfully!")

# Function to display all transactions
def view_transactions():
    try:
        with open(TRANSACTION_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("Date | Description | Amount | Category")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No transactions found. Start by adding some.")

# Function to calculate the balance
def calculate_balance():
    try:
        balance = 0
        with open(TRANSACTION_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                balance += float(row[2])
    except FileNotFoundError:
        print("No transactions found. Balance is 0 Baht")
    return balance

# Main application menu
while True:
    print("\nPersonal Finance Tracker")
    print("1. Add a Transaction")
    print("2. View Transactions")
    print("3. View Balance")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount (positive for income, negative for expense): "))
        category = input("Enter category (Income/ Expense): ")
        add_transaction(date, description, amount, category)
    elif choice == '2':
        view_transactions()
    elif choice == '3':
        balance = calculate_balance()
        print("Your current balance is: %.2f Baht" %balance)
    elif choice == '4':
        generate_report()
    elif choice == '5':
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please choose again.")
    