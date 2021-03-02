# Django Project

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.This project focuses on registering user's using django-registration.

## Installation
1 Create a Python 3.6 virtualenv

2 Install dependencies:

```bash
pip install -r requirements.txt 
```

## Project structure

```
.
├── manage.py
├── requirements.txt
├── static
│   └── django_registration
│       ├── css
│       │   └── bootstrap.css
│       └── js
│           ├── bootstrap.js
│           ├── jquery.js
│           └── popper.js
├── templates
│   └── django_registration
│       ├── base_template.html
│       ├── registration_complete.html
│       └── registration_form.html
└── user_registration
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── settings.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   ├── views.cpython-36.pyc
    │   └── wsgi.cpython-36.pyc
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── wsgi.py

```
## Files  
 1. manage.py: Used to run Command line commands.  
2. settings.py: Here we set our configurations  
3. urls.py: It contains url dispatchers.  
4. views.py: This file contains the business logic required.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
