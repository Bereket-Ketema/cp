n=int(input())
num=list(map(int,input().split()))
count=0
for i in range(n):
    count+=num[i]

print(float(count)/n)