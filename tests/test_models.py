import os
import pytest
import random
from django.utils import timezone
from datetime import datetime
from django.db import IntegrityError, DataError
from django.contrib.auth.models import User
from authenticate.models import MyUser

from quora.models import *


@pytest.fixture
# @pytest.mark.django_db
def testuser():
    user = MyUser.objects.create(username='testuser', password='test12345')
    return user


@pytest.fixture
# @pytest.mark.django_db
def question(testuser):
    question = Question.objects.create(question='random question?',
                                       user=testuser,
                                       )
    return question


@pytest.fixture
# @pytest.mark.django_db
def answer(testuser, question):
    answer = Answer.objects.create(
        question=question, user=testuser, answer='random answer',
        created_at=timezone.now())
    return answer


@pytest.fixture
# @pytest.mark.django_db(transaction=True)
def usercount():
    return MyUser.objects.all().count()


@pytest.fixture
# @pytest.mark.django_db(transaction=True)
def questioncount():
    return Question.objects.all().count()


# @pytest.mark.django_db
class Test_Question:
    def test_question_should_have_a_user(self, testuser, question):
        assert question.user == testuser

    def test_question_should_have_a_date(self, question):
        assert (question.created_at) != None

    def test_question_should_not_exceed_morethan_1000_chars(self, question):
        assert (len(question.question) <= 1000) == True

    def test_if_question_exceeds_1000_chars(self, testuser):
        question = """Choosing a great name for your startup is much trickier than most founders first believe. The best brand names wander into our subconscious, unnoticed. They assimilate smoothly into different parts of our lives and take on real meanings, whether you're talking about jumping into an Uber, going on a Tinder date or Whatsapping a friend.
                    Still, there is more to a great name than its just being memorable. A great name needs to offer the right foundation for a company to build upon. It also has to be available!

                    Here are some steps that might help in naming your startup:

                    1. Start by knowing your audience adasdasdasdasd.

                    Starting with a clear idea of exactly what message you want to send, and whom you want your brand to resonate with will help you first choose a style(preeminent, playful, pragmatic, modern, intriguing, powerful) which will be the north star through the road to choosing a brand name.

                    For example, if you are selling consumer-based products, and your target consumers are millennials, or generations Y or Z, you will have a bit more flexibility to think outside the box, with intriguing names like Urban Decay or playful names like Squatty Potty. However, if you are a corporate company aiming for baby boomers, you'd be smart to choose something more classic, like Stone Eagle Advisors or Zenith Capital."""

        with pytest.raises(DataError):
            Question.objects.create(question=question, user=testuser)

    def test_if_question_has_valid_user(self):
        usercount = MyUser.objects.all().count()

        with pytest.raises(IntegrityError):
            Question.objects.create(
                question='some question', user_id=usercount + 1)


class Test_Answer:

    def test_answer_should_have_a_user(self, testuser, answer, question):
        assert answer.user == testuser

    def test_answer_should_have_a_date(self, answer):
        assert (answer.created_at) != None

    def test_answer_should_not_exceed_morethan_3000_chars(self, answer):
        assert (len(answer.answer) <= 3000) == True

    def test_if_answer_exceeds_3000_chars(self, testuser, question):
        answer = """Choosing a great name for your startup is much trickier than most founders first believe. The best brand names wander into our subconscious, unnoticed. They assimilate smoothly into different parts of our lives and take on real meanings, whether you're talking about jumping into an Uber, going on a Tinder date or Whatsapping a friend.
                    Still, there is more to a great name than its just being memorable. A great name needs to offer the right foundation for a company to build upon. It also has to be available!

                    Here are some steps that might help in naming your startup:

                    1. Start by knowing your audience adasdasdasdasd.

                    Starting with a clear idea of exactly what message you want to send, and whom you want your brand to resonate with will help you first choose a style(preeminent, playful, pragmatic, modern, intriguing, powerful) which will be the north star through the road to choosing a brand name.

                    For example, if you are selling consumer-based products, and your target consumers are millennials, or generations Y or Z, you will have a bit more flexibility to think outside the box, with intriguing names like Urban Decay or playful names like Squatty Potty. However, if you are a corporate company aiming for baby boomers, you'd be smart to choose something more classic, like Stone Eagle Advisors or Zenith Capital.
                    Choosing a great name for your startup is much trickier than most founders first believe. The best brand names wander into our subconscious, unnoticed. They assimilate smoothly into different parts of our lives and take on real meanings, whether you're talking about jumping into an Uber, going on a Tinder date or Whatsapping a friend.
                    Still, there is more to a great name than its just being memorable. A great name needs to offer the right foundation for a company to build upon. It also has to be available!

                    Here are some steps that might help in naming your startup:

                    1. Start by knowing your audience adasdasdasdasd.

                    Starting with a clear idea of exactly what message you want to send, and whom you want your brand to resonate with will help you first choose a style(preeminent, playful, pragmatic, modern, intriguing, powerful) which will be the north star through the road to choosing a brand name.

                    For example, if you are selling consumer-based products, and your target consumers are millennials, or generations Y or Z, you will have a bit more flexibility to think outside the box, with intriguing names like Urban Decay or playful names like Squatty Potty. However, if you are a corporate company aiming for baby boomers, you'd be smart to choose something more classic, like Stone Eagle Advisors or Zenith Capital.
                    Choosing a great name for your startup is much trickier than most founders first believe. The best brand names wander into our subconscious, unnoticed. They assimilate smoothly into different parts of our lives and take on real meanings, whether you're talking about jumping into an Uber, going on a Tinder date or Whatsapping a friend.
                    Still, there is more to a great name than its just being memorable. A great name needs to offer the right foundation for a company to build upon. It also has to be available!

                    Here are some steps that might help in naming your startup:

                    1. Start by knowing your audience adasdasdasdasd.

                    Starting with a clear idea of exactly what message you want to send, and whom you want your brand to resonate with will help you first choose a style(preeminent, playful, pragmatic, modern, intriguing, powerful) which will be the north star through the road to choosing a brand name.

                    For example, if you are selling consumer-based products, and your target consumers are millennials, or generations Y or Z, you will have a bit more flexibility to think outside the box, with intriguing names like Urban Decay or playful names like Squatty Potty. However, if you are a corporate company aiming for baby boomers, you'd be smart to choose something more classic, like Stone Eagle Advisors or Zenith Capital.




                    """

        with pytest.raises(DataError):
            Answer.objects.create(
                answer=answer, user=testuser, question=question)

    def test_if_question_has_valid_user(self, question, usercount):

        with pytest.raises(IntegrityError):
            Answer.objects.create(
                answer='some answer', user_id=usercount+1, question=question)

    def test_if_question_has_valid_question(self, testuser, questioncount):

        with pytest.raises(IntegrityError):
            Answer.objects.create(
                answer='some answer', user=testuser, question_id=questioncount+1)


class TestQuestionVote:

    def test_if_questionvote_instance_is_created(self, question, testuser):
        q = QuestionVote.objects.get_or_create(
            question=question, user=testuser)
        assert q != None

    def test_if_Question_is_upvoted_successfully(self, question, testuser):
        q = QuestionVote.objects.get_or_create(
            question=question, user=testuser)[0]
        assert q.votes == 0
        q.upvote()
        assert q.votes == 1
        q.upvote()
        assert q.votes == 0

    def test_if_Question_is_downvoted_successfully(self, question, testuser):
        q = QuestionVote.objects.get_or_create(
            question=question, user=testuser)[0]
        assert q.votes == 0
        q.downvote()
        assert q.votes == -1
        q.downvote()
        assert q.votes == 0


class TestanswerVote:

    def test_if_answervote_instance_is_created(self, answer, testuser):
        a = AnswerVote.objects.get_or_create(
            answer=answer, user=testuser)
        assert a != None

    def test_if_answer_is_upvoted_successfully(self, answer, testuser):
        a = AnswerVote.objects.get_or_create(
            answer=answer, user=testuser)[0]
        assert a.votes == 0
        a.upvote()
        assert a.votes == 1
        a.upvote()
        assert a.votes == 0

    def test_if_answer_is_downvoted_successfully(self, answer, testuser):
        a = AnswerVote.objects.get_or_create(
            answer=answer, user=testuser)[0]
        assert a.votes == 0
        a.downvote()
        assert a.votes == -1
        a.downvote()
        assert a.votes == 0
