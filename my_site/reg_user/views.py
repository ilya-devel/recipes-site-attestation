from django.shortcuts import render
from . import forms
import logging


logger = logging.getLogger(__name__)

def reg(request):
    form = forms.RegUserForm()
    if request.method == 'POST':
        form = forms.RegUserForm(request.POST)
        if form.is_valid():
            logger.info('User created')
    context = {
        'form': form,
    }
    return render(request, 'registration/reg.html', context=context)
