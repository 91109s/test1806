from django.urls import path
from .views import weather,menu,images
urlpatterns = [
    path('rps', weather.helloworld),#设置路由，匹配数字index/12
    path('weather/', weather.getweather),#查询天气
    path('menu/', menu.get_menu),#获取列表
    path('image', images.getImagetol.as_view()),#获取目录图片
    path('imageUrl', images.getImageUrl), #imageUrl
]