'''
Classes: are blueprints
Objects: are the actual things you built
variables => attributes
functions => methods
'''


class Movie:

    # Class constructor
    def __init__(self, title, year, imdb_score, have_seen):
        # attributes
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    # methods
    def nice_print(self): # Self if similar to 'This' in C# it's used to refer at the same class
        print("Title:", self.title)
        print("Year: ", self.year)
        print("IMDB Score", self.imdb_score)
        print("Have I seen it?: ", self.have_seen)
        pass


# objects
film1 = Movie("Life of Brian", 1979,8.1,True)
film2 = Movie("The Holy Grail",1975,8.2,True)

# print attributes values
print(film1.title, film1.imdb_score)

# Calling a method
film1.nice_print()
print("\n")
Movie.nice_print(film1)

print("\n")
# Array of Objects
films = [film1, film2]
print(films[0].title, films[1].title)