from django.urls import path
from .views import register_view ,home_view, LoginView , dashboard , add_question ,add_answer,like_answer, add_reply
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-question/', add_question, name='add_question'),
    path('answer/<int:question_id>/', add_answer, name='add_answer'),
    path('like/<int:answer_id>/', like_answer, name='like_answer'),
    path('reply/<int:answer_id>/', add_reply, name='add_reply'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
]