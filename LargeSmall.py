num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


largest = num1
smallest = num1

# Check the second number
if num2 > largest:
    largest = num2
elif num2 < smallest:
    smallest = num2

# Check the third number
if num3 > largest:
    largest = num3
elif num3 < smallest:
    smallest = num3

# Outputs the largest and smallest numbers
print("Largest number is:", largest)
print("Smallest number is:", smallest)
