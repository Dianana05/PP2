import os
file_path = input("file you want to delete: ")
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted")
    else:
        print("cannot to delete")
else:
    print("doesn't exist.")
