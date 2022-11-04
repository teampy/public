from django.shortcuts import render

# Create your views here.
def home(r):
    return render (r,'home.html')
def contact(r):
    return render (r,'contact.html')