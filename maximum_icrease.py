n=int(input())
nums=list(map(int,input().split()))
l,r,count,store=0,1,1,[]
while r<n:
    if nums[l]<nums[r]:
      count+=1
    else:
       store.append(count)
       count=1
    if r==n-1:
       store.append(count)
    l+=1;r+=1
if n!=1:
    print(max(store))
else:
   print(1)