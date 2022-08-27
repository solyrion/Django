from django.db import models

"""
이름이 model인 이유는??
1) 일상 용어에서 뭔가를 대표하고 샘플표본으로 받아드릴 만한 단어는?? -> model, specimen(표본)
2) 어떤 데이터를 저장하고 처리할것인지에 대해 고민한 결과들 -> app에대한 데이터모델(database, table)
3) 어떤 프로그램(App)을 만들 때 데이터가 저장되고 관리되는 것이 필요한데 이러한걸 처리하기 위한 모델(표본)이 필요하다
"""

# Create your models here.

# idx        -> X 중요한 PK(primary key)이기 때문에 자동으로 생성
# memo_text
# published_date (예시)

class Memo(models.Model):
    # 자체 메소드 내부적으로 조건에 맞는 table(이름 = 앱이름_class(onememos_Memo) 생성
    # CharField -> 가능한 문자열의 제한이 있음 TextField는 없음
    # auto_now_add = True -> 자동으로 작성된 시간/날짜를 입력시킴.
    memo_text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memo_text # 메모 작성하면 제목으로 바로 뜸. (memo object)으로 안뜨고.

"""
작성후 -> 반영을 해줘야함 -> 어디에? -> admin 사이트에 -> admin.py열고 추가작성

"""