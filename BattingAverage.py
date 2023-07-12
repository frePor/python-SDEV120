# Declare a named constant for array size here.
MAX_AVERAGES = 8

# Declare array here.
battingAverageList = []

# Write a loop to get batting averages from the user and assign them to the array.
for i in range(MAX_AVERAGES):
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    battingAverageList.append(battingAverage)

# Assign the first element in the array to be the minimum and the maximum.
minAverage = battingAverageList[0]
maxAverage = battingAverageList[0]
# Start out your total with the value of the first element in the array.
total = battingAverageList[0]

# Write a loop here to access array values starting with battingAverageList[1]
for i in range(1, MAX_AVERAGES):
    average = battingAverageList[i]

    # Within the loop, test for minimum and maximum batting averages.
    if average < minAverage:
        minAverage = average
    if average > maxAverage:
        maxAverage = average

    # Also accumulate a total of all batting averages.
    total += average

# Calculate the average of the 8 batting averages.
average = total / MAX_AVERAGES

# Print the batting averages stored in the battingAverageList array.
print("Batting averages:", battingAverageList)

# Print the maximum batting average, minimum batting average, and average batting average.
print("Maximum batting average:", maxAverage)
print("Minimum batting average:", minAverage)
print("Mean batting average:", average)