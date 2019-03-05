from django.urls import path, include
urlpatterns = [
    path('service/', include('blog.api.urls')),
    path('auth/', include('authorization.urls')),
]