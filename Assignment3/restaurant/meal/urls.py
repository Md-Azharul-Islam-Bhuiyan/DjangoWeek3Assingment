from django.urls import path
from . import views

urlpatterns = [
    path('showitem/', views.showItem, name='showitem'),
]
