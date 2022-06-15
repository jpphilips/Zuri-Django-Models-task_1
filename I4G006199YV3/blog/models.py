from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# Post

# --------

# Title: A string of maxlength 200, use Django’s models.CharField


# Text: Any amount of text, use Django’s TextField


# Author: A Foreign Key to the current user model. Make use of Django’s get_user_model function.


# Created_date: A date-time column, use Django’s models.DateTimeField.


# Published_date: A date-time column, use Django’s models.DateTimeField.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.Title
