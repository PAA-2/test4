from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('actions/', views.actions_view, name='actions'),
    path('kanban/', views.kanban_view, name='kanban'),
    path('actions/<int:pk>/', views.action_detail, name='action_detail'),
]
