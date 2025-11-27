k,n,w=map(int,input().split())
count,r=0,0
for i in range(1,w+1):
    count+=k*i
print(count-n) if count-n>0 else print(0)