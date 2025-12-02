
cat_names = []
while True:
    print('Enter the name of cat ', str(len(cat_names) + 1), '(Or nothing to stop): ')
    name = input()
    cat_names = cat_names + [name]
    if name == '':
        break
print('The name of your cats are: ')
for name in cat_names:
    print(name)