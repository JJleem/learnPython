# py manage.py createsuperuser
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse  
from rest_framework.routers import DefaultRouter
from api.views import ArticleViewSet


def home(request):
    return HttpResponse("Welcome to my Django API!")  # 원하는 문구로 바꿔도 됩니다

# 2) DRF 라우터 설정
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

# 3) URL 패턴에 home 뷰 추가
urlpatterns = [
    path('', home),                     # ← 루트 경로에 매핑
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]