from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('education', views.education, name='education'),
    path('hobbies', views.hobbies, name='hobbies'),
    path('posts', views.posts, name='posts'),
    path('makepost', views.makepost, name='makepost'),
]