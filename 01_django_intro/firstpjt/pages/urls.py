from django.urls import path
from . import views

# 당장 path를 쓰지 않더라도 urlpatterns를 작성해야함
app_name = 'pages'
urlpatterns = [
     path('index/', views.index, name='index')
]
