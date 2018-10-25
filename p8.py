# http://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html

import sys

user1 = input("enter your name : ")
user2 = input("enter your name as well : ")

user1_select = input("%s, what do you select (rock/paper/scissor) : " % user1)
user2_select = input("%s, what do you select (rock/paper/scissor) : " % user2)

print(user1_select)
print(user2_select)


def show_result(us1, us2):
    print("checking for result...")
    if us1 == us2:
        print("Tie")
    if us1 == "rock":
        if us2 == "scissor":
            print("rock wins")
        else:
            print("paper wins")
    elif us1 == "paper":
        if us2 == "rock":
            print("paper wins")
        else:
            print("scissor wins")
    elif us1 == "scissor":
        if us2 == "paper":
            print("scissor wins")
        else:
            print("rock wins")
    else:
        print("invalid inputs. pls retry")


show_result(user1_select.strip(), user2_select.strip())
