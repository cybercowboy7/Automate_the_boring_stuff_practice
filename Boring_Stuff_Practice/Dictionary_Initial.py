# car_dict = {                    # This creates a dictionary with keys and values
#     'Make': 'Ford',
#     'Model': 'Mustang',
#     'Year': '2019'
# }
#
# print(car_dict['Model'])        # This is how you access the value of a specific key within a dictionary
#
# card_dict2 = {
#     'Model': 'Mustang',
#     'Make': 'Ford',
#     'Year': '2019'
# }

# print(car_dict == card_dict2)       # For dictionaries, they do not have to have the same order to match


# You can iterate through different dictionary items
spam = {'color': 'red', 'age': 42}
for k in spam.keys():
    print(k)
for v in spam.values():
    print(v)
for i in spam.items():          # Key value pair in a dictionary is known as an item
    print(i)

# Can use in and not in operators to check for the presence of keys and values
print('color' in spam.keys())
print('black' in spam.values())


# If you want to get an actual list from one of these methods, pass its list-like return value to the list() function
spam_keys_list = list(spam.keys())
print(*spam_keys_list)