# Generated by Django 5.0 on 2023-12-27 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_rename_v_type_vote_vote_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='vote_type',
            new_name='type',
        ),
    ]
