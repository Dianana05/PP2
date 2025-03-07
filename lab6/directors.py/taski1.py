import os
path = input("way to direc: ")
if not os.path.exists(path):
    print("unreal.")
else:
    file_count = 0
    folder_count = 0
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            file_count += 1
        elif os.path.isdir(full_path):
            folder_count += 1
    print("count files:", file_count)
    print("count foulders:", folder_count)
