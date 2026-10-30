distance = int(input("Distance: "))
age = int(input("Age: "))
fare = distance * 2 + 50

if distance > 100:
    fare += 100
if age >= 60:
    fare *= 0.8

print("Railway Fare:", fare)