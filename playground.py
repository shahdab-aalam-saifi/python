# name="Shahdab Aalam"
# surname='Saifi'

# print(name + " " + surname)
# print(name, surname)


# no=input("Enter number: ")

# print(no)
# print(type(no))

# print(10 is int)
# print(bool(int))

# print("hah" in "ShahdabAalamSaifi")

# print(map(str.lower, "Shahdab") in map(str.lower, ["Shahdab", "Aalam", "Saifi"]))

# print(bin(25), bin(-15), bin(25 | -15), 25 | -15)

# print(~25 << 2)

# nl = [123,3435,12323,546]
# sl = ["shahdab", "aalam", "saifi"]
# fl = [232.3534, 23423.322, 565.322]
# mix = [234, 23423.53, "shahdab"]

# print(nl, sl, fl, mix[2])

# print(nl[::-2])

# print(sl[0][::-1])

# sl.insert(2, "mohamed")

# del sl[2]

# sl.pop(2)

# nl.extend(sl)

# print(nl, sl)

# print(sum(nl), min(nl), max(nl), len(nl))

# print((1, 2, 3))

# print("shahdab".count("a"))

# t=(1, 3, "shahdab", ("tuple"))
# print(t[-1][0])

# t=(323,65,7887,22)
# print(sorted(t))
# print(sorted(t, reverse=True))

# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# months = {
#     "Jan": 31,
#     "Feb": 28,
#     "Mar": 31,
#     "Apr": 30,
#     "May": 31,
# }

# print(months["Apr"])
# print(list(months.keys()))
# print(months.values())

# for month in months:
#     if months[month] == 31:
#         print(month)

# squares = []

# for num in range(1, 11):
#     squares.append(num * num)

# print(squares)

# print([num * num for num in range(1, 11)])
# print([num * num for num in range(1, 11) if num % 2 == 0])

# [print(num * num, end=" ") for num in range(1, 11)]

# fibs = [1, 1]
# for i in range(2, 10):
#     fibs.append(fibs[i-1] + fibs[i-2])

# print(fibs)

# fibs = [1, 1]
# [fibs.append(fibs[i-1] + fibs[i-2]) for i in range(2, 100)]
# print(fibs)

# set1 = ({1, 4, 6,3, 2})
# set2 = {x for x in range(10)}
# set2.add(4234)
# set2.discard(4)

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)

# def add(x, y):
#     # perform action
#     # return result
#     return x + y
#
#
# print(add(10, 20))

# def empty():
#     pass

# print(empty())

# def display_list(lst=[]):
#     for item in lst:
#         print(item)
#     pass
#
# display_list([item for item in range(10)])

# def add_nos(x,y,z):
#     return x + y + z
#
#
# print(add_nos(z=100, y=10, x=2))

# def print_list(lst):
#     for i in lst:
#         print(i)
#     pass
#
#
# print_list([3424, 3214, 2342, 234])

# it = iter([x for x in range(10)])
# print(next(it))
# print(next(it))
# print(next(it))

# p = lambda x, y=10: x + y
# print(p(10))
#
#
# print((lambda x, y=10: print(x + y))(10, 20))

# print((lambda lst: sum(lst)/len(lst))([x for x in range(10)]))

# (lambda lst: print([x for x in lst if x % 2 == 0]))([x for x in range(20)])
#
# (lambda lst: print([x*x for x in lst]))([x for x in range(10, 20)])

# m = map(lambda x: x*x, [x for x in range(10, 20)])
# print(list(m))
#
# m = map(lambda x: x*2, { "first_name": "Shadab Aalam", "last_name" : "Saifi"}.values())
# print(list(m))


# import cx_Oracle
#
# connection = cx_Oracle.connect("hr", "hr")
# connection = cx_Oracle.connect("hr/hr@xe")
#
# cur = connection.cursor()
# for row in cur.execute("select * from EMPLOYEES"):
#     emp = list(row)
#     if emp[1].startswith("A"):
#         print(emp)

# import print_module as m

# print(m.get_employee_names())
# m.greet("Shahdab Aalam Saifi")
# print(m.area_of_circle(10))

# handle = open("file.txt", "r")
#
# for line in handle.readlines():
#     print("*", line, "*")
#
# handle.close()

# with open("file.txt", "r") as handle:
#     print(handle.readline())

# with open("file.txt", "r") as handle:
#     words = handle.read().split()
#     # content = handle.read()
#     # print(content.split())
#     # print(content.split(" "))
#     for word in words:
#         print(word)

# import os
#
# file_path = input("Enter file path: ")
#
# if not os.path.isfile(file_path):
#     print(file_path, "is not a file")
#     exit(-1)
#
# with open(file_path, "r") as handle:
#     max_len = 0
#     max_line = ""
#     for line in handle:
#         line_len = len(line)
#         if max_len < line_len:
#             max_len = line_len
#             max_line = line
#
#     print(max_line, max_len)


# print(sorted([{"line":"content", "len": 7},{"line":"content ", "len": 8}], key=lambda i: i["len"], reverse=True))

# file_name = input("Enter file name: ")
#
# with open(file_name, "w") as handle:
#     while True:
#         line = input("Enter a line (exit - Y): ")
#         if line == "Y":
#             break
#         handle.write(line + "\n")

# import xlsxwriter
# import print_module as m
#
# workbook = xlsxwriter.Workbook("2.xlsx")
# worksheet = workbook.add_worksheet()
#
# # worksheet.write("A1", "Name")
# # worksheet.write("B1", "Salary")
#
# row_num = 1
# # employees = m.get_employee_names()
# employees = m.get_employees()
#
# for row in employees:
#     col_num = 0
#     for data in row:
#         worksheet.write(row_num, col_num, data)
#         col_num += 1
#     row_num += 1
#
# print("Done")
# workbook.close()

