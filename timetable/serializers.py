from rest_framework import serializers
from .models import Timetable

class TimetableSerializer(serializers.ModelSerializer):
    # Read-only fields to display related object's attributes
    teacher = serializers.ReadOnlyField(source='teacher.username')
    classroom = serializers.ReadOnlyField(source='classroom.name')
    block_name = serializers.ReadOnlyField(source='classroom.block.name')

    class Meta:
        model = Timetable
        fields = '__all__'

