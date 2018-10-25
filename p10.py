# http://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

result = [num for num in set(a) if num in b]

print(a)
print(b)
print(result)