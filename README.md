# 📝 FlaskNote

A simple Flask-based note-taking web app to learn the basics of Python
web development using Flask.

------------------------------------------------------------------------

## 🚀 Features

-   Add new notes easily
-   View all saved notes instantly
-   Delete notes when done
-   Built with Flask and HTML templates

------------------------------------------------------------------------

## 🧱 Project Structure

    FlaskNote/
    │
    ├── app.py
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1. Create and Activate Virtual Environment

``` bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Flask

``` bash
pip install flask
```

### 3. Run the Application

``` bash
python app.py
```

Now open your browser and visit:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🧩 Code Overview

### `app.py`

Defines all routes and the core logic for adding and deleting notes.

### `templates/index.html`

The main interface for displaying and interacting with notes.

### `static/style.css`

Handles basic styling for a clean layout.

------------------------------------------------------------------------

## 🧰 Requirements

-   Python 3.8+
-   Flask 3.1.2+

To export dependencies:

``` bash
pip freeze > requirements.txt
```

To install from the file:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 💡 Future Enhancements

-   Add SQLite database for permanent storage
-   Add user authentication
-   Improve UI with Bootstrap or Tailwind CSS

------------------------------------------------------------------------

## 🏁 Author

**Rizwan**
