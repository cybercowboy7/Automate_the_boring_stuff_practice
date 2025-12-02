import random

messages = ['It is so', 'The message is hazy',
            'It is not in the cards', 'Try and ask again',
            'I am not sure what you mean']
print('Ask a yes or no question:')
input('> ')
print(messages[random.randint(0, len(messages) -1)])
