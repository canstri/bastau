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
from lectures.models import Lecture
from courses.models import Course
from django.contrib.postgres.fields import ArrayField

class TaskManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return super(TaskManager, self).filter(content_type=content_type, object_id= instance.id)

    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(content__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Homework(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    problemss = models.ManyToManyField(Problem, related_name='task_problems')
    lectures = models.ManyToManyField(Lecture, related_name='task_lectures')
    courses = models.ManyToManyField(Course, related_name='task_courses')

    objects = TaskManager()

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return str(self.user.username)

    def get_delete_url(self):
        return reverse("tasks:delete", kwargs={"id": self.id})

    def add_problem_url(self):
        return reverse("homeworks:add-problem-api-toggle", kwargs={"slug": self.slug})
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type




def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if not slug:
        slug = slugify(translit(instance.title, 'ru', reversed=True))
    if new_slug is not None:
        slug = new_slug
    qs = Homework.objects.filter(slug=slug).order_by("-id") 
    if qs.exists():
        new_slug = "%s-%s" %(slug, qs[0].id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Homework)


