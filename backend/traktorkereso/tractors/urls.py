from django.urls import path

from . import views

urlpatterns = [
    path('tractors/<int:tractor_id>/ratings/<str:username>', views.Tractors.as_view(), name='tractors'),
] 