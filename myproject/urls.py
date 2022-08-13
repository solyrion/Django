"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
urlpatterns 정리
    -admin등(/)는 기본적으로 장고가 처리는 해주나 가급적 쓰도록하자.
    -마지막단 콤마(,)를 생략해도 되고 붙여도 된다.(마지막줄은)
    -서버 구동 시 변화가 감지되면 자동으로 reload(오류나면 자동적으로 에러)
    -초기화면 views.index 또는 views.main등 상관없음 함수이름일뿐
    -
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('onememos/', include('onememos.urls')),
]
