from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^register/$',views.index),
    url(r'^login/$',views.login),
    url(r'^users/new/$',views.index),
    url(r'^users/$',views.show)
]