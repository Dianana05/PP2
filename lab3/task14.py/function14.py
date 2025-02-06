from functions import gramtounce, solve, filter_prime, is_palindrome, histogram, guess_number_game

gr = float(input("Введите количество граммов для конвертации в унции: "))
print("Это равно", gramtounce(gr), "унций.")

heads = int(input("Введите количество голов: "))
legs = int(input("Введите количество ног: "))
result = solve(heads, legs)
print("Цыплята:", result[0], "Кролики:", result[1])

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
print("Простые числа в списке:", filter_prime(numbers))

word = input("Введите слово или фразу для проверки на палиндром: ")
if is_palindrome(word):
    print("Это палиндром!")
else:
    print("Это не палиндром.")

histogram([4, 9, 7])

guess_number_game()
