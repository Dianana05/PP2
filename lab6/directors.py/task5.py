my_list = ["apple", "banana", "cherry", "orange"]
file_path = input("way: ")
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(item + '\n')
print("it was written")
