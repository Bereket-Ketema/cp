n=int(input())
count=0
for i in range(n):
    line = input().split()
    check=line.count('1')
    if check>=2:
        count+=1
print(count)