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

    def save_local_user(self):
        return self.save()

    @classmethod
    def get_all_local_users(cls):
        return cls.objects.all()

    @classmethod
    def delete_local_user(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_local_user_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def filter_local_user_by_name(cls, name):
        search_results = cls.objects.filter(name=name).all()
        return search_results


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

    def save_profile(self):
        return self.save()

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @classmethod
    def delete_profile(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_profile_by_website(cls, website):
        search_results = cls.objects.filter(website=website).all()
        return search_results


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local_user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, null=True)
    image_url = models.TextField(blank=False, null=True)
    # image = CloudinaryField('uploads/', null=True, blank=False)
    caption = models.CharField(max_length=199, blank=True)
    location = models.CharField(max_length=99, blank=True)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def save_post(self):
        return self.save()

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by("location")

    @classmethod
    def delete_post(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_posts_by_creator_id(cls, creator_id):
        search_results = cls.objects.filter(user__id=creator_id).all()
        return search_results

    @classmethod
    def filter_by_location(cls, location_str):
        filter_results = cls.objects.filter(location__icontains=location_str).all()
        return filter_results


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def add_like(self):
        return self.save()

    @classmethod
    def get_all_likes(cls):
        return cls.objects.all()

    @classmethod
    def delete_like(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_like_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def get_like_by_user_id(cls, id):
        return cls.objects.filter(user__id=id).all()

    @classmethod
    def filter_likes_by_post_id(cls, post_id):
        filter_results = cls.objects.filter(post__id=post_id).all()
        return filter_results


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
