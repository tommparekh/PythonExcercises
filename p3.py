# http://www.practicepython.org/solution/2014/02/26/03-list-less-than-ten-solutions.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lt5_list = []

for i in a:
    if i < 5:
        lt5_list.append(i)

print (lt5_list)