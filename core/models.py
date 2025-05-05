from django.db import models

class User(models.Model):
    """User profile model to store user information and gallery images."""
    # Basic user information
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    skills = models.JSONField(default=list, blank=True)
    gallery_images = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
