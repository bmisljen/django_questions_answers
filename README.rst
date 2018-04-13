=====
QandA
=====

QandA is a simple Django app to for questions and answers. For each
question, visitors can choose between a fixed number of answers as well as add their own
answers.

Detailed documentation is in the "docs" directory.

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

5. Visit http://127.0.0.1:8000/qanda/ to answer and vote on questions.