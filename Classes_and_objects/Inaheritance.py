'''
Whe you have a class (master), and you want to share
the methods and attributes to a children classes
'''

class Person:
    def move(self):
        print("Move 4 spaces")
    def rest(self):
        print("Gains 4 health points")

# inherit from Person
class Doctor(Person):
    '''Since Doctor inherit from person.
        Doctor can use all methods from person
        and of course, they can have its own methods
    '''
    def heal(self):
        print("Heals 10 health points")


class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Move 6 spaces")

# Inherits from Doctor and Fighter
class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns Invisible")

    def heal(self):
        print("Heals 15 health points")

# create an obj from wizard
character = Wizard()
character.heal()