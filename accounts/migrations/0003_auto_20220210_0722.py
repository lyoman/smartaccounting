# Generated by Django 3.2.11 on 2022-02-10 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='designation',
            new_name='business',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
