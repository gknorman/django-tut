from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    # return "<h1>Hello World</h1>" # String of HTML 
    return HttpResponse("<h1>Hello World</h1>")