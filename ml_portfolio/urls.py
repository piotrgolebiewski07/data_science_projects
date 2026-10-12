from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Główna strona
    path('', views.main_home, name="main_home"),

    # Gdy użytkownik wejdzie na: iris/ Django odeśle go do pliku urls w iris_classifier
    path('iris/', include('iris_classifier.urls'))
]
