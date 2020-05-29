#Longest Common Subsequence Problem - Dynamic Programming

def LCS(a, b, m, n):

    if(m == 0 or n == 0):   #empty array
        return 0
    
    elif(a[m-1] == b[n-1]): #both are equal
        return 1 + LCS(a, b, m-1, n-1)

    else:                   #in case array isn't empty, and there are elements but don't correspond
        return max(LCS(a, b, m-1, n), LCS(a, b, m, n-1))


def LCSDP(a, b):    #Bottom up DP Approach
    m = len(a)
    n = len(b)

    Lookup = [[-1]*(n+1) for i in range(m+1)]   #Creating a Lookup Table for Dynamic Approach

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):   #Base Case, String empty
                Lookup[i][j] = 0
            elif(a[i - 1] == b[j - 1]): #If the characters correspond
                Lookup[i][j] = Lookup[i - 1][j - 1] + 1
            else:   #Choosing the best subsequence length in case it doesn't match
                Lookup[i][j] = max(Lookup[i - 1][j], Lookup[i][j - 1])
    
    return Lookup       #Best possible subsequence returned in Lookup[m][n]


def backTrace(a, b):
    Lookup = LCSDP(a, b)
    m, n = len(a), len(b)
    i, j = m, n

    LCSindex = Lookup[m][n] #Starting from the LCS value at the end of the Lookup table
    LCS = ""

    while(i>0 and j>0):
        if(a[i-1] == b[j-1]):   #Appending to the sequence if the value matches
            LCS = LCS + str(a[i - 1])
            i-=1
            j-=1

        elif(Lookup[i - 1][j] > Lookup[i][j - 1]):    #Move leftward the table
            i-=1
        
        else:   #Move upward the table
            j-=1
        
    return LCS[::-1]


if __name__ == "__main__":
    print("\tLongest Common Subsequence Problem")
    
    a, b = [], []
    
    print("Enter an array of elements for A: ")
    a = [x for x in input().split()]
    
    print("Enter an array of elements for B: ")
    b = [x for x in input().split()]

    print("Length of Longest Common Subsequence of A & B - Recursive          :",LCS(a, b, len(a), len(b)))
    
    Lookup = LCSDP(a, b)
    print("Length of Longest Common Subsequence of A & B - Dynamic Programming:",Lookup[len(a)][len(b)])
    print("The Longest Common Subsequence of A & B is: ",backTrace(a,b))

"""
OUTPUT:

PS D:\College Material\Second Year\4th Semester\DAA Lab\Ex6> python LCS.py
        Longest Common Subsequence Problem
Enter an array of elements for A:
A E D F H R
Enter an array of elements for B:
A B C D G H
Length of Longest Common Subsequence of A & B - Recursive          : 3
Length of Longest Common Subsequence of A & B - Dynamic Programming: 3
The Longest Common Subsequence of A & B is:  ADH

"""