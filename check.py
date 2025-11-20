arr=list(map(int,input().split(' ')))
def max_sum(arr,k):

    window=sum(arr[:k])
    maxs=window
    for i in range(len(arr)-k):
        window=window-arr[i]+arr[i+k]
        maxs=max(window,maxs)

    return maxs


# arr = [5, 2, -1, 0, 3]
k = 4
print(max_sum(arr, k))