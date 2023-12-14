import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'recipes_book/index.html')
