# Generated by Django 5.0.6 on 2024-07-10 16:43

import core.movies.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_actors', '0001_initial'),
        ('core_directors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(default='', max_length=150, unique=True)),
                ('plot', models.TextField(default='', max_length=300)),
                ('poster', models.ImageField(null=True, upload_to=core.movies.models.movie_image_file_path)),
                ('released_year', models.DateField()),
                ('duration', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='movies', to='core_actors.actor')),
                ('directors', models.ManyToManyField(related_name='movies', to='core_directors.director')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-released_year'],
            },
        ),
    ]
