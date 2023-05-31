##############################################################
# Name:          ICTPRG302 assignment task
# Purpose:       Employee Hour Tracker
# Author:        Patrick Tracey
# Licence:       Creative Commons
# Created:       02/05/2023 < created
# Last Modified: 04/05/2023 < last updated
# Version    1.0.0
#------------------------------------------------------------

#create a main menu for users to select what they are going to do
def main_menu():

    while True:
        option = None

        print("""======================
====== MAIN MENU =====
1 - Enter Hours Worked
2 - Produce Employee Hours Worked Report

9 - Exit The Application
----------------------""")
        options = input("Enter your menu choice: ")
        print("----------------------")

        if options == '1':
            enter_daily_hours_worked()
        elif options == '2':
            produce_employee_hours_worked()
        elif options == '9':
            print("Exiting the application...")

            break
        else:
            print("Invalid option. Please enter a number from the Menu Options.")


## ---> END of MAIN MENU <---

##allow users to enter their info and hours so that it can be stored on employee_data.txt
def enter_daily_hours_worked():

    employees = []

    with open('employee_data.txt', 'a') as file:
        # Get employee data from user input
        print("\nEnter data for Employee:")
        while True:
            try:
                week_num = input("Enter week number: ")
                float(week_num)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                emp_id = input("Employee ID: ")
                float(emp_id)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        emp_name = input("Employee Name: ")
        hours_worked = []
        for j, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):
            while True:
                try:
                    daily_hours = float(input(f"Enter the number of hours worked on {day}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            hours_worked.append(daily_hours)

        # Store employee data in a dictionary and write to file
        emp_data = {'Week Number': week_num,
                    'ID': emp_id,
                    'Name': emp_name,
                    'Hours Worked': hours_worked}
        employees.append(emp_data)

        file.write(f"Week Number: {emp_data['Week Number']}\n")
        file.write(f"Employee ID: {emp_data['ID']}\n")
        file.write(f"Employee Name: {emp_data['Name']}\n")
        file.write("Hours Worked:\n")
        for j, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):
            file.write(f"\t{day}: {emp_data['Hours Worked'][j]}\n")

    # Print employee records and custom messages based on hours worked
    print("\nEmployee records:")
    for emp in employees:
        print(f"\nWeek Number: {emp['Week Number']}")
        print(f"Employee ID: {emp['ID']}")
        print(f"Employee Name: {emp['Name']}")
        print("Hours Worked:")

        #Custom message for how many hours they work each day
        for j, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):
            if emp['Hours Worked'][j] < 4:
                print(f"\tInsufficient hours worked on {day}.")
            elif emp['Hours Worked'][j] > 10:
                print(f"\tToo many hours worked on {day}.")
            else:
                print(f"\t{day}: {emp['Hours Worked'][j]} hours worked. Good job!")

## Make a custom message for how much they worked in the whole week
        total_hours = sum(emp['Hours Worked'])
        if total_hours < 30:
            print("\n\t\tYou didn’t do enough work this week\n")

        elif total_hours >= 20 and total_hours < 30:
            print("\n\t\tYou have worked a decent number of hours this week.\n")

        else:
            print("\n\t\tYou are working too hard!!\n")

## Store the total_hours worked for the employee in a new text file
        with open('employee_total_hours.txt', 'a') as file:
            file.write(f'Employee {emp_id}: {total_hours}\n')

# produce a report that show the total hours each employee has work
# and how many employees have worked too little or too much
def produce_employee_hours_worked():
    total_hours = {}
    little = 0
    much = 0
    enough = 0
    with open('employee_total_hours.txt', 'r') as file:
        for line in file:
            emp_id, hours = line.split(':')
            total_hours[emp_id.strip()] = float(hours.strip())

    # Print total hours worked by each employee
    for emp_id, hours in total_hours.items():
        print(f"{emp_id}: {hours} hours worked")

    # Calculate number of employees who worked too little or too much
    for hours in total_hours.values():
        if hours < 30:
            little += 1
        elif hours > 40:
            much += 1
        elif 37 <= hours <= 39:
            enough += 1

    print(f"{little} employees worked less than 30 hours this week")
    print(f"{much} employees worked more than 40 hours this week")
    print(f"{enough} employees worked between 37 and 39 hours this week")





main_menu()
