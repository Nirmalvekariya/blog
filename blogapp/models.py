import itertools
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.urls import reverse
from datetime import datetime, date
from django.utils.text import slugify
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, editable=False)
    image = models.ImageField(upload_to='post_image')
    body = HTMLField()
    slug = models.SlugField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Post.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('index')

    def save(self, *args, **kwargs):
        self._generate_slug()
        super(Post, self).save(*args, **kwargs)
        imag = Image.open(self.image.path)
        imag = imag.resize((500, 280))
        imag.save(self.image.path)


class PostManager(models.Manager):
    def get_queryset(self, request):
        query = Post.objects.filter(author=request.user)
        if request.user.is_superuser:
            query = Post.objects.all()
        return query
