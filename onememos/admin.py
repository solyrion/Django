from django.contrib import admin
from onememos.models import Memo #추가 import

# Register your models here.
admin.site.register(Memo)

"""
최종 DB에 반영하기 위해 터미널(cmd)을 이용해서 migrate해야함. 그 전에 2가지를 해야됨
1. 최상위 폴더(mypro~) -> setting.py에 만든 앱을 등록해줘야 함(INSTALLED_APPS) -> 안하면 2단계에서 오류남
2. python manage.py make migrations 명령어 실행 -> onememos안에 migrations폴더에 
만든 models에 기반된 파일들이 생성됨 -> migration 준비단계

model 내용을 수정 할 경우 2번단계 다시 해야됨.

"""
