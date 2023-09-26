def reading_files():
    my_file = open('greeting.txt', 'r')  # w, a

    print(my_file.read(10))
    print(my_file.readline())
    print(my_file.readline())

    my_file.close() # always close the file when you finish to read it

def split_line_by_line():
    my_file = open('greeting.txt', 'r')  # w, a

    # line_by_line = my_file.readlines()
    line_by_line1 = my_file.read().splitlines()
    # print('readlines: ', line_by_line)
    print('splitlines: ', line_by_line1)

    my_file.close()


def read_file_content_manager():
    # using this method, automatically 'close' line
    with open("friends.csv", 'r') as f:
        # print(f.read())
        friends = f.read().splitlines()
        print(friends)  # this will be a list
        for friend in friends:
            friend = friend.split(",")
            name = friend[0]
            year = int(friend[1].strip())  # strip() removed possibles extra spaces
            print(f"In 2030 {name} will be {2030-year} Years Old!")


def read_csv_file():

    with open("movies.txt", "r") as f:
        for line in f.read().splitlines():
            print(line)



# reading_files()
# split_line_by_line()
# read_file_content_manager()
# read_file_content_manager()
read_csv_file()