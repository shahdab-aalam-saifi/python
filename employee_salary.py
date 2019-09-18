import print_module as m
import re


def main():
    file_name = m.save_employee_details()
    name = input("Enter a name: ")

    with open(file_name, "r") as h:
        found = False
        for row in h:
            if re.match(name, row):
                found = True
                lst = re.split(" ", row)
                print(lst[0], lst[2])

        if not found:
            print("Nothing found :(")


if __name__ == '__main__':
    main()