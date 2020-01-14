def suffixMax(arr):
	suffix_max = []
	for i in range(len(arr):
		if(i == 0):
			suffix_max.append(arr[j])
		else:
			suffix_max.append(max(suffix_max[j-1] + arr[j-1], 0))
	
	return suffix_max

def bfMaximalArraySL(suffix_max):
	



def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array: ",arr)	
	
	prefix_sum = prefixSum(arr)

	i, j, ijsum = bfMaximalArrayQuad(arr, prefix_sum)
	print("\ni : {0}\nj : {1}\nMaximal Subarray Sum: {2}".format(i,j,ijsum))
	print("\nSubarray : Array[{0}:{1}]\n".format(i,j),arr[i:j])



main()
