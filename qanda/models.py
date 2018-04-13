import datetime

from django.db import models
from django.utils import timezone

# Question that is being asked 
class Question(models.Model):
    question_name = models.CharField(max_length=80, default='')
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question_name
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text