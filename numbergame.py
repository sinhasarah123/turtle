import random 
playing= True
number=str(random.randint(10,20))
print("i will generate a number frome 10 to 20 you have to guess it")
print ("if u guess correctly the game will end")
while playing:
    guess=input("Enter your guess:")
    if guess==number:
        print("Congratulations! You guessed the number.")
        playing=False
    else:
        print("Sorry, try again.")