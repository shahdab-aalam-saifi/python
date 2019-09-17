def read_names():
    lst_names = []
    while True:
        name = input("Enter name (for exit - X): ")
        if name == "X":
            break
        lst_names.append(name)
    return lst_names


names = read_names()
print(names)