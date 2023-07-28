"""
Name: Average Salary Calculator
Author: Freddie Porter
Summary: This program allows the user to input employee names and their salaries as floating-point numbers(in even hundreds). The program then calculates the average of all salaries then idenfities and displays the names and salaries of employees whose salaries are within $5000 of the average.

Variables:
names - a list that stores employee's names
salaries - a list that stores salaries of employees as floating-point numbers
sentinel - string variable used as a sentinel value to signal the end of input from the user
name - takes input from the user to represent employee name
salary - takes input from the user to represent employee salary
total_salary - stores the total salary of all employees
average_salary - stores the average salary of all employees
salary_range - represents the range within which an employee's salary is considered within the average
employees_within_range - list that stores employee's names and their salaries that are within the specified range
"""


def input_salaries():
    names = []
    salaries = []
    sentinel = "done"

    while True:
        name = input("Enter employee name (or 'done' to finish): ")
        if name.lower() == sentinel:
            break

        salary = float(input("Enter employee salary in even hundreds: "))
        names.append(name)
        salaries.append(salary)

    return names, salaries

def calculate_average(salaries):
    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    return average_salary

def find_within_range(names, salaries, average_salary, salary_range=5):
    employees_within_range = []

    for name, salary in zip(names, salaries):
        if abs(salary - average_salary) <= salary_range:
            employees_within_range.append((name, salary))

    return employees_within_range

def display_employees(names, salaries):
    print("\n1. Displaying names and salaries of all employees:")
    for name, salary in zip(names, salaries):
        print(f"{name}: {salary:.1f}")

def display_average(average_salary):
    print("\n2. Average salary of all employees:", average_salary)

def display_within_range(employees_within_range):
    print("\n3. Employees within 5,000 range of the average salary:")
    for name, salary in employees_within_range:
        print(f"{name}: {salary:.1f}")

if __name__ == "__main__":
    print("Enter employee names and salaries. Type 'done' for name when you're finished.")

    # Input salaries and names
    names, salaries = input_salaries()

    # Calculate average salary
    average_salary = calculate_average(salaries)

    # Find employees within the specified range of the average
    employees_within_range = find_within_range(names, salaries, average_salary)

    # Display results
    display_employees(names, salaries)
    display_average(average_salary)
    display_within_range(employees_within_range)