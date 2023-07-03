"""
HouseSign.py - This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0    # Charge for this sign.
numChars = 8    # Number of characters.
color = "gold"    # Color of characters.
woodType = "oak"    # Type of wood.

# Write assignment and if statements here as appropriate.
charge = 35.00

#Additional charge for number of characters
if numChars > 5:
    additionalChars=numChars-5
    charge +=additionalChars*4

#Charge for type of wood
if woodType=="oak":
    charge+=20.00

#Charge for gold-leaf lettering
if color=="gold":
    charge+=15.00


# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))