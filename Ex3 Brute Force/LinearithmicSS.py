def dcMaxSum(arr, low, high):
    if(low == high):	#base case, only one element
        return arr[0]
    
    else:	#finding maximum of all 3 possible combinations
        mid = (low+high)//2
        return max(	dcMaxSum(arr,low, mid),
					dcMaxSum(arr, mid+1, high),
                    dcMiddleSum(arr, low, mid, high))


def dcMiddleSum(arr, low, mid, high):	#finding the middle sum
	max_sum, left_sum = 0, 0
	for i in range(mid, low-1, -1):	#finding the maximum sum of left subarray
		max_sum = max_sum + arr[i]

		if(max_sum > left_sum):
			left_sum = max_sum

	max_sum, right_sum = 0, 0
	for i in range(mid+1, high):	#finding the maximum sum of right subarray
		max_sum = max_sum + arr[i]

		if(max_sum > right_sum):
			right_sum = max_sum
	
	return left_sum + right_sum		#adding the 2 as max sum of the sub array


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array:\n",arr)	
	
	max_sum = dcMaxSum(arr, 0, len(arr))
	print("\nMaximal Subarray Sum: {0}".format(max_sum))
	
	#timeTester()

main()


"""
OUTPUT:


(base) vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex3 Brute Force$ python LinearithmicSS.py

                Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-1 -1 -1 -1
Array:
 [-1, -1, -1, -1]

Maximal Subarray Sum: 0


(base) vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex3 Brute Force$ python LinearithmicSS.py

                Maximal Sub-Array Sum Finder
Enter a List of Numbers: 
-2 -4 3 -1 5 6 -7 -2 4 3 2
Array:
 [-2, -4, 3, -1, 5, 6, -7, -2, 4, 3, 2]

Maximal Subarray Sum: 13

"""