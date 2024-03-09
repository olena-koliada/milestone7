# report.py 5Milestone
# Part 2 - report
# Write a program report.py that will take as arguments the database file name 
# and month and will print the search result

import csv
from datetime import datetime


def generate_report(database, month):

    # open DB in reading mode
    with open('database.csv', mode='r') as file:
        reader = csv.DictReader(file)

        # create count variables
        total_birthday_count = 0
        total_anniversary_count = 0
        birthday_counts = {}
        work_anniversary_counts = {}
        printed_departments = set()

        for row in reader:
            # getting data for staff from db
            department = row['department']
            birthdate_str = row['birthdate']
            hiringdate_str = row['hiringdate']
          
            # date strings change to datetime objects
            birthdate = datetime.strptime(birthdate_str, '%d.%m.%Y')
            hiringdate = datetime.strptime(hiringdate_str, '%d.%m.%Y')

            # checking and counting birthdates and anniversaries
            if birthdate.month == int(month):
                total_birthday_count += 1
                birthday_counts[department] = birthday_counts.get(department, 0) + 1
            elif hiringdate.month == int(month):
                total_anniversary_count += 1
                work_anniversary_counts[department] = work_anniversary_counts.get(department, 0) + 1


# Print the report by categories and departments
    print("-" * 50)
    print("Celebrations during the month: ")
    print("-" * 50)
    for department in sorted(set(birthday_counts.keys()) | set(work_anniversary_counts.keys())):  # combine the unique departments from both dicts
        if department not in printed_departments:
            printed_departments.add(department)
            print("-" * 50)
            print(f"Department: {department}")
            print("-" * 50)

            if department in birthday_counts:
                print(f"Birthdays: {birthday_counts[department]}")
            else:
                print("Birthdays: No Birthdays this month.")

            if department in work_anniversary_counts:
                print(f"Anniversaries: {work_anniversary_counts[department]}")
            else:
                print("Anniversaries: No anniversaries this month.")

            print("-" * 50)

    print("-" * 50)
    print(f"Total Birthdays: {total_birthday_count}")
    print(f"Total Anniversaries: {total_anniversary_count}")
    print("-" * 50)
# input info from user


database = input("Введіть ім'я файлу бази даних: ")
month = input("Введіть звітний місяць (1-12): ")

generate_report(database, month)
