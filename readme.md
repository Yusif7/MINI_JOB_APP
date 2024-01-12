### JOB APP WITH DJANGO

## Preparing for project

# Commands
- django-admin startproject mysite . => dot means that create project in current directory
- python manage.py startapp job_application => create application
- python manage.py makemigrations => convert code to db type for adding to the db
  - python manage.py migrate => add models to the db

# Configuration
- mysite/setttings/INSTALLED_APPS[add your app name the end of the list]

# Models
- inside app/models.py/create your models
    - def __str__ => accept us to write output when using print method
    - use makemigrations and migrate for adding model to db