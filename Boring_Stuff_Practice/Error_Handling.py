def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid Argument')

print(spam(2))
print(spam(7))
print(spam(0))