def prefixSum(arr):
	prefix_sum = []

	for i in range(len(arr)):
		if(i == 0):
			prefix_sum.append(arr[i])
		else:
			prefix_sum.append(prefix_sum[i-1] + arr[i])

	return prefix_sum
	

def bfMaximalArrayQuad(arr):
	max_sum, max_i, max_j = 0, 0, 0

	prefix_sum = prefixSum(arr)
	print("Prefix Sum:\n",prefix_sum)

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			cur_sum = max(prefix_sum[j] - prefix_sum[i] + arr[i],0)	
			#print(i,j, cur_sum, prefix_sum[j], prefix_sum[i], arr[i])
			if(cur_sum > max_sum):
				max_sum = cur_sum
				max_i, max_j = i,j

	return max_i, max_j+1, max_sum 


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array: ",arr)	
	
	i, j, ijsum = bfMaximalArrayQuad(arr)
	print("\ni : {0}\nj : {1}\nMaximal Subarray Sum: {2}".format(i,j,ijsum))
	if(ijsum!=0):
		print("\nSubarray : Array[{0}:{1}]\n".format(i,j),arr[i:j])

	#timeTester()


main()


"""
OUTPUT:

cs1196@splc29:~/DAA/Ex3$ python QuadSS.py

		Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-2 -4 3 -1 5 6 -7 -2 4 3 2
Array:  [-2, -4, 3, -1, 5, 6, -7, -2, 4, 3, 2]

i : 2
j : 6
Maximal Subarray Sum: 13

Subarray : Array[2:6]
[3, -1, 5, 6]

cs1196@splc29:~/DAA/Ex3$ python QuadSS.py

		Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-1 -1 -1 -1
Array:  [-1, -1, -1, -1]

i : 0
j : 0
Maximal Subarray Sum: 0

Subarray : Array[0:0]
[]

"""
