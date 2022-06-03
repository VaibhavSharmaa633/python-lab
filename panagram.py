s1=input()
s2='abcdefghijklmnopqrstuvwxyz'
c=0
for i in s2:
    if i in s1:
        c=c+1
if c==26:
    print("panagram")
else:
    print("not")
