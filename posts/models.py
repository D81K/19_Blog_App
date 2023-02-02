from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    image = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now_add=True, null=False)
    status = models.CharField(max_length=10, null=False)
    slug = models.SlugField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)