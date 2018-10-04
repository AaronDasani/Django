from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$',views.index,name='registration'),
    url(r'^create/$',views.create,name='create'),
    url(r'^login/$',views.login,name='login'),
    url(r'^loginProccess',views.proccess,name='proccess')


]