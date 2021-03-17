from django.urls import include, path
from rest_framework import routers
from .views import index, TodosViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
]
