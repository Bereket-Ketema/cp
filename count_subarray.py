nums=list(map(int,input().split()))
k=int(input())
target=int(input())
count=0

window=sum(nums[:k])
for i in range(len(nums)-k+1):
    if window == target:
        count+=1
    if i + k < len(nums):
        window = window - nums[i] + nums[i+k]
print(count)
