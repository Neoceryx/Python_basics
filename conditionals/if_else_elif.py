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
    is_raining = False
    is_cold = False

    print("Good morning")
    if is_raining and is_cold:
        print("Bring Umbrella and jacket")
    elif is_raining and not is_cold:  # this is similar to else and if # similar to ! = Niega la variable
        print("Bring Umbrella")
    elif not is_raining and is_cold:
        print("Bring Jacket")
    else:
        print("Shirt is Fine")


def exercise_one():
    ''' you're doing a credit card purchase
    all purchases under 50 $ does not need a pin code to be approve
    '''
    
    amount = 51
    amount_free_to_pin = 50
    if amount <= amount_free_to_pin:
        print(f"Purchase of {amount} does not require nip")
    else:
        print("Please enter you pin!")


# example_one()
# example_two()
# example_tree()
exercise_one()
