import time


def wile_loop_example_one():
    i = 0
    while i < 5:
        i += 1  # increment the counter
        print(f"{i}. {'*' * i} Loops are awesome *")


def while_loop_exercise():
    '''
        Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
        Give user input box: 1. To capture guesses,
        print(and input boxes) 1. If user wins 2. If user loses
        Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

        Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
        Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
    '''

    no_attempts = 0
    attempts_allowed = 3
    number_to_gues = 50

    if number_to_gues >= 50:
        attempts_allowed = 10
        print(f"Number to guest is high, you have {attempts_allowed} attempts")
    else:
        print(f"Number to guest is low, you have {attempts_allowed} attempts")

    while no_attempts < attempts_allowed:

        number_typed = int(input("Try to guess the Number {X}: "))

        if number_typed != number_to_gues:
            no_attempts += 1

            if no_attempts >= attempts_allowed:
                print("Ouuu so bad. Game omer! x.x")
            else:
                print(f"Ops,wrong number, you have {attempts_allowed - no_attempts} chanses")
        else:
            print(f"You win. the number is: {number_to_gues}")
            break

wile_loop_example_one()

while_loop_exercise()