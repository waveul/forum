from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Thread(models.Model):
    Tittle = models.CharField(max_length=150)
    Content = models.TextField(blank=False, null=False, max_length=10000)
    Time_Created = models.DateTimeField(auto_now_add=True)
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Tittle


class Post(models.Model):
    Content = models.CharField(blank=False, null=False, max_length=300)
    Time_Created = models.DateField(auto_now_add=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    ThreadID = models.ForeignKey(Thread, on_delete=models.CASCADE)
