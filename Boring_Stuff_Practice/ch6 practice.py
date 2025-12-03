test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_to_string(items):
    # Handle empty list
    if not items:
        return ''

    # Handle one-item list
    if len(items) == 1:
        return str(items[0])

    # Handle multiple items
    return ', '.join(str(x) for x in items[:-1]) + ', and ' + str(items[-1])

print(list_to_string(test_list))