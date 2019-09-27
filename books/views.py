from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone

import datetime

from books.forms import BookEditForm, AuthorEditForm
from .helper import replacer
from .models import Book, Author


def index(request):
    new_books = Book.objects.filter(date__gte=timezone.now() - datetime.timedelta(days=15))
    context = {
        'new_books': new_books,
    }
    return render(request, 'books/index.html', context)


def books(request):
    all_books = Book.objects.all()

    context = {
        'all_books': all_books,
    }
    return render(request, 'books/books.html', context)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = replacer(request.GET['q'])
        results = Book.objects.filter(Q(title__icontains=q) | Q(writer__name__icontains=q)).distinct()

        context = {
            'q': q,
            'results': results,
            'count': len(results),
        }
        return render(request, 'books/results.html', context)
    else:
        return render(request, 'books/results.html')


def authors(request):
    all_authors = Author.objects.all().order_by('name')

    context = {
        'all_authors': all_authors,
    }
    return render(request, 'books/authors.html', context)


def author(request, slug):
    one_author = get_object_or_404(Author, slug=slug)
    books_of_author = Book.objects.filter(writer=one_author)

    context = {
        'author': one_author,
        'books_of_author': books_of_author
    }
    return render(request, 'books/author.html', context)


def book(request, slug):
    one_book = get_object_or_404(Book, slug=slug)
    if not request.session.get(str(one_book.id), False):
        request.session[str(one_book.id)] = True
        one_book.views_count += 1
        one_book.save()
    context = {
        'book': one_book,
    }
    return render(request, 'books/book.html', context)


@login_required
def edit_book(request, slug):
    one_book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        form = BookEditForm(request.POST, request.FILES, instance=one_book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(one_book.get_absolute_url())
    else:
        form = BookEditForm(instance=one_book)

    context = {
        'form': form,
        'book': one_book
    }
    return render(request, 'books/edit_book.html', context)


@login_required
def edit_author(request, slug):
    one_author = get_object_or_404(Author, slug=slug)
    if request.method == "POST":
        form = AuthorEditForm(request.POST, request.FILES, instance=one_author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(one_author.get_absolute_url())
    else:
        form = AuthorEditForm(instance=one_author)

    context = {
        'form': form,
        'author': one_author
    }
    return render(request, 'books/edit_author.html', context)


# Error handlers
def handler404(request, exception):
    response = render(request, "books/404.html")
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'books/500.html')
    response.status_code = 500
    return response
