usage = int(input("Data usage in GB: "))
budget = int(input("Budget: "))

plans = [199, 299, 399]

for p in plans:
    if p <= budget:
        print("Eligible Plan:", p)
        break
else:
    print("No suitable plan")