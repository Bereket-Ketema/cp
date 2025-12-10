y="A man, a plan, a canal: Panama"
z=''
for i in y:
    if i.isalpha():
        z+=i.lower()
print(z)