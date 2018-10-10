from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^profile/(?P<currentPage>\d+)$',views.index,name='index'),
    url(r'^create/(?P<currentPage>\d+)$',views.create,name='create'),
    url(r'^createComment/(?P<post_id>\d+)/(?P<currentPage>\d+)$',views.createComment,name='createComment'),
    url(r'^destroy/(?P<user_id>\d+)/(?P<currentPage>\d+)$',views.destroy,name='destroy')
]

