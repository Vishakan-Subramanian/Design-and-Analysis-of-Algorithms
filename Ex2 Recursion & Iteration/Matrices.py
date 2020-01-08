#Question 1: Subdivison 2.


def matrixInput(i):
    row1, col1 = map(int, input("Enter The Number of Rows and Columns of Matrix (space separated): ").split())
    print("Enter the elements:")
    mat1 = [[int(input()) for j in range(col1)] for i in range(row1)]
    return mat1,row1,col1

def matrixPrint(mat):
    for i in range(len(mat)):
        print("\n")
        for j in range(len(mat[0])):
            print(mat[i][j],end = "\t")

    print("\n")

def matrixMultiply(mat1,mat2):
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
	    for j in range(len(mat2[0])):
		    for k in range(len(mat2)):
			    result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def matFastPower(x,n):
	if(n==1):
		return x
	elif(n%2 !=0):
		 return matrixMultiply(x, matFastPower(x,n-1))
	else:
		return matrixMultiply(matFastPower(x,n//2), matFastPower(x,n//2))


def fibonacciFinder(n):
    basematrix = [[0,1],[1,1]]
    basevalues = [[0],[1]]
    basematrix = matFastPower(basematrix,n)
    fibomatrix = matrixMultiply(basematrix,basevalues)

    print("The ",n,"th Fibonacci Number is: ",fibomatrix[0][0])



def main():
    print("Enter 2 matrices to multiply.")
    mat1,row1,col1 = matrixInput(1)
    mat2,row2,col2 = matrixInput(2)
    print("Matrix 1: \n")
    matrixPrint(mat1)
    print("Matrix 2: \n")
    matrixPrint(mat2)
    
    try:
        if(col1!=row2):
            raise Exception("The column length of Matrix 1 needs to be the same as row length of Matrix 2.")
        print("Result Matrix: \n")
        result = matrixMultiply(mat1,mat2)
        matrixPrint(result)
        exp = int(input("Enter Power to which Matrix 1 is to be raised: "))
        expomat = matFastPower(mat1,exp)
        matrixPrint(expomat)
        n = int(input("Enter the nth Fibonacci Term you wish to find: "))
        fibonacciFinder(n)

    except Exception as error:
        print("Error: ",error) 


main()


"""
OUTPUT:

python Matrices.py
Enter 2 matrices to multiply.
Enter The Number of Rows and Columns of Matrix (space separated): 2 2
Enter the elements:
1
2
3
4
Enter The Number of Rows and Columns of Matrix (space separated): 2 2
Enter the elements:
1
2
3 
4
Matrix 1: 



1       2

3       4

Matrix 2:



1       2

3       4

Result Matrix:



7       10

15      22

Enter Power to which Matrix 1 is to be raised: 5


1069    1558

2337    3406

Enter the nth Fibonacci Term you wish to find: 7
The  7 th Fibonacci Number is:  13
"""