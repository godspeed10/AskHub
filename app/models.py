from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_answers", blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Answer by {self.created_by.username} to {self.question.title}"


class Reply(models.Model):
    answer = models.ForeignKey(Answer, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.created_by.username} to Answer ID {self.answer.id}"
