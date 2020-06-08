from django.contrib import admin

from .models import Apartment, Photo, ToBook

# Register your models here.


admin.site.register(Photo)
admin.site.register(ToBook)


class AdditionalImgLine(admin.TabularInline):
    model = Photo


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'room_value', 'description_title', 'price', 'description')
    fields = ('name', 'room_value', 'description_title', 'price', 'description', 'images')
    inlines = (AdditionalImgLine,)


admin.site.register(Apartment,ApartmentAdmin)
