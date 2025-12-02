# ASSERTIONS ARE FOR PROGRAMMER ERRORS, NOT USER ERRORS.
# USERS SHOULD ONLY SEE USER ERRORS RAISED FROM EXCEPTIONS AND TRY AND EXCEPT STATEMENTS

ages = [24, 25, 23, 19, 36, 32]
def numerical_order(list_input):
    list_input.sort()
    assert list_input[0] <= list_input[-1]      # Checks to ensure the .sort function actually works before printing output
    # for age in list_input:
    #     print(age, end=' ')
    print(*list_input)      # Easier than utilizing a for loop to print indexes within the list
                            # For loops are better if you need to apply logic per-item

numerical_order(ages)