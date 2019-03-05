from django.db import models
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default="title")
    content = models.TextField(null=True) #内容
# Create your models here.
