n=input()
c=[]
for i in range(len(n)):
    if n[i].isalpha() and n[i] not in c:
        c.append(n[i])
print(len(c))