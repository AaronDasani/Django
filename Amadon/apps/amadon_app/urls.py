from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^$',views.redirect_main,name='redirect_main'),
    url(r'^amadon/$',views.index,name='index'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^validate_buy/(?P<product_id>\d+)$',views.validate_purchase,name='validate_purchase')

]