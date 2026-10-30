material = int(input("Material cost: "))
labour = int(input("Labour cost: "))
machine = int(input("Machine cost: "))
selling = int(input("Selling price: "))

cost = material + labour + machine
profit = selling - cost

print("Profit:", profit)
if profit >= 500:
    print("Target Achieved")
else:
    print("Target Not Achieved")