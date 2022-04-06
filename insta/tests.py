import os

from django.test import TestCase


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')
import django
django.setup()

from .models import User, Post, Like, Profile, LocalUser


# Create your tests here.
class PostTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        self.test_post = Post(user=self.test_user, image_url='galleria_imgs/hobbies_7.jpg',
                              location="test_loc", caption="The caption",
                              local_user=None)

    # testing instance
    def test_instance(self):
        img = self.test_post
        self.assertEqual(self.test_post, img)

    # testing save method
    def test_save_img_method(self):
        original_len = Post.get_all_posts()
        print(f'original len {len(original_len)}')
        self.test_post.save_post()
        new_len = Post.get_all_posts()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_img_method(self):
        self.test_post.save_post()
        original_len = Post.objects.all()
        print(f'the categorys are{len(original_len)}')
        Post.delete_post(self.test_post.id)
        new_len = Post.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_img_by_id_method(self):
        self.test_post.save_post()
        req_result = Post.get_post_by_id(self.test_post.id)
        self.assertTrue(req_result is not None)

    def test_search_posts_method(self):
        self.test_post.save_post()
        search_results = Post.search_posts_by_creator_id(self.test_user.id)
        print(f'The list length {len(search_results)}')
        self.assertTrue(search_results != [])

    def test_filter_posts_list_method(self):
        self.test_post.save_post()
        filter_results = Post.filter_by_location("Kileleshwa")
        print(f'The list length {len(filter_results)}')
        self.assertTrue(filter_results != [])


class LikeTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        self.test_post = Post(user=self.test_user, image_url='galleria_imgs/hobbies_7.jpg',
                              location="test_loc", caption="The caption",
                              local_user=None)

        self.test_like = Like(post=self.test_post, user=self.test_user)

    # testing instance
    def test_instance(self):
        like = self.test_like
        self.assertEqual(self.test_like, like)

    # testing save method
    def test_add_like_method(self):
        original_len = Like.get_all_likes()
        print(f'original len {len(original_len)}')
        self.test_post.save_post()

        self.test_like.add_like()
        new_len = Like.get_all_likes()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_like_method(self):
        self.test_post.save_post()
        self.test_like.add_like()
        original_len = Like.objects.all()
        print(f'the categorys are{len(original_len)}')
        Like.delete_like(self.test_like.id)
        new_len = Like.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_like_by_creator_id_method(self):
        self.test_post.save_post()
        self.test_like.add_like()
        req_result = Like.get_like_by_user_id(self.test_user.id)
        self.assertTrue(req_result is not None)

    def test_get_like_by_like_id_method(self):
        self.test_post.save_post()
        self.test_like.add_like()
        req_result = Like.get_like_by_id(self.test_like.id)
        self.assertTrue(req_result is not None)

    def test_filter_likes_list_method(self):
        self.test_post.save_post()
        self.test_like.add_like()
        filter_results = Like.filter_likes_by_post_id(self.test_post.id)
        print(f'The list length {len(filter_results)}')
        self.assertTrue(filter_results != [])


class ProfileTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        # self.test_local_user = Like(user=self.test_user, user=self.test_user)

        self.test_profile = Profile(user=self.test_user, profile_img='galleria_imgs/hobbies_7.jpg',
                                    bio="test_loc", website="Thewe.com",)


    # testing instance
    def test_instance(self):
        profile = self.test_profile
        self.assertEqual(self.test_profile, profile)

    # testing save method
    def test_save_profile_method(self):
        original_len = Profile.get_all_profiles()
        print(f'original len {len(original_len)}')
        self.test_profile.save_profile()

        new_len = Profile.get_all_profiles()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_profile_method(self):
        self.test_profile.save_profile()
        original_len = Profile.objects.all()
        print(f'the categorys are{len(original_len)}')
        Profile.delete_profile(self.test_profile.id)
        new_len = Profile.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_profile_by_id_method(self):
        self.test_profile.save_profile()
        req_result = Profile.get_profile_by_id(self.test_profile.id)
        self.assertTrue(req_result is not None)

    def test_search_profile_by_website_method(self):
        self.test_profile.save_profile()

        req_result = Profile.search_profile_by_website(self.test_profile.website)
        self.assertTrue(req_result is not None)


class LocalUserTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        # self.test_local_user = Like(user=self.test_user, user=self.test_user)

        self.test_local_user = LocalUser(user=self.test_user, email='email@email.com',
                                         name="test_loc")


    # testing instance
    def test_instance(self):
        l_user = self.test_local_user
        self.assertEqual(self.test_local_user, l_user)

    # testing save method
    def test_save_l_user_method(self):
        original_len = LocalUser.get_all_local_users()
        print(f'original len {len(original_len)}')
        self.test_local_user.save_local_user()

        new_len = LocalUser.get_all_local_users()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_l_user_method(self):
        self.test_local_user.save_local_user()
        original_len = LocalUser.objects.all()
        print(f'the categorys are{len(original_len)}')
        LocalUser.delete_local_user(self.test_local_user.id)
        new_len = LocalUser.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_l_user_by_id_method(self):
        self.test_local_user.save_local_user()
        req_result = LocalUser.get_local_user_by_id(self.test_local_user.id)
        self.assertTrue(req_result is not None)

    def test_filter_l_user_by_name_method(self):
        self.test_local_user.save_local_user()

        req_result = LocalUser.filter_local_user_by_name(self.test_local_user.name)
        self.assertTrue(req_result is not None)


