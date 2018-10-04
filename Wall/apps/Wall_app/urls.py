from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^create/$',views.create,name='create'),
    url(r'^createComment/(?P<post_id>\d+)$',views.createComment,name='createComment'),
    url(r'^destroy/(?P<user_id>\d+)$',views.destroy,name='destroy')
]

