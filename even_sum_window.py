nums=list(map(int,input().split()))
k=int(input())

count=0
window=sum(nums[:k])
count+=1 if window%2==0 else None
for i in range(1,len(nums)-k+1):
    window=window-nums[i-1]+nums[i+k-1]
    if window%2==0:
        count+=1 

print(count)