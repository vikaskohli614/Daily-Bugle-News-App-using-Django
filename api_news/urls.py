from django import views
from django.urls import path
from api_news import views

urlpatterns = [
    path("",views.home, name='home'),
]

#Your API key is: cd43a137c659423f961a90a3e8ead57f