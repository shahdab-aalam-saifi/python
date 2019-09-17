empNo=input("Enter employee no.: ")
empName=input("Enter employee name: ")
basicSalary=int(input("Enter employee basic salary: "))
allowance=int(input("Enter employee allowance: "))
deductions=int(input("Enter employee deductions: "))

print("Employee name is", empName)

grossSalary=basicSalary+allowance
netSalary=grossSalary-deductions

print("Salary in hand", netSalary)