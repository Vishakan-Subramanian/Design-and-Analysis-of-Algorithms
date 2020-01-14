def bfMaximalArrayCubic(arr):
	max_sum = 0
	max_i,max_j = 0,0

	for i in range(len(arr)):
		j = i
		for j in range(len(arr)+1):
			sub = arr[i:j]
			cur_sum = sum(sub)
			if(cur_sum > max_sum):
				max_sum = cur_sum
				max_i, max_j = i,j
	return max_i, max_j, max_sum



def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array: ",arr)
	
	i, j, ijsum = bfMaximalArrayCubic(arr)
	print("\ni : {0}\nj : {1}\nMaximal Subarray Sum: {2}".format(i,j,ijsum))
	print("\nSubarray : Array[{0}:{1}]\n".format(i,j),arr[i:j])



main()


"""
OUTPUT:

cs1196@splc29:~/DAA/Ex3$ python CubicSS.py

		Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-2 -4 3 -1 5 6 -7 -2 4 3 2
Array:  [-2, -4, 3, -1, 5, 6, -7, -2, 4, 3, 2]

i : 2
j : 6
Maximal Subarray Sum: 13

Subarray : Array[2:6]
[3, -1, 5, 6]


cs1196@splc29:~/DAA/Ex3$ python CubicSS.py

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
