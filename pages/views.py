from django.shortcuts import render

def home(request):
    return render(request,"food_vis/home.html",{})

def about(request):
    return render(request,"food_vis/about.html",{})

def record(request):
    return render(request,"food_vis/record.html",{})

    
