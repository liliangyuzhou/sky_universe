"""sky_universe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from star_app.views import user_views
from star_app.views.service import service_detail_views, service_list_views
from star_app.views.interface import interface_list_views, interface_detail_views
from star_app.views.service import service_interface_detail_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('backend/user/register', user_views.register),
    # path('backend/user/login', user_views.login_user),
    # path('backend/user/get_user', user_views.get_user),
    path('backend/user/', user_views.UserViews.as_view()),

    path('backend/service/', service_list_views.ServiceListView.as_view()),
    path('backend/service/<int:pk>', service_detail_views.ServiceDetailView.as_view()),
    path('backend/service/<int:pk>/interfaces', service_interface_detail_views.ServiceInterfaceDetailView.as_view()),

    path('backend/interface/', interface_list_views.InterfaceListView.as_view()),
    path('backend/interface/<int:pk>', interface_detail_views.InterfaceDetailView.as_view()),
]
