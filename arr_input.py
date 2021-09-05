from array import *
A = array('i',[])
n = int(input("Enter the size of array"))
print("Enter "+str(n)+"Elements to insert")
for i in range(n):
    x= int(input())
    A.append(x)
print(A)

for i in range(n):
    print(A[i])
