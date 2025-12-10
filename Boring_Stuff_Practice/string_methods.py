# upper() and lower() string methods
# user_input = input('Enter a string: ')
# user_upper = user_input.upper()
# print(user_upper)
#
# user_input2 = input('Enter another string: ')
# user_lower = user_input2.lower()
# print(user_lower)

# isupper() and islower()
name = "alex"
print(name.islower())   # Will print True
print(name.isupper())   # Will print False


# isalpha() Returns True if the string consists only of letters and isn’t blank
# isalnum() Returns True if the string consists only of letters and numbers (alphanumerics) and isn’t blank
# isdecimal() Returns True if the string consists only of numeric characters and isn’t blank
# isspace() Returns True if the string consists only of spaces, tabs, and newlines and isn’t blank
# istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
# The startswith() and endswith() methods return True if the string value on which they’re called begins or ends (respectively) with the string passed to the method
# The join() method is useful when you have a list of strings that need to be joined together into a single string value
# The split() method works the opposite way: we call it on a string value, and it returns a list of strings
# The rjust() and ljust() string methods return a padded version of the string on which they’re called, with spaces inserted to justify the text. The first argument to both methods is an integer length for the justified string
# The center() string method works like ljust() and rjust() but centers the text, rather than justifying it to the left or right
# The strip() string method will return a new string without any whitespace characters at the beginning or end
# while the lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively



hello = "Hello"
print(hello.center(20, '='))


