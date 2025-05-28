from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.CharField(max_length=100)  # Helps with recommendations
    tags = models.ManyToManyField("Tag", blank=True)  # Keyword-based recommendations
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
