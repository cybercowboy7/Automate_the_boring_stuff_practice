class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return (f'Name: {self.name}\n'
               f'Age: {self.age}\n'
               f'Gender: {self.gender}')
        return profile

alex = Human("Alex", 26, "Male")

prof_create = Human(input("Name: "), int(input("Age: ")), input("Gender: "))
print()
print("Here is Alex's profile:\n",alex, "\n", sep="")

print("Here is your profile:\n",prof_create, sep="")

helping = help(Human)

print(helping)


