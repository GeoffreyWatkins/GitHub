import datetime
from datetime import datetime
import os
# imported the required modules
username = input("Enter your username: ")
password = input("Enter your password: ")
# defined the username and password variables

def login(username, password):
    with open("user.txt", "r+") as f:
        data = f.readlines()
    valid = False

    while not valid:

        for user in data:
            user = user.split(", ")

            if user[0] == username and user[1].strip() == password:
                valid = True
                menu(username)

        if not valid:
            print("Invalid credentials!\n")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
    menu(username)
# defined function for login and set parameters accordingly
def menu(username):
    if username == "admin":

        print("Please select one of the following options:")
        print('''
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        ''')
    else:
        print("Please select one of the following options:")
        print('''
    a - add task
    va - view all tasks
    vm - view my tasks    
    e - exit
    ''')
# made a menu function that displays alternate menu for the normal user and the admin alike
    choice = input("enter your choice: ")

    run_menu(username, choice)


def run_menu(username, choice):
    if choice == "r" and username == "admin":
        register(username)
    elif choice == "a":
        add_task(username)
    elif choice == "va":
        view_all(username)
    elif choice == "vm":
        print()
        view_mine(username)
    elif choice == "gr" and username == "admin":
        generate_reports(username)
    elif choice == "ds" and username == "admin":
        display_statistics(username)
    elif choice == "e":
        exitt()
    else:
        print("invalid choice please try again\n")
        menu(username)
# and then the run_menu is used when the user makes a choice and the assosiated function is executed for that selection

def register(username):
    if username == "admin":

        users = open("user.txt", "r").readlines()
        existing_usernames = [user.split(", ")[0] for user in users]

        with open("user.txt", "a+") as f:
            valid = False
            new_username = input("Enter new username here: ")
            while new_username in existing_usernames:
                new_username = input("That username already exists!\nEnter new username here: ")
            password = input("Enter your new password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                print("registered")

                f.write(f"\n{new_username}, {password}")
                f.close()
                return menu(username)

            else:
                print("Passwords do not match")
                register(username)

    else:
        print("Your not allowed register")
        menu(username)
# the register function is there for the admin to create new users as well as to check if a user has been added before

def add_task(username):
    with open("tasks.txt", "a+") as f:
        task_username = input("enter task username: ")
        task_name = input("enter task name: ")
        task_desc = input("enter task description: ")
        task_year = input("enter year number here: ")
        task_month = input("enter month here (Format Example) - Jan: ")
        task_day = input("enter day here: ")
        due_date = f"{task_day} {task_month} {task_year}"
        completed = "No"
        f.write(
            f"\n{task_username}, {task_name}, {task_desc}, {datetime.now().strftime('%d %b %Y')}, {due_date}, {completed}")
        print("Task added successfully")

    menu(username)
# the add task function was made to be able to add new task to the program if so was needed
# asked for all the details and stored it accordingly

def view_all(username):
    with open("tasks.txt", "r+") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(",")
            print("assign to: ", line[0])
            print("task  name: ", line[1])
            print("task description: ", line[2])
            print("due date: ", line[3])
            print("completed:", line[4])

            print("==============")

    menu(username)
# this function is there so that the user can see all of the tasks and see to whom they are assigned to

def view_mine(username):
    tasks = []
    old_tasks = open("tasks.txt", "r").readlines()
# this function is to be used by the user in order to check and edit it if they were so inclined
    with open("tasks.txt", "r+") as f:
        lines = f.readlines()
        # Printing the tasks
        task_number = 0
        for line in lines:
            if line.startswith(username):
                task_number += 1
                tasks.append(line)
                line = line.strip().split(",")
                print(f"{task_number}) Title: {line[1]}")
                print("\tassign to: ", line[0])
                print("\ttask description: ", line[2])
                print("\tdue date: ", line[4])
                print("\tcompleted:", line[5])
                print("==============")
    task_number = int(input("Would you like to edit a task?\nEnter task number to edit (-1 to exit): "))
    if task_number != -1:
        # Change Task only if the task is not already completed
        task_data = tasks[task_number - 1].strip("\n").split(", ")
        if task_data[-1] == "No":
            user_choice = input(
                "Select an option:\n1) Mark as complete\n2) Change Assignee\n3) Edit task due date\n4) Exit\n: ")
            # Get the users input and change the needed field otherwise exit
            if user_choice == "1":
                task_data[-1] = "Yes"
            elif user_choice == "2":
                task_data[0] = input("Enter the new assignee name: ")
            elif user_choice == "3":
                task_year = input("enter year number here: ")
                task_month = input("enter month here (Format Example) - Jan: ")
                task_day = input("enter day here: ")
                due_date = f"{task_day} {task_month} {task_year}"
                task_data[4] = due_date
            elif user_choice == "4":
                print("Exiting task editor.")
            else:
                print("Incorrect input. Exiting task editor.")

            old_tasks[old_tasks.index(tasks[int(task_number) - 1])] = ", ".join(task_data)
            new_tasks = [task.strip("\n") for task in old_tasks]
            file = open("tasks.txt", "w")
            file.write("\n".join(new_tasks))
            file.close()
        else:
            print("The task is already completed! You cannot edit. Exiting task editor...")
    menu(username)


def generate_reports(username):
    if username == "admin":
        generate_task_overview()
        generate_user_overview()
        print("Completed")


def generate_task_overview():
    # Store all the tasks
    tasks = open("tasks.txt", "r").readlines()
    # total number of tasks
    total_tasks = len(tasks)
    # Total un/completed tasks
    total_completed = 0
    total_uncompleted = 0
    # Overdue and uncompleted tasks
    total_overdue_uncompleted = 0

    # Get total number of completed tasks and
    # total number of uncompleted tasks
    for line in tasks:
        line = line.split(", ")
        if line[-1].lower() == "yes":
            total_completed += 1
        else:
            total_uncompleted += 1
        # If the task is past its due date
        # total completed and overdue
        if datetime.now() > datetime.strptime(line[-3], "%d %b %Y") and line[-1].lower().strip() == "no":
            total_overdue_uncompleted += 1

    # % Uncompleted
    perc_uncompleted = round((total_uncompleted / total_tasks) * 100, 2)
    # % completed
    perc_completed = round((total_completed / total_tasks) * 100, 2)
    file = open("task_overview.txt", "w")
    task_overview = f"Total Tasks: {total_tasks}\n" \
                    f"Total completed tasks: {total_completed}\n" \
                    f"Total uncompleted tasks: {total_uncompleted}\n" \
                    f"Total overdue and uncompleted: {total_overdue_uncompleted}\n" \
                    f"Percentage uncompleted: {perc_uncompleted}\n" \
                    f"Percentage completed: {perc_completed}\n" \
                    "_______________________________________________"
    file.write(task_overview)
    file.close()


def generate_user_overview():
    # Store users and tasks
    users = open("user.txt", "r").readlines()
    tasks = open("tasks.txt", "r").readlines()
    # Total users
    total_users = len(users)
    # Total tasks
    total_tasks = len(tasks)
    user_overview_data = [f"Total amount of users:                     {total_users}\n"
                          f"Total amount of tasks:                     {total_tasks}\n"
                          f"_______________________________________________\n"]

    for user in users:
        user = user.split(", ")
        # Total user owned tasks
        user_tasks = 0
        user_completed = 0
        user_uncompleted = 0
        total_overdue_uncompleted = 0

        for task in tasks:
            task = task.split(", ")
            if task[0] == user[0]:
                user_tasks += 1
                if task[-1].lower() == "yes":
                    user_completed += 1
                else:
                    user_uncompleted += 1
                # If the task is past its due date
                # total completed and overdue
                if datetime.now() > datetime.strptime(task[-3], "%d %b %Y") and task[-1].lower() == "no":
                    total_overdue_uncompleted += 1

        # Total percentage assigned to user
        # Percentage of tasks owned by user
        try:
            perc_owned = round((user_tasks / total_tasks) * 100, 2)
            # Total user percentage completed
            perc_completed = round((user_completed / user_tasks) * 100, 2)
            # Percentage user uncompleted
            perc_uncompleted = round((user_uncompleted / user_tasks) * 100, 2)
            # Percentage user overdue and uncompleted
            perc_overdue_uncompleted = round((user_uncompleted / user_tasks) * 100, 2)
        except ZeroDivisionError:
            perc_owned = 0.0
            # Total user percentage completed
            perc_completed = 0.0
            # Percentage user uncompleted
            perc_uncompleted = 0.0
            # Percentage user overdue and uncompleted
            perc_overdue_uncompleted = 0.0

        user_overview_data.append(f"User Name:                                 {user[0]}\n"
                                  f"Percentage Tasks owned:                    {perc_owned}\n"
                                  f"Percentage Tasks completed:                {perc_completed}\n"
                                  f"Percentage Tasks uncompleted:              {perc_uncompleted}\n"
                                  f"Percentage Tasks uncompleted and Overdue:  {perc_overdue_uncompleted}\n"
                                  "_______________________________________________\n")
    file = open("user_overview.txt", "w")
    file.write("".join(user_overview_data))
    file.close()


def display_statistics(username):
    if username == "admin":
        # Check if generated reports exist, if not generate them
        if not os.path.exists("user_overview.txt") or not os.path.exists("task_overview.txt"):
            generate_reports(username)
        print()
        print(open("task_overview.txt").read())
        print(open("user_overview.txt").read())

    menu(username)


def exitt():
    print("Thank you for using  task manager!")
    exit()
# the exit function is there to leave the program once you are done working in it.

login(username, password)
