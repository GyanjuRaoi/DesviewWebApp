from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Question(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='question', blank=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home-url")

class Comment(models.Model):

    content = models.TextField()
    commentDate = models.DateTimeField(default=timezone.now)
    upvote = models.IntegerField(null=True, default=0)
    image_comment = models.ImageField(upload_to='answer', blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("home-url")




    

    
    


