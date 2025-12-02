import random

def get_answer(answer_choice):
    if answer_choice == 1:
        return "It is so"
    elif answer_choice == 2:
        return "It is not in the cards"
    elif answer_choice == 3:
        return "Nope"
    elif answer_choice == 4:
        return "The answer is hazy"
    elif answer_choice == 5:
        return "Try again"
    return None


input("Ask a yes or no question: ")
print(get_answer(random.randint(1,5)))
