n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k-1]
count = 0

for s in scores:
    if s >= threshold and s > 0:
        count += 1

print(count)
