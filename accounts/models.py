from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
from markdown_deux import markdown
#from comments.models import Comment
from django.utils.safestring import mark_safe
from transliterate import translit, get_available_language_codes
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from pagedown.widgets import PagedownWidget
from django.contrib.postgres.fields import ArrayField

def upload_location(instance, filename):
    ProfileModel = instance.__class__
    new_id = ProfileModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.DecimalField(null = True, max_digits=3, decimal_places=0)
    school = models.TextField(blank = True,null = True)
    birthdate = models.DateField(null = True, blank = True)
    country = models.TextField(blank = True,null = True)
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field",)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    skills = ArrayField(ArrayField(models.TextField()), default=[['number theory', '0'], ['inequalities', '0'], ['polynoms', '0'], ['functions', '0']])
    number_theory_skills = ArrayField(ArrayField(models.TextField()), default=[['Четность', '0'], ['Делимость', '0'], ['Индукция', '0']])
    inequalities_skills = ArrayField(ArrayField(models.TextField()), default=[['AM-GM', '0'], ['Неравенство Коши', '0']])
    polynom_skills = ArrayField(ArrayField(models.TextField()), default=[['ФСУ', '0'], ['Замена переменных', '0']])
    function_skills = ArrayField(ArrayField(models.TextField()), default=[['Переменные', '0']])
    achievments = ArrayField(models.TextField(), default=['None'])
    class Meta:
        ordering = ["-rating"]


    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"user": self.user})

    """
    @property
    def comments(self):
        qs = Comment.objects.filter_by_author(self.user)
        return qs
    """
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()