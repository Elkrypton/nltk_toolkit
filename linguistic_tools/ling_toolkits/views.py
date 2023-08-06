from django.shortcuts import render
from tools import stemmer
# Create your views here.


def index(request):
    return render('index.html', request)

def stemmer(request)