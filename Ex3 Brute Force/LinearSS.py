def suffixMax(arr):
	suffix_max = []
	for i in range(len(arr)):
		if(i == 0):
			suffix_max.append(arr[i])
		else:
			suffix_max.append(max(suffix_max[i-1] + arr[i], 0))
	
	return suffix_max

def bfMaximalArrayLinear(arr, suffix_max):
	max_sum = 0
	for i in range(len(arr)):
		max_sum = suffix_max



def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array: ",arr)	
	
	suffix_max = suffixMax(arr)
	print(suffix_max)
	#i, j, ijsum = bfMaximalArrayLinear(arr, suffix_max)
	#print("\ni : {0}\nj : {1}\nMaximal Subarray Sum: {2}".format(i,j,ijsum))
	#print("\nSubarray : Array[{0}:{1}]\n".format(i,j),arr[i:j])



main()
