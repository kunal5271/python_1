#write a python program where user will enter time in second display the given time in hour,minutes and seconds:
t=int(input("Enter the time in second:\n"))
h=t//3600
m=(t%3600)//60
s=t%60
print(h,m,s,sep=":")
print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')