#1
def task(n):
    for i in range(n+1):
        yield i**2
n=int(input("n="))
for diana in task(n):
    print(diana, end=" ")

#2
def task2(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input("n="))
print(", ".join(str(diana) for diana in task2(n)))

#3
def task3(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input("n="))
for diana in task3(n):
    print(diana, end=" ")

#4
def task4(a, b):
    for i in range(a, b+1):
        yield i**2
a=int(input("a="))
b=int(input("b="))
for diana in task4(a, b):
    print(diana, end=" ")

#5
def task5(n):
    for i in range(n, -1, -1):
        yield i
n=int(input("n="))
for diana in task5(n):
    print(diana, end=" ")