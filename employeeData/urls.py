from django.urls import path
from .views import EmployeeUploadView
from . import views

urlpatterns = [
    path('api/upload/', EmployeeUploadView.as_view(), name='upload'),
    path('data/', views.EmployeeListView.as_view()),
]
