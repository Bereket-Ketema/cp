n =  list(input("Enter a list of vowels: "))
l,r=0,len(n)-1
v=set(['a','e','i','o','u','A','E','I','O','U'])
while l<r:
    if n[l] not in v:
        l+=1
    if n[r] not in v:
        r-=1
    if n[l] in v and n[r] in v:
        n[l],n[r]=n[r],n[l]
        l+=1
        r-=1
print("".join(n))