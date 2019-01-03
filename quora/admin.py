from django.contrib import admin
from quora.models import Question, Answer, Question_Vote, Answer_Vote, Comment

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Question_Vote)
admin.site.register(Answer_Vote)
admin.site.register(Comment)
