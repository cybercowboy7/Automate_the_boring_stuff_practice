
while True:
    name = input('Enter your name: ')
    if name != 'Joe':
        continue
    print('Hello Joe, what is your password? ')
    password = input('Enter your password: ')
    if password == 'Lemon':
        break
print('Access Granted')
