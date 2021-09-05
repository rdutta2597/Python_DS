def reverseArr(A,start,end):
    while start < end:
        A[start], A[end]=A[end],A[start] #swap
        start +=1
        end -=1
    
A=[]
n=int(input("Enter the no. of elements"))
print("Enter the elements:")
for i in range(0,n+1):
    x = int(input())
    A.append(x)
print("Entered array:",A)
print("Reversed array:",end="")
reverseArr(A,0,n)
print(str(A))


