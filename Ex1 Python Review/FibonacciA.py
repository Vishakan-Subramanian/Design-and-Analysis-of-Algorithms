def fibR(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibR(n-1)+fibR(n-2)



print("\t\tRecursive Fibonacci Series : ")
n= int(input("\n\n\tEnter Number N: "))
print("The ",n,"th Fibonacci number is: ",fibR(n),end="\n")

"""
python Fibonacci.py
		Recursive Fibonacci Series : 


	Enter Number N: 10
The 5 th Fibonacci number is:  55
"""
