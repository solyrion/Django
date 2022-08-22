from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
"""
request 인자는 뭐지?? 말그대로 사용자가 보낸 내용?을 받는 인자
-> request객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다.(포수느낌)
request.GET, request.POST, request.COOKIE -> 보내는 방식(사전형 데이터)에 따라 받는 방식이 달라짐.
"""

"""
render 함수와 template 파일의 관계
        - 웹사이트 개발 시 파이썬 코드와 데이터를 템플릿 파일로 만들어주는 함수(쉽게말해 html)
        - 결국 리턴은 html파일로 return
        - 이렇게 html파일로 리턴한 것을 --> template 파일임.
        - 그러나 템플릿 파일이 html 파일은 아니다. 장고만의 특수한 파일.
        - 이러한 파일은 대부분의 프레임워크에서도 마찬가자임. 전용파일개념
        - 또한 장고에서만 사용할 수 있는 문법(태크)등을 이러한 템플릿에 적용.->일반 html 파일 X
        - 당연히 템플릿도 규칙과 최소한의 문법(태그)이 존재.
        - 조건처리,반복처리 등이 가능 -> 얼핏 프로그래밍 언어처럼도 보이나 -> 언어라기 보다 전용표현정도
"""

def index(request):
    # return HttpResponse("Onememos~ Hello, Wolrd!! 12341234")
    # 이미 onememos까지 path설정이기에 '템플릿 경로'안에 쓸 필요 없음. 또한 templates폴더는 경로에 언급 x
    return render(request, 'main.html')


def createMemo(request):
    memoContent = request.GET['memoContent']
    return HttpResponse("Create Memo="+memoContent)
