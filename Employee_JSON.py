import json

with open("employee.json","r")as f:

    employees=json.load(f)
for e in employees:
    print("Name:",e["name"])
    print("Department:",e["department"])
    print()


