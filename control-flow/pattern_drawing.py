size = int(input("Enter the size of the pattern: "))

i = 0
while i < size:
    # inner loop to print stars in each row
    for j in range(size):
        print("*", end="")
    # Move to the next line after printing each row
    print()
    i += 1
# This code takes an integer input for the size of the pattern and prints a square pattern of asterisks.