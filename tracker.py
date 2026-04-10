import matplotlib.pyplot as plt
from storage import load_data, save_data
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.data = load_data()

    def add_expense(self, amount, category):
        expense = {
            "amount": amount,
            "category": category,
            "date": str(datetime.now())
        }
        self.data.append(expense)
        save_data(self.data)

        print("Expense added!")

        total = sum(exp["amount"] for exp in self.data)
        print(f"💰 Updated Total: {total}")

    def view_expenses(self):
        for exp in self.data:
            print(exp)

    def summary(self):
        total = sum(exp["amount"] for exp in self.data)
        print(f"Total: {total}")

    # THIS MUST BE INSIDE THE CLASS
    def show_graph(self):
        if not self.data:
            print("No data to display.")
            return

        categories = {}

        for exp in self.data:
            categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

        names = list(categories.keys())
        values = list(categories.values())

        plt.figure()
        plt.bar(names, values)
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")

        plt.show()