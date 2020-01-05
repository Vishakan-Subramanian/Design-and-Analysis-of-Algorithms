"""
Insertion Sort: Parts 1 2 3 and 4
"""

def ordered_insert(a):
	if len(a) != 1:
		for i in range(len(a)-2, -1, -1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
	return a


def ordered_insert_iter(a, n): 
	if n != 1:
		for i in range(n-2, -1, -1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
	return a[:n]


def ordered_insert_rec(a, n):
	if n != 1 and a[n-2] > a[n-1]:
		a[n-2], a[n-1] = a[n-1], a[n-2]
		a[:n-1] = ordered_insert_iter(a, n-1)
	return a


print("Enter a list of numbers :")
a = [int(x) for x in input().split()]
a = ordered_insert_rec(a, len(a))
print("Ordered list : ", a)



"""
OUTPUT:

python InsSortA.py
Enter a list of numbers :
1 4 8 3
Ordered list :  [1, 3, 4, 8]

"""




