from statistics import median
a=int(input())
b=list(map(int,input().split()))
if (len(b)==a):
    b.sort()
    print(median(b))
    
