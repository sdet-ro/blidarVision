# Generated by Django 3.2.7 on 2021-10-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloaterMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phone', models.CharField(max_length=12, verbose_name='phone')),
            ],
        ),
    ]