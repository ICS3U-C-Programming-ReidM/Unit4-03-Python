#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program calculates the power of two of a positive integer


while True:
    user_num = input("Enter a whole number: ")

    if user_num.lstrip("-").isdigit():
        user_num = int(user_num)

        if user_num >= 0:
            for i in range(user_num + 1):
                print(f"{i}*2 = {i * i}")
            break
        else:
            print(f"{user_num} is not positive.")
    else:
        print(f"{user_num} is not an integer.")
