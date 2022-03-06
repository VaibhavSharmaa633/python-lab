#sum of last three digit of your university roll no.
x=int(input("enter the university roll no"))
a=x%10
x=x//10
b=x%10
x=x//10
c=x%10
sum=a+b+c
print(sum)
