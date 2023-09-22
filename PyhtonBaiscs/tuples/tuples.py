# Tuples - faster Lists you can't change, are collection which can storage duplicated values
def tuples_example():
    print(( "-" * 18 ) + " Tuples Examples " + ( "-" * 18 ))

    my_tuple = (3,2,4,0,8)
    print(my_tuple)

    # split the tuple
    print(my_tuple[1:3])


def set_example():
    print(("-" * 18) + " Sets Examples " + ("-" * 18))
    # Sets - blazingly fast unordered Lists, does not allow duplicated

    friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
    my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
    # We can do the same that list. but sets are more fasters than lists

    print(friends_set)

    # Operations whit Sets
    print("Values in common")
    print(friends_set.intersection(my_friends_set))

    print("Values which are not in both sets")
    print(friends_set.difference(my_friends_set))

    print("Join both sets")
    print(friends_set.union(my_friends_set))


def best_practice_to_create_list_tuples_and_sets():
    empty_list = []
    empty_list = list()

    empty_tuple = []
    empty_tuple = tuple()

    empty_set = {}  # this is wrong, this is a dictionary
    empty_set = set()

def sets_exercise():
    # 1. Check if ‘Eric’ and ‘John’ exist in friends
    # 2. combine or add the two sets
    # 3. Find names that are in both sets
    # 4. find names that are only in friends
    # 5. Show only the names who only appear in one of the lists
    # 6. Create a new cars-list without duplicates

    friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
    my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
    cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']

    print(("-" * 18) + " Sets Exercise " + ("-" * 18))

    is_in_set = ("Eric" in friends) and ("John" in friends)
    print(is_in_set)

    combined_sets = friends.union(my_friends)
    print(f"Combined sets: {combined_sets}")

    print("Names that are in both sets are:")
    print(friends.intersection(my_friends))

    print("Names that are only in friends are")
    print(friends.difference(my_friends))

    print("Show only the names who only appear in one of the lists")
    print(my_friends.symmetric_difference(friends))

    new_cars = set(cars)
    print(f"New car list whit out duplicates: {list(new_cars)}")



tuples_example()
set_example()
sets_exercise()