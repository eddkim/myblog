from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.post_create, name='post_create'),
    path('introduce/', views.introduce, name='introduce'),
    path('introduce2/', views.introduce2, name='introduce2'),
    path('introduce3/', views.introduce3, name='introduce3'),
    path('introduce4/', views.introduce4, name='introduce4'),

]