from django.shortcuts import render

def home(request):
    return render(request,"food_vis/home.html",{})

def about(request):
    return render(request,"food_vis/about.html",{})

def record(request):
    return render(request,"food_vis/record.html",{})

def province1(request):
    return render(request,"food_vis/province1.html",{})

def province2(request):
    return render(request,"food_vis/province2.html",{})
    
def province3(request):
    return render(request,"food_vis/province3.html",{})
    
def province4(request):
    return render(request,"food_vis/province4.html",{})
    
def province5(request):
    return render(request,"food_vis/province5.html",{})
    

def visualization(request):
    return render(request,"food_vis/visualization.html",{})

def feedback(request):
    return render(request,"food_vis/feedback.html",{})
        




    
