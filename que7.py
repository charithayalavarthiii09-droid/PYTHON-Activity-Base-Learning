price = int(input("Price: "))
qty = int(input("Quantity: "))

total = price * qty

if total >= 1000:
    total -= total * 0.10

tax = total * 0.05
print("Final Bill:", total + tax)