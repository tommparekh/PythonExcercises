# http://www.practicepython.org/solution/2014/05/15/12-list-ends-solutions.html

mylist = [1, 4,2,56,32,13,45]


def list_ends(lst):
    return [lst[0], lst[-1]]


end_lst = list_ends(mylist)
print(end_lst)