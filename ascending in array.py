a=int(input())
b=list(map(int,input().split()))
if (len(b)==a):
    b.sort()
    for i in range(a):
        print(b[i], end=" ")
