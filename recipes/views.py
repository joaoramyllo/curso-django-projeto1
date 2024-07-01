from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "recipes/pages/home.html", context={"name": "João Ramyllo"})


def recipes(request, id):
    return render(
        request, "recipes/pages/recipe-view.html", context={"name": "João Ramyllo"}
    )
