n=list(map(int,input().split()))
k=int(input())
window=n[:k]

l=0
count=0
store=[]
for i in range(1,len(n)-k+1):
    while l<k:
        if window[l]%2==0:
            count+=1
        l+=1
    store.append(count)
    count=0;l=0
    window.pop(0)
    window.append(n[i+k-1])
print(store)
