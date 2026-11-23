import os
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.categories = ["Food", "Transport", "Utilities", "Entertainment"]
        self.load_data()

    def load_data(self):
        # Step 2: Load existing data and clean missing/invalid entries
        if os.path.exists(self.filename):
            self.df = pd.read_csv(self.filename)
            self.df = self.df.dropna(subset=["Date", "Amount", "Category"])
            self.df["Amount"] = pd.to_numeric(self.df["Amount"], errors="coerce")
            self.df = self.df[self.df["Amount"] > 0]
        else:
            self.df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])

    def save_data(self):
        self.df.to_csv(self.filename, index=False)

    def add_expense(self, date, amount, category, description):
        # Step 1: Validate inputs using control structures
        try:
            datetime.strptime(date, "%Y-%m-%d")
            amt = float(amount)
            cat = category.strip().title()
            desc = description.strip()
            if amt <= 0 or cat not in self.categories or not desc:
                return False
        except (ValueError, TypeError):
            return False

        new_row = pd.DataFrame([{
            "Date": date,
            "Amount": round(amt, 2),
            "Category": cat,
            "Description": desc
        }])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.save_data()
        return True

    def get_summary(self):
        # Step 3: Calculate total, average, and category-wise spending using NumPy
        if self.df.empty:
            return

        amounts = np.array(self.df["Amount"])
        total = np.sum(amounts)
        average = np.mean(amounts)

        print(f"\nTotal Expenses: ${total:.2f} | Average Expense: ${average:.2f}")
        print("Category-wise Spending:")
        for cat in self.categories:
            cat_data = np.array(self.df[self.df["Category"] == cat]["Amount"])
            cat_total = np.sum(cat_data) if len(cat_data) > 0 else 0.0
            print(f"  {cat}: ${cat_total:.2f}")

    def filter_expenses(self, condition):
        # Step 4: Filter expenses by category, date range, or amount
        if self.df.empty:
            return self.df

        cond = str(condition).strip()
        if cond.title() in self.categories:
            return self.df[self.df["Category"].str.lower() == cond.lower()]
        elif "-" in cond:
            return self.df[self.df["Date"].str.contains(cond)]
        else:
            try:
                max_amt = float(cond)
                return self.df[self.df["Amount"] <= max_amt]
            except ValueError:
                return self.df

    def generate_report(self):
        # Outputs a summary report with key metrics: Category share, Monthly average spending, and Trends
        if self.df.empty:
            return

        amounts = np.array(self.df["Amount"])
        total_spent = np.sum(amounts)
        print(f"\nTotal: ${total_spent:.2f} | Average: ${np.mean(amounts):.2f}")

        # Spending Percentage by Category using NumPy
        cat_spending = {}
        for cat in self.categories:
            cat_amounts = np.array(self.df[self.df["Category"] == cat]["Amount"])
            cat_sum = np.sum(cat_amounts) if len(cat_amounts) > 0 else 0.0
            cat_spending[cat] = cat_sum
            percentage = (cat_sum / total_spent) * 100 if total_spent > 0 else 0.0
            print(f"Spending Percentage by Category ({cat}): ${cat_sum:.2f} ({percentage:.2f}%)")

        top_cat = max(cat_spending, key=cat_spending.get)
        print(f"Top Spending Category: {top_cat}")

        # Monthly Average Spending using Pandas Grouping
        df_temp = self.df.copy()
        df_temp["Month"] = pd.to_datetime(df_temp["Date"]).dt.to_period("M").astype(str)
        monthly = df_temp.groupby("Month")["Amount"].agg(["sum", "mean"]).reset_index()
        monthly.columns = ["Month", "Total Spent", "Monthly Average Spending"]

        for _, row in monthly.iterrows():
            print(f"Month {row['Month']}: Total = ${row['Total Spent']:.2f}, Monthly Average Spending = ${row['Monthly Average Spending']:.2f}")

        top_month = monthly.loc[monthly["Total Spent"].idxmax()]
        print(f"Top Spending Period: {top_month['Month']}")

    # Step 5: Data Visualization (Matplotlib & Seaborn)
    def plot_bar_chart(self):
        cat_totals = self.df.groupby("Category")["Amount"].sum().reset_index()
        plt.figure(figsize=(7, 5))
        sns.barplot(data=cat_totals, x="Category", y="Amount")
        plt.title("Total Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Expenses ($)")
        plt.show()

    def plot_line_graph(self):
        trend = self.df.groupby("Date")["Amount"].sum().reset_index()
        plt.figure(figsize=(8, 5))
        plt.plot(pd.to_datetime(trend["Date"]), trend["Amount"], marker="o", color="blue")
        plt.title("Spending Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount Spent ($)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def plot_pie_chart(self):
        cat_totals = self.df.groupby("Category")["Amount"].sum()
        plt.figure(figsize=(6, 6))
        plt.pie(cat_totals, labels=cat_totals.index, autopct="%1.1f%%", startangle=90)
        plt.title("Proportional Spending Distribution by Category")
        plt.show()

    def plot_histogram(self):
        amounts = np.array(self.df["Amount"])
        plt.figure(figsize=(7, 5))
        plt.hist(amounts, bins=8, color="skyblue", edgecolor="black")
        plt.axvline(np.mean(amounts), color="red", linestyle="--", label=f"Average (${np.mean(amounts):.2f})")
        plt.title("Frequency Distribution of Expense Amounts")
        plt.xlabel("Expense Amount ($)")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()


def main():
    tracker = ExpenseTracker()

    menu = """
=== SMART EXPENSE TRACKER ===
1. Log New Expense
2. View All Expenses & Summary
3. Filter Expenses
4. Generate Report
5. Visualizations
6. Exit
Enter choice (1-6): """

    while True:
        choice = input(menu).strip()

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            amount = input("Enter amount: ").strip()
            category = input("Enter category (Food, Transport, Utilities, Entertainment): ").strip()
            description = input("Enter description: ").strip()
            if tracker.add_expense(date, amount, category, description):
                print("Expense added.")
            else:
                print("Invalid expense input.")

        elif choice == "2":
            print(tracker.df.to_string(index=False))
            tracker.get_summary()

        elif choice == "3":
            cond = input("Enter category, date, or max amount to filter: ").strip()
            print(tracker.filter_expenses(cond).to_string(index=False))

        elif choice == "4":
            tracker.generate_report()

        elif choice == "5":
            v_choice = input("Select chart (1. Bar, 2. Line, 3. Pie, 4. Histogram): ").strip()
            if v_choice == "1":
                tracker.plot_bar_chart()
            elif v_choice == "2":
                tracker.plot_line_graph()
            elif v_choice == "3":
                tracker.plot_pie_chart()
            elif v_choice == "4":
                tracker.plot_histogram()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
