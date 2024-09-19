import numpy as np
import time
import random
from playsound import playsound
import winsound

def calc(a, b):
    return np.log2(b - a) + 1 
    # +1 because a and b are also included in the list of possible selections.

def ask():
    print("Do you want to play another game? Enter Yes or No")
    decision = input()
    return decision


decision = "Yes"
while(decision == "Yes"):
    # Description of the game:
    print("Give me 2 numbers (enter separated). I will select a number from between these 2 numbers, inclusive of the numbers. I will give you some amount of chances to guess the number I have selected. For each number you guess, I will tell you if the number you have guessed is greater than or less than the number I have selected.")
    
    time.sleep(0.5)

    print("Welcome to the game of guessing the number! Please enter the numbers range in which you want me to guess a number: ")

    a = int(input())
    b = int(input())

    print(f'Thank you for the giving me the range of the numbers. I have selected \n a number between {a} and {b}.')
    d = calc(a, b)
    print(f"According to my calculations, you can guess the number in {int(d)} times if you play optimally.")
    time.sleep(2)
    print("It's your turn now! Try guessing the number: ")

    num_to_guess = random.randint(a, b)

    chances = int(d)

    guesses_made = 0

    while(guesses_made < chances):
        guess = int(input())
        guesses_made += 1
        if(guess == num_to_guess):
            print("Congratulations! You guessed the number in ", guesses_made, "tries")
            playsound('./sounds/WinSound.wav')
            decision = ask()
            break  
        else:
            if(guesses_made == chances):
                print("Sorry, you lost the game. The number I had chosen was: ", num_to_guess)
                playsound('./sounds/LossSound.wav')
                print("Better luck next time!")
                decision = ask()
                break
            elif(guess > num_to_guess):
                winsound.Beep(5000, 1000)  
                print("Your guess is greater than the number. You have ", chances - guesses_made, "chances remaining.")
            else:
                winsound.Beep(5000, 1000)  
                print("Your guess is less than the number. You have ", chances - guesses_made, "chances remaining.")

print("Thank you for playing the game. See you next time!")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)