#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program rolls two dice (d6) until doubles are rolled


import random


def main():
    # This function rolls two dice (d6) until doubles are rolled

    # Function variables
    overall = 0
    repeats = int(input(
                  "Enter the amount of times you want to roll the dice: "))
    print("")

    # Process
    for iteration in range(repeats):

        # Loop variables
        roll_counter = 0
        first_number = 0
        second_number = 1

        while first_number != second_number:
            first_number = random.randint(1, 6)
            second_number = random.randint(1, 6)
            roll_counter = roll_counter + 1
            overall = overall + 1
            print("Your rolls:", first_number, "and", second_number)

        # While loop output
        print("You successfully rolled doubles after", roll_counter,
              "attempts!")
        print("Percentage of rolling doubles per", roll_counter,
              "rolls: {0}%".format(1/roll_counter*100))
        print("")

    # For loop output
    percentage = (iteration/overall)*100
    print("After {0} iterations, the percentage of doubles rolled is {1}%"
          .format(repeats, percentage))


if __name__ == "__main__":
    main()
