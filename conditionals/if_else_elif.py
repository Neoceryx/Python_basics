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


def exercise_two():
    # Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
    # Hint: use 3 separate inputs
    # Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
    # formula is: temp in C*9/5 + 32 = temp in f

    operation_type = input("Choose your operation (+,-,*,/ or 'f' for fahrenheit)")
    number1 = float(input("Enter the first number:"))

    if operation_type.lower() == "f":
        fahrenheit = (number1 * 9 / 5) + 32
        print(f"Conversion from Celsius: {number1} to fahrenheit is: {fahrenheit}")
    else:
        number2 = float(input("Enter the second number:"))

        result = 0  # initialize the variable
        if operation_type == "+":
            result = number1 + number2
        elif operation_type == "-":
            result = number1 - number2
        elif operation_type == "*":
            result = number1 * number2
        elif operation_type == "/":
            result = number1 / number2
        else:
            print("Ups. Something wrong happend")

        print(f"The operation was: {number1} {operation_type} {number2} = {result}")


# example_one()
# example_two()
# example_tree()
# exercise_one()
exercise_two()
