from django.shortcuts import render,HttpResponse
from .models import Car
from .forms import CarForm
# Create your views here.

def index(request):
    #if the user submitted a post
    if request.method == 'POST':
        form=CarForm(request.POST)
        #if there are no errors create the post , create a new car model and go to the victory page
        if form.is_valid():
            Car.objects.create(make=request.POST['make'],model=request.POST['model'],year=request.POST['year'],mph=request.POST['mph'])

            return render(request,'cwApp/congrats.html')
         #otherwise list errors
        else:
            allEntries=Car.objects.all
            context={
                    'errors':form.errors,
                    'allEntries': allEntries,
                    'form':form,
                }
            return render (request,'cwAPP/index.html',context)
    # code to carry information to index template
    allEntries=Car.objects.all()
    form=CarForm()
    context={
        'allEntries':allEntries,
        'form':form,
    }
    return render(request,"cwApp/index.html",context)
