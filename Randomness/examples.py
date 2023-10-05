import random as r  # to work whit random

def example_one():

    # Generates a random number between 0 and 1 but not 1
    print(f"random: {r.random()}")

    # multiply by 6 to generate a randon number between 0 and 6 but not 6
    print(f"random: {r.random() * 6}")

    # generate a randon number given two numbers
    print(f"uniform: {r.uniform(1,6)}")

    #  returns a randomly selected element from the specified range.
    print(r.randrange(1,100,2))  # Optional. An integer specifying the incrementation. Default 1


#  work whit list
def example_two():
    friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']

    # get random value form list
    print(r.choice(friends_list))

    # get multiple values whit out duplicated values, specifi the number of samples that will be taken
    print(r.sample(friends_list, 2))

    # Shuffle a list (reorganize the order of the list items):
    # Deprecated since Python 3.9. Removed in Python 3.11.
    pass

example_one()
example_two()