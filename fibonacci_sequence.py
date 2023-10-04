# #Fibonacci Series:
# '''Write a program that genereates and prints the first n terms of the Fibonacci series using the while loop.'''
n=int(input())
a=0
b=1
print(a,b,end=' ')
while n-2>0:
    c=a+b
    print(c,end=' ')
    a,b=b,c
    n-=1

