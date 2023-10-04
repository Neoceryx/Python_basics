''' Dicionaries Comprehension '''

movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']


def example_one():

    # create a nested list, suing movies and year
    print(list(zip(movies, year)))

    # create a dictionary using movies and year
    # old way
    new_dic = dict()
    for m, y in zip(movies, year):
        new_dic[m] = y

    print(new_dic)

    # using comprehension
    new_dic2 = {m: y for m, y in zip(movies, year)}
    print("Movies dictionary created comprehension")
    print(new_dic2)

    # create a new dictionary with all the movies less to 1983
    new_dic3 = {m: y for m, y in zip(movies, year) if y < 1983}
    print("Print all movies less than 1983")
    print(new_dic3)

    # create a dictionary whit all the movies less than 1983 and that only contains 'Monty'
    new_dic4 = {m: y for m,y in zip(movies,year) if y < 1983 and m.startswith('Monty')}
    print("All the movies less 1983 and it starts whit 'Monty'")
    print(new_dic4)
    # end function


def example_two():
    '''Comprehension can also be added to create a list of tuples_and_sets '''
    new_values = [(n, m, y) for n, m, y in zip(names, movies, year)]
    print(new_values)  # the output will be a list of tuples_and_sets

    new_values2 = [[n + "s favorite movie was " + m + " from " + str(y)] for n,m,y in zip(names, movies, year) if y < 1982 ]
    print(new_values2) # the output will be a nested list
    pass


# example_one()
example_two()

