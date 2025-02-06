import random
import math

def gramtounce(gr):
    ounce = 28.3495231 * gr
    return ounce

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "no answer"

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

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

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
