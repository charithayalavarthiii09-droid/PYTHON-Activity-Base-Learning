marks = int(input("Aggregate: "))
subject = int(input("Subject marks: "))
attendance = int(input("Attendance: "))
income = int(input("Family income: "))

if marks >= 75 and subject >= 60 and attendance >= 75 and income <= 250000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible")