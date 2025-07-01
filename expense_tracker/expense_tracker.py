
balance = 0
transactions = []

while True:
    print("\n1. Add Income\n2. Add Expense\n3. View Balance\n4. Exit")
    choice = input("Select: ")

    if choice == '1':
        amount = float(input("Enter income: "))
        transactions.append(("Income", amount))
        balance += amount
    elif choice == '2':
        amount = float(input("Enter expense: "))
        transactions.append(("Expense", -amount))
        balance -= amount
    elif choice == '3':
        print(f"\nCurrent balance: ${balance}")
        for t in transactions:
            print(f"{t[0]}: ${abs(t[1])}")
    elif choice == '4':
        break
