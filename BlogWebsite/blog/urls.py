from django.urls import path
from . import views
urlpatterns = [
     path('', views.main, name='index'),
     path('users/', views.user, name='users'),
     path('blogs/', views.blogtitles, name='blogs'),
     path('comments/', views.comments, name='comments'),
     path('categories/', views.categories, name='categories'),
     path('blogs/blogdetails/<int:ID>', views.blogdetails, name='blogdetails'),
]
