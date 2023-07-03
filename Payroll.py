#input salary and dependent values 

salary = float(input("Enter the salary: ")) 
numDependents = int(input("Enter the number of dependents: "))

# variables

stateTax = 0.065 * salary
federalTax = 0.28 * salary
dependentDeduction = (0.025 *numDependents) * salary 
takeHomePay = salary - stateTax - federalTax - dependentDeduction

# Calculate stateTax here.

print("State Tax: $" + str(stateTax))

# Calculate federalTax here.

print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.

print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.

# Calculate takeHomePay here.

print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
