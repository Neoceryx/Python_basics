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


def dictionary_exercise():
    # It’s...not really an adventure game...#Ver 1.0
    # Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
    # The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
    # one way to buy by typing the key 'newt' in an input box...or something
    # at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
    # ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
    # Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
    # ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
    # Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
    # as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

    # create stores
    freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100,
                   'grim reaper': 500, 'minstrel': -15}
    antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75,
                'german joke': 5}
    pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

    # create an dempty shopping cart
    cart = {}
    # loop through stores/dicts
    for shop in (freelancers, antiques):

        # inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
        buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()

        # update the cart
        cart.update({buy_item: shop.pop(buy_item)})  # use pop...
        buy_items = ", ".join(list(cart.keys()))
    print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')


def dictionary_exercise_two():

    print("ver 1.2 add ability to exit a store without buying and go to next by typing 'exit',"
          " and to exit if a nonexistant item is bought(typed)"
          "Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message "
          "about total cost and how much gold you have left")

    # create stores
    freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100,
                   'grim reaper': 500, 'minstrel': -15}
    antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75,
                'german joke': 5}
    pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

    # create an dempty shopping cart
    cart = {}
    gold = 1000
    # loop through stores/dicts
    for shop in (freelancers, antiques):

        # inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
        buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()

        if buy_item != "exit":
            if shop.get(buy_item) is not None:
                # update the cart
                item_cost = shop.pop(buy_item)
                cart.update({buy_item: item_cost})  # use pop...
                buy_items = ", ".join(list(cart.keys()))
                total_sum = sum(cart.values())

                print(f'You Purchased {buy_items}. your total is {total_sum} gp, you still having:{gold - total_sum} gp to spend Today it is all free. Have a nice day of mayhem!')

            else:
                print("Upps this item is not valid")
                break  # exit if not found a valid item in the store
        else:  # exit if user type 'exit'
            continue




# dictionary_example_one()
# dictionary_example_two()
# dictorionay_example_three()
# dictionary_exercise()
dictionary_exercise_two()