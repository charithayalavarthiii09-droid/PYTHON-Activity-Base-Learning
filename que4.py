basic = int(input("Basic salary: "))
allowance = int(input("Allowances: "))
overtime = int(input("Overtime: "))
incentive = int(input("Incentive: "))

gross = basic + allowance + overtime + incentive
net = gross - gross * 0.10

print("Gross:", gross)
print("Net Salary:", net)