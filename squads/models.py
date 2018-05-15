from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
from markdown_deux import markdown
from homeworks.models import Homework
from django.utils.safestring import mark_safe
from transliterate import translit, get_available_language_codes

def upload_location(instance, filename):
    CourseModel = instance.__class__
    if CourseModel.objects.order_by("id").last():
        new_id = CourseModel.objects.order_by("id").last().id + 1
    else:
        new_id=0
    return "%s/%s" %(instance.id, filename)


class Squad(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.PROTECT)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='group_followers')
    followers_number = models.IntegerField(default=0)
    class Meta:
        ordering = ['-followers_number']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if not self.slug:
            self.slug = slugify(translit(self.title, 'ru', reversed=True))
        return reverse("squads:detail", kwargs={"slug": self.slug})
    
    def get_delete_url(self):
        return reverse("squads:delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("squads:update", kwargs={"slug": self.slug})

    def get_list_url(self):
        return reverse("squads:list")

    def get_markdown(self):
        return mark_safe(markdown(self.content))

    def get_follow_url(self):
        return reverse("squads:follow-toggle", kwargs={"slug": self.slug})

  

    @property
    def tasks(self):
        qs = Homework.objects.filter_by_instance(self)
        return qs

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
    qs = Squad.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_course_receiver, sender=Squad)