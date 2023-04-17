from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def details(request, question_id):
    return HttpResponse("<h2>You're looking at question </h2> %s." % question_id)