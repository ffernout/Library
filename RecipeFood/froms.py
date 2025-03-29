from django import forms
from django.shortcuts import get_object_or_404, render
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('title', 'description')

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'quantity', 'unit']


def ingredient_create(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return ('recipe_detail')
    else:
        form = IngredientForm()
    return render(request, 'recipes/ingredient_form.html', {'form': form, 'recipe': recipe})