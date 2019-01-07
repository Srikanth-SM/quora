from django.forms import ModelForm

from quora.models import Question, Answer, Comment


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question',)


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', 'question')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'answer')
