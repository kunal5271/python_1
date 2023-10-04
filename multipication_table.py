#Multipication Table:
#Using For Loop:
i=int(input("Enter The Number:"))
for j in range(1,11):
    print(f'{i} x {j}\t= {i*j}')


#Using While Loop:    
i=int(input("Enter The Number:"))
j=1
while j<11:
    print(f'{i} x {j}\t= {i*j}')
    j+=1