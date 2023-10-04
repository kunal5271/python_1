#Frequency of character in string:

"""
st= input('Enter the string:\n')
ch= input("Enter the character to count:\n")
count=0
for i in st:
    if i==ch :
        count+=1
print(count)

"""
#Frequency of all character in given string:

st= input('Enter the string:\n')
reg=''
for x in st:
    count=0
    if x not in reg:
        for i in st:
            if i == x :
                count+=1
        print(x,":",count)
        reg+=x    