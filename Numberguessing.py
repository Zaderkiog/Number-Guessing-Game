import random
import os


clear = lambda: os.system('cls')

def number_to_guess():
    number = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
    return random.choice(number)

def user_guess(user_choice, number):
     
     if user_choice == number:
         print("You win!")
     else:
         print("You loose!")

def user_input():
    print("Welcome, this is a guessing game.")
    print("Please, choose any number between 1 and 10. You'll have tree chances to guess it")
    user_number = int(input("Enter your answer: "))
    while user_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("The number isn't in the range")
        user_number = int(input("Enter your answer: "))
    return user_number

def play(lives):
    number = number_to_guess()
    userchoice = user_input()
    user_guess(userchoice, number)
    print(f"The number was {number}")

    if userchoice != number:
        lives = lives - 1
        if lives > 0:
            print("Try again!")
            play(lives)
        elif lives == 0:
            clear()
            print("You spent your chances!")

initial_lives = 3
play(initial_lives)