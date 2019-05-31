from books.models import Book, Author
from django.forms import ModelForm, TextInput, Textarea, FileInput


class BookEditForm(ModelForm):

    class Meta:
        model = Book
        exclude = ['date', 'genre', 'writer', 'publisher', 'published']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Book title'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'isbn': TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'annotation': Textarea(attrs={'class': 'form-control'}),
        }


class AuthorEditForm(ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Author\'s name'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'bio': Textarea(attrs={'class': 'form-control'}),
            'born_date': TextInput(attrs={'class': 'form-control', 'placeholder': 'Born date'}),
            'death_date': TextInput(attrs={'class': 'form-control', 'placeholder': 'Death date'}),
        }