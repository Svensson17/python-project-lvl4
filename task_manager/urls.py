"""task_manager URL Configuration

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
from task_manager.views import IndexView, \
    UsersList, \
    CreateUser, \
    LoginUser, \
    LogoutUser,\
    EditUser, \
    DeleteUser

urlpatterns = [
    path('users/<int:pk>/delete/', DeleteUser.as_view(), name='delete_user'),
    path('users/<int:pk>/update/', EditUser.as_view(), name='edit_user'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('users/create/', CreateUser.as_view(), name='register'),
    path('users/', UsersList.as_view(), name='users'),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
