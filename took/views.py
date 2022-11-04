from django.shortcuts import render
from django.contrib import messages
from .models import My

def home(r):
    return render (r,'home.html')

def contact(req):
    if req.method=='POST':
        if req.POST['email']and req.POST['password']:
       
           
            email=req.POST['email']
            password=req.POST['password']
            contact=My(email=email,password=password)
            # contact.email=req.POST['email']
            # contact.password=req.POST['password']     
           

            contact.save()
            messages.info(req,'Your Input is Received ,Thanks !')
            return render(req,'contact.html',{})
    else:
       
         return render (req,'contact.html',{})
