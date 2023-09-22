def multiline_message():
    msg = """ Este
      es 
      un
      mesnaje
      super
      largo"""

    print(msg)


def find_and_replace():
    msg = "Welcome to python 101: Strings"

    # get the position where parameter is located
    locate = msg.find('h')
    print(locate)

    new_string = msg.replace("python", "Java")

    print(f"original Sentence: {msg}")
    print(f"Repalce sentence is: {new_string}")


def check_is_exist():
    msg = "Welcome to python 101: Strings"

    # validate if 'python' exists in the sentence
    is_in_string = "python" in msg
    print(f"python :{is_in_string}")

    # validate '101' exist in the sentence in negative form
    is_in_string = "101" not in msg  # 101 does not appear in msg? = False. it is appear
    print(f"101: {is_in_string}")


def format_string():
    msg = "Welcome to python 101: Strings"

    name = "terry"
    color = "rED"

    # Basic concatenation
    msg1 = '[' + name + '] loves the color ' + color + '!'

    # Interpolation
    msg2 = f"[{name.capitalize()}] loves the color {color.capitalize()} !"

    print(msg1)
    print(msg2)


multiline_message()
find_and_replace()
check_is_exist()
format_string()
