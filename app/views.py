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
            login(request, user)  # auto-login after register
            return redirect('login')  # Change as needed
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/app/dashboard/'  # or use reverse('question_list')
    



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



# {% extends 'base.html' %}
# {% block content %}
# <div class="container mt-5">
#     <h2 class="text-center mb-4">📋 Questions Feed</h2>

#     <div class="text-end mb-3">
#         <a href="{% url 'add_question' %}" class="btn btn-success">+ Ask a Question</a>
#     </div>

#     {% for question in questions %}
#         <div class="card mb-4 shadow-sm">
#             <div class="card-header bg-primary text-white">
#                 <strong>{{ question.title }}</strong><br>
#                 <small>Asked by {{ question.created_by.username }} on {{ question.created_at|date:"M d, Y" }}</small>
#             </div>
#             <div class="card-body">
#                 <p>{{ question.description }}</p>

#                 <hr>
#                 <h5>💬 Answers:</h5>

#                 {% for answer in question.answers.all %}
#                     <div class="border p-3 mb-3 rounded">
#                         <p>{{ answer.content }}</p>
#                         <small>— {{ answer.created_by.username }}</small>

#                         <div class="d-flex align-items-center gap-2 mt-2">
#                             <form method="post" action="{% url 'like_answer' answer.id %}">
#                                 {% csrf_token %}
#                                 <button class="btn btn-sm btn-outline-primary">👍 Like ({{ answer.total_likes }})</button>
#                             </form>
#                             <a href="{% url 'add_reply' answer.id %}" class="btn btn-sm btn-outline-secondary">↩️ Reply</a>
#                         </div>

#                         {% for reply in answer.replies.all %}
#                             <div class="mt-3 ms-4 border-start ps-3 text-muted">
#                                 <p class="mb-1">{{ reply.content }}</p>
#                                 <small>— {{ reply.created_by.username }}</small>
#                             </div>
#                         {% empty %}
#                             <div class="ms-4 mt-2 text-muted">No replies yet.</div>
#                         {% endfor %}
#                     </div>
#                 {% empty %}
#                     <p class="text-muted">No answers yet.</p>
#                 {% endfor %}

#                 <a href="{% url 'add_answer' question.id %}" class="btn btn-outline-secondary mt-2">➕ Answer This</a>
#             </div>
#         </div>
#     {% empty %}
#         <p>No questions found.</p>
#     {% endfor %}
# </div>
# {% endblock %}
