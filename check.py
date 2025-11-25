n=int(input())
s="I hate "
r='it'
n=n-1
for i in range(n):
    if i%2==0:
      s+='that I love '
    else:
       s+='that I hate '
print(s+r)