# To-Do App

A simple task management web app built with Flask. Users can register, log in, and manage their personal to-do list.

## Features

- User registration and login
- Add, edit, complete, and delete tasks
- Each user sees only their own tasks
- Data stored in a SQLite database

## Tech Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

## Project Structure

```
TO-DO-APP/
├── app/          # App setup and database models
├── routes/       # Auth and task routes
├── static/       # CSS and JavaScript
├── templates/    # HTML templates
├── run.py        # Entry point
└── requirements.txt
```

## How to Run Locally

1. Clone the repository
   ```
   git clone https://github.com/Sneha-2110/todo-app-flask.git
   cd todo-app-flask
   ```

2. Create and activate a virtual environment
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run the app
   ```
   python run.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Author

Sneha Pandit