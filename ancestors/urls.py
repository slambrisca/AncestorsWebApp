from django.urls import path
from . import views

urlpatterns = [
    path("show/person/<int:person_id>",views.show_person, name='show_person'),
    path("show/person/<int:person_id>/file/<int:file_id>",views.show_file, name='show_file'),
    path("",views.index, name='index')
]