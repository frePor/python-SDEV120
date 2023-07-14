# JumpinJava.py - This program looks up and prints the names and prices of coffee orders.  
# Input:  Interactive
# Output:  Name and price of coffee orders or error message if add-in is not found 

# Declare variables.
NUM_ITEMS = 5 # Named constant

# Initialized list of add-ins
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices
addInPrices = [.89, .25, .59, 1.50, 1.75]
foundIt = False # Flag variable
orderTotal = 2.00  # All orders start with a 2.00 charge
addIn = ""
while addIn != "XXX":
# Get user input
    addIn = input("Enter coffee add-in or XXX to quit: ")
    if addIn in addIns:
        foundIt = True
        index = addIns.index(addIn)
        print(addIn+" Price is $ "+str(addInPrices[index]))
        orderTotal += addInPrices[index]
    else:
        print("Sorry we do not carry that.")
# Write the rest of the program here.
print("Order Total is $"+str(orderTotal))
