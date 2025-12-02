# hello = 'Hello'
#
# for i in range(8):
#     print('i is equal to ', str(i), 'on this iteration', sep=' ')
#

# total = 0
# for num in range(100):
#     total = total + num
# print(total)

# print('Hello!')
# i = 0
# while i < 10:       # Range is 0 - 9 and does not include 10. This is known as closed, open range
#     print('i is equal to ', i, sep=' ')
#     i += 1
# print('Goodbye!')

# print('This is a display of how 3 range() arguments work')
# for num in range(0, 24, 2):     # syntax for range() arguments is range(start, stop, interval)
#     print(num)
# print('Display complete!')

print('This is a display of how 3 range() negative arguments work')
for num in range(10, -1, -1):     # syntax for range() arguments is range(start, stop, interval)
    print(num)
print('Display complete!')
