=====
QandA 
=====

QandA is a simple Django app for questions and answers. A user can add a question,
answer the question with one or more answers, vote a question up or down and search for specific questions 
by question name or question text. The questions and answers are saved in a PostgreSQL database. 
Try it out by visiting: 

https://django-qanda.herokuapp.com/qanda/

And for the admin interface:

https://django-qanda.herokuapp.com/admin/
(admin username: guest, password: guestpassword) 


Running locally:

*** If cloning the project to run locally you will need to update the database settings in the settings.py file as they are currently 
set to run on Heroku *** 

The 5 most recent questions are displayed on the home page: http://127.0.0.1:8000/qanda/ along with their votes counts. You
can click on a question to view it and add answers or click on the up/down arrows to up vote or down vote the question. Searching 
questions by question name and question text is also supported from the home page. 

A configured admin interface can be found at: http://127.0.0.1:8000/admin and it can be used for adding questions and answers. Unit test
cases are also available and can be run using: python manage.py test qanda  


Quick start
-----------
0. Either clone the git repo into a local folder and transfer the qanda folder into your Django project or use pip to install 
the: django-qanda-0.1.zip file (located in the git repo) by using the following command:

 pip install --user django-qanda-0.1.zip

1. Add "qanda" to your Django project INSTALLED_APPS section of the settings file like this:

    INSTALLED_APPS = [
        ...
        'qanda',
    ]

2. Include the qanda URLconf in your Django project urls.py file like this:

    path('qanda/', include('qanda.urls')),

3. In your Django project directory, run: `python manage.py migrate` to create the qanda models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create questions and answers (you'll need the Admin app enabled in your Django project).

5. Visit http://127.0.0.1:8000/qanda/ to create questions, answer questions and vote on questions.

6. To run test cases in the same directory as manage.py run: python manage.py test qanda

7. To uninstall the app: pip uninstall django-qanda
