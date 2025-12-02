spam = ['apples', 'bananas', 'tofu', 'cats']

def string_return(list_input):
    input_type = type(list_input) is list
    if input_type == True:
        final_output = str(list_input)
        print(final_output)

string_return(spam)


