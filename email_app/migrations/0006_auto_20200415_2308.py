# Generated by Django 2.2.12 on 2020-04-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0005_email_bool'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='SendEmail',
        ),
    ]
