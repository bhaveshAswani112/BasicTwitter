from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.show_tweets, name='tweets'),
    path('create/', views.create_tweet, name='create'),
    path('<int:tweetid>/edit/', views.edit_tweet, name='edit'),
    path('<int:tweetid>/delete/', views.delete_tweet, name='delete'), 
    path('register/', views.register, name='register'), 
]
