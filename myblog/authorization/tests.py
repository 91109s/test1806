import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")# project_name 项目名称
django.setup()
from django.test import TestCase
from authorization import models
# Create your tests here.
p = models.Users(name='lucy', address='jiujiangm', city='jiujiang', country='cn')
p.save()
#models.Users.objects.create(name='lucy', address='jiujiangm', city='jiujiang', country='cn')