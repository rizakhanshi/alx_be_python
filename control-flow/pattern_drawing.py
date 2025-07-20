# pattern_drawing.py
# This script draws a square pattern of asterisks using nested loops.

size = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
