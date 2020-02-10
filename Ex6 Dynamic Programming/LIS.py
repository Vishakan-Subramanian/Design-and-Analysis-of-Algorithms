import math

	
def getInput(array):	#to get input

	print("Enter the array elements: ")		
	array = [int(x) for x in input().split()]
	array.append(math.inf)
	return array


def exhaustLIS(j):	#exhaustive searching for LIS
		
	best = 1
	for i in range(0,j):
		if array[i] < array[j]:
			best = max(best, exhaustLIS(i) + 1)
		
	return best


def dynamicLIS(n):	#dynamic programming of LIS

	L = [1 for x in range(n)]
	
	for j in range(0, n):
		for i in range(0, j):
			if array[i] < array[j]:
				L[j] = max(L[j], L[i] + 1)
	
	return L[n -1]


def dynamicPredLIS(n):	#dynamic programming using Predecessor Matrix

	L = [1 for x in range(n)]
	P = [-1 for x in range(n)]
	print(array)
	
	for j in range(0, n):
		for i in range(0, j):
			if array[i] < array[j]:
				#L[j] = max(L[j], L[i] + 1)
				if L[i] + 1 > L[j]:
					P[j] = i
				L[j] = max(L[j], L[i] + 1)
	
	return L[n -1], P


def iterTraceLIS(n):	#finding the Trace of the LIS using Pred. Matrix, iteratively
	
	trace = []
	
	while(P[n] != -1):
		trace.append(array[P[n]])
		n = P[n]
	return trace[::-1]
	

def recurTraceLIS(trace, n):	#finding the Trace of the LIS using Pred. Matrix, recursively
	if(P[n] != -1):
		trace.append(array[P[n]])
		return recurTraceLIS(trace, P[n])
	else:
		return trace[::-1]
	


if __name__ == "__main__":
	print("\n\t\tLongest Increasing Subsequence\n")

	array = []
	array = getInput(array)
	n = len(array)

	length, P = dynamicPredLIS(n)	

	print("\nExhaustive 	- The LIS of the given array is :", exhaustLIS(n - 1) - 1)
	print("\nDynamic    	- The LIS of the given array is :", dynamicLIS(n - 1))
	print("\nDynamic.Pred	- The LIS of the given array is :", length)
	print("\nPredecessor Matrix: ", P)
	print("\nIterative Trace   : ", iterTraceLIS(len(P) - 1))
	print("\nRecursive Trace   : ", recurTraceLIS([], len(P) - 1))




"""
OUTPUT:

cs1196@splc29:~/DAA/Ex6$ python LIS.py

		Longest Increasing Subsequence

Enter the array elements: 
2 4 3 5 1 7 6 9 8

The LIS of the given array is : 5

cs1196@splc29:~/DAA/Ex6$ python LIS.py

		Longest Increasing Subsequence

Enter the array elements: 
5 1 5 7 2 4 9 8

The LIS of the given array is : 4

cs1196@splc29:~/DAA/Ex6$ python LIS.py

		Longest Increasing Subsequence

Enter the array elements: 
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6

The LIS of the given array is : 6

cs1196@splc29:~/DAA/Ex6$ python LIS.py

		Longest Increasing Subsequence

Enter the array elements: 
2 4 3 5 1 7 9 6 8 
[2, 4, 3, 5, 1, 7, 9, 6, 8, inf]

Exhaustive 	- The LIS of the given array is : 5

Dynamic    	- The LIS of the given array is : 5

Dynamic.Pred	- The LIS of the given array is : 6

Predecessor Matrix:  [-1, 0, 0, 1, -1, 3, 5, 3, 5, 6]

Iterative Trace   :  [2, 4, 5, 7, 9]

Recursive Trace   :  [2, 4, 5, 7, 9]

"""
