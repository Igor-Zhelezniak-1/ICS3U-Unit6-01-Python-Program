#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program generate random numbers

import random


def main():
    # this function generate random numbers
    summ = 0
    random_numbers = []
    print("Starting ...\n")
    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)  # a number between 0 and 100
        random_numbers.append(random_number)

    for loop_counter in range(0, 10):
        print("This is random number: {0}".format(random_numbers[loop_counter]))
        summ = summ + random_numbers[loop_counter]

    average = summ / 10
    print("\nThe average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
