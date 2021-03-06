from django.conf.urls import url, include
from . import views
#from django.contrib.auth.views import login
from django.contrib import admin
#from django.contrib.auth import views as auth_views

urlpatterns = [                 #legger til url som leder sil sider
    url(r"^$", views.startside, name='startside'),
    url(r"^lanser$", views.lanser, name='lanser'),
    url(r"^valgtlanse$", views.valgtlanse, name='valgtlanse'),
    url(r"^info$", views.info, name='info'),
    url(r'^master$', views.master, name='master'),
    #url(r"^test$", views.test, name='test'),
    url(r"^csrf$", views.csrf, name='csrf'),
    url(r"^data$", views.data, name='data'),
    url(r'^login$', views.mylogin, name='login'),
    url(r'^logout$', views.mylogout, name='logout'),
  ]