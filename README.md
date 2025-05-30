# django_blog_project

Table of Contents
About
Installation
Repository Structure
Usage
Contributing

About
This repository is designed for a blog project with different posts and authors can handle write, edit different posts and track each user activity.

Installation
To get started with this repository, follow these steps:

Create a virtual environment (if you haven't done so already):
python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the dependencies:

pip install -r requirements.txt

Run the migrations:
python manage.py makemigrations
python manage.py migrate
Start the development server:

python manage.py runserver
Now open your browser and go to http://127.0.0.1:8000/ to view your Django application.

Repository Structure
Here’s an overview of the directory structure:

/django_blog_126
│
├── /blog                     # web app
├── /config                   # Main project folder
│
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── .gitignore                # Git ignore file
└── README.md                 # This README file
Usage
this web app is for managing articles based on subject of article. this application can track different users behavior.
Contributing
if you want , you can data analysis application on tracked data.
