# Generated by Django 4.2.21 on 2025-05-27 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_imatge_post_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='email',
            new_name='email_address',
        ),
    ]
