#2 task
import math
def temp(f):
    c=(5/9)*(f-32)
    return c
f=int(input())
celci=temp(f)
print("celci",celci)

#task 1
def gramtounce(gr):
    ounce=28.3495231*gr
    return ounce
gr=int(input("gram="))
result=gramtounce(gr)
print(result)

#task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "no answer"
heads=int(input("heads="))
legs=int(input("legs="))
print(solve(heads, legs))

#task 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num):
            result.append(num)
    return result

numbers=[]
n=int(input("n="))
for i in range(n):
    num=int(input())
    numbers.append(num) 
print(filter_prime(numbers))

#task 5
from itertools import permutations

def print_permutations(s):
    perms = permutations(s)  
    for p in perms:
        print("".join(p)) 

s = input("s:")
print_permutations(s)

#task 6
def reverse_sentence(sentence):
    words = sentence.split() 
    reversed_words = words[::-1] 
    return " ".join(reversed_words)  

sentence = input("sentence:")
print(reverse_sentence(sentence))

#task 7
def has_33(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True
    return False 

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))  

#task 8
def spy_game(nums):
    sequence = [0, 0, 7]
    i = 0 
    for num in nums:
        if num == sequence[i]:
            i += 1  
        if i == len(sequence): 
            return True
    return False
a=input("input;")
nums=list(map(int, a.split()))
print(spy_game((nums)))


#task 9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input("radius: "))
print(sphere_volume(radius))

#task 10
def unique_elements(lst):
    unique_lst = [] 
    for item in lst:
        if item not in unique_lst: 
            unique_lst.append(item)  
    return unique_lst


a= input(":")
lst = list(map(int, a.split()))  

print( unique_elements(lst))

#task 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

word = input("word:")

if is_palindrome(word):
    print("palindrom")
else:
    print("not palindrom.")

#task 12
def histogram(lst):
    for num in lst:
        print('*' * num) 
user_input = input("input: ")
lst = list(map(int, user_input.split()))

histogram(lst)

#task 13
import random

def guess_number_game():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    attempts = 0 
    while True:
        print("Take a guess.")
        guess = int(input()) 
        attempts += 1  
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job, " + name + "! You guessed my number in " + str(attempts) + " guesses!")
            break 
guess_number_game()

#task 14

