# Michael Carr
# Programing Assignment 3
# MIS 301
# 03-20-2024

# Generates the slots
import random
def spin_slots(coins):
    slot1 = random.randint(0,9)
    slot2 = random.randint(0,9)
    slot3 = random.randint(0,9)
# Generates the machine
    print(" _=========_")
    print("|#|~-~-~-~|#|")
    print("|#|" + " " + str(slot1) + " " + str(slot2) + " " + str(slot3) + " " + "|#|" + "   0") 
    print("|#|~-~-~-~|#|  /")
    print("============= []")
# Uses a coin per spin
    coins -= 1 
# Winning conditions: JACKPOT and Match
    if slot1 == slot2 and slot2 == slot3:
        print("JACKPOT!")
        coins += 10
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("Nice Match!")
        coins += 3
    print("You have " + str(coins) + " tokens left!")
    return coins 
# Runs main
def main():
# Getting starting coins and checking value
    int_is_valid = False
    while not int_is_valid:
        try:
            coins = input("how many tokens are you starting with? ")
            coins = int(coins)
            int_is_valid = coins > 0
        except ValueError:
            print("Please input an integer greater than 0!")
# Spin slots until user decides to quit 
        user_input = input("Press carriage return to spin the slots, or type any other character to quit!")
        while user_input == "":
            if coins < 1:
                print("Sorry, you are out of coins")
                quit()
            coins = spin_slots(coins)
            user_input = input("Press carriage to spin the slots, or type any other character to quit!")
            print("You left with " + str(coins) + " tokens!")
        quit() 
# Starts program
main()
