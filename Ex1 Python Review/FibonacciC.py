def fibR(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibR(n-1)+fibR(n-2)


def fibM(m,n):
	fib_table = []
	for i in range(m,n+1):
		fib_table.append(fibR(i))
	return fib_table



fib_table = []
print("\n\n\t\tNth Fibonacci Term\n")
val = 1


while val!=0:
	val = int(input("\nAny Number to Enter Input\n0 to Exit\n->"))
	if(val==0):
		print("\n\t\tExiting...")
		continue	
	n= int(input("\n\n\tEnter Number N: "))
	if(len(fib_table)-1>=n):
		print("\n\t\tThe ",n,"th Fibonacci Number is(Pre-Computed): ",fib_table[n])
	else:
		fib_table = fib_table + fibM(len(fib_table),n)
		print("\n\t\tThe ",n,"th Fibonacci Number is(Computed Now): ",fib_table[n])
	

"""
cs1196@splc29:~/DAA/Ex1$ python FibonacciC.py


		Nth Fibonacci Term


Any Number to Enter Input
0 to Exit
->1


	Enter Number N: 5

		The  5 th Fibonacci Number is(Computed Now):  5

Any Number to Enter Input
0 to Exit
->1


	Enter Number N: 8

		The  8 th Fibonacci Number is(Computed Now):  21

Any Number to Enter Input
0 to Exit
->1


	Enter Number N: 4

		The  4 th Fibonacci Number is(Pre-Computed):  3

Any Number to Enter Input
0 to Exit
->1


	Enter Number N: 9

		The  9 th Fibonacci Number is(Computed Now):  34

Any Number to Enter Input
0 to Exit
->0

		Exiting...
"""
