from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index' ),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throws/', views.throws, name='throws'),
    path('catch/', views.catch, name='catch'),
    # path('hello/asd/', views.hello1, name='hello1'),
    path('hello/<name>/', views.hello, name='hello'), #<str:name> 타입 안쓰면 str 이 디폴트
]
