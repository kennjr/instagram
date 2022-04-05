from django.urls import path

from insta import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_method, name='logout_page'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('posts/<int:post_id>/', views.post_page, name='post_page'),
    path('users/<int:uid>/', views.profile, name='profile'),
    path('new_post/', views.new_post, name='new_post')
]
