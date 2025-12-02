def collatz(number):
    print(number, end=' ')

    if number == 1: # Base case where recursion will stop if it == 1
        return
    elif number % 2 == 0:
        return collatz(number // 2)
    elif number % 2 == 1:
        return collatz(3 * number + 1)

try:
    user_input = int((input('Enter your number: ')))
    collatz(user_input)
except ValueError:
    print('Error: Please input an integer')


