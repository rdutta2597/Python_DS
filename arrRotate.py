def rotate(arr,n):
    t=arr[n-1]
    print(t)
    i=1
    for i in range(n):
        print(arr[i])


n=5
arr=[33,54,88,22,66]
print(rotate(arr,n))