from django.urls import path
from . import views


urlpatterns = [
    path("reviews/", views.ReviewListCreateView.as_view(), name="Review_create_list"),
    path("reviews/<int:pk>/", views.ReviewRetrieveUpdateDestroyView.as_view(), name="Review_detail")
]
