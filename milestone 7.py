# milestone 7
from flask import Flask, request, jsonify
import csv


app = Flask(__name__)

employee_id = 0


def generate_unique_id(employee):
    global employee_id
    id = employee_id
    employee_id += 1
    return id


@app.get("/birthdates")
def get_birthdays():
    month = request.args.get("month")
    department = request.args.get("department")

    employees = []
    with open("database.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract birthday month from 'birthdate' field
            birthdate_month = row["birthdate"].split(".")[1]
            if birthdate_month == month and row["department"] == department:
                employees.append({
                    "id": generate_unique_id(row),
                    "name": f"{row['first_name']} {row['last_name']}",
                    "birthday": row["birthdate"]
                })
    report = {
        "total": len(employees),
        "employees": employees
    }

    return jsonify(report)


@app.get("/anniversaries")
def get_anniversaries():
    month = request.args.get("month")
    department = request.args.get("department")

    employees = []
    with open("database.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract anniversary month from 'hiringdate' field
            anniversary_month = row["hiringdate"].split(".")[1]
            if anniversary_month == month and row["department"] == department:
                employees.append({
                    "id": generate_unique_id(row),
                    "name": f"{row['first_name']} {row['last_name']}",
                    "anniversary": row["hiringdate"]
                })
    report = {
        "total": len(employees),
        "employees": employees
    }

    return jsonify(report)


if __name__ == '__main__':
    app.run(debug=True)
