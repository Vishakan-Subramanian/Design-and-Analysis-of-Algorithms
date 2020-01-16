def suffixMax(arr):
	suffix_max = []
	suffix_max.append(max(arr[0],0))
	for i in range(1, len(arr)):
		suffix_max.append(max(suffix_max[i-1] + arr[i],0))
	
	return suffix_max


def subarrayMax(arr):
	suffix_max = suffixMax(arr)
	print("Suffix Array:\n",suffix_max)

	max_sum, from_ind, to_ind = 0, 0, 0

	for i in range(len(arr)):
		max_sum = max(max_sum, suffix_max[i])
		if(suffix_max[i] == 0):
			from_ind = i

		if(suffix_max[i] == max_sum):
			to_ind = i
		
	return from_ind, to_ind, max_sum
	


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array:\n",arr)	
	
	i, j, max_sum = subarrayMax(arr)
	if(i>=j):	#excluding impossible combinations
		i, j = 0, 0
	
	print("\ni : {0}\tj : {1}\nMaximal Subarray Sum: {2}".format(i,j,max_sum))

	#timeTester()

main()


"""
OUTPUT:

vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex3 Brute Force$ python LinearSS.py

                Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-1 -1 -1 -1
Array:
 [-1, -1, -1, -1]
Suffix Array:
 [0, 0, 0, 0]

i : 0   j : 0
Maximal Subarray Sum: 0


vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex3 Brute Force$ python LinearSS.py

                Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-2 -4 3 -1 5 6 -7 -2 4 3 2
Array:
 [-2, -4, 3, -1, 5, 6, -7, -2, 4, 3, 2]
Suffix Array:
 [0, 0, 3, 2, 7, 13, 6, 4, 8, 11, 13]

i : 1   j : 10
Maximal Subarray Sum: 13

"""
