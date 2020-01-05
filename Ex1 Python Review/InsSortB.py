"""
Insertion Sort: Parts 5 6
"""

def ordered_insert(a,n):
    last = a[n-1]
    i = n-2
    while(i>=0):
        if(a[i]>last):
            a[i+1] = a[i]
            i-=1
        else:
            break
    a[i+1] = last


def ins_sort_rec(a,n):
    if(n<=1):
        return
    
    ins_sort_rec(a,n-1)
    ordered_insert(a,n)



def ordered_insert_first(a,n):
	for i in range(0,n):
		if(a[i]>a[i+1]):
			a[i], a[i+1] = a[i+1], a[i]
	return a



print("Enter a list of numbers :")
a = [int(x) for x in input().split()]
a = ordered_insert_first(a, len(a)-1)
print("Ordered list : ", a)


print("\nEnter a list of numbers :")
a = [int(x) for x in input().split()]
ins_sort_rec(a, len(a))
print("Ordered list : ", a)





"""
OUTPUT:

python InsSortB.py
Enter a list of numbers :
8 3 5 6 7
Ordered list :  [3, 5, 6, 7, 8]

Enter a list of numbers :
8 3 20 4 7 2 2 58
Ordered list :  [2, 2, 3, 4, 7, 8, 20, 58]
"""