"""Load_Scheduler URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path
from Runs import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Auth Codes
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    #Runs
    path('schedule/create', views.create_run.as_view(), name='create_run' ),
    path('runs/', views.detail_run.as_view(), name='detail_run' ),
    path('schedule/<int:pk>/update', views.update_run.as_view(), name='update_run' ),
    path('schedule/<int:pk>/delete', views.delete_run.as_view(), name='delete_run' ),
    path('schedule/<int:pk>/pdf', views.GeneratePdf.as_view(), name='GeneratePdf' ),
    path('', views.Table_View.as_view(), name='Table_View'),
    path('schedule/detailspdf/', views.detailspdf.as_view(),name='detailspdf'),
    #path('schedule/csv', views.export_view.as_view(), name='export_view')
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
