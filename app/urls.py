from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("read/", views.read, name='read'),
    path("create/", views.create, name='create'),
    path("deleted/", views.del_render, name='deleted'),
    path("update/", views.update, name='Update'),
    path("update_form/<int:student_id>", views.update_form, name='update_form'),
    path("delete/<int:student_id>", views.delete, name='delete')
]
