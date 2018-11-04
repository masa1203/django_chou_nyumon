from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    params = {
        'title':'Hello/index',
        'msg':'this is sample page.',
        'goto':'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'this is next page.',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)