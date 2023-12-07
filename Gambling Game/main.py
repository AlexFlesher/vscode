# Import

import random
import math

# Variables

balance = 100

# Functions

#-------------------------------------------------------------------------------------------------------------------------------------

def mainScreen():
    print("\nWelcome to the Casino! Here we have various games for you to bet money on.")
    print(f"\nYour current balance is ${balance}.")

    print("\nWhat game would you like to play?")
    print("1. Dice Roll")
    print("2. Coin Flip")
    print("3. Guess and Gain")

def diceRollGame():
    global balance

    while True:
        print("What would you like to do?")
        print("1. How to play")
        print("2. Play the game")
        print("3. Go back to game selection")
        diceRollOption = input("Please type the number of the option you wish to select: ")

        if diceRollOption == '1':
            print("\n----------------------------------------------------------------------------------------------------------------\n")
            print("Here is how to play:")
            print("A 6 sided dice is rolled. You will then be asked to guess the number in which the dice landed on.")
            print("If your guess is correct, then your bet is doubled.")
            print("If your guess is one away, then you keep your bet.")
            print("If your guess is 2 or more away, then you lose your bet.")
            print("\n----------------------------------------------------------------------------------------------------------------\n")

        elif diceRollOption == '2':
            while True:
                while True:
                    try:
                        betAmount = int(input("\nHow much do you want to bet? $"))
                        break
                    except ValueError:
                        print("Please type a valid bet amount.")

                if betAmount > balance:
                    print(f"You only have ${balance} remaining.")
                    continue

                num = random.randint(1, 6)
                print("\nA dice has been rolled.")
                while True:
                    try:
                        diceGuess = int(input("What number did the dice land on? "))
                        break
                    except ValueError:
                        print("\nPlease type a valid guess (1-6).")

                if diceGuess == num:
                    print(f"\nCorrect! The dice landed on {num}! You recieved ${betAmount*2}.")
                    balance = balance + betAmount*2
                    

                elif diceGuess == num - 1 or diceGuess == num + 1:
                    print(f"\nClose one! The dice landed on {num}. Your recieved ${betAmount}.")
                    balance = balance + betAmount
                    

                else:
                    print(f"\nSorry, the dice landed on {num}. You lost ${betAmount}.")
                    balance = balance - betAmount
                    
                playdiceRollGameAgain = input("Do you want to play again? (yes/no): ").lower()
                if playdiceRollGameAgain != "yes" and playdiceRollGameAgain != "y":
                    mainScreen()
                    return

        elif diceRollOption == '3':
            mainScreen()
            return

        else:
            print("\nInvalid option. Please enter a valid number.\n")

def coinFlipGame():
    global balance 

    while True:
        print("\nWhat would you like to do?")
        print("1. How to play")
        print("2. Play the game")
        print("3. Go back to game selection")
        coinFlipGameOption = input("Please type the number of the option you wish to select: ")

        if coinFlipGameOption == '1':
            print("\n----------------------------------------------------------------------------------------------------------------\n")
            print("Here is how to play:")
            print("A coin will be flipped.")
            print("If you pick the side that the coin lands on correctly, then your bet will be doubled.")
            print("If you pick the side incorrectly, then you lose your bet.")
            print("\n----------------------------------------------------------------------------------------------------------------\n")

        elif coinFlipGameOption == '2':
            while True:
                while True:
                    try:
                        betAmount = int(input("How much do you want to bet? $"))
                        break
                    except ValueError:
                        print("Please type a valid bet amount.")

                if betAmount > balance:
                    print(f"You only have ${balance} remaining.")
                    continue

                num = random.randint(1, 2)
                if num == 1:
                    coinSide = "HEADS"
                elif num == 2:
                    coinSide = "TAILS"

                print("A coin has been flipped.")

                coinFlipChoice = input("What side has the coin landed on, Heads or Tails? ").upper()

                if coinFlipChoice == "H":
                    coinFlipChoice = "HEADS"
                elif coinFlipChoice == "T":
                    coinFlipChoice = "TAILS"

                if coinFlipChoice == coinSide:
                    print(f"Correct! The coin landed on {coinSide}! You recieved ${betAmount*2}.")
                    balance = balance + betAmount*2
                    
                else:
                    print(f"Sorry, the coin landed on {coinSide}. You lose ${betAmount}.")
                    balance = balance - betAmount

                playCoinFlipGameAgain = input("Do you want to play again? (yes/no): ").lower()
                if playCoinFlipGameAgain != "yes" and playCoinFlipGameAgain != "y":
                    mainScreen()
                    return

        elif coinFlipGameOption == '3':
            mainScreen()
            return

        else:
            print("Invalid option. Please enter a valid number.\n")
    
def guessGainGame():
    global balance 

    while True:
        print("\nWhat would you like to do?")
        print("1. How to play")
        print("2. Play the game")
        print("3. Go back to game selection")
        guessGainGameOption = input("Please type the number of the option you wish to select: ")

        if guessGainGameOption == '1':
            print("\n----------------------------------------------------------------------------------------------------------------\n")
            print("Here is how to play:")
            print("A number will be selected at random from 1-10")
            print("If you guess a number that isnt the one selected, you gain 10 percent of your bet.")
            print("You may make as many guesses as you want, and back out any time you want.")
            print("If you back out before guessing the selected number, you win the money you have gained so far.")
            print("However, if you guess the selected number, you gain nothing and lose the amount you bet.")
            print("\n----------------------------------------------------------------------------------------------------------------\n")

        elif guessGainGameOption == '2':
            while True:
                while True:
                    try:
                        betAmount = int(input("\nHow much do you want to bet? $"))
                        break
                    except ValueError:
                        print("Please type a valid bet amount.")

                if betAmount > balance:
                    print(f"You only have ${balance} remaining.")
                    continue

                num = random.randint(1, 10)
                print("\nA number has been selected.")

                totalEarnings = 0
                numGuesses = 0

                while True:
                    while True:
                        try:
                            userGuess = int(input("\nWhat number would you like to guess? "))
                            if userGuess >= 1 and userGuess <= 10:
                                break
                            else:
                                print("You must guess a number between 1 and 10.")

                        except ValueError:
                            print("Please enter a valid number.")
                        
                    roundEarnings = math.ceil(betAmount / 10)
                        
                    if userGuess == num:
                        print(f"\nOh no! You guessed the selected number. You have lost ${betAmount}.")
                        balance = balance - betAmount - totalEarnings
                        playGuessGainGameAgain = input("Would you like to play again? (yes/no): ").lower()

                        if playGuessGainGameAgain != "yes" and playGuessGainGameAgain != "y":
                            mainScreen()
                            return
                        else:
                            break

                    else:
                        print(f"\n{userGuess} was not the selected number. You have gained ${roundEarnings}")
                        balance = balance + roundEarnings
                        numGuesses = numGuesses + 1
                        totalEarnings = roundEarnings * numGuesses
                            
                        gameNextRound = input("Would you like to keep guessing? (yes/no): ")
                        if gameNextRound != "yes" and gameNextRound != "y":
                            print(f"You earned a total of ${totalEarnings}.")
                            mainScreen()
                            return
                        else:
                            continue
                        

        elif guessGainGameOption == '3':
            mainScreen()
            return
        
        else:
            print("Invalid option. Please enter a valid number.\n")

# End of game functions

#-------------------------------------------------------------------------------------------------------------------------------------

mainScreen()

while True:
    gameSelection = input("Please type the number of the game you wish to play: ")
    if gameSelection == '1':
        print("\n")
        diceRollGame()

    elif gameSelection == '2':
        print("\n")
        coinFlipGame()

    elif gameSelection == '3':
        print("\n")
        guessGainGame()

    else:
        print("Please type a valid number (1-3)")

