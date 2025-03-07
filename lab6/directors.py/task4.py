import os
fille=r'c:/Users/user/Desktop/PP2/lab6/directors.py/task3.py'
count=0
with open(fille, 'r') as file:
    for line in file:
        count+=1
print("numbers lines:", count)
