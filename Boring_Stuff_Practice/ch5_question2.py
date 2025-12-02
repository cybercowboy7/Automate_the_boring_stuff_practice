eggs = input("Enter a string: ")
eggs_final = eggs.lower()
bacon = input("Enter another string: ")
bacon_final = bacon.lower()

assert eggs_final != bacon_final

print("Eggs != Bacon, here are your inputs\n", "input 1:",eggs,"\n","input 2:",bacon,"\n")
