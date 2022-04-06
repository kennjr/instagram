import os

from django.test import TestCase


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')
import django
django.setup()

from .models import User, Post


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


