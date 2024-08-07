import os
import uuid

from django.db import models

from core.abstract.models import AbstractModel


def actor_image_path(instance, filename):
    """
    Generate file path for new actor profile image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('actors', filename)


class Actor(AbstractModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    actor_photo = models.ImageField(null=True, upload_to=actor_image_path)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
