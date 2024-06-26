# postboxProject/ postboxProject/ urls.py (프로젝트 내 urls.py) 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), # 추가
]