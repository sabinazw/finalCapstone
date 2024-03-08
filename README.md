
# Task Manager Capstone Project

## Description

This Task Manager project is designed to help users efficiently manage tasks within a team or organization. It allows for task assignment, editing, viewing, and report generation, offering both administrative and user-level functionalities. The system supports task operations such as adding new tasks, viewing all or specific user tasks, editing tasks, marking tasks as completed, and generating comprehensive reports for tasks and user overviews.

## Features

- **User Authentication:** Supports user login with username and password validation.
- **Task Management:** Allows adding, viewing, editing, and marking tasks as completed.
- **User Registration:** Admins can register new users, enabling task assignment and management for multiple team members.
- **Report Generation:** Generates detailed reports on tasks and user activities, including task completion status and overdue tasks.
- **Statistics Display:** Exclusive to admin users, displaying statistics on the number of tasks and registered users.

## Installation

Before you start, ensure you have Python installed on your system. This project was developed with Python 3.8.x. 

1. Clone the repository or download the source code.
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

First, run the `task_manager.py` script to initialize the application. The script checks for essential files (`user.txt` and `tasks.txt`) and creates them if they do not exist, setting up a default admin account.

```bash
python task_manager.py
```

## Usage

Upon running the script, you'll be greeted by a login prompt. Use the default login details (`username: admin, password: password`) or credentials of an existing user.

Once logged in, you'll be presented with a menu offering various options:

- **Register a User (r):** Only available for admin users. Allows adding new users to the system.
- **Add a Task (a):** Enables users to add new tasks, specifying details such as the task name, assigned user, due date, and description.
- **View All Tasks (va):** Lists all tasks currently in the system, along with their details.
- **View My Tasks (vm):** Shows tasks assigned to the logged-in user, with options to edit or mark tasks as complete.
- **Generate Reports (gr):** Generates and saves task and user overview reports into `task_overview.txt` and `user_overview.txt` respectively.
- **Display Statistics (ds):** Available to the admin, showing the number of tasks and registered users.
- **Exit (e):** Logs out the user and exits the application.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
