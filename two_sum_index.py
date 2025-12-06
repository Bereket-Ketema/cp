num=list(map(int,input().split()))
target=int(input())
def work(num,target):
    l,r=0,len(num)-1
    while l<r:
        if num[l]+num[r]==target:
            return num.index(num[l]), num.index(num[r])
        elif num[l]+num[r]<target:
            l+=1
        else:
            r-=1
print(work(num,target))
