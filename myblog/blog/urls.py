
from django.conf.urls import url,include
import blog.views as bv
urlpatterns = [
    url(r'^$',bv.index)#设置路由，匹配数字index/12
]