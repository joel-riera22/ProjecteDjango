from django.test import TestCase
from .models import Author, Post, Tag
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Anna", last_name="Martí", email="anna@example.com")
        self.tag = Tag.objects.create(caption="Django")

    def test_create_post(self):
        post = Post.objects.create(
            title="Test Post",
            excerpt="Test excerpt",
            image_name="test.jpg",
            date=timezone.now(),
            slug="test-post",
            content="Contingut de prova",
            author=self.author
        )
        post.tags.add(self.tag)
        self.assertEqual(post.author.email, "anna@example.com")
        self.assertIn(self.tag, post.tags.all())
