import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'recipes_book/index.html')
