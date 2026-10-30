venue = int(input("Venue cost: "))
food = int(input("Catering cost: "))
equipment = int(input("Equipment cost: "))
transport = int(input("Transport cost: "))
fee = int(input("Fee per participant: "))

total = venue + food + equipment + transport
count = (total + fee - 1) // fee

print("Total Cost:", total)
print("Break-even Participants:", count)