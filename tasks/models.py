from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True,blank=True)

    def __str__(self):
        return self.title

class OAuthKey(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OAuth Key (Created: {self.created_at})"

class GoogleOAuthKey(models.Model):
    name = models.CharField(max_length=255, help_text="Friendly name for this key configuration")
    client_id = models.CharField(max_length=255, help_text="Google OAuth Client ID")
    client_secret = models.CharField(max_length=255, help_text="Google OAuth Client Secret")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserInvitation(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=50, unique=True, blank=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(50)  # Generate a unique token
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email