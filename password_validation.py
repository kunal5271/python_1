#Password Validation:
'''Implement a program that asks for a password and keep asking until the correct password is entered. Use a while loop for this'''
password='Kunal'
n=input("Enter your password")
while True:
    if password==n:
        print("Welcome")
        break
    else:
        print("Wrong password ,try again")
        n=input("Enter your new password")