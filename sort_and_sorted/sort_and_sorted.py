my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'
my_set = {1,4,5,7,9,10}

# sorted will return a list ordered
# (you cand pass, a list, tuple, dictionary)

print("My list")
print(my_list,'original')
print(sorted(my_list))
print(my_list, "New")

print("\n My tuple")
print(my_tuple, "Original")
print(sorted(my_tuple))
print(my_tuple, "new")

print("\n my string")
print(my_string, "Original")
print(sorted(my_string))
print(my_string, "new")

print("\n My dictionary")
print(my_dict, "Original")
print(sorted(my_dict))  # Order only the keys
print(my_dict, "new")

print("\n My dictionary")
print(my_dict, "Original")
print(sorted(my_dict.items()))  # Order by the keys
# print(sorted(my_dict.values(), reverse())) # order the values in reverse mode
print(my_dict, "new")




