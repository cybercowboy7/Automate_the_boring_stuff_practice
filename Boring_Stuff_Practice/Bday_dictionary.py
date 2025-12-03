

birthday_dict = {'Alice': 'April 1st', 'Alex': 'Nov. 20th'}
while True:
    print("Enter a name: (blank to quit")
    name = input()
    if name == '':
        break
    if name in birthday_dict:
        print(birthday_dict[name] + ' is the birthday of ' + name)
    else:
        print('I do not have information for the name ' + name)
        print('What is their birthday?')
        bday = input()
        birthday_dict[name] = bday
        print('The databse has been updated')
