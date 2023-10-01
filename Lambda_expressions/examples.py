'''Lambda or Anonymus funcitons, single lines funcitons '''
# (Sintax) variable = lamda parameter(s): expression.

def example_one():
    x = 3
    square = lambda num:num*num;
    print(square(x))

def example_two():
    # Sorting using lambda
    monty_python = ['John Marwood Cleese', 'Eric Idle', 'Michael Edward Palin', 'Terrence Vance Gilliam',
                    'Terry Graham Perry Jones', 'Graham Arthur Chapman']

    # sort the list by name
    monty_python.sort(key=lambda name: name.split(" "))

    # sort the list by first_name
    # monty_python.sort(key = lambda name:name.split(" ")[-1])
    print(monty_python)



# Lambdas Part 2
'''
Exmaple: calculate consultancy
'''

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours

walking_cost = price_calc(10,30)
premiun_cost = price_calc(1,25)
print(f"Walking Cost: {walking_cost(2)}") # return 70:  python resolved the multiplications first
print(f"Premium Cost: {premiun_cost(2)}")


# unpacking concept
print((lambda *args: sum(args))(2,3,4,50))


#example_one()
# example_two()




