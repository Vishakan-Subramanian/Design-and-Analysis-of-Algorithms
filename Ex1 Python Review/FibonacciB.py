def fibI(n):
	a=0
	print(a,end=" ")
	b=1
	for i in range(n-1):
		print(b,end=" ")
		temp = b	
		b = a+b
		a = temp
		
	print(b,end="\n")
	return b
	


n= int(input("\nEnter Number N: "))
print("\nIterative Fibonacci Series Print:\n")
n_fib = fibI(n)
print("The ",n,"th Fibonacci number is: ",n_fib,end="\n")

"""
cs1196@splc29:~/DAA/Ex1$ python FibonacciB.py

Enter Number N: 5

Iterative Fibonacci Series Print:

0 1 1 2 3 5
The  5 th Fibonacci number is:  5
"""
