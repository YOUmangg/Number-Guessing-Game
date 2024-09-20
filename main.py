import numpy as np
import time
import random
from playsound import playsound
import winsound

#next update, add time elapsed. //time.time() includes sleeping time, publish alternative in next one.
#Check for the path for sounds. It's local specific atm
#Check for more exceptions in input. 

def calc(a, b):
    return np.log2(b - a) + 1 
    # +1 because a and b are also included in the list of possible selections.

def ask():
    print("Do you want to play another game? Enter Yes or No")
    decision = input()
    return decision

def check_for_valid_input(a, b):  #considering only one edge case as of now, where a == b
    if(a == b):
        return False
    else:
        return True

decision = "Yes"
while(decision == "Yes"):
    # Description of the game:
    start_time = time.time()
    print("Give me 2 numbers (enter separated). I will select a number from between these 2 numbers, inclusive of the numbers. I will give you some amount of chances to guess the number I have selected. For each number you guess, I will tell you if the number you have guessed is greater than or less than the number I have selected.")
    
    time.sleep(0.5)

    print("Welcome to the game of guessing the number! Please enter the numbers range in which you want me to guess a number: ")

    while(True):
        a = int(input())
        b = int(input())
        if(check_for_valid_input(a, b) == True):
            break
        else: 
            print("Enter valid numbers, please. Input again")

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
            end_time = time.time()
            print("Congratulations! You guessed the number in ", guesses_made, "tries")
            print("You took {} seconds to complete the game.".format(round((end_time - start_time), 2)))
            try:
                playsound(r'Projects\Number-Guessing-Game\sounds\WinSound.wav')
            except:
                print("Unable to play audio at the moment. Sorry!")
            decision = ask()
            break  
        else:
            if(guesses_made == chances):
                end_time = time.time()
                print("Sorry, you lost the game. The number I had chosen was: ", num_to_guess)
                print("You took {} seconds to complete the game.".format(round((end_time - start_time), 2)))
                try:
                    playsound(r'Projects\Number-Guessing-Game\sounds\LossSound.wav')
                except:
                    print("Unable to play audio at the moment. Sorry!")
                print("Better luck next time!")
                decision = ask()
                break
            elif(guess > num_to_guess):
                winsound.MB_ICONEXCLAMATION  
                print("Your guess is greater than the number. You have ", chances - guesses_made, "chances remaining.")
            else:
                winsound.MB_ICONEXCLAMATION
                print("Your guess is less than the number. You have ", chances - guesses_made, "chances remaining.")

print("Thank you for playing the game. See you next time!")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)