a=int(input())
z=list(map(int,input().split()))
if a==len(z):
    for i  in range(a):
        print(z[i],i)
