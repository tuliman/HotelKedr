from django.contrib.sitemaps import Sitemap
from .models import Apartment
from django.shortcuts import reverse


class ApartmentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Apartment.objects.all()


    def location(self, obj):
        return reverse('apartment_detail_url', args=[str(obj.slug)])
