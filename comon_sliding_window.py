num = list(map(int, input().split()))
k = int(input())

# compute first window sum
window = sum(num[:k])
maxs = window

# slide starting from index 0
for i in range(len(num) - k):
    window = window - num[i] + num[i + k]
    maxs = max(maxs, window)

print(maxs / k)