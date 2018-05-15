from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

import cloudinary


class Post(models.Model):
    # author = models.ForeignKey('settings.AUTH_USER_MODEL')
    title = models.CharField(max_length=200)
    short_summary = models.CharField(max_length=200, validators=[MinValueValidator(140)])
    text = HTMLField()
    picture = CloudinaryField('image')
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish():
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # @receiver(pre_delete, sender=Post)
    # def photo_delete(sender, instance, **kwargs):
    #     cloudinary.uploader.destroy(instance.picture.public_id)


