'''
Allow create, list, tuples, dictionaries
The comprehension, contains the same code as for loop
'''


def exersice_one():


    ''' give me a list with num squared for each num in numbers '''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    new_list = list()

    # # way no 1 to do it
    # for num in numbers:
    #     new_list.append(num * num)  #
    #
    # print(new_list)

    # using comprehension
    new_list = [ num * num for num in numbers]
    print(new_list)

    # give me a list with num for each num in numbers if num is even
    new_list2 = [num for num in numbers if num % 2 == 0]
    print(new_list2)

    # using lambda
    new_list3 = filter(lambda num: num % 2 == 0, numbers)
    print(list(new_list3))

    # I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
    new_list_4 = list()
    for letter in "span":
        for num in range(4):
            new_list_4.append((letter, num))
    print(new_list_4)

    # using Comprehensions
    new_list_5 = [(letter, num)for letter in 'spam' for num in range(4)]
    print(new_list_5)


    # Parse string items to int
    test_list = ['1', '4', '3', '6', '7']
    # using list comprehension to
    # perform conversion
    test_list = [int(i) for i in test_list]
    print(test_list)

    # using map() to
    # perform conversion
    test_list_2 = list(map(int, test_list))
    print(f"Using Map funtion: {test_list_2}")


# exersice_one()
#s = "hello world"
s = "1 w 2 r 3g"

arr = s.split(" ")
arr2 = list()
for c in arr:
    arr2.append(c[0:1].upper() + c[1:])

print(" ".join(arr2))
#print(s.title())



'''
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''

