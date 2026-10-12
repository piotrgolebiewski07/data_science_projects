import joblib
import pandas as pd

from django.shortcuts import render
from django.conf import settings


model = joblib.load(settings.BASE_DIR / "notebooks_and_models" / "iris" / "iris_model.pkl")


def iris_home(request):
    prediction = None

    if request.method == "POST":
        try:
            sepal_length = float(request.POST.get("sepal_length"))
            sepal_width = float(request.POST.get("sepal_width"))
            petal_length = float(request.POST.get("petal_length"))
            petal_width = float(request.POST.get("petal_width"))
        except (ValueError, TypeError):
            return render(
                request,
                "iris_classifier/iris.html",
                {"error": "Podaj poprawne liczby we wszystkich czterech polach."}
            )

        if min(sepal_length, sepal_width, petal_length, petal_width) <= 0:
            return render(
                request,
                "iris_classifier/iris.html",
                {"error": "Wymiary muszą być większe do 0."}
            )

        features = pd.DataFrame(
            [[sepal_length, sepal_width, petal_length, petal_width]],
            columns=model.feature_names_in_)

        prediction = model.predict(features)[0]
        species = ["Iris setosa", "Iris versicolor", "Iris virginica"]
        prediction = species[int(prediction)]

    return render(
        request,
        "iris_classifier/iris.html",
        {
            "prediction": prediction,
            "values": request.POST
        }
    )

