# http://www.practicepython.org/solution/2014/07/25/13-fibonacci-solutions.html

# 1,1,2,3,5,8

count = int(input("how many numbers of fibonachhi series you want to generate : "))

def gen_fib(count):
    fib_list = []

    if count == 1:
        fib_list = [1]
    elif count == 2:
        fib_list = [1,1]
    else:
        fib_list = [1, 1]
        i = 0
        while i < count-2:
            fib_list.append(fib_list[i] + fib_list[i+1])
            i = i+1

    return fib_list


fib_list = gen_fib(count)
print(fib_list)