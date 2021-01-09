from django.shortcuts import render, redirect
from django import forms


class NewMealForm(forms.Form):
    title = forms.CharField(label="Meal title", required=True)


meals = [
    'Pierogi leniwe z bułką tartą, masłem i cukrem',
    'Karkówka z dynią, pomidorami',
    'Zupa krem z dyni',
    'Zupa krem z pomidorów',
    'Rosół',
    'Indyk z papryką i z kaszą pęczak',
    'Łazanki z kapustą i boczkiem',
    'Makaron z tuńczykiem',
    'Pizza',
    'Wątróbka drobiowa z cebulą',
    'Zupa ogórkowa',
    'Szakszuka'
]


def index(request):
    return render(request, 'meals/index.html', {"meals": meals})


def new_meal(request):
    form = NewMealForm()
    return render(request, 'meals/new_meal.html', {"form": form})


def add_meal(request):
    if request.method == "POST":
        form = NewMealForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if title not in meals:
                meals.append(title)
        return redirect("index")
    else:
        return redirect("new_meal")


def edit_meal(request, meal_id):
    if request.method == "POST":
        print(request.POST)
        form = NewMealForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            print(title)
        return redirect("index")
    else:
        meal = meals[meal_id]
        form = NewMealForm({"title": meal})
        return render(request, 'meals/edit_meal.html', {"form": form})
