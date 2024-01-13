### JOB APP WITH DJANGO

## Preparing for project

# Commands
- django-admin startproject mysite . => dot means that create project in current directory
- python manage.py startapp job_application => create application
- python manage.py makemigrations => convert code to db type for adding to the db
  - python manage.py migrate => add models to the db

# Configuration
- mysite/setttings/INSTALLED_APPS[add your app name the end of the list]
- inside app/ after creating templates => create urls.py  => make it to connect views to urls
  - create urlpatterns inside urls.py
  - inside project / using include add your path to project urlpattern list 

# Models
- inside app/models.py/create your models
    - def __str__ => accept us to write output when using print method
    - use makemigrations and migrate for adding model to db

# View 
- inside app/views/ create your views
  - render(return which page you need)
  - add templates directory inside app and create html file here
  - create urls.py in app add urlpattern
  - add your path in app to project urls.py using include method