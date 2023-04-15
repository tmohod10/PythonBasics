from sys import argv
from random import randint

first_num = int(argv[1])
last_num = int(argv[2])
answer = randint(first_num, last_num)

while True:
    try:
        guess = int(input(f"Guess a number {first_num} to {last_num}: "))
        if first_num <= guess <= last_num:
            if answer == guess:
                print("You are a genius")
                break
            else:
                print("Try again")
        else:
            print(f"Enter a number between {first_num} and {last_num}")
    except ValueError:
        print("Please enter a number")
        continue
