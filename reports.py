import csv
import matplotlib.pyplot as plt

def generate_report():
    income = 0
    expenses = 0

    try:
        with open('transactions.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                amount = float(row[2])

                if amount > 0:
                    income += amount
                else:
                    expenses += abs(amount)

        print("Total Income: %.2f Baht" % income)
        print("Total Expenses: %.2f Baht" % expenses)
        print("Remaining Balance: %.2f Baht" % (income - expenses))

        generate_chart(income, expenses)

    except FileNotFoundError:
        print("No transactions found. Report cannot be generated.")

# Function to create a bar chart for income and expenses
def generate_chart(income, expenses):
    labels = ["Income", "Expenses"]
    values = [income, expenses]

    plt.bar(labels, values, color=["green", "red"])
    plt.title("Income vs Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (Baht)")
    plt.tight_layout()
    plt.show()
