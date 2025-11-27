n=int(input())
num=list(map(int,input().split()))
count=1
for i in range(n):
    print(num.index(count)+1,end=' ')
    count+=1