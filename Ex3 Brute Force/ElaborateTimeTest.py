#This Function has been used in all 4 programs to find running times for the different
#algorithms and the resulting graphs have been saved.

def timeTester():
	import random
	import matplotlib.pyplot as plt
	import time

	times1 = []
	times2 = []
	times3 = []
	times4 = []
	n_values = []

	for n in range(10, 1000, 50):
		arr = [random.randrange(1000) for i in range(n)]

		start1 = time.time()
		i, j, ijsum = bfMaximalArrayCubic(arr)
		end1 = time.time()

		start2 = time.time()
		i, j, ijsum = bfMaximalArrayQuad(arr)
		end2 = time.time()

		start3 = time.time()
		max_sum = dcMaxSum(arr, 0, len(arr)) #function to test
		end3 = time.time()

		start4 = time.time()
		i, j, max_sum = subarrayMax(arr)
		end4 = time.time()

		n_values.append(n)
		times1.append(end1-start1)
		times2.append(end2-start2)
		times3.append(end3-start3)
		times4.append(end4-start4)

	plt.xlabel("Length of N")
	plt.ylabel("Running Time")
	plt.plot(n_values, times1, 'h', color = "blue", label = "O(n^3)")  	#graphing Cubic
	plt.plot(n_values, times2, '*', color = "red", label = "O(n^2)")   	#graphing Quadratic
	plt.plot(n_values, times3, 'D', color = "black", label = "O(nlogn)")   #graphing Linearithmic
	plt.plot(n_values, times3, 'o', color = "green", label = "O(n)")   	#graphing Linear
	plt.grid()
	plt.ylim(-0.1, 0.4)
	plt.legend()
	plt.show()
	plt.title("Time Complexity Analysis")



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
	#print("Prefix Sum:\n",prefix_sum)

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			cur_sum = max(prefix_sum[j] - prefix_sum[i] + arr[i],0)	
			#print(i,j, cur_sum, prefix_sum[j], prefix_sum[i], arr[i])
			if(cur_sum > max_sum):
				max_sum = cur_sum
				max_i, max_j = i,j

	return max_i, max_j+1, max_sum 



def suffixMax(arr):
	suffix_max = []
	suffix_max.append(max(arr[0],0))
	for i in range(1, len(arr)):
		suffix_max.append(max(suffix_max[i-1] + arr[i],0))
	
	return suffix_max


def subarrayMax(arr):
	suffix_max = suffixMax(arr)
	#print("Suffix Array:\n",suffix_max)

	max_sum, from_ind, to_ind = 0, 0, 0

	for i in range(len(arr)):
		max_sum = max(max_sum, suffix_max[i])
		if(suffix_max[i] == 0):
			from_ind = i

		if(suffix_max[i] == max_sum):
			to_ind = i
		
	return from_ind, to_ind, max_sum


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


if __name__ == "__main__":
	timeTester()