st=input("Enter the string:")
al=''

# for i in st:
#     if 'a'<=i<='z' or 'A'<=i<='Z':
#         al+=i
# print(al)

for i in st:
    if i.isalpha():
        al+=i
print(al)