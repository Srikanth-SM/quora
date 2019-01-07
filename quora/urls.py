"""quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from authenticate import views as auth_views
from quora import views

app_name = 'quora'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/question/<int:question_id>/',
         views.question_detail, name='question_detail'),
    path('home/ask_question/', views.ask_question, name='ask_question'),
    path('home/question/<int:question_id>/answer_question/',
         views.answer_question, name='answer_question'),
    path('home/question/<int:question_id>/answer/<int:answer_id>/comment/',
         views.comment_answer, name='comment_answer'),
    path('home/question/<int:question_id>/upvote/',
         views.vote_question, name='upvote_question'),
    path('home/question/<int:question_id>/downvote/',
         views.vote_question, name='downvote_question'),
    path('home/question/<int:question_id>/upvote/<int:answer_id>/',
         views.vote_answer, name='upvote_answer'),
    path('home/question/<int:question_id>/downvote/<int:answer_id>/',
         views.vote_answer, name='downvote_answer'),

]
