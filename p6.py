# http://www.practicepython.org/solution/2014/03/19/06-string-lists-solutions.html

word = input ("enter the string : ")

word = str(word)
drow = word[::-1]

if word == drow:
    print("Strings are  pallindrome ")
else:
    print("Strings are not pallindrome")
print(word)
print(drow)