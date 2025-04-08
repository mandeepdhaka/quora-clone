# Quora Clone

This is a simple Django-based web application inspired by Quora. It allows users to register, post questions, answer questions, like answers, and log out. The project demonstrates basic functionality for user authentication, question/answer posting, and answer liking.

## Features

- **User Registration**: Allows users to create an account.
- **Login/Logout**: Users can log in and log out of the application.
- **Post Questions**: Users can post questions with a title and description.
- **View Questions**: All users can view questions posted by others.
- **Answer Questions**: Logged-in users can answer questions posted by others.
- **Like Answers**: Users can like answers posted by others, with the ability to unlike.

## Technologies Used

- **Django**: A high-level Python web framework used to build this application.
- **SQLite**: The default database used by Django for simplicity.
- **HTML/CSS**: Used for basic web pages. The project does not focus on advanced design but on functionality.

## Setup Instructions

Clone this repository to your local machine.

```bash
# Step 1: Clone the repository and navigate into the project directory
git clone https://github.com/mandeepdhaka/quora-clone.git
cd quora-clone

# Step 2: Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Step 3: Install Django
cd quora
pip install -r requirements.txt

# Step 4: Apply migrations to set up the database schema
python manage.py makemigrations
python manage.py migrate

# Step 5: Start the development server
python manage.py runserver
