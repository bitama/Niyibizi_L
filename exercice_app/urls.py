from django.urls import path
from .import views

urlpatterns=[
    path("",views.index),
    path("trips/new",views.new_trip),
    path("trips/create",views.create_trip),
    path("trips/<int:trip_id>/delete",views.remove_trip),
    path("trips/<int:trip_id>/edit",views.edit_trip),
    path("trips/<int:trip_id>/update", views.update_trip),
    path("trips/<int:trip_id>/views",views.view_detail)
]