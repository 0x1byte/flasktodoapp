# Flask To-Do List App

## Description

The Flask To-Do List App is a lightweight web application designed to help users manage their daily tasks efficiently. This project is built with Flask, a Python web framework, and provides a user-friendly interface for adding, updating, and deleting tasks. It serves as a practical example of how to create a web-based task management system using Flask.

## Project Structure

- **project.py**: This is the main application file that contains the Flask application. It defines the routes, handles HTTP requests, and interacts with the SQLite database to manage tasks.

- **templates**: This directory contains the HTML templates used to render the web pages of the application. There are two main templates: `index.html` for the homepage displaying tasks and `update.html` for updating tasks.

- **requirements.txt**: This file lists the Python packages required to run the application. You can use `pip` to install these packages with the command `pip install -r requirements.txt`.

- **todos.db**: This is an SQLite database file used to store the task data. It is automatically created when you run the application for the first time.

- **test_project.py**: This file contains unit tests for the Flask application. It uses the `pytest` framework to test the routes and functionality of the app.

- **README.md**: You're currently reading the project README, which provides an in-depth explanation of the project, its structure, and usage instructions.

## Design Choices

The Flask To-Do List App was designed to be a simple yet functional task management tool. Here are some key design choices:

- **SQLite Database**: We opted for an SQLite database to store tasks. It's a lightweight and serverless database that suits the needs of this project. However, in a production application, you might choose a more robust database like PostgreSQL or MySQL.

- **User-Friendly Interface**: The application provides a clean and intuitive user interface, making it easy for users to add, update, and delete tasks. The design is minimalistic to ensure a smooth user experience.

- **Testing**: We included unit tests using `pytest` to ensure the functionality of the app. This helps identify and fix issues as the project evolves.

- **Separation of Concerns**: The project follows a basic Model-View-Controller (MVC) pattern. The database operations are handled in the model, the templates define the views, and the Flask application file (`project.py`) serves as the controller.

## Installation and Usage

To run the Flask To-Do List App on your local machine, follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/0x1byte/flasktodoapp.git`

2. Navigate to the project directory: `cd flask-todo-app`

3. Install the required Python packages using pip: `pip install -r requirements.txt`

4. Start the Flask application: `python project.py`

5. Access the app in your web browser by visiting `http://localhost:5000`.
