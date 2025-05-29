from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    image_name = models.ImageField(null=True)
    date = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="posts",
        null=True
    )

    tags = models.ManyToManyField(
        "Tag",
        related_name="posts"
    )

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.tag
