#1
import math
a=[5,6,87,12,9,12,3]
b=math.prod(a)
print('result:', b)

#2
a=input('a:')
upper=0
lower=0
for char in a:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
print('lower:', lower)
print('upper:', upper)

#3
a=input('text:')
a = a.replace(" ", "").lower()
if a==a[::-1]:
    print('palindrom')
else:
    print('not palindrom')

#4
import math
import time
a=int(input("a="))
b=int(input("b="))
time.sleep(b/1000)
root=math.sqrt(a)
print(f"square of {a} after {b} miliseconds is {root} ")

#5
a=("hello", 1, 0)
b=all(a)
print("All elements are true?",b)

