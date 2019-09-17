import print_module as m

employees = list(m.get_employee_names().keys())

# for employee in employees:
#     print(employee, len(employee))

# list(map(lambda e: print(e, len(e)), employees))

mp = map(lambda e: (e, len(e)), employees)
print(dict(mp))
