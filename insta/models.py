from django.db import models
from django.contrib.auth.models import User


class LocalUser(models.Model):
    # We're using the default user model created by django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=88)
    email = models.EmailField(unique=True)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} (@{self.user})'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='images', blank=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=99, blank=True)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local_user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, null=True)
    image_url = models.TextField(blank=False, null=False)
    caption = models.CharField(max_length=199, blank=True)
    location = models.CharField(max_length=99, blank=True)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


# # Create your models here.
# class Message(models.Model):
#     # We're using the default user model created by django
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     body = models.TextField()
#     # The auto_now is updated every time a model item is updated/saved with new changes
#     updated = models.DateTimeField(auto_now=True)
#     # The auto_now_add is updated once, when the model item is created/added to the db
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.body[0:50]}'
#
