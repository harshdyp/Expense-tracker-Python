# Smart Expense Tracker

A simple Python application to log, analyze, and visualize personal expenses using Control Structures, Object-Oriented Programming (OOP), NumPy, Pandas, Matplotlib, and Seaborn.

---

## Project Overview

The Smart Expense Tracker helps users monitor their spending habits over time. It provides:
1. **Expense Logging & Validation**: Enter date, amount, category, and description with input validation.
2. **OOP Design**: Built with the `ExpenseTracker` class implementing core management methods.
3. **Data Analysis**: Computes totals, averages, category percentages, and monthly metrics using NumPy and Pandas.
4. **Data Visualization**: Generates Bar Charts, Line Graphs, Pie Charts, and Histograms with Matplotlib and Seaborn.

---

## Deliverables

- `expense_tracker.py`: Complete Python script implementing all required modules and visualizations.
- `expenses.csv`: Sample dataset structured with columns `Date`, `Amount`, `Category`, `Description`.
- `README.md`: Documentation containing project description, dependencies, and setup/usage instructions.

---

## Dependencies

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- Seaborn

### Installation

Install the required libraries with pip:

```bash
pip install numpy pandas matplotlib seaborn
```

---

## Setup and Usage Instructions

1. Place `expense_tracker.py` and `expenses.csv` in the same directory.
2. Run the application from your terminal:

```bash
python expense_tracker.py
```

### Menu Options

```text
=== SMART EXPENSE TRACKER ===
1. Log New Expense
2. View All Expenses & Summary
3. Filter Expenses
4. Generate Report
5. Visualizations
6. Exit
```

- **Option 1 (Log New Expense)**: Enter expense date (`YYYY-MM-DD`), positive amount, category (`Food`, `Transport`, `Utilities`, `Entertainment`), and description.
- **Option 2 (View All Expenses & Summary)**: Displays all stored records and overall summary metrics calculated using NumPy.
- **Option 3 (Filter Expenses)**: Filter expenses by category, date, or maximum amount.
- **Option 4 (Generate Report)**: Displays category spending percentages, monthly average spending, and top spending categories and periods.
- **Option 5 (Visualizations)**: Displays financial charts:
  - Bar Chart: Total expenses by category
  - Line Graph: Spending trends over time
  - Pie Chart: Proportional spending distribution by category
  - Histogram: Frequency distribution of expense amounts
- **Option 6 (Exit)**: Exits the application.

---

## Programmatic Usage

You can also import and use the `ExpenseTracker` class directly in Python:

```python
from expense_tracker import ExpenseTracker

tracker = ExpenseTracker("expenses.csv")

# 1. Log an expense
tracker.add_expense("2025-04-01", 35.00, "Food", "Lunch")

# 2. View summary
tracker.get_summary()

# 3. Filter expenses
food_records = tracker.filter_expenses("Food")

# 4. Generate summary report
tracker.generate_report()

# 5. Visualizations
tracker.plot_bar_chart()
tracker.plot_line_graph()
tracker.plot_pie_chart()
tracker.plot_histogram()
```
