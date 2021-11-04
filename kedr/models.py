import os

from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from time import time
from PIL import Image

# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(time())


class Apartment(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Уникальный индикатор',
                            help_text='Английскими буквами русские слова')
    room_value = models.CharField(max_length=100, verbose_name="Количество комнат")
    description_title = models.TextField(blank=True, verbose_name="Краткое описание")
    price = models.CharField(max_length=50, verbose_name="Стоимость Аренды")
    description = models.TextField(blank=True, verbose_name="Полное описание")
    images = models.ImageField(upload_to='apartment/', verbose_name="Изображение")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('apartment_list_url', kwargs={'slug': self.slug})


class Photo(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='apartment/')


class ToBook(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name="Телефонный номер", blank=True)
    description = models.TextField(db_index=True, verbose_name='Пожелания по подбору')
    reservation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('to_book_url')


class ApartmentReview(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя Фамилия Отчество', blank=True)
    review = models.TextField(verbose_name='Отзыв')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Комментарий добавлен')
