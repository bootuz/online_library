from django.urls import path
from . import views
from django.conf.urls.static import static
from library import settings

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('author/<slug:slug>', views.author, name='author'),
    path('book/<slug:slug>', views.book, name='book'),
    path('search/', views.search, name='search'),
    path('404/', views.handler404, name='error'),
    path('book/<slug:slug>/edit_book', views.edit_book, name='edit_book'),
    path('author/<slug:slug>/edit_author', views.edit_author, name='edit_author'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

