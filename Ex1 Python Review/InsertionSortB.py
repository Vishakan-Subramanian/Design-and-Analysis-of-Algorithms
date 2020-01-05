def swap(a, m, n):
    a[m], a[n] = a[n], a[m]


def temp_sorting(a,n):
    temp = a[n-1]
    i = n-2
    while(i>=0):
        if a[i] > temp:
            a[i+1] = a[i]
        else:
            a[i+1] = temp
            break
        i = i-1
    return a 

print("Enter a list of numbers in ascending order, except the last element :")
a = [int(x) for x in input().split()]
a = temp_sorting(a, len(a))
print("Ordered list : ", a)
