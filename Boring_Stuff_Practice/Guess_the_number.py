import random

print('I am thinking of a number between 1 and 20')
magic_number = random.randint(1, 20)
count = 1
while True:
    guess = input('Enter your guess here: ')
    guess = int(guess)
    if guess == magic_number:
        print('You guessed it!')
        break
    elif guess < magic_number:
        print('Your guess is too low! Try again...')
    elif guess > magic_number:
        print('Your guess is too high! Try again...')
    count = count + 1

print('It took you', count, 'tries to guess the correct number', sep=' ')

