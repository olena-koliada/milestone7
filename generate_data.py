# generate_data.py
import random


# name,surname, department lists
first_names = ["Ivan", "Maria", "Petro", "Elena", "Andriy", "Natalia", "Anna", "Alexander", "Tetyana", "Yurii"]
last_names = ["Kovalenko", "Grygorenko", "Shevchenko", "Boiko", "Levchenko", "Kravchenko", "Dovchenko", "Hnatenko", "Granenko", "Kucherenko"]
departments = ["HR", "Finance", "Engineering", "R_D", "Analytical"]


# birthdates
def generate_random_birthdates():
    year_b = random.randint(1983, 2003)
    month = random.randint(1, 12)
    if month != 2:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 28)
    return f"{day}.{month}.{year_b}"


# hiringdates
def generate_random_hiringdates(year_b):
    year_b = int(birthdate.split(".")[2])
    min_year_h = year_b + 18   # mind the minim age of hiring
    year_h = random.randint(min_year_h, 2023)  # to mind the max year of hiring

    # year_h = random.randint(2000, 2022)
    month = random.randint(1, 12)
    if month != 2:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 28)
    return f"{day}.{month}.{year_h}"


# staff list


staff = []
for _ in range(20):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    department = random.choice(departments)
    birthdate = generate_random_birthdates()
    hiringdate = generate_random_hiringdates(birthdate)
    employee = {"first_name": first_name, "last_name": last_name, "department": department, "birthdate": birthdate, "hiringdate": hiringdate}
    staff.append(employee)

# Вивід результату
for employee in staff:
    print(f"{employee['first_name']:.15} {employee['last_name']:.15}, {employee['department']:.20}, birthdate: {employee['birthdate']:.10}, hiringdate: {employee['hiringdate']:.10}")
