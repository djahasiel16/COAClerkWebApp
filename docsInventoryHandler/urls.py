from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="docsInventoryIndex"),
    path('update-document/<int:pk>/edit/', views.update_document, name='update-document'),
    path('filtered/', views.apply_filter, name='apply_filter'),
]