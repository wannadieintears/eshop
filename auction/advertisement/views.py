from django.shortcuts import render
from bboard.models import Bboard


def index(request, pk):
    bb = Bboard.objects.filter(id=pk)
    context = {'bb': bb}
    return render(request, 'advertisement/advertisement.html', context)
