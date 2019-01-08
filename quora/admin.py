from django.contrib import admin
from quora.models import Question, Answer, QuestionVote, AnswerVote, Comment

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionVote)
admin.site.register(AnswerVote)
admin.site.register(Comment)
