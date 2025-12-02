import sys

while True:
    user_input = input('Tell me about your day, if you would like to exit type "exit": ')
    if user_input.lower() == 'exit':
        sys.exit()
    print("Here is a recap of your day:", user_input, sep=' ')


