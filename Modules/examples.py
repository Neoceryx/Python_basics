
# import platform as pl

from platform import platform as pv

print(pv())


def zip_example():
    '''
    Python’s zip() function creates
    an iterator that will aggregate elements
    from two or more iterables. You can use
    the resulting iterator to quickly and consistently
    solve common programming problems,
    like creating dictionaries.
    '''

    nums = "1234"
    letters = ["a","b", "c", "d"]
    names = ["john", "Eric", "Michael", "Graham", "Joe"]

    combo = list(zip(nums,letters,names))
    print(combo)

def zip_exercise():
    '''Given the following string create a dictionary'''
    keys = 'this parrot is deceased'
    values = 'denna papegojan är avliden'

    # split the string in a list
    keys = keys.split()
    values = values.split()

    en_sv_dict = dict(zip(keys, values))
    print(en_sv_dict)

    # second way to create the dictionary Nested list
    new_dict = {key:value for key,value in zip(keys,values)}
    print(new_dict)

    # we have two lists, one for keys and other for values
    en, sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
    print(en, sv)


# zip_example()
zip_exercise()

