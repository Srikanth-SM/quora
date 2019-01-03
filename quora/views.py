import os
from django.shortcuts import render, redirect
from quora.models import Question, Answer, Comment

TEMPLATE_DIR = 'quora'


def home(request):
    template = os.path.join(TEMPLATE_DIR, 'home.html')
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, template, context)
