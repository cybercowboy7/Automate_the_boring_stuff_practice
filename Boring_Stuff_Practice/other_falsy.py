name = ''
while not name:     # not name == True since '' == False
    print('Enter your name:')
    name = input('>')
    print(bool(name))       # Can you tell you the bool falsey or truthy value of a variable
print('How many guests will you have?')
num_of_guests = int(input('>'))
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')
