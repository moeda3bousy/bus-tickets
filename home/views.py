from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import RideForm

def available(request):
        if request.method == 'POST':
                form= RideForm(request.POST,request.FILES)
                if  form.is_valid():
                        form.save() 
                        return redirect('confirmation/')
                        if  form.save() :
                          form=  RideForm()
                          
        form= RideForm(request.POST,request.FILES)          
        context= {
                  'forms': form,
                   'available': Available.objects.all(),
                  }
                
        return render(request,'available.html', context)  


def thanks(request):
    
        context= {
             'pic':  Thanks.objects.all()
                  }
                
        return render(request,'thanks.html', context)  

     



