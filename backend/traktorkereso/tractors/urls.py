from django.urls import path

from . import views

urlpatterns = [
    path('tractors/<int:tractor_id>', views.TractorView.as_view()),
    path('tractors/<int:tractor_id>/ratings/<str:username>', views.TractorView.as_view(), name='tractors'),
] 