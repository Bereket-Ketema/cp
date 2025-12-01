nums=list(map(int,input().split()))
k=int(input())

count=0
store=0
window=nums[:k]
for i in range(k):
    if window[i]%2!=0:
        count+=1
if count>k-count:
    store+=count

for i in range(1, len(nums) - k + 1):
    left = nums[i - 1]
    right = nums[i + k - 1]

    if left % 2 != 0:
        count -= 1

    if right % 2 != 0:
        count += 1

    if count>k-count:
        store+=count

print(store)