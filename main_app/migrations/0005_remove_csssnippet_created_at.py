# Generated by Django 5.0 on 2023-12-21 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_csssnippet_created_csssnippet_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csssnippet',
            name='created_at',
        ),
    ]
