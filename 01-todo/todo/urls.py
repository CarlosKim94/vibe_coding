from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todo_index"),
    path("new/", views.create_todo, name="todo_create"),
    path("<int:pk>/", views.detail, name="todo_detail"),
    path("<int:pk>/edit/", views.edit_todo, name="todo_edit"),
    path("<int:pk>/delete/", views.delete_todo, name="todo_delete"),
    path("<int:pk>/toggle/", views.toggle_resolved, name="todo_toggle"),
]
