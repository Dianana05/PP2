#set 
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#access set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#add set items
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#remove set items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

