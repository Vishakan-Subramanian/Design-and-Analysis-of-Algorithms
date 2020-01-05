"""
Insertion Sort: Part 7
"""

def ordered_insert_power(a, n): 
	if n != 1:
		x = a[1]
		k = 1
		i = 2 ** k
		while i<n:
			if a[i] < x:
				a[(i)//2] = a[i]
			else:
				break
			k += 1
			i = 2 ** k
		a[(i)//2] = x
	return a




a = [0, 39, 0, 0, 1, 0, 0, 0, 7]
a = ordered_insert_power(a, len(a))
print("Ordered list : ", a)



"""
OUTPUT:

python InsSortC.py
Ordered list :  [0, 0, 1, 0, 7, 0, 0, 0, 39]

"""