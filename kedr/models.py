from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from time import time


# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(time())


class Apartment(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, db_index=True)
    room_value = models.CharField(max_length=100)
    description_title = models.TextField(blank=True)
    price = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('apartment_list_url', kwargs={'slug': self.slug})


class Photo(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/apartment')


class ToBook(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100,verbose_name='Емеил')
    phone_number = models.CharField(max_length=20,verbose_name="Телефонный номер")
    description = models.TextField(db_index=True,verbose_name='Пожелания по подборуу')
    reservation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('to_book_url')
