
"""
List can contain multiples values,
numbers, strings, booleans.

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

"""

def example_one():
    friends =['Jhon', 'Michel', 'Terry', 'Eric', 'Graham']

    print(friends)

    # invierte la lista
    #print(friends[::-1])

    # you can also use negative index
    # slice the list to get a sub list
    print(friends[:2])

    print(f"There is: {len(friends)} friend in the list")

    # get the number of times 'Michel' appear in the array
    print(friends.count('Graham'))

    # get the index by value
    print(friends.index("michel"))


def exercise_two_shorting():
    # shorting list
    friends =['Jhon', 'Michel', 'Terry', 'Eric', 'Graham']
    cars = [911,130,328,535,740,308]
    print(f"Original List\n {friends}")

    # shor the list Asc
    friends.sort()
    print(f"Shorted list\n {friends}")

    # invert the list. order in Desc
    friends.sort(reverse=True)
    print(f"inverted list:\n {friends}")

    friends.reverse()
    print(f"Reversed list:\n {friends}")


def exercise_three_adding():
    # A list is a mutable element
    friends = ['Jhon', 'Michel', 'Terry', 'Eric', 'Graham']
    cars = [911, 130, 328, 535, 740, 308]

    # add an elemnt at the end of the list
    friends.append("TerryG")
    print(friends)

    # add an element to the list in the specified position
    friends.insert(1, "Terry2G")
    print(friends)

    # Change the value in a specify position
    friends[1] = "Jorge"
    print(friends)

    # Combine two list in only one
    friends.extend(cars)
    # new_friends = friends + cars
    print(friends)
    # print(new_friends)

def exercise_four_removing():
    # A list is a mutable element
    friends = ['Jhon', 'Michel', 'Terry', 'Eric', 'Graham']
    cars = [911, 130, 328, 535, 740, 308]

    print("Removing elements form list")
    friends.remove("Terry")
    print(friends)

    # remove the last value from the array. you can pass index to be poped
    friends.pop()
    print(friends)

    # clone the list
    new_friends = friends.copy() # or friends[:]
    print(new_friends)

    # empty the list
    # friends.clear()


def exercise():
    '''
    You sell lemonade over two weeks, the lists show number
    of lemonades sold per week
    profit for each lemonades sold is 1.5$
    Add another day to week 2 list by capturing a number as input
    Combine the two lists into the list called 'sales'
    Calculate / print how much you have earned on:
    Best day
    Worst day
    Separately and in total

    sales_w1 = [7,3,42,19,15,35,9]
    sales_w2 = [12,4,26,10,7,28]
    sales = []
    '''
    
    limonade_price = float(1.5)

    sales_w1 = [7, 3, 42, 19, 15, 35, 9]
    sales_w2 = [12, 4, 26, 10, 7, 28]

    new_day = input("Please Add another Day")
    sales_w2.append(int(new_day))

    # combine the two lists
    sales = sales_w1 + sales_w2

    best_day_earnings = max(sales) * limonade_price
    worst_day_earnings = min(sales) * limonade_price
    total_earnings = best_day_earnings + worst_day_earnings

    print(f"Money Earned in best day was: {best_day_earnings}")
    print(f"Earnings in worst day was: {worst_day_earnings}")
    print(f"Total Earnings: {total_earnings}")


# example_one()
# exercise_two_shorting()
# exercise_three_adding()
#exercise_four_removing()
exercise()
