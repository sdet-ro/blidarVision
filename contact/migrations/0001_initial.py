# Generated by Django 3.2.7 on 2022-01-23 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=15)),
                ('year_of_birth', models.CharField(max_length=4)),
                ('english_level', models.CharField(choices=[('1', 'Începător'), ('2', 'Mediu'), ('3', 'Avansat')], max_length=20)),
                ('experience', models.CharField(choices=[('1', 'Nu'), ('2', 'Da, sub 6 luni'), ('3', 'Da, peste 6 luni')], max_length=20)),
                ('message', models.CharField(blank=True, max_length=5000, null=True)),
                ('facebook', models.CharField(default='N/A', max_length=5000)),
                ('instagram', models.CharField(default='N/A', max_length=5000)),
                ('date_sent', models.DateTimeField(auto_now=True, verbose_name='application_sent_time')),
            ],
        ),
        migrations.CreateModel(
            name='FloaterMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phone', models.CharField(max_length=12, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('name', models.CharField(max_length=60)),
                ('message', models.CharField(max_length=5000)),
                ('date_sent', models.DateTimeField(auto_now=True, verbose_name='message_sent_time')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1048)),
                ('slug', models.SlugField(max_length=1048)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
