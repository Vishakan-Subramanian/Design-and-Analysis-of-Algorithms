def swap(a, m, n):
    a[m], a[n] = a[n], a[m]


def ordered_insert(a, n):
    for i in range(n-1, 0, -1):
        print(i, i-1)
        if a[i] < a[i-1]:
            swap(a, i, i-1)
    return a


def ordered_insert_recursion(a,n):
    if a[n-1] >= a[n-2]:
        return a
    else:
        swap(a,n-1,n-2)
        return (ordered_insert_recursion(a,n-1))
    

print("Enter a list of numbers in ascending order, except the last element :")
a = [int(x) for x in input().split()]
a = ordered_insert_recursion(a, len(a))
print("Ordered list : ", a)
