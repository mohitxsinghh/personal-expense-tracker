import json
from datetime import datetime

# File to save the data
DATA_FILE = 'expenses.json'


def load_expenses():
    """Loads expenses from a file at the start of the program."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist yet


def save_expenses(expenses):
    """Saves the current expenses to a file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Adds a new expense to the list."""
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the category (e.g., Food, Transport, etc.):")
        date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")

        # Use today's date if none is provided
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        # Create a new expense entry
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount entered. Please try again.")


def view_summary(expenses):
    """Displays the total spending by category and overall."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    category_totals = {}
    total_spending = 0

    # Summarize expenses
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        total_spending += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    # Display the summary
    print("\nSummary of expenses:")
    for category, total in category_totals.items():
        print(f"Category: {category} | Total spent: ${total:.2f}")
    
    print(f"Overall total spent: ${total_spending:.2f}")


def view_spending_over_time(expenses):
    """Displays spending over time (daily, weekly, or monthly)."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nSpending over time:")
    time_option = input("Choose time period - (D)aily, (W)eekly, (M)onthly: ").upper()

    time_format = '%Y-%m-%d'  # Default to daily
    if time_option == 'W':
        time_format = '%Y-%W'  # Week number format
    elif time_option == 'M':
        time_format = '%Y-%m'  # Month format

    spending_by_time = {}

    # Aggregate spending by time
    for expense in expenses:
        time_key = datetime.strptime(expense["date"], '%Y-%m-%d').strftime(time_format)
        amount = expense["amount"]

        if time_key in spending_by_time:
            spending_by_time[time_key] += amount
        else:
            spending_by_time[time_key] = amount

    # Display the spending summary
    for time_key, total in spending_by_time.items():
        print(f"Time period: {time_key} | Total spent: ${total:.2f}")


def menu():
    """Displays the main menu and handles user input."""
    expenses = load_expenses()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View summary")
        print("3. View spending over time")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            view_spending_over_time(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
