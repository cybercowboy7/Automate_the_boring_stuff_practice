# Basic list behavior and methods being used on lists in python
from library.mediafiles.images_to_pdf import convert_to_image_pdf

number = [1, 2, 3, 4, 6, 5, 34, 45, 4, 7, 8, 9, 8, 3, 76, 8, 8, 8, 8]
count = 0
for i in number:    # Iterates through the list and counts how many indexes are in its
    count += 1
print(number.count(8))      # Counts the number of times the number 8 appears in this list
print(count)

# Alternative to the above method of counting indexes in a list
print(len(number))

Layered_list = [['Alex', 'Bob'],[27, 35]]       # Lists can contain other lists as indexes

# Here is how you would access a list as an index of another list

print(Layered_list[0][1])      # This will print 'Bob'
print(Layered_list[0][-1])      # Can use a negative index to access things at the end of your list, in this case Bob
                                    # since -1 accesses last index in list

# Example of slicing a list
print(number[0:4])  # 0 is the starting index, and it will display 0-3 and leave out 4. In this case 6 is the 4th index
print(number[1:])   # This indicates that index 1 is the starting point and prints the rest of the list past 1
print(number[:2])   # This indicates it will go up to, but not include the 2 index
print(number[:])    # This prints out the whole list

# You can perform operations on lists as well

combination_list = number + Layered_list
print(combination_list)
print(combination_list[19][0])

Layered_list = Layered_list * 3     # adds ['Alex', 'Bob'], [27, 35] two more times to the list
print(Layered_list)

# Deleting indexes from a list

del Layered_list[4:6]       # Deletes indexes 4 and 5
print(Layered_list)

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])     # Will print true since howdy is in the list
print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])  #Will print false since howdy is in the list

# Multiple Assignment trick (Tuple unpacking)
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat  # This line is the same as doing size = cat[0], color = cat[1] etc.
print(cat[0])
print(size)

# Utilizing enumerate() to enumerate a list

colors = ['Red', 'Blue', 'Grey', 'Green', 'Blue']
for index, item in enumerate(colors):
    print('Index is', index, 'and item is', item)



