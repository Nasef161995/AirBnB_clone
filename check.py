#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name


person = Person("mohamed")

# Set the 'name' attribute of the person object using setattr()
setattr(person, 'name', 'mona')

# Access the 'name' attribute
print(person.name)  # Output: John Doe
