def min( arr, n):
    minn = arr[0]
    maxx = arr[0]
    for i in range(n):
        if arr[i] < minn:
            minn = arr[i]
        if arr[i] > maxx:
            maxx = arr[i]
    return minn,maxx
    
n=5
arr=[33,54,88,22,77]
print("Minimum element and maximum element :",min(arr,n))


