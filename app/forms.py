from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Question, Answer, Reply


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']




class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
