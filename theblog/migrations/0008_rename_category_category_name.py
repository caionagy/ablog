# Generated by Django 4.0.3 on 2022-03-30 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_category_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
