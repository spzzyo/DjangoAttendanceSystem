# Generated by Django 4.2 on 2023-05-11 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
