class Plotter:  #to plot graphs
    
    times_1 = []
    times_2 = []
    n_values = []

    def plot_graph(self):
        import random
        import matplotlib.pyplot as plt
        import time
            
        for n in range(10, 1000, 50):
            test = Inversions()
            test.array = [random.randrange(1000) for i in range(n)]
            buf_array = [0 for i in range(n)]

            start1 = time.time()
            pairs = test.disordered_pairs()                     #Brute Force
            end1 = time.time()

            start2 = time.time()
            pairs = test.merge_sort(test.array, buf_array, 0, n-1)    #Divide And Conquer
            end2 = time.time()

            self.n_values.append(n)
            self.times_1.append(end1-start1)
            self.times_2.append(end2-start2)

        plt.xlabel("Length of N")
        plt.ylabel("Running Time")
        plt.plot(self.n_values, self.times_1, '^', color = 'blue', label = "O(n^2)")   #Graphing Brute Force
        plt.plot(self.n_values, self.times_2, 'v', color = 'green' , label = "O(nlogn)") #Graphing Divide And Conquer
        plt.grid()
        plt.legend()
        plt.show()
        plt.title("Time Complexity Analysis")


class Inversions: #for Inversion Checking
    array = []

    def __init__(self):
        self.array = [5, 4, 3, 2, 1]
    

    def get_input(self):
        self.array = [int(x) for x in input().split()]
    

    def disordered_pairs(self):
        pairs = 0

        for i in range(len(self.array)):
            elt = self.array[i]
            for j in range(i+1, len(self.array)):
                if self.array[i] > self.array[j]:
                    pairs+=1
    
        return pairs


    def merge(self, array, buf_array, left, mid, right): 
        i, j, k, pairs = left, mid+1, left, 0
        #merging into buffer array as recursion cannot be used
        while i <= mid and j <= right:  
  
            if array[i] <= array[j]: #no inversions
                buf_array[k] = array[i] 
                k += 1
                i += 1
            else:  
                buf_array[k] = array[j] 
                pairs += (mid-i + 1) #There are mid - i inversions if array[i] > array[j]
                k += 1
                j += 1

        while i <= mid: #remaining elements - left
            buf_array[k] = array[i] 
            k += 1
            i += 1

        while j <= right: #remaining elements - right
            buf_array[k] = array[j] 
            k += 1
            j += 1


        for x in range(left, right + 1): #copying sorted subarray into original array
            array[x] = buf_array[x] 
          
        return pairs     
    

    def merge_sort(self, arr, temp_arr, left, right):
  
        pairs = 0
  
        if left < right:
            mid = (left + right)//2
            #calculating no. of inversions as an extension of merge sorting
            pairs += self.merge_sort(arr, temp_arr, left, mid)  #inversions in left halff
            pairs += self.merge_sort(arr, temp_arr, mid + 1, right) #inversions in right half
            pairs += self.merge(arr, temp_arr, left, mid, right) #merge
        
        return pairs
    


if __name__ == "__main__":
    print("Enter an array of numbers separated by spaces: \n")
    
    r = Inversions()
    r.get_input()

    print("\n\tBrute Force Algorithm\n")
    print("Number of disordered pairs in {0} is {1}.\n".format(r.array, r.disordered_pairs()))


    print("\n\tDivide And Conquer Algorithm\n")
    print("Number of disordered pairs in {0} is {1}.\n".format(r.array, r.merge_sort(r.array, [0 for x in range(len(r.array))], 0, len(r.array)-1)))


    plot = Plotter()
    plot.plot_graph()



"""
OUTPUT:

vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex4 Rankings$ python RankingsQuad.py
Enter an array of numbers separated by spaces: 

1 2 3 4 5

            Brute Force Algorithm

Number of disordered pairs in [1, 2, 3, 4, 5] is 0.

        Divide And Conquer Algorithm

Number of disordered pairs in [1, 2, 3, 4, 5] is 0.

vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex4 Rankings$ python RankingsQuad.py
Enter an array of numbers separated by spaces: 

5 4 3 2 1

            Brute Force Algorithm

Number of disordered pairs in [5, 4, 3, 2, 1] is 10.

        Divide And Conquer Algorithm

Number of disordered pairs in [1, 2, 3, 4, 5] is 10.

"""