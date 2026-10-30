expense = float(input("Foreign expense: "))
rate = float(input("Exchange rate: "))
budget = float(input("Budget: "))

total = expense * rate
total += total * 0.02

print("Total Expense:", total)
if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")