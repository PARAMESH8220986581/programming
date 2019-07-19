d,f=map(int,input().split())
a=list(map(int,input().split()))
s=0
if d==len(a):
     for i in range(d):
          if (a[i]==f):
               s+=1
     print(s)
