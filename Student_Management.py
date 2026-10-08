students=[{"id":1,"name":"sakthi","age":23},{"id":2,"name":"vel","age":21},{"id":3,"name":"Mukil","age":27}]
print("All Student")
for s in students:
    print("ID:",s["id"])
    print("Student Name:",s["name"])
    print("Age:",s["age"])

search_id=int(input("Enter Student ID:"))

for s in students:
    if(search_id==s["id"]):
        print("ID:",s["id"])
        print("Student Name:",s["name"])
        print("Age:",s["age"])

        