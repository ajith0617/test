from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    status_choice =[('C','Completed'),('P','Pending')]
    priority_choice =[('1','1'),('2','2'),('3','3')]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2 , choices=status_choice)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    priority = models.CharField(max_length=3 , choices=priority_choice)
