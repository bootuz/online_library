import os

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .helper import rename_and_path


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Author\'s name')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    photo = models.FileField(upload_to='author_photos', blank=True, verbose_name='Photo')
    bio = models.TextField(default='', blank=True, verbose_name='BIO')
    born_date = models.CharField(max_length=100, default='', blank=True, verbose_name='Birthday')
    death_date = models.CharField(max_length=100, default='', blank=True, verbose_name='Day of death')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Genre')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['title']

    def __str__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=200, verbose_name='Publisher')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        ordering = ['title']

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Book title')
    slug = models.SlugField(unique=True, max_length=100, verbose_name='URL')
    cover = models.FileField(upload_to=rename_and_path, blank=True, storage=OverwriteStorage(), verbose_name='Cover')
    e_pub = models.FileField(upload_to=rename_and_path, blank=True, storage=OverwriteStorage(), verbose_name='EPUB')
    pdf = models.FileField(upload_to=rename_and_path, blank=True, storage=OverwriteStorage(), verbose_name='PDF')
    isbn = models.CharField(max_length=100, blank=True, verbose_name='ISBN')
    annotation = models.TextField(default='', blank=True, verbose_name='Annotation')
    published = models.DateField(blank=True, verbose_name='Book publication date')
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Publisher')
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Genre')
    writer = models.ManyToManyField(Author, blank=True, verbose_name='Author')
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='Date')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-date']

    def __str__(self):
        return self.title
