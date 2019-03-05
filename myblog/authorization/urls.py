from django.urls import path
from authorization import views
urlpatterns = [
    path('test', views.test_session),
    path('test2', views.test_getCooice)
]