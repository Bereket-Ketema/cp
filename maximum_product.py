nums=list(map(int,input().split()))
k=int(input())

window=nums[:k]
count=1
value=0
for i in range(k):
    count*=nums[i]
value=max(value,count)
for i in range(1, len(nums) - k+1):
    count /= nums[i-1]
    count *= nums[i + k-1]
    value=max(value,count)

print(value)


