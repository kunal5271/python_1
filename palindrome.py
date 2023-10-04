#Palindrome Checker:
n=int(input())
r=0
s=0
check=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if check==s:
    print("palindrome")
else:
    print("not palindrome")

    