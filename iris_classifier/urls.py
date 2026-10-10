from django.urls import path
from . import views


urlpatterns = [
    path('', views.iris_home, name='iris_home')
]