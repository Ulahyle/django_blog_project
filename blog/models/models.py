from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    wrote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('report_post', 'can report post')
        ]

    def __str__(self):
        return f"{self.title}"

class SearchSubject(models.Model):
    CHOICES = (
        ('tag_name', 'Name Tag'),
        ('key_word', 'Key Word'),
        ('title', 'Title'),
    )
    custom_field = models.CharField(max_length=50, choices=CHOICES, default='tag_name')
class InputSearch(models.Model):
    custom_input = models.CharField(max_length=50)
class PostAuthor(models.Model):
    first_name = models.TextField(null=False, blank=False)
    last_name = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"author name is : {self.first_name} {self.last_name}"
class CustomPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField()
    rate = models.IntegerField(null=False, blank=False)
    tag = models.CharField(max_length=100, null=False, blank=False)
    authors = models.ManyToManyField(PostAuthor)
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.subject}"
        



