from django.urls import path
from . import views


urlpatterns = [
    path('load-rci-data/', views.loadRCIData, name='load-rci-data')
]