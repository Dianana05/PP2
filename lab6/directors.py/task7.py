source_file = "c:/Users/user/Desktop/PP2/lab6/source.txt"
destination_file = "c:/Users/user/Desktop/PP2/lab6/destination.txt"
with open(source_file, "r") as src:
    content = src.read()
with open(destination_file, "w") as dst:
    dst.write(content)
print(f"copy the contents of a {source_file} to {destination_file}.")