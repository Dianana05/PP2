import json
with open(r"C:\Users\user\Desktop\PP2\lab4\create.json", "r") as file:
    create=json.load(file)

newstudent={"name": "David", "age": 28,"city": "Almaty"}
create["students"].append(newstudent)
students=create["students"]

with open("create.json", "w") as file:
    json.dump(create, file, indent=4)

print("New student was added")

students=create["students"]
for student in students:
    print("Имя:", student["name"], ", Возраст:", student["age"], ", Город:", student["city"])