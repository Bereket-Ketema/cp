n=int(input())
nums=[]
count=0
nums=[int(input()) for i in range(n)]
for i in range(n):
  if i!=n-1 and nums[i] !=nums[i+1]:
    count+=1
  if i==n-1:
    count+=1
print(count)