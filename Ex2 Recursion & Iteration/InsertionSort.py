#Question 1: Subdivison 2.


def orderedInsertion(item, array):
    n = len(array)

    if(n==0):
        array = [item]

    elif(array[n-1] < item):
        array.append(item)

    else:
        array = orderedInsertion(item, array[0:n-1]) + array[n-1:]
    
    return array


def main():
    list1 = [5,10,20,35,50]
    print(orderedInsertion(15,list1))
    print(orderedInsertion(35,list1))
    print(orderedInsertion(2,list1))

main()


"""
OUTPUT:

python InsertionSort.py
[5, 10, 15, 20, 35, 50]
[5, 10, 20, 35, 35, 50]
[2, 5, 10, 20, 35, 50]

"""