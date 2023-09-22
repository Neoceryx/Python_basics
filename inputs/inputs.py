def input_example_one():
    name = input("What's your name?:")
    age = input("What's your age?:")

    print(f"Hello {name.upper()} your are {age.upper()} years old")


def input_example_two():
    num1 = input("Enter a number: ")
    num2 = input("Enter a second number: ")

    result = float(num1) + float(num2)
    print(f"The addition are {result}")

def input_exercise():
    '''Distance converter Kilometers to Miles

    * Take two inputs from user:
    their first name and distance in KM

    * print greet user by name and show KM and vile values

    1 mile = 1.609 KM
    '''

    user_name = input("What' s your name?: ")
    distance_km = input("Type your distance in KM: ")

    distance_to_miles = float(distance_km) / 1.609

    # round float number in just Two decimals
    print(f"Hello {user_name.title()} your distance in {distance_km} KM , in miles is: {round(distance_to_miles, 2)}")

#input_example_one()
#input_example_two()
input_exercise()