# Generated by Django 5.0.6 on 2024-07-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_actors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='updated',
            new_name='updated_at',
        ),
    ]