from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

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
    # 이미 onememos까지 path설정이기에 '템플릿 경로'안에 쓸 필요 없음. 또한 templates폴더는 직접적으로 경로에 언급 x
    return render(request, 'main.html')

def createMemo(request):
    """
    request 인자는 뭐지?? 말그대로 사용자가 보낸 내용?을 받는 인자
    -> request객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다.(포수느낌)
    request.GET, request.POST, request.COOKIE -> 보내는 방식(사전형 데이터)에 따라 받는 방식이 달라짐.
    서버의 특정주소에 보내는 방식은 = POST (회원가입 / 게시판)
    """
    # memoContent = request.GET['memoContent']
    memoContent = request.POST['memoContent']

    return HttpResponse("Create Memo="+memoContent)


# 앞으로 공부할 내용
'''
1. 뷰페이지 템플릿 꾸미기(Form) --> 입력과 출력
2. 템플릿 파일의 목적(용도)
            - 뷰페이지 처리 --> 템플릿 파일
            - 개발과 디자인의 분리
            - 개발자 코드 vs 디자이너(HTML, CSS) 코드 --> 문제발생.. 분리필요
            - 다른 프레임워크들에서도 보통 template(s) 이라는 폴더명을 만들어 템플릿 폴더로 인식시켜서 사용.
            - 아무튼 디자니어(뷰페이지 담당자) 입장에서는 템플릿 언어의 고유문법이나 태그 공부필요
3. 관리자모드에서의 DB 조작 vs 터미널 명령 프롬프트에서의 DB조작(sqlite, dbshell)
            - 이 과정에서 오류가 발생하곤 한다 -> 이때 -> 어떻게 처리해줘야 하는지에 대해서 체크.
            - sqlite  tool 설치가 안되서 나는 오류.
            - http://www.sqlite.org/download.html 여기서 관련 툴 다운로드
            - 압축을 풀면 3개의 실행파일 중 sqlite3.exe 실행파일을 생성한 프로젝 루트 폴더에 넣어놓고 sqlite Db에 접속
            - 툴을 통해 db의 테이블 정보 확인 및 테이블명 규칙성 확인 -> 실제 테이블명 확인
4. 꾸민 폼 페이지에서 한 줄 메모 작성 --> DB에 입력 및 출력
'''


















