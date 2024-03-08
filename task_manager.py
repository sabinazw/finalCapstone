import os
from datetime import datetime, date
from tabulate import tabulate

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# DECORATING FUNCTIONS
def decorate1(text):
    print('='*70)
    print(text)
    print('='*70)

def decorate2(text):
    print('-'*70)
    print(text)
    print('-'*70)  

def decorate3(text):
    print(text)
    print('-'*70)

def decorate4(text):
    print('-'*70)
    print(text)
    

# USERNAME AND PASSWORD DATA RELATED FUNCTIONS
def default_user_file():
    """Create a default user.txt file if it doesn't exist.
    """
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

def user_data_list():
    """Create a list with text lines as items from user.txt file
    :return: list of lines from user.txt file
    :rtype: list
    """
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
    return user_data

def username_password_dict(user_data):
    """Create a dictionary with username:password items from user.txt file
    :param user_data: list of text lines from user.txt file
    :type user_data: list
    :return: list of dictionaries with username keys and password values
    :rtype: dict
    """
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
    return username_password


# TASK DATA RELATED FUNCTIONS
def default_task_file():
    """Create a default tasks.txt file if it doesn't exist.
    """
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            default_file.write("admin;Add functionality to task manager;Add additional options and refactor the code.;2022-12-01;2022-11-22;No")

def task_data_func():
    """Create a list with text lines as items from tasks.txt file
    :return: list of lines from tasks.txt file
    :rtype: list
    """
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
    return task_data

def task_list_func():
    """Create a list of tasks dictionaries as items from tasks.txt file
    :param task_data: list of text lines from taks.txt file
    :type task_data: list
    :return: list of dictionaries tasks key:value pairs
    :rtype: list
    """
    task_list = []
    for t_str in task_data:
        curr_t = {}
        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)
    return task_list


# TASK EDITING FUNCTIONS
def which_task_to_edit():
    """Check which task user wants to edit
    :return: number of task to edit
    :rtype: int
    """
    while True:
        print('-'*70)
        edit_task = input("Which task would you like to edit: ")
        if edit_task.isdigit():  # Check if input is a digit
            number = int(edit_task)
            if 0 < number <= len(task_num):  # Check if input is within the specified range
                print(f"You chose to edit task number '{number}'.")
                number = int(edit_task)                            
                break
            else:
                print(f"Input must be greater than 0 and less or equal to {len(task_num)} . Please try again.")
        else:
            print("Input must be a number. Please try again.")
    return number 

def edit_the_task(task_word_index:int,new_text:str):
    """Edit specific category in task
    :param task_word_index: index of the task category to edit eg. 'title' is index 1
    :type task_word_index: int
    :param new_text: enter new text to overwrite choosen task category
    :type new_text: str
    :return: new task with changed details
    :rtype: str
    """
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        new_list = []

    for i, line in enumerate(lines):
        if i == num:
            new_line = lines[i].strip('\n').split(';')
            new_line[task_word_index] = new_text
            final_lines = ";".join(new_line)
            new_list.append(final_lines)
        else:
            new_line = lines[i].strip('\n').split(';')
            final_lines = ";".join(new_line)
            new_list.append(final_lines)

    with open('tasks.txt', 'w') as file:
        file.write("\n".join(new_list))      
    print("Your task has been sucessfully updated!\n")

def edit_the_task_with_condition(task_word_index:int,new_text:str,completed_index = 5):
    """Edit specific category in task with a condition only if task is not completed
    :param task_word_index: index of the task category to edit eg. 'title' is index 1
    :type task_word_index: int
    :param new_text: enter new text to overwrite chosen task category
    :type new_text: str
    :param completed_index: default 'completed' task category index = 5
    :type completed_index: int
    :return: new task with changed details
    :rtype: str
    """
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        new_list = []

        for i, line in enumerate(lines):
            if i == num:
                new_line = lines[i].strip('\n').split(';')
                if new_line[completed_index].lower() == 'no':
                    new_line[task_word_index] = new_text
                    final_lines = ";".join(new_line)
                    new_list.append(final_lines)
                    print("Your task has been sucessfully updated!\n")
                else:
                    new_line[task_word_index]
                    final_lines = ";".join(new_line)
                    new_list.append(final_lines)
                    print("The task has been completed, you can't make changes.\n")
            else:
                new_line = lines[i].strip('\n').split(';')
                final_lines = ";".join(new_line)
                new_list.append(final_lines)

    with open('tasks.txt', 'w') as file:
        file.write("\n".join(new_list)) 


# MAIN MENU FUNCTIONS
def reg_user():
        """Register a new user
    :return: updated str with username and password data
    :rtype: str
    """
        # Check if the new username exists is in user register, 
        # if yes ask to enter new username
        new_username = input("New Username: ")
        for username in username_password.keys():
            while new_username == username:
                print(f"Username '{new_username}' already exist, enter new username")
                return reg_user()
            
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            decorate3("New user has been added!")

            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        
        else:
            decorate3("Passwords do not match!")

def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.'''
    
    task_username = input("Name of person assigned to task: ")

    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return add_task()

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    decorate3("\nTask has been successfully added!")

def view_all():
    """View all the tasks
    """
    for i, t in enumerate(task_list,1):
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            if t['completed'] == False:
                disp_str += f"Task complete? \t No\n"
            else:
                disp_str += f"Task complete? \t Yes\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(f"Task number {i}\n")
            print(disp_str)
            print('-'*70)

def view_mine():
    """View only specific user tasks
    """
    for n, task in enumerate(task_list):
        if task['username'] == curr_user: 
            my_list.append(task)
            task_num.append(n)
    for num, my_task in enumerate(my_list,1):                  
        disp_str = f"Task: \t\t {my_task['title']}\n"
        disp_str += f"Assigned to: \t {my_task['username']}\n"
        disp_str += f"Date Assigned: \t {my_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {my_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        if my_task['completed'] == False:
            disp_str += f"Task complete? \t No\n"
        else:
            disp_str += f"Task complete? \t Yes\n"
        disp_str += f"Task Description: \n {my_task['description']}\n"
        print(f"Task number {num}\n")
        print(disp_str)
        print('-'*70)

# =============================================================================
# MAIN PROGRAM


# Create default user file if it doesn' exists
default_user_file()

user_data = user_data_list()
username_password = username_password_dict(user_data)

decorate1("\t\t\tTASK MANAGER")
print("Welcome, please login to your 'TASK MANAGER' account")
print("Default login details: 'username' = admin, 'password' = password\n")

# Login to the task manager program
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        print("Please try login again with different username.\n")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        print("Please try login again with different password.\n")
        continue
    else:
        print("Login Successful!")
        logged_in = True

# Create default task file if it doesn't exist
default_task_file() 

while True:
    # Presenting the menu to the user and 
    # Making sure that the user input is converted to lower case.
    print()
    decorate2("*** Main Menu ***")
    menu = input('''Select one of the following Options below:
 r - Registering a user
 a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
 e - Exit
: ''').lower()

    if menu == 'r':
        #REGISTER A USER
        decorate1("\t\t\tREGISTER NEW USER") 
        reg_user()

    elif menu == 'a':
        #ADD NEW TASK      
        decorate1("\t\t\tADD NEW TASK")
      
        task_data = task_data_func()
        task_list = task_list_func()        
        add_task()

    elif menu == 'va':
        # VIEW ALL THE TASKS                    
        decorate1("\t\t\tALL TASKS")    

        task_data = task_data_func()
        task_list = task_list_func()
        view_all()
                  

    elif menu == 'vm':
        # VIEW MY TASKS 
        decorate1("\t\t\tMY TASKS")
          
        task_data = task_data_func()
        task_list = task_list_func()

        # List of dictionaries with tasks items for specific user
        my_list = []
        # List of lines indexes in the tasks.txt for user related tasks
        task_num = []
        
        view_mine()
        
        while True:
            """User menu to edit specific tasks
            """
            decorate3("*** Task Menu ***")
            option_menu = input("""Select one of the following Options below:
        
         t - Change the 'Task' title
        td - Change the 'Task Description'
        un - Change the 'Username' to whom the task is assigned
        dd - Change the 'Due Date'
        mc - Mark the task as completed
        -1 - Exit to main menu
""").lower()
            if option_menu == 't':
            # Change the task title and write changes to file
                       
                # Number of task chosen from users specific tasks list
                number_of_task = which_task_to_edit()

                # This is a number of task choosen by user and
                # it is represented as task index position in a tasks.txt
                num = task_num[number_of_task-1]
                print()    
                new_title_name = input("Enter your new task title: ")
                edit_the_task(1,new_title_name)
          
            elif option_menu == 'td':
            # Change the task description and write changes to file 
                number_of_task = which_task_to_edit()     
                num = task_num[number_of_task-1]
                print()           
                new_task_description = input("Enter your new task description: ")
                edit_the_task(2,new_task_description)

            elif option_menu == 'un':
            # Change the username to whom the task is assigned
                   
                number_of_task = which_task_to_edit()     
                num = task_num[number_of_task-1]

                user_list = list(username_password)
                user_string = ",".join(user_list)
                new_task_user = input(
f"""
Which user would you like to assign to the task? 
Choose from registerd users [{user_string}]:""").lower()
                
                # Check if chosen new user is in the user registry
                while new_task_user not in user_list:
                    new_task_user = input(f"Choose user from registered users [{user_string}] :").lower()
                
                print()

                # If the new user is in the registry, 
                # edit the task only if the task is not yet completed
                edit_the_task_with_condition(0, new_task_user) 
                
               
            elif option_menu == 'dd':
                # Change the due date

                number_of_task = which_task_to_edit()     
                num = task_num[number_of_task-1]

                # Check if the new due dae is in the correct date format
                while True:
                    try:
                        task_due_date = input("Enter new due date of task (YYYY-MM-DD): ")
                        new_due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
                print()
 
                # Edit the task only if the task is not yet completed
                edit_the_task_with_condition(3,task_due_date)
            
            elif option_menu == 'mc':
                # Mark the task as completed
                
                number_of_task = which_task_to_edit()     
                num = task_num[number_of_task-1]

                # Edit the task only if the task is not yet completed
                edit_the_task_with_condition(5,'Yes')                  

            elif option_menu == '-1':
                # Exit task menu
                break
            else:
                decorate2("You have made a wrong choice, Please Try again")
             

        
    elif menu == 'gr':
        # TASK OVERVIEW AND USER OVERVIEW REPORTS

        # Create default files for task_overview and user_overview
        if not os.path.exists("task_overview.txt"):
            with open("task_overview.txt", "w") as default_file:
                default_file.write("text")

        if not os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "w") as default_file:
                default_file.write("text")


        task_data = task_data_func()
        task_list = task_list_func()
        total_tasks = len(task_data)        

        # -----TASK OVERVIEW REPORT-----

        curr_date = datetime.today()
        # completed tasks count
        yes_count = 0
        # incompleted tasks count
        no_count = 0
        # incompleted and overdue tasks count
        incomplete_overdue = 0
        for dict in task_list:
            for w in dict.values():
                if w == True:
                    yes_count +=1
                elif w == False:
                    no_count +=1
                    for k in dict.keys():
                        if k == 'due_date' and dict[k]< curr_date:
                            incomplete_overdue +=1
                
        disp_tasks = f"""{'='*70}
TASK OVERVIEW REPORT
{'='*70}
"""
        disp_tasks += f"1. The total number of tasks: {total_tasks}\n"
        disp_tasks += f"2. Total number of completed tasks: {yes_count}\n"
        disp_tasks += f"3. Total number of uncompleted tasks: {no_count}\n"
        disp_tasks += f"4. Total number of tasks that haven't been completed and are overdue: {incomplete_overdue}\n"
        disp_tasks += f"5. The percentage of tasks that are incomplete: {round((no_count/total_tasks)*100,2)}%\n"
        disp_tasks += f"6. The percentage of tasks that are overdue: {round((incomplete_overdue/total_tasks)*100,2)}%\n"

        # Write disp_tasks text report to task_overview file
        with open('task_overview.txt', 'w') as file:
            file.write(disp_tasks)
      
        decorate4("Task overview report has been successfully generated and saved at 'task_overview.txt' file!")

        
        # -----USER OVERVIEW REPORT-----
            
        # user:password dicionary
        user_data = user_data_list()
        username_password = username_password_dict(user_data)
        total_users = len(username_password.keys())

        # Empty list to append all users report data (report title, username, 
        # disp_users_data text )
        disp_users_data = [] 

        report_title = f"""{'='*70}
USER OVERVIEW REPORT
{'='*70}"""
        disp_users_data.append(report_title)

        for user in username_password.keys():
            # specific user task counter
            user_task_count = 0 
            # specific user task completed counter
            user_task_compl = 0 
            # specific user task incompleted and overdue
            user_task_notcompl_overdue = 0 
            # report title
            user_name = f"""Username: {user}"""

            disp_users_data.append(user_name)

            for dict in task_list:
                for v in dict.values():
                    if user == v:
                       user_task_count +=1
                       for k in dict.keys():
                            if dict[k] == True:
                                user_task_compl +=1
                            elif dict[k] == False:
                                for k in dict.keys():
                                    if k == 'due_date' and dict[k]< curr_date:
                                        user_task_notcompl_overdue += 1
            
            # Calculate percentages to display in a text                  
            percent_func = lambda a, b: f"{round((a/b)*100,1)}%" if (b > 0) else 'No tasks assigned'
            user_rep2 = percent_func(user_task_count, total_tasks)
            user_rep3 = percent_func(user_task_compl, user_task_count)
            user_rep4 = percent_func((user_task_count - user_task_compl),user_task_count)
            user_rep5 = percent_func(user_task_notcompl_overdue,user_task_count)

            # Each user data display           
            user_disp = f"""1. Total number of tasks assigned to '{user}': {user_task_count}
2. The % of the total number of tasks assigned to '{user}': {user_rep2}
3. The % of the tasks assigned to '{user}' that have been completed: {user_rep3}
4. The % of the tasks assigned to '{user}' that must still be completed: {user_rep4}
5. The % of the tasks assigned to '{user}' that has not yet been completed and are overdue: {user_rep5}
{'-'*70} 
"""         # Each user string data added to display list  
            disp_users_data.append(user_disp)

        # Join display list into one string and write to text file
        with open('user_overview.txt', 'w') as file:
            file.write("\n".join(disp_users_data))
        print("User overview report has been successfully generated and saved at 'user_overview.txt' file!")
        
   
    elif menu == 'ds':
        # DISPLAY STATISTICS - for 'admin' use only
        if curr_user == 'admin': 
            decorate1("\t\t\tSTATISTICS")
            '''If the user is an admin they can display statistics about number of users
                and tasks.'''
            
            user_data = user_data_list()
            username_password = username_password_dict(user_data)        
            num_users = len(username_password.keys())
            
            task_data = task_data_func()
            task_list = task_list_func()
            num_tasks = len(task_list)

            # Generate report from user.txt file
            print("\n========== USER REPORT ==========")
            print(f"Number of users registered: \t {num_users}\n")
            headers1 = ['Username', 'Password']
            list_of_users = [[k,v] for k,v in username_password.items()]

            # Create a table with all the users from register
            table1 = tabulate(list_of_users,headers=headers1,tablefmt='grit')
            print(table1)

            # Generate report from tasks.txt file
            print("\n\n========== TASK REPORT ==========")
            print(f"Number of tasks assigned: \t {num_tasks}\n")
            headers2 = ['Username', 'Task Title', 'Task Description', 'Due Date', 'Date Assigned', 'Task Complete?']

            # List of lists tasks
            list_of_tasks = []
            for dict in task_list:
                # Empty list holder for modified user task
                t_list = []
                for k in dict.keys():
                    if k == 'due_date' or k == 'assigned_date':
                        t_list.append(dict[k].strftime("%Y-%m-%d"))
                    elif k == 'completed':
                        if dict[k] == True:
                            t_list.append('Yes')
                        else:
                            t_list.append('No')            
                    else:
                        t_list.append(dict[k])

                # Every modified user task is appended as list to list_of_tasks list
                list_of_tasks.append(t_list)

            # Create a table with all the tasks from register
            table2 = tabulate(list_of_tasks,headers=headers2,tablefmt="grit")
            print(table2)
  
        else:
            decorate4("Please login to 'admin' account to view 'Statistics Reports'")

    elif menu == 'e':
        decorate2('Goodbye!!!')
        exit()

    else:
        print('-'*70)
        print("You have made a wrong choice, Please Try again")
        print('-'*70)