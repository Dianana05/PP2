import os
path = input("way: ")
if os.path.exists(path):
    print("its exist.")
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    print("directory:", directory)
    print("fle:", filename)
else:
    print("doesn't exist.")
