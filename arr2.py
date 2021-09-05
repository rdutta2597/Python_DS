N = int(input("Enter the size of array:"))
array = list(map(int,input("Enter "+str(N)+" elements in array:").split(' ')[:N]))
p = len(array)
if N > p:
    print("Array size is out of bound")
else:
    print(array)
