from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

def recipe_create(request):
    if request.method == 'POST':
        form = Recipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = Recipe()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('recipe_list')

def ingredient_create(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = Ingredient(request.POST)
        if form.is_valid():
            ingredient = form.save()
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', recipe_id=recipe.id)

    else:
        form = Ingredient()

    return render(request, 'recipes/ingredient_form.html', {'form': form, 'recipe': recipe})
