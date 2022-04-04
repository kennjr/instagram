from django.urls import path

from insta import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('users/<int:uid>/', views.profile, name='profile'),
]