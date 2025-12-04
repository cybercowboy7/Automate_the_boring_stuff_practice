# Regular string - Will process the \ as an escape character
# print('Hello....\n this is a test...\\')
#
# # Raw string - Will treat the \ as actual characters instead of the escape character
# print(r'Hello...here is a directory to look at C:\User\Home\Documents')

# Multiline strings: Do not need to escape characters in multiline strings
# print('''Dear Alice,
#
# We are interested in your profile's thumbnail and can use your help
#
# Sincerely,
#
# AK''')

# Multiline comments
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def say_hello():
    """This function prints hello.
    It does not return anything."""
    print('Hello!')

# Slicing strings
greeting = "Hello, world!"
greeting_slice = greeting[0:5]
print(greeting_slice)

# Utilizing f-strings:
name = 'Alex'
age = 27
print(f'My name is {name} and I am {age} years old')

# %s and format()

print('My name is %s and I am %s years old' % (name, age))

print('My name is {} and I am {} years old'.format(name, age))