# Tuples are immutable like strings

tuple_test = (1, 2, 3)
print(tuple_test)           # Prints the whole tuple
print(tuple_test[0])        # Prints 1
# tuple_test[0] = 100         # Causes an eror since tuples are immutable
# print(tuple_test[0])

# Tuples with one value need a trailing comma
tuple_test2 = (1)               # This is an integer not a tuple
print(type(tuple_test2))
tuple_test3 = (1,)              # This is a tuple due to the trailing comma
print(type(tuple_test3))

# List() and tuple() conversions

names_list = ['John', 'Sally']
tuple_names = ('John', 'Sally')
print(tuple(names_list))        # Converts the names_list list into a tuple
print(list(tuple_names))        # Converts the tuple_names tuple into a list