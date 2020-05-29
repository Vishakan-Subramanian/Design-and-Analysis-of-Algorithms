class MagicSquare:
    
    def __init__(self, n):
        self.n = n  #size of square
        self.sum = (self.n) * (((self.n ** 2) + 1) / 2) #magic number
        self.grid = [[0 for i in range(self.n)] for j in range(self.n)] #magic square
        self.cells = n*n    #value limit for a cell
        self.iter = 0
    
    def printSquare(self):  #print the magic square
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j], end = " ")
            print("\n")

    def checkValue(self, value):    #check if the given value is unique in the square

        for i in range(self.n):
            if not(value in self.grid[i]):
                continue
            else:
                return False
        
        return True
    
    def isMagicSquare(self):    #checking if magic square property is satisfied
        row_sum, col_sum, diag_sum, anti_sum = 0, 0, 0, 0
        
        for row in range(self.n):   #checking for 0s
            for col in range(self.n):
                if(self.grid[row][col] == 0):
                    return False
        
        for row in range(self.n):   #sum of rows
            row_sum = 0
            for col in range(self.n):
                row_sum += self.grid[row][col]
            
            if(row_sum != self.sum):
                return False
        
        for col in range(self.n):   #sum of columns
            col_sum = 0
            for row in range(self.n):
                col_sum += self.grid[row][col]
            
            if(col_sum != self.sum):
                return False
        
        for diag in range(self.n):  #sum of diagonal and anti-diagonal
            diag_sum += self.grid[diag][diag]
            anti_sum += self.grid[self.n - 1 - diag][diag]
        
        if(diag_sum != self.sum):
            return False
        
        if(anti_sum != self.sum):
            return False
        
        return True

    def makeMagicSquare(self):  #making a magic square using Backtracking Algorithm
        self.iter+=1
        for i in range(self.cells):
            row = i // self.n
            col = i % self.n

            if(self.grid[row][col] == 0):   #choose an empty cell
                for value in range(1, self.cells + 1):  #choose a value
                    if(self.checkValue(value) == True): #check uniqueness of value
                        self.grid[row][col] = value
            
                        if(self.isMagicSquare() == True):   #if the magic square is finished
                            return True
                        else:   #incomplete magic square
                            if(self.makeMagicSquare() == True): #recursive call to fill to the next cell
                                return True
                            
                break   #if the value does not make a magic square, backtrack
        self.grid[row][col] = 0 #back to default value 
        
            


if __name__ == "__main__":
    print("\n\t\tMagic Square Solver\n")
    
    n = int(input("Enter the Size of the Square (N > 2) : "))
    #n < 2 CANNOT BE SOLVED
    #n > 3 TAKES A VERY LONG TIME TO BACKTRACK
    
    magic_square = MagicSquare(n)
    result = magic_square.makeMagicSquare()
    
    if(result == True):
        print("\nMagic Square:\n")
        magic_square.printSquare()
        print("No. of Iterations to Solve:", magic_square.iter)
    else:
        print("\nCould not solve the Magic Square.")

"""
OUTPUT:

python MagicSquare.py

                Magic Square Solver

Enter the Size of the Square (N > 2) : 3

Magic Square:

2 7 6

9 5 1

4 3 8

No. of Iterations to Solve: 187768

"""