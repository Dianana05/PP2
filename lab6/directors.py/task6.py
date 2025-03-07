import string
folder = input("way foulder: ")
for letter in string.ascii_uppercase:
    file_path = folder + '/' + letter + '.txt'
    with open(file_path, 'w') as file:
        file.write("This is file " + letter)
print("files from a to z were created.")
