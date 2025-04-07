from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, ReplyForm
from django.contrib.auth.decorators import login_required



def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/app/dashboard/' 
    



@login_required
def dashboard(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'questions': questions})

@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.created_by = request.user
            q.save()
            return redirect('dashboard')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

@login_required
def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.created_by = request.user
            answer.save()
            return redirect('dashboard')
    else:
        form = AnswerForm()
    return render(request, 'add_answer.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('dashboard')



@login_required
def add_reply(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.answer = answer
            reply.created_by = request.user
            reply.save()
            return redirect('dashboard')
    else:
        form = ReplyForm()
    return render(request, 'add_reply.html', {'form': form, 'answer': answer})

