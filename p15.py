#  http://www.practicepython.org/solution/2014/05/28/15-reverse-word-order-solutions.html

teststr = "My name is Michele"

split_str = teststr.split(" ")
print(split_str)

split_str_rev = split_str[::-1]
print(" ".join(split_str_rev))