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

# Models => create for db 
- inside app/models.py/create your models
    - def __str__ => accept us to write output when using print method
    - use makemigrations and migrate for adding model to db

# View 
- inside app/views/ create your views
  - render(return which page you need)
  - add templates directory inside app and create html file here
  - create urls.py in app add urlpattern
  - add your path in app to project urls.py using include method

# Forms => create for views(users)
- inside app / create forms.py => add your form here
- import your form to app/views.py

# Email send with django
 - from django.core.mail import EmailMessage - add this class in app\views
 - create message body, and message function 
 - project\ settings.py\ add email settings

# Add admin panel
- app \ admin.py => add register
## Admin user
- Stop program 
  - in terminal python manage.py createsuperuser

# Base html with jinja
- Create base html in templates directory
  - Extend another pages from base.html


## GET - POST 
# GET request, which means we are getting data in our browser, we are getting that form to be displayed in our browser.
# When we fill in the spaces and we press that submit button, that is a POST request.
# So as a user, as a visitor of the website, when you press that button, you are doing a POST request.


