a=int(input())
k=list(map(int,input().split()))
s=0
h=len(k)
for i in range(h):
    s+=k[i]
q=s//h
print(q)
