from array import *
A=array('i',[])

n=int(input("Enter size of array:"))
print("Enter "+str(n)+" elements is array:")
for i in range(n):
    x=int(input())
    A.append(x)
print()

print(A[0])
print(A[1])
print(A[2])

