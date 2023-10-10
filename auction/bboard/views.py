from django.shortcuts import render
from .models import Bboard


def index(request):
    bb = Bboard.objects.all()
    context = {'bb': bb}
    return render(request, 'bboard/bboard.html', context)
