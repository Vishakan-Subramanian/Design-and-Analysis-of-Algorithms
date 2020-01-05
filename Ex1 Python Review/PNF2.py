def swap(a, m, n):
    a[m], a[n] = a[n], a[m]
    return a


def PNF(a, low, high):
    b = []
    for num in a:
        if(num < a[low]):  # pivoting at low
            b.append(num)

    for num in b:
        a.remove(num)

    b = b + a
    a = b
    return a


a = [int(x) for x in input("Enter a list of numbers: ").split()]
a = PNF(a, 0, len(a))
print(a)


"""
OUTPUT:

python PNF2.py
#Enter a list of numbers: 3 -2 39 18 3 0 -2 -4 92 -3 -3
#[3, -2, 39, 18, 3, 0, -2, -4, 92, -3, -3] 11
[-2, 0, -2, -4, -3, -3, 3, 39, 18, 3, 92]

"""