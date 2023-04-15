from sys import argv
from random import randint


# first_num = int(argv[1])
# last_num = int(argv[2])

def run_guess(first_num, last_num, guess, ans):
    if first_num <= guess <= last_num:
        if ans == guess:
            print("You are a genius")
            return True
    else:
        print(f"Enter a number between {first_num} and {last_num}")


if __name__ == "__main__":
    first_num = 1
    last_num = 2
    ans = randint(first_num, last_num)

    while True:
        try:
            guess = int(input(f"Guess a number {first_num} to {last_num}: "))
            if run_guess(first_num, last_num, guess, ans) is True:
                break
        except ValueError:
            print("Please enter a number")
            continue
