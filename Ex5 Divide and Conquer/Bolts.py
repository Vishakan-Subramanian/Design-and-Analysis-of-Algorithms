class Bolts:
	
	bolts = []
	nuts = []
	n = 0	#number of nuts/bolts

	
	def quadPair(self, nuts, bolts):	#pairing using Brute Force
		pair_tuples = []
		
		for nut in nuts:
			for bolt in bolts:
				if(nut == bolt):
					pair_tuples = pair_tuples + [(nut,bolt)]
		
		return pair_tuples


	def quickPartition(self, arr, low, high, pivot):	
		i = low
		j = low
		while(j < high):	#default quick sorting
			if(arr[j] < pivot):
				arr[i], arr[j] = arr[j], arr[i]
				i+=1
			elif(arr[j] == pivot):	#case where the nut and bolt match, where we need to swap that with the last elt. of array
				arr[j], arr[high] = arr[high], arr[j]
				j-=1	#should not consider this as a valid iteration for j, so decrement
			j+=1

		arr[i], arr[high] = arr[high], arr[i]	#swap i and high, as in usual quick sort procedure to put pivot in its place
		return i	#the array is partitioned at i now


	def quickPair(self, low, high):
		if(low >= high):
			return

		pivot = self.quickPartition(self.nuts, low, high, self.bolts[high])	#partitioning nuts with a self-chosen bolt 
		self.quickPartition(self.bolts, low, high, self.nuts[pivot])	#partitioning bolts with the correct position nut

		self.quickPair(low, pivot - 1)
		self.quickPair(pivot + 1, high)
		
				


if __name__ == "__main__":

	print("\n\t\tNUTS AND BOLTS\n")	
	
	b = Bolts()
	
	b.n = int(input("Enter the number of nuts/bolts: "))
	print("Enter the sizes of nuts:")
	b.nuts = [int(x) for x in input().split()]
	print("Enter the sizes of bolts:")
	b.bolts = [int(x) for x in input().split()]
	
	print("\n\tBrute Force Pairing")
	print("The proper pairing of nuts and bolts: ")
	print(b.quadPair(b.nuts, b.bolts))

	
	print("\n\tQuick Sort Pairing")
	b.quickPair(0, b.n - 1)
	print("Sorted nuts and bolts:")
	print(b.nuts)
	print(b.bolts)



"""

OUTPUT:

(base) vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex5 Divide and Conquer$ python Bolts.py

                NUTS AND BOLTS

Enter the number of nuts/bolts: 9
Enter the sizes of nuts:

1 2 3 4 5 6 7 8 9 0 
Enter the sizes of bolts:

0 9 8 7 6 5 4 3 2 1

        Brute Force Pairing
The proper pairing of nuts and bolts: 
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (0, 0)]

        Quick Sort Pairing
Sorted nuts and bolts:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

(base) vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex5 Divide and Conquer$ python Bolts.py

                NUTS AND BOLTS

Enter the number of nuts/bolts: 7
Enter the sizes of nuts:
2 1 3 4 5 7 6 
Enter the sizes of bolts:
3 4 1 2 6 5 7 

        Brute Force Pairing
The proper pairing of nuts and bolts: 
[(2, 2), (1, 1), (3, 3), (4, 4), (5, 5), (7, 7), (6, 6)]

        Quick Sort Pairing
Sorted nuts and bolts:
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]

"""