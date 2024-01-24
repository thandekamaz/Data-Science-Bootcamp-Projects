# Import the datetime module to handle date and time operations
from datetime import datetime

# Function to add user data to a file
def add_user_data(existing_data, new_data):
    combined_data = {**existing_data, **new_data}

    # Open the 'user.txt' file in write mode
    with open('user.txt', 'w') as user:
        # Write each username and password to the file
        for username, password in combined_data.items():
            user.write(f'{username},{password}\n')

# Initial user data and new user data to be added
existing_data = {'admin': 'adm1n'}
new_data = {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'user4': 'pass4', 'user5': 'pass5'}

# Add user data to the file
add_user_data(existing_data, new_data)

# Combine existing and new user data
combined_data = {**existing_data, **new_data}

# Function to get user credentials through input
def get_user_credentials():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        yield username, password

# Function to validate user credentials
def validate_credentials(username, password, combined_data):
    if username not in combined_data:
        print("Error: Invalid username. Please try again.")
        return False
    elif combined_data[username] != password:
        print("Error: Invalid password. Please try again.")
        return False
    else:
        print("Login successful!")
        return True

# Loop to continuously prompt for user credentials until valid
for username, password in get_user_credentials():
    if validate_credentials(username, password, combined_data):
        break

# Function to register a new user
def register_user(existing_data, new_data):
    if username != "admin":
       print("Error: Only the user with the username 'admin' is allowed to register users.")
       return 
    
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm the password: ")

    # Check if password confirmation matches
    if confirm_password == new_password:
        # Add new user to data and update file
        new_data[new_username] = new_password
        add_user_data(existing_data, new_data)
        print("User registered successfully!")
    else:
        print("Error: Password confirmation does not match. Please try again.")

# Function to display statistics (total users and tasks)
def display_statistics():
    if username != 'admin':
        print("Error: Only the user with the username 'admin' is allowed to view statistics.")
        return
    with open('user.txt', 'r') as user_file:
        total_users = sum(1 for line in user_file)

    with open('tasks.txt', 'r') as tasks_file:
        # Count the number of unique usernames in tasks.txt
        unique_usernames = set(line.split(',')[0].strip() for line in tasks_file if line.strip())

    total_tasks = len(unique_usernames)

    print(f"Total number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}")

# Function to check if a username exists in the file
def is_existing_username(username):
    with open('user.txt', 'r') as user_file:
        existing_usernames = [line.split(',')[0].strip() for line in user_file]
    return username in existing_usernames

# Function to add a new task
def add_task():
    while True:
        assignee_username = input("Enter the username of the person the task is assigned to: ")

        # Check if the assigned username exists
        if not is_existing_username(assignee_username):
            print("Error: The entered username does not exist. Please enter an existing username.")
            continue

        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

        # Validate date format
        try:
            datetime.strptime(task_due_date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Please enter the date in the format YYYY-MM-DD.")
            continue

        current_date = datetime.now().strftime("%Y-%m-%d")
        task_status = 'No'

        with open('tasks.txt', 'a') as file:
            # Write task information to the 'tasks.txt' file
            file.write(f'{assignee_username},{task_title},{task_description},{task_due_date},{current_date},{task_status}\n')

        print("Task added successfully!")
        break

# Function to view all tasks
def view_all_tasks():
    with open('tasks.txt', 'r') as file:
        tasks_data = file.readlines()

    if not tasks_data:
        print("No tasks available.")
        return

    print("\nAll Tasks:")
    for task_line in tasks_data:
        task_info = task_line.strip().split(',')
        if len(task_info) == 6:
            print(f"Assignee: {task_info[0]}\nTitle: {task_info[1]}\nDescription: {task_info[2]}\n"
                  f"Assigned Date: {task_info[3]}\nDue Date: {task_info[4]}\nStatus: {task_info[5]}\n")

# Function to view tasks assigned to a specific user
def view_my_tasks(username):
    with open('tasks.txt', 'r') as file:
        tasks_data = file.readlines()

    assigned_tasks = []

    for task_line in tasks_data:
        task_info = task_line.strip().split(',')

    # Check if the line has exactly 6 elements and the username matches
    if len(task_info) == 6 and task_info[0] == username:
        assigned_tasks.append(task_info)

    if not assigned_tasks:
        print(f"No tasks assigned to {username}.")
        return

    print(f"\nTasks Assigned to {username}:")
    for task_info in assigned_tasks:
        print(f"Title: {task_info[1]}\nDescription: {task_info[2]}\n"
              f"Assigned Date: {task_info[3]}\nDue Date: {task_info[4]}\nStatus: {task_info[5]}\n")

# Main loop for the user interface
while True:
    # Display menu options and get user input
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display statistics
e - exit
: ''').lower()
    
    # Check user's choice and perform corresponding action
    if menu == 'r':
        register_user(existing_data, new_data)
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all_tasks()
    elif menu == 'vm':
        # Get username for viewing tasks
        username = input("Enter your username: ")
        view_my_tasks(username)
    elif menu == 's':
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        # Exit the program
        break
    else:
        print("Invalid option. Please choose a valid option.")
