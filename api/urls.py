from django.urls import path
from api.views import ShelfIdentificationView

urlpatterns = [
    path('shelf-identifier/', ShelfIdentificationView.as_view()),
]
