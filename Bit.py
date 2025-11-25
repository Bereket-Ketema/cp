n=int(input())
count=0
for i in range(n):
    c=input()
    if c=="++X" or c=="X++":
        count+=1 
    else:
        count-=1
print(int(count))    