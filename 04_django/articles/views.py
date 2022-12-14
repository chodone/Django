import re
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()   # save() 인스턴스를 통해 새롭개 생성된 값을 article에 저장
            return redirect('articles:detail', article.pk)
    else:
        # new
        form = ArticleForm
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)






    # form = ArticleForm(request.POST)
    # if form.is_valid():
    #     article = form.save()   # save() 인스턴스를 통해 새롭개 생성된 값을 article에 저장
    #     return redirect('articles:detail', article.pk)
    # print(f'에러 : {form.errors}')
    # # return redirect('articles:new')
    # context = {
    #     'form' : form
    # }
    # return render(request, 'articles/new.html', context)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)

#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail' , article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)




    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail' , article.pk)
    # context={
    #     'form' : form,
    #     'article' : article
    # }
    # return render(request , 'articles/edit.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)