n=int(input())
nums=[1,2,3,4,5]
r,count,k=4,0,0
while n!=k:
    if nums[r]+k<=n:
        k+=nums[r]
        count+=1
    else:
        r-=1
print(count)