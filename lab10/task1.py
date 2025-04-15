import psycopg2
import csv

conn=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cursor=conn.cursor()
with open('phonebook.csv','r',encoding='utf-8')as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("INSERT INTO phonebok (name, phone) VALUES (%s, %s)", (row[0], row[1]))

conn.commit()
while True:
    print("меню фoнбукa")
    print("1.пользователь косу")
    print("2.обновление имя\тел")
    print("3.найти юзера")
    print("4.удалить юзера")
    print("5.показать всех")
    print("6.выйти")

    choice=input("deistvie:")
    
    if choice=="1":
        name=input("name;")
        phone=input("phone number:")
        cursor.execute("INSERT INTO phonebok (name,phone) VALUES (%s, %s)", (name,phone))
        conn.commit()

    elif choice == "2":
        old_name = input("enter to update ")
        new_name = input("new name if you want update but if don't just ostav pustym ")
        new_phone = input("new phone if don't ta je fignya ")
        
        if new_name:
            cursor.execute("UPDATE phonebok SET name = %s WHERE name = %s", (new_name, old_name))
        if new_phone:
            cursor.execute("UPDATE phonebok SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))
        conn.commit()
        print("updated")

    elif choice == "3":
        filter_value = input("enter name or phone to search")
        cursor.execute("SELECT * FROM phonebok WHERE name ILIKE %s OR phone = %s", (f"%{filter_value}%", filter_value))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == "4":
        to_delete = input("vvesty chtoto dlya udalenya")
        cursor.execute("DELETE FROM phonebok WHERE name = %s OR phone = %s", (to_delete, to_delete))
        conn.commit()
        print("deleted, udalyaetsya")

    elif choice == "5":
        cursor.execute("SELECT * FROM phonebok ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == "6":
        print("Vyxod")
        break

    else:
        print("error")


cursor.close()
conn.close()
