from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    # author = models.ForeignKey('settings.AUTH_USER_MODEL')
    title = models.CharField(max_length=200)
    short_summary = models.CharField(max_length=200, validators=[MinValueValidator(140)])
    text = HTMLField()
    picture = models.ImageField()
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


