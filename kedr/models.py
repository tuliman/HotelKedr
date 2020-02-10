from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from time import time


# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(time())


class Apartment(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    room_value = models.CharField(max_length=100, db_index=True)
    description_title = models.TextField(blank=True, db_index=True)
    price = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True)
    apartment_obj = models.ManyToManyField('Photo', related_name='images')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('apartment_list_url', kwargs={'slug': self.slug})


class Photo(models.Model):
    img = models.ImageField(upload_to='media/apartment')


class ToBook(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    phone_number = models.CharField(max_length=20, db_index=True)
    description = models.TextField(db_index=True)
    reservation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('to_book_url')
