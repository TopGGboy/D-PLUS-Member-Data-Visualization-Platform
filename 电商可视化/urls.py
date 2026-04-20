"""
URL configuration for 电商可视化 project.

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
from django.urls import path
from PLUSUser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plushome/', views.plushome),

    # 左侧数据加载
    path('useredu/', views.plus_useredu),  # 用户学历
    path('usercity/', views.plus_usercity),  # 用户城市
    path('usersex/', views.plus_usersex),  # 用户性别

    # 右侧数据加载
    path('plusacc/', views.plus_acc),  # PLUS累计在籍会员数趋势分析
    path('plusold_new_plus/', views.plus_old_new_plus),  # PLUS在籍会员中新会员VS老会员比例
    path('plususer_times/', views.plus_user_times),  # PLUS会员开通次数分布分析

    # 中间数据加载
    path('plus_uds/', views.plus_uds),  # PLUS会员每日各状态（拉新、续费、召回）开通会员数分析
]
