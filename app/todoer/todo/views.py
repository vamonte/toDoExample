from rest_framework.viewsets import ModelViewSet
from todo.serializers import TodoSerializer
from todo.models import Todo


class TodoViewset(ModelViewSet):
    serializer_class = TodoSerializer
    ordering = ('title',)
    queryset = Todo.objects.all()
