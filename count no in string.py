a=str(input())
s=0
for i in a:
     if i.isdigit():
          s+=1
     else:
          pass
if s>=1:
     print('Yes')
else:
     print("No")
