"""askBakaev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from autorize import views as author_views
from main import views as main_views
from question import views as quest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    # path('question/', quest_views.question, name='question'),
    path('new/', quest_views.new_question, name='new'),
    path('tags/', main_views.tags, name='tags'),
    path('settings/', main_views.settings, name='settings'),
    path('reg/', author_views.reg, name='reg'),
    path('login/', author_views.login, name='login'),
    path('question/<int:pk>/', quest_views.QuestView.as_view()),
]
