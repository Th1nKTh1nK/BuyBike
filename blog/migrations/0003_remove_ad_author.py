# Generated by Django 2.2.6 on 2019-10-19 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_ad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='author',
        ),
    ]
