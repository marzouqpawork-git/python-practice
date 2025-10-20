import random
num= random.randint(1,10)
guess=0
while guess != num:
    guess=int(input("Guess a number between 1to10: "))
    if guess<num:
        print("Too Low")
    elif guess>num:
        print("Too High")
    else:
        print("You have guessed the number successfully!!!")