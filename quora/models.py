import uuid
import sys
import logging
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from authenticate.models import MyUser


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Question(models.Model):
    question = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):

        return mark_safe('{}<br/><sub><h6>{}, {}</sub></h6>'.format(self.question, self.created_at.strftime('%d/%b/%y'), self.user))

    def get_question_upvoters(self):
        return self.question_vote_set.filter(votes=1)

    def get_answers_to_question(self):
        return self.answer_set.all()


class Answer(models.Model):
    answer = models.CharField(max_length=3000, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return mark_safe("<b>{}</b>  <span style='float:inherit'><sub> --{}, {}</sub></span>".format(self.answer, self.created_at.strftime('%d/%b/%y'), self.user))

    def get_answer_upvoters(self):
        return self.answer_vote_set.filter(votes=1)

    def get_comments_for_answer(self):
        return self.comment_set.all()


class QuestionVote(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}, {}, {}".format(self.question, self.user, self.votes)


class AnswerVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    votes = models.IntegerField(default=0)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False)
    comment = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return mark_safe("{} <span style='float:right'><sub> -- {}, {}</span> ".format(self.comment, self.created_at.strftime('%d/%b/%y'), self.user))
