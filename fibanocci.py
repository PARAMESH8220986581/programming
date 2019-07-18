m=int(input("enter"))
first=1
second=1
for i in range(m):
    print(first, end=" ")
    temp=first
    first=second
    second=first+temp
