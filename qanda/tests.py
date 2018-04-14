import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse 

from .models import Question, Answer


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
def create_question(question_name, question_text, days, votes):
    """
    Create a question with the given `question_name` and `question_text` and publish the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published) and the number of votes for
    the question.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_name=question_name,
                                   question_text=question_text, 
                                   pub_date=time,
                                   votes=votes)

def create_answer(question, answer_text):
    """
    Create an answer for a given question with an `answer_text` and the number of 
    votes that the question has received 
    """
    return Answer.objects.create(question=question, 
                                 answer_text=answer_text)
    
class QuestionIndexViewTests(TestCase):
   
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('qanda:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Questions Yet")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question_one = create_question(question_name="question_one", 
                        question_text="Past question.", 
                        days=-30, 
                        votes=0)
        response = self.client.get(reverse('qanda:index'))
        self.assertContains(response, question_one.question_name)

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_name="question_one", 
                        question_text="Future question.", 
                        days=30, 
                        votes=0)
        response = self.client.get(reverse('qanda:index'))
        self.assertContains(response, "No Questions Yet")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question_one = create_question(question_name="question_one", 
                        question_text="Past question.", 
                        days=-30, 
                        votes=0)
        question_two = create_question(question_name="question_two", 
                        question_text="Future question.", 
                        days=30, 
                        votes=0)
        response = self.client.get(reverse('qanda:index'))
        self.assertContains(response, question_one.question_name)

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question_one = create_question(question_name="question_one", 
                        question_text="Past question.", 
                        days=-30, 
                        votes=0)
        question_two = create_question(question_name="question_two", 
                        question_text="Future question.", 
                        days=-5, 
                        votes=0)
        response = self.client.get(reverse('qanda:index'))
        self.assertContains(response, question_one.question_name)
        self.assertContains(response, question_two.question_name)

class QuestionDetailViewTests(TestCase):
    
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_name="question_one", 
                                          question_text="Past question.", 
                                          days=30, 
                                          votes=0)
        url = reverse('qanda:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_name="question_one", 
                                        question_text="Past question.", 
                                        days=-5, 
                                        votes=0)
        url = reverse('qanda:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        
    def test_answer_created(self):
        """
        The detail view should display the question along with all answers 
        created for that question and the votes for each question 
        """
        some_question = create_question(question_name="question_one", 
                                        question_text="Past question.", 
                                        days=-30, 
                                        votes=5)
        answer_one = create_answer(question=some_question, answer_text="answer one")
        answer_two = create_answer(question=some_question, answer_text="answer two")
        url = reverse('qanda:detail', args=(some_question.id,))
        response = self.client.get(url)
        self.assertContains(response, some_question.question_text)
        self.assertContains(response, 5)
        self.assertContains(response, answer_one.answer_text)
        self.assertContains(response, answer_two.answer_text)             