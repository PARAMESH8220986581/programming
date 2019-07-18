a=str(input())
s=0
for i in a:
    if i.isdigit():
        pass
    elif i.isalpha():
        pass
    elif i.isspace():
        pass
    else:
        s+=1
print(s)
