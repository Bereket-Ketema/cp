n=list(map(int,input().split()))
n.sort()
print("check again") if(max(n)-min(n)>=10) else print("final"+" "+str(n[1]))
