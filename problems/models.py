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
from django.contrib.postgres.fields import ArrayField

from accounts.models import Profile
from hashtags.models import Hashtag

class ProblemManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return super(ProblemManager, self).filter(content_type=content_type, object_id= instance.id)

    def filter_by_author(self, author):
        return super(ProblemManager, self).filter(user=author)

    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(content__icontains=query)|
                         Q(hashtags__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class Problem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    content2 = models.TextField(default='')
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    level = models.IntegerField(default=1)

    objects = ProblemManager()
    hashtags= ArrayField(models.TextField(), default = [''])
    hashtag_list = models.ManyToManyField(Hashtag, related_name='problem_hashtags')

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("problems:detail", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("problems:delete", kwargs={"id": self.id})
    
    def get_profile(self):
        return reverse("accounts:profile", kwargs={"user":self.user})



class CheckProblem(models.Model):
    user = models.PositiveIntegerField(null = True)
    problem_id = models.PositiveIntegerField(null = True)
    actions = ArrayField(ArrayField(models.TextField()), default=[['first', 'first_hidden', 'not_in_task']])
    solved = models.BooleanField(default=False) 
    current_string = models.TextField(default = 'de')
    current_status = models.TextField(default = 'Wrong')
    current_input = models.TextField(default = '')
    current_output = models.TextField(default = '')

class Lemma(models.Model):
    name = models.TextField(default='')

class Theorem(models.Model):
    name = models.TextField(default='')



