'''

# try:
    # Code you want to run
# except:
    #executed if error occurs
# else:
    #executed if no error
# finally:
    #always executed
'''


def example_one():
    try:
        num = int(input("Enter a number between 1 and 30:"))
        num1 = 30 / num

        if num > 30:
            raise ValueError(
                num)  # The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
    except ValueError as err:
        print(err, num, "Bad value not between 1 and 30")
    except ZeroDivisionError as err:
        print(err, "You can't divide by Zero!!!")
    except:
        print("Invalid Input")
    else:
        print(f"30 divided by {num} is  {num1}")
    finally:
        print("**Thank you for playing")


example_one()
