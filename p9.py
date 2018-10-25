# http://www.practicepython.org/solution/2014/04/10/09-guessing-game-one-solutions.html

import random

random_num = random.randint(1,9)
answer_found = False

while not answer_found:
    user_num = input("enter the number : ")
    try:
        user_num = int(user_num)
    except ValueError:
        print("enter any integer. Text input is not allowed")
        continue

    if user_num == random_num:
        print("You got it")
        answer_found = True
    elif user_num > random_num:
        print("Too high")
    else:
        print("Too low")
