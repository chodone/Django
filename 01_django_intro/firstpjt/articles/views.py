from email import message
from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def greeting(request):
    family = ['Tom' , 'Mom', "Dad"]
    context = {
        'name' : 'Alice', 
        'age' : 25, 
        'family' : family
    }
        
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['가지덮밥', '차돌된찌', '오리주물럭', '열무국수' ]
    context = {
        'foods' : foods,
    }
    return render(request, 'articles/dinner.html', context)

def throws(request):

    return render(request, 'articles/throws.html')

def catch(request):
    # raise

    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    message = request.GET.get('message')
    mes = request.GET.get('mes1')
    context={
        'message': message,
        'mes': mes
    }


    return render(request, 'articles/catch.html', context)

def hello(request, name):
    
    context ={
        'name' : name
    }
    return render(request, 'articles/hello.html' , context)

def hello1(request):

    return render(request, 'articles/hello1.html')

