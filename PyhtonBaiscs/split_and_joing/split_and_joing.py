def examples():
    msg = 'Welcome to Python 101: Split and Join'
    csv = 'Eric,John,Michael,Terry,Graham'
    friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']
    print('Welcome to Python 101: Split and Join')

    # break the string char by char
    print(list(msg))

    # break the sentence by character. default by empty space
    print(msg.split())
    # break the list by 'comma'
    print(csv.split(","))

    # Joning String, jing the list, using "-"
    print("-".join(friends_list))

    # replace value in the string by other
    print(msg.replace(" ", ""))


def exercise_one():
    print("\n ---------- Exercise One  ---------")
    csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
    friends_list = ['Exercise: fill me with names']
    # From the list above fill a list(friends_list) properly
    # with the names of all the friends. One per "slot"
    # you may need to run same command several times
    # use print() statements to work your way through the exercise

    friends_list.clear()
    names = ",".join(csv.split(":"))
    names = ",".join(names.split(";"))
    names = names.split(",")
    print(names)

    friends_list = list(names)

    # for name in names:
    #     friends_list.append(name)

    print(friends_list)

    # Second solution
    names2 = csv.replace(":",',').replace(";", ",").split(",")
    print(f"Replace: {names2}")

examples()
exercise_one()