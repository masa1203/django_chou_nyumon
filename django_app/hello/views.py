from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend

# Create your views here.

def index(request):
    data = Friend.objects.all().values()
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)