def print_array(a, low, high):
    print(a[low:high])


def read_array(a):
    a = [int(x) for x in input().split()]
    return a, len(a)


def minimum(a, low, high):
    b = a[low:high]
    return b.index(min(b))+low  # to return the appropriate index in list a


def swap(a, m, n):
    a[n], a[m] = a[m], a[n]
    return a


def sel_sort(a):
    n = len(a)
    for i in range(n):
        temp = minimum(a, i, n)
        a = swap(a, temp, i)
    return a


a = []
print("Selection Sorting of List")
print("\nEnter a list of Numbers: ")
a, n = read_array(a)
print("Minimum of List is : ", a[minimum(a, 0, len(a))])
print("Selection Sorted List: \n")
a = sel_sort(a)
print(a)


"""
python SelSortA.py
Selection Sorting of List

Enter a list of Numbers:
5 3 29 1 28 3
Minimum of List is :  1
Selection Sorted List:

[1, 3, 3, 5, 28, 29]

python SelSortA.py
Selection Sorting of List

Enter a list of Numbers:
5 4 3 2 1
Minimum of List is :  1
Selection Sorted List:

[1, 2, 3, 4, 5]

"""