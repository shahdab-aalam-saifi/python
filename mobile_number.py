# data = {
#     "ABC": 123,
#     "DEF": 456,
#     "GHI": 789,
# }

# empName=input("Enter employee name: ")

# print(data[empName])

data = [
    "ABC", 123,
    "DEF", 456,
    "GHI", 789,
]

empName=input("Enter employee name: ")

i=data.index(empName)

print(data[i+1])