from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('name')
    return render(request, 'home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})