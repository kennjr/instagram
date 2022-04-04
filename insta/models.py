from django.db import models


class User(models.Model):
    # We're using the default user model created by django
    username = models.CharField(max_length=44)
    name = models.CharField(max_length=88)
    email = models.EmailField(unique=True)
    password = models.TextField()
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} (@{self.username})'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='images')
    bio = models.TextField()
    website = models.CharField(max_length=99)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name}'

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
