from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration.as_view(), name='registration'),
    path('details/<int:id>', views.resume_details, name='details'),
    path('download/<int:id>', views.download, name='download'),
]