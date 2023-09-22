def concatenate_string():
    sentence = "Hello world from python"

    # print two times the same sentence
    print(sentence + " - " + sentence)


def print_n_times_same_sentence():
    sentence = "Hello world from python"
    n_times_to_print = 2

    print(sentence * n_times_to_print)


def string_operations():
    sentence = "hellO WoRld"

    print(f"Original Sentence: {sentence}")
    print(f"Sentence in Upper Case: {sentence.upper()}")
    print(f"Sentece in Lower case: {sentence.lower()}")
    print(f"Sentence in Capital case: {sentence.capitalize()}")
    print(f"Sentence in Title format: {sentence.title()}")


def string_len_and_count():
    sentence = "Welcome to Python 101: Strings"
    word_to_find = "Python"

    print(f"There are {len(sentence)} characteres in : {sentence}")
    print(f"{word_to_find} appears {sentence.count(word_to_find)} times in sentence")


def slicing_string():
    # Slicing is to get sub strings form another one
    sentence = "Welcome to Python 101: Strings"

    # start position : end position
    # you can use negative index to slice the string
    print(f"First slice was: {sentence[0:6]}")
    print(f"Negative index slicing is: {sentence[-1:-8]}")
    print(sentence.capitalize())


def exercice_one():
    '''
    From String Welcome to python 101:Strings
    , extract text and create/print a new string that says:

    "1 Welcome Ring To Tyler"
    * Every first letter in a world should be capitalized (Title format)

    * print the same string backwards
    '''

    msg = "Welcome to python 101:Strings"

    new_text = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
    print(new_text.title())
    print(f"backward is: {new_text[::-1].title()}")


concatenate_string()
print_n_times_same_sentence()
string_operations()
string_len_and_count()
slicing_string()
exercice_one()