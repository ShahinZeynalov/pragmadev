# Generated by Django 2.2.12 on 2020-04-15 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailTemplate',
            new_name='Email',
        ),
    ]
