# Social App (Twiter Clone)

A Twitter-like social media web application built with Django. This application allows users to register, login, and interact with the platform by posting tweets, uploading photos, and searching through tweets.

## Features

*   **User Authentication**: Secure user registration, login, and logout functionality.
*   **CRUD Operations for Tweets**: 
    *   **Create**: Users can post new tweets with text (up to 240 characters) and attach optional photos.
    *   **Read**: A public feed where all tweets are displayed, ordered by the latest.
    *   **Update**: Users can edit their own previously posted tweets.
    *   **Delete**: Users can remove their own tweets.
*   **Search functionality**: Users can search for specific tweets containing a keyword.
*   **Media Support**: Ability to upload and display images with tweets.

## Technologies Used

*   **Backend**: Python, Django 6.0.6
*   **Database**: SQLite3 (default Django configuration)
*   **Frontend**: HTML, CSS (Django Templates)
*   **Media Handling**: Django's built-in `ImageField` and media root configuration.

## Prerequisites

Before you begin, ensure you have met the following requirements:
*   Python 3.8+ installed on your system.
*   `pip` (Python package installer).

## Installation and Setup

1.  **Clone or Download the Repository**
    Navigate to the project directory:
    ```bash
    cd "Social App"
    ```

2.  **Create and Activate a Virtual Environment**
    It's recommended to use a virtual environment to manage dependencies.
    *   **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Dependencies**
    Since the `requirement.txt` file uses UTF-16 LE encoding, you can install the packages using:
    ```bash
    pip install -r requirement.txt
    ```
    *(Note: If you face encoding issues on some systems, you might need to convert the file to UTF-8 or install packages manually: `pip install Django==6.0.6 asgiref==3.11.1 sqlparse==0.5.5 tzdata==2026.2`)*

4.  **Run Migrations**
    Navigate into the `chaiheadq` directory where `manage.py` is located, and apply database migrations:
    ```bash
    cd chaiheadq
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional)**
    To access the Django Admin panel, create an admin account:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    Start the server:
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**
    Open your web browser and navigate to:
    *   Application: `http://127.0.0.1:8000/tweet/`
    *   Admin Panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
Social App/
│
├── chaiheadq/               # Main Django project directory
│   ├── chaiheadq/           # Project settings and configurations
│   ├── tweet/               # Main app handling tweets and user actions
│   ├── templates/           # Global HTML templates
│   ├── static/              # Static files (CSS, JS, Images)
│   ├── media/               # User-uploaded media files (photos)
│   ├── manage.py            # Django management script
│   └── db.sqlite3           # SQLite Database file
│
├── venv/                    # Python virtual environment
├── requirement.txt          # Python dependencies
└── README.md                # Project documentation
```

## How to Use

1.  **Register**: Click on the registration link to create a new account.
2.  **Login**: Use your credentials to log in.
3.  **Post a Tweet**: Navigate to the tweet creation page to post your thoughts and optional images.
4.  **Manage Tweets**: Go to the tweet feed to view all posts. You will see "Edit" and "Delete" options on the tweets you authored.
5.  **Search**: Use the search bar in the tweet feed to find specific content by keywords.
