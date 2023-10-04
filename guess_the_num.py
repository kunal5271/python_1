#Guess the number:
import random
comp_num=random.randrange(1,101)
score=10

while True:
    user_num=int(input("Guess The Number between 1 and 100:"))
    if user_num == comp_num:
        print("You Win!",score)
        break
    elif user_num < comp_num:
        print("Too Small")
    else:
        print("Too large")
    score=score-1        
        