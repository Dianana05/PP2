import os
path = input("way to file: ")
if os.path.exists(path):
    print("exist")
    if os.access(path, os.R_OK):
        print("can read.")
    else:
        print("cannot read.")
    if os.access(path, os.W_OK):
        print("can write")
    else:
        print("cannot write")
    if os.access(path, os.X_OK):
        print("can execute")
    else:
        print("cannot execute.")
else:
    print("doesn't exist.")
