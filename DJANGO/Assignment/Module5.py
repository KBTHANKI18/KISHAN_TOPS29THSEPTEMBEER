#Q-1 Why Django should be used for web-development? Explain how you can create a project in Django?
#A-1 Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.
#    Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your
#    app without needing to reinvent the wheel.


#    Steps to create a project in Django:
#    (1)Use the django-admin tool to generate a project folder, the basic file templates, and manage.py, which serves as your project management script.
#    (2)Use manage.py to create one or more applications. ...
#    (3)Register the new applications to include them in the project.
#    (4)Hook up the url/path mapper for each application.

#Q-2 how to check installed version of django project.
#A-2 Django can be installed easily using pip within your virtual environment. This will download and install the latest Django release.
#    After the installation has completed, you can verify your Django installation by executing django-admin --version in the command
#    prompt.  
    
#Q-3 Explain what does django-admin.py make messages command is used for?    
#A-3 makemessages. Runs over the entire source tree of the current directory and pulls out all strings marked for translation.
#    It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory.

#Q-4 What is Django URLs?Make program to create django urls.
#A-4 Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against 
#    path_info . Once one of the URL patterns matches, Django imports and calls the given view, which is a Python function 
#    (or a class-based view). 

       
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]
"""

#Q-5 What is a QuerySet?Write program to create a new Post object in database:
#A-5 A QuerySet is a collection of data from a database. A QuerySet is built up as a list of objects.
#    QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage. 
#    In this tutorial we will be querying data from the Member table.

"""
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
   
"""

#Q-6 Mention what command line can be used to load data into Django? 
#A-6 To load data into Django you have to use the command line Django-admin.py loaddata. The command line will searches the data 
#    and loads the contents of the named fixtures into the database.  


