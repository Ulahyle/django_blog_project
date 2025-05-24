from django.db import models


class SearchTag(models.Model):
    tag_name = models.CharField(max_length=50)
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


