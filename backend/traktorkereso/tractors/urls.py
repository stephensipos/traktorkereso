from django.urls import path

from . import views

urlpatterns = [
    path('compare', views.Compare.as_view()),
    path('tractors', views.TractorList.as_view()),
    path('tractors/<int:tractor_id>', views.TractorView.as_view()),
    path('tractors/<int:tractor_id>/ratings/<str:username>', views.RatingView.as_view(), name='tractors'),
] 