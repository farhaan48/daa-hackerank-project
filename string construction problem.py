# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xKX-BynQx5bHaWpt7I2jMy5WB0jw3_HT
"""

def stringConstruction(s):
    return len(set(s))

def main():
    print("String Construction Cost Calculator")
    print("-----------------------------------")

    # Input the number of test cases
    while True:
        try:
            n = int(input("Enter the number of test cases: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(f"\nEnter {n} strings, one per line:")

    # Process each test case
    for i in range(n):
        s = input().strip()
        cost = stringConstruction(s)
        print(cost)

if __name__ == "__main__":
    main()