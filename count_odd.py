nums = list(map(int, input().split()))
k = int(input())

count = 0
for i in range(k):
    if nums[i] % 2 != 0:
        count += nums[i]

store = count

# Step 2: slide
for i in range(1, len(nums) - k + 1):
    left = nums[i - 1]
    right = nums[i + k - 1]

    if left % 2 != 0:
        count -= left

    if right % 2 != 0:
        count += right
    store+=count

print(store)
