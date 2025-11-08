n = list(map(int, input("Enter a list of numbers: ").split()))
l,r=0,1
count=0
while r<len(n):
    if n[l]>n[r]:
        count+=1
    l+=1
    r+=1
if len(n)==1 or n[0]:
    print("True")
if count>1:
    print('False')
