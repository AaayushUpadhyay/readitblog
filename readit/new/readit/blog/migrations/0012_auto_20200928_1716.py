# Generated by Django 3.0.7 on 2020-09-28 11:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200928_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default=True, null=True),
        ),
    ]
