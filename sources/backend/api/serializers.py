from rest_framework import serializers
from backend.api.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name', 'date', 'isComplete')