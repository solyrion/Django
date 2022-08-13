from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
request 인자는 뭐지?? 말그대로 사용자가 보낸 내용?을 받는 인자
-> request객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다.(포수느낌)
request.GET, request.POST, request.COOKIE -> 보내는 방식(사전형 데이터)에 따라 받는 방식이 달라짐.
"""
def index(request):
    return HttpResponse("Onememos~ Hello, Wolrd!!")

def createMemo(request):
    memoContent = request.GET['memoContent']
    return HttpResponse("Create Memo="+memoContent)
