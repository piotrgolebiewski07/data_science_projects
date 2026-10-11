from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Główna strona
    path('', views.main_home, name="main_home"),

    # Gdy użytkownik wejdzie na: iris/ Dajngo odeśle go do pliku urls w iris_classifier
    path('iris', include('iris_classifier.urls'))
]
'''<h1 class="display-4 fw-bold">Witaj w moim świecie Data Science</h1>
        <p class="lead text-light opacity-75">Interaktywny przegląd projektów opartych na Machine Learningu</p>'''