n=int(input())
s,r="I hate ",'it'
n-=1
for i in range(n):
    s+='that I love ' if i%2==0 else 'that I hate '
print(s+r)