from cProfile import label
from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from enum import Enum


class User(AbstractUser):
    pass


class Gallery(models.Model):
    video = models.FileField(upload_to="gallery/videos", null=True, blank=True)
    image = models.ImageField(
        upload_to="gallery/images", null=True, blank=True)


class Settings(models.Model):

    key = models.CharField(max_length=255, null=False, blank=False)
    value = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="settings/images", null=True, blank=True)
    file = models.FileField(upload_to="settings/files", null=True, blank=True)


class Newsletter(models.Model):

    email = models.EmailField()


class Contact(models.Model):

    class DepartmentChoices(models.TextChoices):
        OPERATIONS = 'operations', 'Operations'

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    department = models.CharField(
        max_length=100, choices=DepartmentChoices.choices)
    message = models.TextField()


class Clients(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="clients", null=False, blank=False)


class Slider(models.Model):

    class PosistionChoices(models.TextChoices):
        left = "left", "Left"
        right = "right", "Right"
        center = "center", " Center"

    image = models.ImageField(
        upload_to="slides/images", null=False, blank=False)
    video = models.FileField(upload_to="slides/videos", null=True, blank=True)
    headline = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    is_video = models.BooleanField(default=False)
    action_text = models.CharField(max_length=30, null=True, blank=True)
    action_link = models.CharField(
        max_length=500, default="#", null=True, blank=True)
    content_position = models.CharField(
        max_length=20, choices=PosistionChoices.choices, default=PosistionChoices.left)


class Page(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, editable=True)
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField()

    # ------------seo----------

    # description = models.TextField(null=True, blank=True)
    # keywords = models.CharField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    def get_parent_path(self, list=None):

        parenturl = []

        if list is not None:
            parenturl = list

        if self.parent is not None:
            parenturl.insert(0, self.parent.slug)
            return self.parent.get_parent_path(parenturl)

        return parenturl

    def get_absolute_url(self):

        path = ''

        if self.parent is not None:
            parentlisting = self.get_parent_path()
            for parent in parentlisting:
                path = path + parent + '/'

        path = path + self.slug

        return reverse("website:page", kwargs={"path": path, "slug": self.slug})


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    designation = models.CharField(max_length=100, null=False, blank=False)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="team", null=False, blank=False)

    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    dribble = models.CharField(max_length=255, null=True, blank=True)


# class Menu(models.Model):
#     name = models.CharField(max_length=100, null=False, blank=False)
#     pages = models.ManyToManyField(Page)


# class MenuPage(models.Model):
#     pages = models.ManyToManyField(Page)

class JobApplication(models.Model):

    class MaritalStatus(models.TextChoices):

        single = "single", "Single"
        married = "married", "Married"

    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    marital_status = models.CharField(
        max_length=15, null=True, blank=True, choices=MaritalStatus.choices)

    eduction_highest = models.CharField(
        "Education Highest", max_length=255, null=True, blank=True)
    eduction_second_highest = models.CharField(
        "Education Second Highest", max_length=255, null=True, blank=True)

    employer_1 = models.CharField(max_length=100, null=True, blank=True)
    designation_1 = models.CharField(max_length=100, null=True, blank=True)
    experience_1 = models.TextField(null=True, blank=True)

    employer_2 = models.CharField(max_length=100, null=True, blank=True)
    designation_2 = models.CharField(max_length=100, null=True, blank=True)
    experience_2 = models.TextField(null=True, blank=True)

    employer_3 = models.CharField(max_length=100, null=True, blank=True)
    designation_3 = models.CharField(max_length=100, null=True, blank=True)
    experience_3 = models.TextField(null=True, blank=True)

    audio = models.FileField(upload_to='applications/audio/', blank=True, null=True)
    cv = models.FileField(upload_to='applications/resumes/', blank=False, null=False)
