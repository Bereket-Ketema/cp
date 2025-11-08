n=input("Enter a list of numbers: ").split(' ')
l,r=0,1
while r<len(n):
    if n[l]<=n[r]:
        l+=1
        if r==len(n)-1:
            print("True")
        r+=1
    else:
        print("False")
        break
if len(n)==1:
    print("True")