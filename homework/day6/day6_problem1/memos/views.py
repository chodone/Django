from django.shortcuts import render,redirect
from .models import Memo
from .forms import MemoForm

# Create your views here.

def index(request):
    memos = Memo.objects.all()
    context = {
        'memos' : memos
    }

    return render(request, 'memos/index.html', context)
    

def create(request):
    if request.method == 'POST':
        # create
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save()   # save() 인스턴스를 통해 새롭개 생성된 값을 article에 저장
            return redirect('memos:detail', memo.pk)
    else:
        # new
        form = MemoForm
    context = {
        'form' : form
    }
    return render(request, 'memos/create.html', context)

def detail(request, pk):
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo,
    }
    return render(request, 'memos/detail.html', context)


def delete(request, pk):
    article = Memo.objects.get(pk=pk)
    article.delete()
    return redirect('memos:index')



