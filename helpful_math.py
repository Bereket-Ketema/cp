maths=input()
num=[]
for i in range(0,len(maths),2):
    num.append(maths[i])
num.sort()
for i in range(len(num)):
    if len(num)>1 and i!=len(num)-1:
        print(num[i] +"+",end='')  
    elif len(num)==1 or i==len(num)-1:
        print(num[i])