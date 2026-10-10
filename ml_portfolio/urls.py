from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Gdy użytkownik wejdzie na: iris/ Dajngo odeśle go do pliku urls w iris_classifier
    path('iris', include('iris_classifier.urls'))
]
