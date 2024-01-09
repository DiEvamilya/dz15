"""
URL configuration for CoursePlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from program.views import start_list_view, detail_course_view, create_course_view, update_course_view, \
    delete_course_view, detail_module_view, create_module_view, update_module_view, delete_module_view, \
    detail_lesson_view, create_lesson_view, update_lesson_view, delete_lesson_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_list_view, name='start_list'),
    path('course_detail/<slug:slug>/', detail_course_view, name='course_detail'),
    path('create/', create_course_view, name='course_create'),
    path('update/<str:pk>/', update_course_view, name='course_update'),
    path('delete/<slug:slug>/', delete_course_view, name='course_delete'),
    path('module_detail/<slug:slug>/', detail_module_view, name='module_detail'),
    path('create-module/', create_module_view, name='module_create'),
    path('update-module/<slug:slug>/', update_module_view, name='module_update'),
    path('delete-module/<slug:slug>/', delete_module_view, name='module_delete'),
    path('lesson_detail/<slug:slug>/', detail_lesson_view, name='lesson_detail'),
    path('create-lesson/', create_lesson_view, name='lesson_create'),
    path('update-lesson/<slug:slug>/', update_lesson_view, name='lesson_update'),
    path('delete-lesson/<slug:slug>/', delete_lesson_view, name='lesson_delete'),
]
