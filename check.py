n=19
n=str(n)

def loop(n):
    keep=[]
    while True:
        store=0
        for i in n:
            store+=pow(int(i),2)
        if store==1:
            return True
        elif store not in keep:
            keep.append(store)
            return loop(str(store))
        else:
            return False

print(loop(n))