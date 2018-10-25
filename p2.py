# http://www.practicepython.org/solution/2014/02/15/02-odd-or-even-solutions.html

num_str = input("enter any number")
num = int(num_str)
if num % 2 == 0:
    print(num_str + " is an even number")
else:
    print(num_str + " is an odd number")