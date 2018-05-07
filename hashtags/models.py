from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.utils import timezone


from django.utils.text import slugify
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from transliterate import translit, get_available_language_codes

from django.urls import reverse

from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import Profile

class Hashtag(models.Model):
    name = models.TextField(default = '')

    def url(self):
        return reverse("hashtags:thread", kwargs={"hashtag": self.name})
