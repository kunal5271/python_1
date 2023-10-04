#Countdown Timer:
'''Write a program that takes an integer input from the user and counts downs from that number to 1 using the while loop.'''

import time
a=int(input("Enter a number"))

while a>0:
    print(a)
    a=a-1
    time.sleep(1)
print('stop')