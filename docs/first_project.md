# Creating a Django Project on Windows

This guide will walk you through the steps to create a Django project on a Windows system.

## Prerequisites

- [Python](https://www.python.org/downloads/windows/): Ensure you have Python installed on your Windows system.
- During the Python installation, make sure to check the box that says "Add Python x.x to PATH." This will make it easier to run Python and pip from the command line.

## Steps

1. **Create workshop folder**: Create a folder as `C:/workshops/django/`.
2. **Open a Command Prompt**: Open a Command Prompt and switch (CD) to above folder.
3. **Verify Python Version**: In the Command Prompt, verify the installed Python version to ensure you have the correct Python version required for your Django project. Type the following command:
   ```bash
   python --version
4. **Install Django**: In the Command Prompt, install Django system-wide using pip:
   ```bash
   pip install django
5. **Create a Django Project**: Navigate to the directory where you want to create your Django project and run the following command to create a new project with the name "demo_project":
   ```bash
   django-admin startproject demo_project

   OR

   python -m django startproject demo_project
   
6. **Navigate to the Project Directory**:Change your working directory to the newly created project folder:
   ```bash
   C:\workshops\django> cd demo_project
7. **Initialize the Database**: Django uses a database to store information about your project. You'll need to create the database schema and tables by running the following commands:
   ```bash
   python manage.py migrate
   python manage.py makemigrations
8. **Create a Superuser**: You can create a superuser to access the Django admin interface for managing your application. Run the following command and follow the prompts to set user credentials (you can set user = admin and password = admin):
   ```bash
   python manage.py createsuperuser   

9. **Start the Development Server**: To run your Django project locally, use the development server. Run the following command:
   ```bash
   python manage.py runserver
10. **Access the application in browser**:

   - http://127.0.0.1:8000/ (change the port number if app is running on a different port)
   - http://127.0.0.1:8000/admin/ (change the port number if app is running on a different port). Log in with the superuser credentials to manage your application.

**_That's it! You've successfully created a Django project named "demo_project" on a Windows system. You can begin developing your web application using Django._**
