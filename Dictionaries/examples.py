def dictionary_example_one():
    movie = {
        'title': 'Life of Brian',
        'year': 1979,
        'cast': ['john', 'Eric', 'Michael', 'George', 'Terry']
    }

    # getting the values, is by keyname
    print(movie['title'])
    print(movie.get('budget'))  # you will get 'none' if the key does not exist.
    # print(movie.get('budget', 'this does not exit')) # custom error message can be added

    # change the value of one key
    movie['title'] = "The holy Grail"

    movie.update({'title': 'The Holy Grail', 'year': 1975, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']})
    movie['budget'] = 250000  # we add a new key names budget
    print(movie)

    # # removing value form dictionary
    # del movie['year']
    # print(movie)

    # The pop() method removes the specified item from the dictionary.
    year = movie.pop('year')  # removes 'year' key and retrive and storage value in the variable
    print(year)
    print(movie)


def dictionary_example_two():
    movie = {
        'title': 'Life of Brian',
        'year': 1979,
        'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
    }

    # getting the keys
    print(movie.keys()) # get an list fo keys

    # getting the values
    print(movie.values()) # get a list of values

    # getting the items
    print(movie.items()) # get a list of tuples of key and value

    print("\n Iterating over Dictionary")
    # iterating over the dictionary
    for key, value in movie.items():
        print(key, value)

def dictorionay_example_three():
    python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
    holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
    life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}

    # A dictionary can contain multiple times the same key, but different values o same

    # meber test
    print("Arthur" in holy_grail)
    if "Arthur" not in holy_grail:
        print('He\'s not here')  # we add '\' to display the aphostrofy

    # Combine a dictionary
    people = {}
    people1 = {}
    people2 = {}

    # combine dictionaries in a new one
    people.update(python)
    people.update(holy_grail)
    people.update(life_of_brian)
    print(sorted(people.items()))

    print("\nMethod 2 join dictionaries by compresion")
    # method 2 Compresion
    for groups in (python,holy_grail,life_of_brian):
        people1.update(groups)
    print(sorted(people1.items()))

    print("\nMethod 3 unpacking 3.5 latter")
    people2 = {**python, **holy_grail, **life_of_brian}
    print(sorted(people2.items()))

    # We need to pay attention at the data type, sinde we have an string, the sum method, will display and error
    print("\nThe Sum if the ages is: ", sum(people2.values()))

# dictionary_example_one()
# dictionary_example_two()
dictorionay_example_three()