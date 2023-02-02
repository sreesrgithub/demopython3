from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.
def home(request):
    return render(request, 'home.html')


def index(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, 'index.html', {'result1': obj1, 'result2': obj2})
