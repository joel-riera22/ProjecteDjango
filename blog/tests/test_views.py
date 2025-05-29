from django.urls import reverse
from django.test import TestCase
from .models import Author, Post
from django.utils import timezone

class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Marc", last_name="Ribas", email="marc@example.com")
        self.post = Post.objects.create(
            title="Vista Test",
            excerpt="...",
            image_name="test.jpg",
            date=timezone.now(),
            slug="vista-test",
            content="...",
            author=self.author
        )

    def test_post_detail_view(self):
        response = self.client.get(reverse("post-detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_author_detail_view(self):
        response = self.client.get(reverse("author-detail", args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)
