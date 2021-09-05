from array import *
A=array('i',[])

n=int(input("Enter size of array:"))
print("Enter elements {} is array:",n)
for i in range(n):
    x=int(input())
    A.append(x)
A.reverse()
print(str(A))