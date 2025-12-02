# import time, sys
#
# try:
#     while True:  # The main program loop
#         # Draw lines with increasing length:
#         for i in range(1, 9):
#             print('-' * (i * i))
#             time.sleep(0.1)
#
#         # Draw lines with decreasing length:
#         for i in range(7, 1, -1):
#             print('-' * (i * i))
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     sys.exit()

import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())