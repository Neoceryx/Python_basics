''' Functions Examples
split your code block and is easy to re-use

always declare the function before tu use it
'''


def greeting_function():
    print("Hello world")


# parameters = kind of variable which will be used in the funciton
# age = 28 as default value
def greeting(name, age=28):
    # 'f' is for format
    print(f"Hello {name}  , you're {age}")


'''
greeting_function()
greeting("Brian", )
greeting("Brian", 32)

user_name = input("Please enter you'r name")
greeting(user_name, 32)
'''


def greeting2(name, age=28, color="Red"):
    print(f'Hello {name.capitalize()}, you are {age}!')
    print(f"And you will be {int(age) + 1} years old next birthday")
    print(f"We hear you like the color {color.lower()}")


def function_exercise():
    '''
    1. Add new print statement - on a new line
        which says 'We hear you like the color xxx! xxx is a string with color
    2. extend the function with another  input parameter 'color', that defaults to 'red'
    3. Capture the color via an input box as variable:color
    4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
      adding 1 to the age
    5. Capitalize first letter of the 'name', and rest are small caps
    6. Favorite color should be in lowercase
    '''

    name = input('Enter your name: ')
    age = input('Enter your age: ')
    color = input("Enter your favorite color: ")
    greeting2(name, int(age), color)


# It is a Best Practice
def named_notation():
    # Named notations helps to make your code more readable
    greeting2("daniel", 78, "hotpink")

    ''' example: Is not necesary to pass your parameters in the same 
    order as you added in the function, only add the correct parameter name
    and python will know whats is each value '''
    greeting2(age=78, name="Daniel", color="hotpink")


function_exercise()
