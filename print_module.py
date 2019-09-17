import cx_Oracle as oracle
import math


def greet(name=""):
    print("Hello", name)


def get_employee_names():
    connection = oracle.connect("hr/hr@xe")
    rows = connection.cursor().execute("select first_name, salary from employees")
    return dict((x for x in rows))

def get_employees():
    connection = oracle.connect("hr/hr@xe")
    rows = connection.cursor().execute("select * from employees")
    return list(rows)

def area_of_circle(r = 0):
    return math.pi * r**2

