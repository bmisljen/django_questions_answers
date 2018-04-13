from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_name']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # add answers in an inline fashion 
    inlines = [AnswerInline]
    list_display = ('question_name', 'question_text', 'pub_date', 'was_published_recently')
    # filter questions by date published 
    list_filter = ['pub_date']
    # search for specific questions 
    search_fields = ['question_name']
    
# Add the ability to add questions and answers to the admin view 
admin.site.register(Question, QuestionAdmin)
