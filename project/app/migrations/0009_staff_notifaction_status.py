# Generated by Django 4.2 on 2023-05-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_subject_created_at_staff_notifaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notifaction',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]