def hello():
    # Prints three greetings
    print("Good Morning!")
    print("Good Afternoon!")
    print("Good Evening!")

# print("Calling the hello() function. Standby...")

def say_hello():    # Example without argument
    name = input('What is your name? ')
    print('Hello,', name, sep=' ')

def hello_argument(name):
    print('Hello,', name, sep=' ')

hello_argument('Alex')  # Alex is the argument being passed to the name parameter