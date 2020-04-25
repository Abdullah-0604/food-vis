from django.shortcuts import render

def home(request):
    return render(request,"food_vis/home.html",{})

def about(request):
    return render(request,"food_vis/about.html",{})

def record(request):
    return render(request,"food_vis/record.html",{})

def province(request):
    return render(request,"food_vis/province.html",{})

def visualization(request):
    return render(request,"food_vis/visualization.html",{})

def feedback(request):
    return render(request,"food_vis/feedback.html",{})




    
