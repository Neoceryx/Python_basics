def variables_basics():
    var1 = 5
    var2 = 10.0
    var3 = 4j

    # to display the data type storaged in the variable
    print(type(var1))
    print(type(var2))
    print(type(var3))

    var4 = "Hello world"
    print(type(var4))

    # list
    mylist = [1, 2, 3, 'hello', 5.0]

    # overrite the value in the 4 postion. to 5.0 to hello
    mylist[4] = "world"

    # iterate over the list
    for val in mylist:
        print(val)
