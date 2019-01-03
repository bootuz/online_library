# Generated by Django 2.1.4 on 2019-01-01 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Author's name")),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('photo', models.FileField(blank=True, upload_to='author_photos', verbose_name='Photo')),
                ('bio', models.TextField(blank=True, default='', verbose_name='BIO')),
                ('born_date', models.CharField(blank=True, default='', max_length=100, verbose_name='Birthday')),
                ('death_date', models.CharField(blank=True, default='', max_length=100, verbose_name='Day of death')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Book title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('cover', models.FileField(blank=True, upload_to='covers', verbose_name='Cover')),
                ('e_pub', models.FileField(blank=True, upload_to='epub', verbose_name='EPUB')),
                ('pdf', models.FileField(blank=True, upload_to='pdf', verbose_name='PDF')),
                ('isbn', models.CharField(blank=True, max_length=100, verbose_name='ISBN')),
                ('annotation', models.TextField(blank=True, default='', verbose_name='Annotation')),
                ('publisher', models.CharField(blank=True, max_length=250, null=True, verbose_name='Publisher')),
                ('published', models.DateField(blank=True, verbose_name='Book publication date')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Genre')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ManyToManyField(blank=True, to='books.Author', verbose_name='Author'),
        ),
    ]
