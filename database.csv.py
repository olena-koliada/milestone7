# database 5 Milestone_report.py

import csv
from generate_data import staff

with open('database.csv', 'w') as file:
    fieldnames = ['first_name', 'last_name', 'department', 'birthdate', 'hiringdate']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(staff)
