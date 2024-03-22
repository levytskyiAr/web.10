from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb
def main(request, page = 1):
    db = get_mongodb()
    quotes = db.quotes.find()
    par_page = 10
    paginator = Paginator(list(quotes), par_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
     

def Jane_Austen(request):
    return render(request, 'quotes\austen.html')

def Albert_einstein(request):
    return render(request, 'quotes\einstein.html')

def Rowling(request):
    return render(request, 'quotes\rowling.html')

def Andre_Gide(request):
    return render(request, 'quotes\gide.html')

def Marilyn_Monroe(request):
    return render(request, 'quotes\monroe.html')

