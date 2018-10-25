# http://www.practicepython.org/solution/2014/03/26/07-list-comprehensions-solutions.html

import random

def print_even_list():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    evenlist = [number for number in a if number %2 ==0 ]
    print(evenlist)


def print_random_list():
    numlist = []
    random_list_len = random.randint(5,15)

    while len(numlist) <= random_list_len:
        numlist.append(random.randint(1, 100))

    evenlist = [number for number in numlist if number % 2 == 0]
    
    print(numlist)
    print (evenlist)


print_random_list()