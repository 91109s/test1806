from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=25, db_index=True)#定义索引
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    focus_cities = models.TextField(default='[]')
    def __str__(self):
        return '%s' % (self.name)