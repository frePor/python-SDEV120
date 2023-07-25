"""
    Name: Wally's Training Gym Enrollment Tracker
    Author: Freddie Porter
    Summary: This program sorts each trainer's number of enrollees into Wally's Training Gym into three categories, 0-5 new members, 6-10 new members, and 11-15 new members.
    
    Variables: 
    category_0_to_5 - number of trainers who enrolled 0-5 new members
    category_6_to_10 - number of trainers who enrolled 6-10 new members
    category_11_to_15 - number of trainers who enrolled 11-15 new members
    trainers - list that stores each trainer's name and number of new members they enrolled
    trainer - loop variable that iterates over the list from the 'trainers' variable and represents each trainer's information
    name - used to store the last name of each trainer that is entered by the user
    enrollment - used to store the number of new members enrolled by each trainer
    trainers_enrollments - stores the list of each trainer's enrollment number
"""    

def display_enrollment_categories(trainers):
    category_0_to_5 = 0
    category_6_to_10 = 0
    category_11_to_15 = 0

    for trainer in trainers:
        enrollment = trainer[1]
        if enrollment <= 5:
            category_0_to_5 += 1
        elif enrollment <= 10:
            category_6_to_10 += 1
        elif enrollment <= 15:
            category_11_to_15 += 1

    # Displays the number of trainers in each category
    print("Number of trainers with 0-5 new members:", category_0_to_5)
    print("Number of trainers with 6-10 new members:", category_6_to_10)
    print("Number of trainers with 11-15 new members:", category_11_to_15)


def collect_enrollments():
    trainers = [] #Array containing all trainer's last names

    for i in range(1, 16):
        name = input(f"Enter Trainer {i}'s last name: ") #Prompts user to input last name of trainer up to 15 trainers
        enrollment = int(input(f"Enter the number of new members enrolled by Trainer {i}: ")) #Prompts user to input number of new members enrolled by the trainer that was entered

        trainers.append((name, enrollment)) 

    return trainers


def main():
    print("Welcome to Wally's Training Gym Enrollment Tracker")
    trainers_enrollments = collect_enrollments()
    display_enrollment_categories(trainers_enrollments)


if __name__ == "__main__":
    main()

