import cx_Oracle as oracle
import math


def greet(name=""):
    print("Hello", name)


def get_employee_names():
    connection = oracle.connect("hr/hr@xe")
    rows = connection.cursor().execute("select first_name, salary from employees")
    return dict((x for x in rows))


def save_employee_details(file_name="employee.txt"):
    with oracle.connect("hr/hr@xe") as connection:
        rows = connection.cursor().execute("select first_name, last_name, salary, job_id from employees")
        with open(file_name, "w") as h:
            for row in rows:
                h.write("{} {} {} {}\n".format(row[0],row[1], row[2], row[3]))
    return file_name


def get_employees():
    connection = oracle.connect("hr/hr@xe")
    rows = connection.cursor().execute("select * from employees")
    return list(rows)


def area_of_circle(r=0):
    return math.pi * r**2

