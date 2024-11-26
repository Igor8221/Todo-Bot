from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_list, task_create, task_edit, task_delete
from django.urls import path

# Создание роутера для API
router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

# Объединённые маршруты
urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('<int:pk>/edit/', task_edit, name='task_edit'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
] + router.urls


