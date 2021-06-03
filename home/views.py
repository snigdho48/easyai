from django.shortcuts import render

# Create your views here.

def index(request):  
    if request.user.is_authenticated:
        return render(request,'analytics/home.html',)
    else:
        return render(request,'home/index.html',)
        
    #return render(request,'home/index.html',)