# Generated by Django 2.2.12 on 2020-04-15 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0007_auto_20200415_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendemail',
            old_name='html_template',
            new_name='message',
        ),
    ]
