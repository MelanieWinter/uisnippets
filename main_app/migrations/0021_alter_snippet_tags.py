# Generated by Django 5.0 on 2023-12-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_snippet_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main_app.tag'),
        ),
    ]
