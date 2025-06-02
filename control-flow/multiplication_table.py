number = int(input("Enter a number to see its multiplication table:"))

for i in range(1,11):
    result = number * i
    print(f"{number} x {i} = {result}")
# This code takes a number as input and prints its multiplication table from 1 to 10.
# It uses a for loop to iterate through the numbers 1 to 10, multiplying each by the input number and printing the result in a formatted string.