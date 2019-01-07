# Generated by Django 2.1.4 on 2019-01-07 22:26

import books.helper
import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190108_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, storage=books.models.OverwriteStorage(), upload_to=books.helper.rename_and_path, verbose_name='Cover'),
        ),
    ]