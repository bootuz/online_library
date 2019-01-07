# Generated by Django 2.1.4 on 2019-01-07 22:19

import books.helper
import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190106_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='e_pub',
            field=models.FileField(blank=True, storage=books.models.OverwriteStorage(), upload_to=books.helper.rename_and_path, verbose_name='EPUB'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, storage=books.models.OverwriteStorage(), upload_to=books.helper.rename_and_path, verbose_name='PDF'),
        ),
    ]