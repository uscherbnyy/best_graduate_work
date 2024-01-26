"""
URL configuration for To_Do_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ToDo import views


urlpatterns = [
    path('', views.home),
    path('listusers/', views.listusers),
    path('user_selection/', views.user_selection),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('update/', views.update),
    path('destroy/', views.destroy),
    path('create_task/', views.create_task),
    path('task_list/', views.task_list),
    path('sort_status/', views.sort_status),
]
