import logging
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from . import models
from random import choice

logger = logging.getLogger(__name__)


def index(request):
    recipes = models.Recipe.objects.all()
    result = []
    if len(recipes) > 5:
        while len(result) < 5:
            tmp = choice(recipes)
            if tmp not in result:
                result.append(tmp)
    else:
        result = recipes
    context = {
        'recipes': result,
    }
    return render(request, 'recipes_book/index.html', context=context)


def recipe_info(request, id: int):
    recipe = models.Recipe.objects.filter(pk=id).first()
    context = {
        'recipe': recipe
    }
    return render(request=request, template_name='recipes_book/recipe_info.html', context=context)
