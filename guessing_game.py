#! /usr/bin/python3
import random
def guess_loop ():
    number_to_guess = random.randint(1, 100)
    try_count = 0
    print("I have in mind a number in between 1 and 100, can you findit?")
    while True:
            try:
                guess = int(input())
                if guess > number_to_guess:
                    print("The number to guess is lower")
                    try_count += 1
                elif guess < number_to_guess:
                    print("The number to guess is higher")
                    try_count += 1
                else:
                    print("You just found the number , it was indeed",guess)
                    print(f'With {try_count} try')
                    return
            except ValueError as err:
                print("Invalid input , please enter an integer")
guess_loop()
