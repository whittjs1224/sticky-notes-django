# Sticky Notes (Django)

A Django web app for creating, viewing, editing and deleting sticky
notes. Each note has a title, some content and a color (yellow, pink, blue
or green), and the notes are shown as color cards on the home page.

## Features

- **Create** a note with a title, content and color
- **Read** all notes on the home page (most recently updated first), or open
one note to see it in full
- **Update** a note's title, content or color
- **Delete** a note, after a confirmation page
- Manage notes in Django's admin site at `/admin/`
- Styled with Bootstrap 5 and custom stylesheet

## Project structure

```
sticky_notes_task/
├── design/                 Use case, sequence and class diagrams
├── requirements.txt
└── sticky_notes/            Django project (contains manage.py)
    ├── sticky_notes/       Project settings and top-level URLs
    └── notes/              The notes app
        ├── models.py       Note model
        ├── forms.py        NoteForm (ModelForm)
        ├── views.py        CRUD views
        ├── urls.py         App URL patterns
        ├── admin.py        Admin site settings
        ├── tests.py         Model and view tests
        ├── templates/      base.html and the notes/ page templates
        └── static          notes/css/styles.css
```

## Setup

Requires Python 3.12 or newer.

1.  Create and activate a virtual environment in the `sticky_notes_task`
    folder:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install the requirements:

    ```
    pip install -r requirements.txt
    ```

3.  Move into the Django project folder and create the database:

    ```
    cd sticky_notes
    python manage.py migrate
    ```

4.  (Optional) Collect static files and create an admin account:

    ```
    python manage.py collectstatic
    python manage.py createsuperuser
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

    Then open http://127.0.0.1:8000/ in a browser.

## Pages

| Address                  | Page                       |
|--------------------------|----------------------------|
| `/`                      | All notes                  |
| `/note/new/`             | Create a note              |
| `/note/<id>/`            | View one note              |
| `/note/<id>/edit/`       | Edit a note                |
| `/note/<id>/delete/`     | Confirm and delete a note  |
| `/admin/`                | Django admin site          |

## Running the test and linter

With the virtual environment active, run the tests from the `sticky_notes`
folder and the linter from the `sticky_notes_task` folder (where `.flake8`
is):

```
cd sticky_notes
python manage.py test notes
cd ..
python -m flake8
```
