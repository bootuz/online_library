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
    path('404/', views.handler404, name='error')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

