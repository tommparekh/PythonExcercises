# http://www.practicepython.org/solution/2014/04/16/11-check-primality-functions-solutions.html



def get_number():
    return int(input("enter the number : "))

def check_prime(num):
    prime = False
    if num == 1:
        prime = False
    elif num == 2:
        prime = True
    else:
        prime = True
        for number in range(2, int((num/2)+1)):
            if num % number == 0:
                prime = False
                break

    return prime

def print_is_prime(prime, num):
    if prime:
        msg = " is prime "
    else:
        msg = " is not prime "
    print(num, msg, sep="", end = "\n\n")



user_num = get_number()
isprime = check_prime(user_num)
print_is_prime(isprime, user_num)