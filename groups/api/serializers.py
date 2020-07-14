from rest_framework import serializers
from groups.models import Group

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = [
            'pk',
            'slug',
            'name',
            'description',
        ]
