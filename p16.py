# http://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html

import string
import random

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))