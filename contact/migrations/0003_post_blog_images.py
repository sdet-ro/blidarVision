# Generated by Django 3.2.7 on 2022-02-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_images',
            field=models.ImageField(null=True, upload_to='media/blog_images'),
        ),
    ]