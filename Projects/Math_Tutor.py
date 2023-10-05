import random as r

'''
Create application to practice multiplications tables
- user specifies number of random practices questions
- user is presented with a promp e.g 5X5 = and inputs the anwser for each questions
- when all questions are answered: printout following info
    a Some form of 'thanks for playing greetings'
    b Number of correct answered/total answers
    c % correct

'''


def count_answers(answers ,no_exercises):

    god_answered = answers.count(True)
    correct_percentage = (god_answered / no_exercises) * 100
    print("\n")
    print("thanks for playing greetings")
    print(f"Number of correct answered: {god_answered} / total answers: {no_exercises}")
    print(f"{round(correct_percentage, 2)} % correct ")


def generate_questions(num_exercices):

    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    user_answers = list()

    for i in range(1, num_exercices + 1):
        n1, n2 = r.sample(numbers, 2)  # get two randon number
        answer = int(input(f"Solve next exersice {n1} x {n2} = ??"))

        result = n1 * n2
        if answer == result:
            user_answers.append(True)
        else:
            user_answers.append(False)
    else:
        count_answers(user_answers, num_exercices)

    pass
    # end function


print("Application to practice multiplicaiton tables")
no_times = int(input("How many questions do you want to try solve?"))
generate_questions(no_times)
