from django.db import models
from django.contrib.auth import get_user_model

# User model.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    facebook = models.URLField(max_length=250, null=True, blank=True)
    instagram = models.URLField(max_length=250, null=True, blank=True)
    twitter = models.URLField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(max_length=250, null=True, blank=True)
    youtube = models.URLField(max_length=250, null=True, blank=True)
    github = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username