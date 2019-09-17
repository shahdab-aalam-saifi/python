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