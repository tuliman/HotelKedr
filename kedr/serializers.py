from rest_framework import serializers

from kedr.models import ApartmentReview, ToBook


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentReview
        fields = ['name', 'review', "create_at"]


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToBook
        fields = ['name', 'email', 'phone_number', 'description', 'reservation_date']
