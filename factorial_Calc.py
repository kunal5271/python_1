#Factorial Calculation:
'''Write the program that calculates the factorial of the given positive integer using the while loop'''
a=int(input("enter the number:"))
fact=1
while a>0: 
    fact=fact*a
    a=a-1
print(fact)
