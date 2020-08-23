from django.urls import path
from trip import views

urlpatterns = [
  path('list/', views.TravelView.as_view(), name='list-travels'),
  path('details/<int:pk>/', views.TripDetailView.as_view(), name='details-travel')
]
