# Generated by Django 2.1.15 on 2020-06-13 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='actors',
            new_name='actor',
        ),
    ]
