nums=list(map(int,input().split()))
k=int(input())

count=0
store=[]
window=nums[:k]
for i in range(k):
    if window[i]%2 !=0:
        count+=window[i]
    store.append(count)
for i in range(1,len(nums)-k+1):
    left=nums[i-1]
    right=nums[i+k-1]
    if left%2!=0:
        count-=left
    if right%2!=0:
        count+=right
    store.append(count)

print(max(store))