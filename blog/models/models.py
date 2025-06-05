from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class SearchSubject(models.Model):
    CHOICES = (
        ('tag_name', 'Name Tag'),
        ('key_word', 'Key Word'),
        ('title', 'Title'),
    )
    Tag_field = models.CharField(max_length=50, choices=CHOICES, default='tag_name')
class InputSearch(models.Model):
    custom_input = models.CharField(max_length=50)
class VoteByUser(models.Model):
    CHOICES = (
        ('1', '1 star'),
        ('2', '2 stars'),
        ('3', '3 stars'),
        ('4', '4 stars'),
        ('5', '5 stars'),
    )
    custom_field = models.CharField(max_length=50, choices=CHOICES)
    id_field = models.IntegerField(null=False, blank=False,default=0)

class CustomPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(null=False, blank=False)
    tag = models.CharField(max_length=100, null=False, blank=False)
    authors = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    class Meta:
        permissions = [
            ('report_post', 'can report post')
        ]

    def __str__(self):
        return f"{self.title}"

class ReportPost(models.Model):
    post_title = models.CharField(max_length=100)
    reporter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_time = models.DateTimeField(auto_now_add=True)

class Contactmodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
        



