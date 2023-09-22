from variables.basics import variables_basics
from type_casting.data_type_casting import casting_examples

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("--------- Variables Basics ---------")
    variables_basics()
    print("--------- Variables Basics ---------\n")

    print("--------- Casting Basics ---------")
    casting_examples()
    print("--------- Casting Basics ---------\n")


    # Operators
    val = 15; val2 =2
    print(f"division is: {val / val2}")

    # floor divtion. round the resoult to the most near value
    # example 15 / 2 = 7.5      =>  15//2 = 7
    print(f"floor division is: {val // val2}")

