#!/uer/bin/env python

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print ("guess the number!")

x = random.randint(1,100)
guess = None

while x != guess:

     guess = int(input("pick a number between 1 to 100: "))

     if x ==guess:
        print("you genius!")
     elif x > guess:
        print("try a bigger number.")
     elif x < guess:
        print("try a small number.")
main()

    