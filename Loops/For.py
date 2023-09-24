'''
Is better to use 'for' loop when
 you know the number of iteration that you're gonna needed
'''


def for_loop_example_one():
    # Iterate over the srtring (strin si an array of chars)
    for char in "Norwegain Blue":
        print(char)


def for_loop_example_two():
    # range to specify the numbers of iterations
    for x in range(2, 8):  # start, and end parameters
        print(x)

    print("\n")
    friends = ('John', 'Terry', 'Eric', 'Michael', 'George')
    for name in friends:
        print(name)

    # neasted loops (ciclos anidados)
    friends2 = ('John', 'Terry', 'Eric')
    numbers = (1, 2, 3)
    for name in friends2:
        for n in numbers:
            print(name, n)


def for_loop_exercise():
    '''
    You're having a party and want to invite your friends
    you want print out invitations for each friend using for loops
    The names are in two lists 'names' and 'names1'
    You also need to add extra named to the list using an 'input box',
    when you run the code printout one invitation to each friend per line
    Names should be properly capitalized

    :return:
    Example out put
    * John Cleese! you are invited to the party on saturday
    * Eric Idle! You are invited to the party on saturday.

    *hint You may need two 'for' loops to solve this exercise

    names = ['john ClEEse','Eric IDLE','michael']
    names1 = ['graHam chapman', 'TERRY', 'terry jones']
    '''

    names = ['john ClEEse', 'Eric IDLE', 'michael']
    names1 = ['graHam chapman', 'TERRY', 'terry jones']

    # combine two list in other one
    party_guests = names + names1
    party_day = "saturday"

    for n in range(2):
        new_guest = input("Write the name for the new guest: ")
        party_guests.append(new_guest)

    for guest in party_guests:
        print(f"{guest.title()}! you are invited to the party on {party_day}")


# for_loop_example_one()
# for_loop_example_two()
for_loop_exercise()
