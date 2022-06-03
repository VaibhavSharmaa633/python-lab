#program by function which take a string and convert it into uppercase without using predefine function.
def upper(s):
    a=''
    for i in s:
        a=a+chr(ord(i)-32)
    print(a)
s=input()
upper(s)
