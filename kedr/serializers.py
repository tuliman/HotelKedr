from rest_framework import serializers

from kedr.models import ApartmentReview


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentReview
        fields = ['name', 'review', "create_at"]

