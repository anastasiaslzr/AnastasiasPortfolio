from django.db import models

# Create your models here.
class PortfolioItem (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200, default="google.com")
    #insert images
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Hobby(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #insert images
    image = models.ImageField(upload_to="hobbies/", blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"