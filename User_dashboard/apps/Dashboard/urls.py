from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^admin/$',views.Dashboard,name="Dashboard"),
    url(r'^admin/editUser/(?P<user_id>\d+)$',views.editUser,name="editUser"),
    url(r'^admin/addUser/$',views.addUser,name="addUser"),
    url(r'^update/(?P<user_id>\d+)$',views.update,name="update"),
    url(r'^destroy/$',views.destroy,name="destroy"),


]