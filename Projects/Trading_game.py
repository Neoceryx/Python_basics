"""
Draw a marble from a bag (assume it's random)
a bag has 10 marbles: 6 green and 4 red
if you draw a green marble you win same amout that you belt
if you draw a red marble you lose amount you bet.

Marbles are repleaced into bag after each round

before each draw decide how much you will bet and enter it

you start the game whit 1000 gold pieces

the number of rounds/draws should be variable

if you lose the hald of money game is over
show out data as you go along
"""

# number of round are variable(random)
# initial gold = 1000
# enter your bet amout
# bag = 6G & 4R

import random as r

bag = ["g", "g", "g", "g", "g", "g", "r", "r", "r", "r"]
money = 1000
rounds = r.randrange(1, 5)

last_marble = ""
score = money

for i in range(rounds):

    bet_amount = int(input("Enter you bet amount: "))
    last_marble = r.choice(bag)

    if last_marble == "g":
        score = score + bet_amount
        print(f"round {i + 1}|{rounds}: marble was: {last_marble}. you win: {bet_amount}: {score}|{bet_amount}")

    else:
        score = score - bet_amount
        print(f"round {i + 1}|{rounds}: marble was: {last_marble}. you lose: {bet_amount}:  {score}|{bet_amount}")

    # validate if you don't lose half money
    if score <= (money / 2):
        print("Game over")
        break
    else:
        print(f"You earnings: {score}")

    pass
    # end foreach



# iterate over n rounds
# get a randon marble

# if canica es verde: ganas apuesta, sino perdes