from django.shortcuts import render
from rest_framework import status, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodosViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['post'])
    def pending(self, request, *args, **kwargs):
        return self.changeStatus(self, request, *args, **kwargs, status=False)

    @action(detail=True, methods=['post'])
    def complete(self, request, *args, **kwargs):
        return self.changeStatus(self, request, *args, **kwargs, status=True)

    def changeStatus(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.status = kwargs['status']
        todo.save()
        return Response(TodoSerializer(todo).data)

def index(request):
    return render(request, template_name='index.html')
