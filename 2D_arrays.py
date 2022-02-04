#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Feb 2022
# This program uses a 2D array

import random


def sum_of_numbers(passed_in_2D_list):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("Enter the amount of rows: "))
    columns = int(input("Enter the amount of columns: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 10)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    sum = sum_of_numbers(a_2d_list)
    print("The sum of all the numbers is: {0} ".format(sum))


if __name__ == "__main__":
    main()
