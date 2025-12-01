nums = list(map(int, input().split()))
k = int(input())

store = 0

for i in range(len(nums) - k + 1):
    window = nums[i:i+k]
    store += min(window)

print(store)
