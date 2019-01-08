import os
import sys
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from quora.models import Question, Answer, Comment, QuestionVote, AnswerVote
from quora.forms import QuestionForm, AnswerForm, CommentForm

TEMPLATE_DIR = 'quora'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def home(request):
    template = os.path.join(TEMPLATE_DIR, 'home.html')
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, template, context)


@login_required
def question_detail(request, question_id):
    template = os.path.join(TEMPLATE_DIR, 'question_detail.html')
    logging.info("Inside question_detail view,{}".format(question_id))

    try:
        question_detail = Question.objects.get(id=question_id)
        context = {
            'question': question_detail
        }
        return render(request, template, context)
    except Question.DoesNotExist as e:
        messages.info(request, "The Question does not exist")
        return redirect("quora:home")


@login_required
def ask_question(request):
    template = os.path.join(TEMPLATE_DIR, 'ask_question.html')
    logging.info("Inside ask_question")
    question_form = None
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.cleaned_data['question']
            user = request.user
            user_question = Question(question=question, user_id=user.id)
            user_question.save()
            return redirect("quora:home")
        else:
            messages.info(request, question_form.errors)
            return redirect("quora:home")
    else:
        question_form = QuestionForm()
        # logging.debug(question_form)
    context = {"form": question_form}
    return render(request, template, context)


@login_required
def answer_question(request, question_id):
    template = os.path.join(TEMPLATE_DIR, 'answer_question.html')
    question_form = None
    try:
        question = Question.objects.get(id=question_id)
        if request.method == 'POST':
            import pdb
            pdb.set_trace()
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.cleaned_data['answer']
                user = request.user
                user_answer = Answer(
                    answer=answer, question_id=question_id, user_id=user.id)
                user_answer = user_answer.save()
                logging.debug(user_answer)
                return redirect("quora:home")
            else:
                messages.info(request, answer_form.errors)
                return redirect("quora:home")
        else:
            question_form = QuestionForm(instance=question)
        context = {"form": question_form}
        return render(request, template, context)
    except Answer.DoesNotExist:
        messages.info(request, "Question does not exist")
        return redirect("quora:home")


@login_required
def comment_answer(request, question_id, answer_id):
    template = os.path.join(TEMPLATE_DIR, 'comment_answer.html')
    answer_form = None
    try:
        answer = Answer.objects.get(id=answer_id, question_id=question_id)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            logging.debug("Inside comment_answer method POST")
            if comment_form.is_valid():
                comment = request.POST.get('comment')
                user = request.user
                user_comment = Comment(
                    comment=comment, answer_id=answer_id, user_id=user.id)
                user_comment.save()
                return redirect('quora:home')
            else:
                messages.info(request, comment_form.errors)
                return redirect("quora:home")
        else:
            answer_form = AnswerForm(instance=answer)
        context = {'form': answer_form}
        return render(request, template, context)
    except Answer.DoesNotExist:
        messages.info(request, "Answer does not exist")
        return redirect("quora:home")


@login_required
def vote_question(request, question_id):
    path = request.path
    user = request.user
    upvote = 'upvote' in path
    question_vote = None
    try:
        question_vote = QuestionVote.objects.get(
            user_id=user.id, question_id=question_id)
    except QuestionVote.DoesNotExist:
        question_vote = QuestionVote(
            user_id=user.id, question_id=question_id)
    finally:
        if question_vote.question.user_id != user.id:
            if upvote:
                question_vote.upvote()
            else:
                question_vote.downvote()
            question_vote.save()
            messages.success(request, "Question voted successfully")
        else:
            messages.error(request, "Question can't be upvoted by self")
        return redirect('quora:home')


@login_required
def vote_answer(request, question_id, answer_id):
    path = request.path
    user = request.user
    upvote = 'upvote' in path
    answer_vote = None
    try:
        answer_vote = AnswerVote.objects.get(
            user_id=user.id, answer_id=answer_id)
    except AnswerVote.DoesNotExist:
        answer_vote = AnswerVote(
            user_id=user.id, answer_id=answer_id)
    finally:
        if answer_vote.answer.user_id != user.id:
            if upvote:
                answer_vote.upvote()
            else:
                answer_vote.downvote()
            answer_vote.save()
            messages.success(request, "Answer voted successfully")
        else:
            messages.error(request, "Answer can't be upvoted by self")
        return redirect('quora:home')
