
from django.contrib import admin
from django.urls import path, include
from tasks.views import (
    register_with_token,
    GenericTaskView,
    GenericTaskCreateView,
    GenericTaskUpdateView,
    GenericTaskDeleteView,
)

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Google Authentication via django-allauth
    path('accounts/', include('allauth.urls')),
    
    # Task Management
    path('', GenericTaskView.as_view(), name='task_list'),
    path('create-task/', GenericTaskCreateView.as_view(), name='task_create'),
    path('update-task/<int:pk>/', GenericTaskUpdateView.as_view(), name='task_update'),
    path('delete-task/<int:pk>/', GenericTaskDeleteView.as_view(), name='task_delete'),
    path('register/<str:token>/', register_with_token, name='register_with_token'),
]
