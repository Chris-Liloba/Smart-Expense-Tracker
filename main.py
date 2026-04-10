from tracker import ExpenseTracker

def menu():
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")

tracker = ExpenseTracker()

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        tracker.add_expense(amount, category)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.summary()
    
    elif choice == "4":
        tracker.show_graph()
        input("\nPress Enter to continue...")
    
    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
        input("Press Enter to continue...")