from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ('pk', 'created_at')
        fields = ('pk', 'title', 'created_at', 'status', 'comment')
