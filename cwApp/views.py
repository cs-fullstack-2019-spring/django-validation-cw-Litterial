from django.shortcuts import render,HttpResponse
from .models import Car
from .forms import CarForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form=CarForm(request.POST)
        if form.is_valid():
            Car.objects.create(make=request.POST['make'],model=request.POST['model'],year=request.POST['year'],mph=request.POST['mph'])

            return render(request,'cwApp/congrats.html')

        else:
            allEntries=Car.objects.all
            context={
                    'errors':form.errors,
                    'allEntries': allEntries,
                    'form':form,
                }
            return render (request,'cwAPP/index.html',context)

    allEntries=Car.objects.all()
    form=CarForm()
    context={
        'allEntries':allEntries,
        'form':form,
    }
    return render(request,"cwApp/index.html",context)
