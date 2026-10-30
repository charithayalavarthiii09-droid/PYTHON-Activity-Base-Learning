c = int(input("Consultation: "))
d = int(input("Diagnostic: "))
t = int(input("Treatment: "))

bill = c + d + t

if bill >= 5000:
    bill -= bill * 0.10

print("Hospital Bill:", bill)