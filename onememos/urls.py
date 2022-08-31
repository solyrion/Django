from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/onememos/createMemo/
    path('', views.index, name='index'),
    path('createMemo/', views.createMemo),
    #localhost:8000/onememos/createMemo/?memoContent=대한민국 url에 바로 치는것
    #?memoContent=대한민국 -> GET방식으로 보내는 방법.
]

# path 안에 '' == http://localhost:8000/onememos/ 라는 default값 이 파일 기준.
# path(a, b) --> a라는 입력이 들어왔을때 b를 보여준다.
# path('', views.index, name='index') views == views.py (onememo안에)
