from django.contrib.auth.models import User
from django.db import models
import uuid


class Question(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.CharField(max_length=200, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{}\n{}".format(self.question, self.user)

    def get_question_upvoters(self):
        return self.question_vote_set.all()

    def get_answers_to_question(self):
        return self.answer_set.all()


class Answer(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    answer = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{},{},{}".format(self.question, self.answer, self.user)

    def get_answer_upvoters(self):
        return self.answer_vote_set.all()

    def get_comments_for_answer(self):
        return self.comment_set.all()


class Question_Vote(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    votes = models.IntegerField(default=False)

    def __str__(self):
        return "{}, {}, {}".format(self.question, self.user, self.votes)


class Answer_Vote(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    votes = models.BooleanField(default=False)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False)
    comment = models.CharField(max_length=500, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)
