from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='rci-index'),
    path('load-rci-data/', views.loadRCIData, name='load-rci-data')
]