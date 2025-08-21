import random 
while True:
    user=input("enter 'rock', 'paper' or 'scissors': ")
    computer=random.choice(['rock', 'paper', 'scissors'])
    if user==computer:
        print("It's a tie!")
    elif (user=='rock' and computer=='scissors') or (user=='paper' and computer=='rock') or (user=='scissors' and computer=='paper'):
        print("You win!")
    else:
        print("You lose!")