from django.urls import path
from .views import ProductViews

urlpatterns = [
    path('product_items/', ProductViews.as_view()),
    path('product_items/<int:id>', ProductViews.as_view())
]
