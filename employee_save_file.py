class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return str({"id": self.id, "name": self.name, "salary": self.salary})


def save(lst, file_name="employee.txt"):
    with open(file_name, "w") as h:
        for employee in lst:
            h.write(str(employee) + "\n")


employees = [
    Employee(100, "Shahdab", 1000),
    Employee(101, "Aalam", 2000),
    Employee(102, "Saifi", 3000),
]

save(employees)
save(employees, "data.txt")

