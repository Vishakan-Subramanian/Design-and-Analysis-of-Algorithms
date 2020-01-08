#Question 1: Subdivison 1.


def recursivePower(x,n):
	if(n == 0):
		return 1
	else:
		return x * recursivePower(x,n-1)


def iterPower(x,n):
	result = 1
	for _ in range(0,n):
		result = result*x
	return result

def recursiveFastPower(x,n):
	if(n==0):
		return 1
	elif(n%2 !=0):
		return x * recursiveFastPower(x,n-1)
	else:
		return recursiveFastPower(x,n//2) * recursiveFastPower(x,n//2)

def iterFastPower(x,n):
	result = 1
	while(n>0):
		if(n%2 == 0):
			n//=2
			result *= (x**(n))
		else:
			result *= x
			n-=1		

	return result





def main():
	x = int(input("Enter the Base: "))
	n = int(input("Enter the Exponent: "))
	print("Result for Recursive Power is : ",recursivePower(x,n))
	print("Result for Iterative Power is : ",iterPower(x,n))
	print("Result for Recursive Fast Power is : ",recursiveFastPower(x,n))
	print("Result for Iterative Fast Power is : ",iterFastPower(x,n))
	print("\n------------------------------------------------------\n")
	
	

main()



"""
OUTPUT:

python Exponents.py
Enter the Base: 3
Enter the Exponent: 4
Result for Recursive Power is :  81
Result for Iterative Power is :  81
Result for Recursive Fast Power is :  81
Result for Iterative Fast Power is :  81

------------------------------------------------------

"""	
