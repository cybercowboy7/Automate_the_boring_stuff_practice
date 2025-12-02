# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam,
# and prints Greetings! if anything else is stored in spam.

spam = input("What do you want spam to equal? ")

spam_int = int(spam)

if spam_int == 1:
    print("Hello")
elif spam_int == 2:
    print("Howdy")
else:
    print("Greetings!")

