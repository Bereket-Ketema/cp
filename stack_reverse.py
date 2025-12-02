num=input()
store=''
for i in range(len(num)-1,-1,-1):
    store+=num[i]
print(store)