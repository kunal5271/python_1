#Prime Number Checker:
n=int(input("Enter the number:"))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")