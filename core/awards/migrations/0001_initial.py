# Generated by Django 5.0.6 on 2024-07-01 07:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('award_name', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award', to='core_actors.actor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
