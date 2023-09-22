def example_one():
    is_raining_today = True
    is_cold = False

    print("Good morning")
    if is_raining_today or is_cold:  # print if one is true
        print("Bring Umbrella")
    else:
        print("Umbrella is Optional")


def example_two():
    is_raining_today = True
    is_cold = True
    print("Good morning")

    if is_raining_today and is_cold:  # print only if both are true
        print("Bring Umbrella")
    else:
        print("Umbrella is Optional")


def example_tree():
    is_raining_today = True
    is_cold = False

    print("Good morning")
    if is_raining_today and is_cold:
        print("Bring Umbrella and jacket")
    elif is_raining_today and not is_cold:  # this is similar to else and if # similar to ! = Niega la variable
        print("Bring Umbrella")
    else:
        print("Umbrella is Optional")


# example_one()
# example_two()
example_tree()
