from django.contrib import admin
from .models import Author, Book, Genre, Publisher


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'published', 'date']
    filter_horizontal = ['writer']
    autocomplete_fields = ['publisher', 'genre']


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)
