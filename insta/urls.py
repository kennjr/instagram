from django.urls import path

from insta import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('users/<int:uid>/', views.profile, name='profile'),
]