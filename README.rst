=====
QandA 
=====

QandA is a simple Django app to for questions and answers. A user can add a question,
answer the question with one or more answers, vote a question up or down and search for specific questions 
by question name or question text. 

The 5 most recent questions are displayed on the index page: http://127.0.0.1:8000/qanda/ along with their votes. You
can click on a question to view and add answers or click on the up/down arrows to up vote or down vote the question. 

A configured admin interface is also included for adding questions and answers and test cases are also available. 


Quick start
-----------

1. Add "qanda" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'qanda',
    ]

2. Include the qanda URLconf in your project urls.py like this::

    path('qanda/', include('qanda.urls')),

3. Run `python manage.py migrate` to create the qanda models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a questions (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/qanda/ to create questions, answer questions and vote on questions.

6. To run test cases in the same directory as manage.py run: python manage.py test qanda

Alternatively, you can also install the app using the "django-qanda-0.1.zip" package via pip:

pip install --user django-qanda-0.1.zip

To uninstall:

pip uninstall django-qanda
