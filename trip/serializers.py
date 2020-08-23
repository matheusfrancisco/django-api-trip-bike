from rest_framework import serializers

from trip.models import Trip


class TravelSerialization(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = [
            'id',
            'start_date',
            'end_date',
            'classification',
            'rate'
        ]

    def update(self, instance, validated_data):
        instance.rate = validated_data.get("rate", instance.rate)
        instance.classification = validated_data.get(
            "classification",
            instance.classification
        )
        return instance
