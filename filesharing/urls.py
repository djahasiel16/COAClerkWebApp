from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/',views.upload, name='upload_file'),
    path('upload-success/', views.success, name='upload_success'),
]