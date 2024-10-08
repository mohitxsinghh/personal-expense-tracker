# personal-expense-tracker

## Overview

The **Personal Expense Tracker** is a Python-based command-line application that allows users to record and track their daily expenses. The program supports categorizing expenses, summarizing spending by category, and viewing spending trends over time (daily, weekly, or monthly). All data is stored in a JSON file, enabling persistence between sessions.

## Features

- **Add Expense**: Record new expenses by entering the amount, category, and date.
- **View Summary**: See a summary of total spending by category and overall.
- **View Spending Over Time**: View expenses over different time periods (daily, weekly, or monthly).
- **Persistent Data**: Expenses are saved in a `JSON` file for future use.

## How It Works

### 1. **Add an Expense**

You can add a new expense with the following details:
- `Amount`: The monetary value of the expense.
- `Category`: The category for the expense (e.g., Food, Transport, etc.).
- `Date`: The date of the expense (default is today's date if no date is provided).

### 2. **View Summary**

The summary feature provides a breakdown of total spending per category as well as an overall total. This helps users understand where their money is going.

### 3. **View Spending Over Time**

The program allows users to view their spending over specific time intervals:
- Daily
- Weekly
- Monthly

### 4. **Data Persistence**

All expenses are stored in a `JSON` file (`expenses.json`). When the program starts, it loads any existing data from the file. All new entries are automatically saved to this file.

## How to Run

### Requirements

- Python 3.x

### Running the Program

1. Clone or download the code to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the code.
4. Run the following command:

```bash
python expense_tracker.py
