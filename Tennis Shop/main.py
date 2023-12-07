# Variables

balance = 500

items5 = ["$5 Tennis Balls", "$5 Racket Grip", "$5 Shock Absorber"]

items20 = ["$20 Sports Cap", "$20 Tennis Bag"]

items100 = ["$100 Tennis Racket", "$100 Tennis Shoes"]

# Introduce the shop to the user

print("Welcome to Alex's Tennis Shop!")
print(f"Your balance is ${balance}.")

# Functions

# Check the users balance
def checkbal():
    print(f"Your current balance is ${balance}.")

# List the items in the shop
def shop():
    print("Here are the items we have available in our shop:")
    for product5 in items5:
        print(product5 + "\n")
    for product20 in items20:
        print(product20 + "\n")
    for product100 in items100:
        print(product100 + "\n")

# How many
def howMany():
    amount = input("How many?: ")
    if amount.isDigit:
        amount = amount * 5
        print("This item has been added to your cart.")
    else:
        print("Your amount must be a whole number. Please type a valid amount.")

# End the program
def quit():
    print("Thank you for shopping at Alex's Tennis Shop! Please come again!")

# If user wants to shop
def purchasing():
    print("What would you like to buy?")
    purchase = input()
    if purchase in items5:
        howMany()


# Ask the user what they want to do

print("\n" + "Options:" + "\n")
print("1. Browse the shop")
print("2. Check my balance")
print("3. Quit Shopping")

decision = int(input("\nWhat would you like to do? (Please type the number of your choice): "))

# Open the shop

if decision == 1:
    shop()

elif decision == 2:
    checkbal()

elif decision == 3:
    quit()

else:
    print("Please type a valid number for one of the options above.")


