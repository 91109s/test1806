from django.db import models
class wife(models.Model):
    pass
class Husband(models.Model):
    #删除一个时，也会删除具有wife属性的
    wife = models.OneToOneField(wife, on_delete=models.CASCADE)

class Mather(models.Model):
    pass
class Father(models.Model):#设置wife属性不删除
    wife = models.OneToOneField(Mather, on_delete=models.DO_NOTHING)





