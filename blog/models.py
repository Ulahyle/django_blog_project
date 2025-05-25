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
