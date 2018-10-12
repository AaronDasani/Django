from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$',views.register,name='registration'),
    url(r'^create/$',views.create,name='create'),
    url(r'^login/$',views.login,name='login'),
    url(r'^loginProccess',views.proccess,name='proccess'),
    url(r'^logoff',views.logoff,name='logoff')


]