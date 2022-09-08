from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Travel
from .forms import TravelForm

# Create your views here.

def index(request):
    travels = Travel.objects.all()
    context = {
        'travels' : travels
    }

    return render(request, 'travels/index.html', context)
    

def create(request):
    if request.method == 'POST':
        # create
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()   # save() 인스턴스를 통해 새롭개 생성된 값을 article에 저장
            return redirect('travels:detail', travel.pk)
    else:
        # new
        form = TravelForm
    context = {
        'form' : form
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travel.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)


def delete(request, pk):
    article = Travel.objects.get(pk=pk)
    article.delete()
    return redirect('travels:index')

def update(request, pk):
    travel = Travel.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail' , travel.pk)
    else:
        form = TravelForm(instance=travel)

    context = {
        'travel': travel,
        'form' : form,
    }
    return render(request, 'travels/update.html', context)





