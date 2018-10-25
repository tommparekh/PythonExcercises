# http://www.practicepython.org/solution/2014/03/05/04-divisors-solutions.html


def div():
    __author__ = 'Mihir Parekh'

    num = int(input("enter the numbrer : "))

    lst = list(range(1,num+1))

    divisorList = []

    for number in lst:
        if num % number == 0:
            divisorList.append(number)

    print(divisorList)


num = int(input("enter the number : "))
x = range(2,11)

for i in x:
    if num % i == 0:
        print (i)


div()