from __future__ import unicode_literals

from django.conf import settings

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
from accounts.models import Profile
from problems.models import Problem
from django.contrib.postgres.fields import ArrayField

class TaskManager(models.Manager):
    def all(self):
        return super(TaskManager, self)

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return super(TaskManager, self).filter(content_type=content_type, object_id= instance.id)

    def filter_by_author(self, author):
        return super(TaskManager, self).filter(user=author)

    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(content__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Task(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    problem_ids = ArrayField(models.IntegerField(), default=[])
    lecture_ids = ArrayField(models.IntegerField(), default=[])
    course_ids = ArrayField(models.IntegerField(), default=[])

    objects = TaskManager()

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return str(self.user.username)

    def get_delete_url(self):
        return reverse("tasks:delete", kwargs={"id": self.id})
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    @property
    def problems(self):
        qs = Problem.objects.filter_by_instance(self)
        return qs




