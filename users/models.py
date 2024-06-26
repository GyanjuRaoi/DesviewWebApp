from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile',  blank=True)
    profession = models.CharField(max_length=50, default=' ')

    def __str__(self):
        return self.user.username

    
    

class Friends(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name='users_friends')

    def __str__(self):
        return self.user.username

    def add_friend(self, friend):
        if hasattr(self, 'friends') and friend != self:
            self.friends.add(friend)

    def remove_friend(self, friend):
        if hasattr(self, 'friends'):
            self.friends.remove(friend)

    





