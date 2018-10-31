from django.conf.urls import url
from .import views

app_name='dashboard'

urlpatterns=[
    url(r'^$',views.dashboard, name='dashboard'),
    url(r'^product/(?P<product_id>\w+)/(?P<product_brand>\w+)$',views.product_page, name='product_page'),
    url(r'^checkout/$',views.checkout, name='checkout'),
    url(r'^thankYou/$',views.thankYou, name='thankYou'),
    url(r'^payementProcess/$',views.payementProcess, name='payementProcess'),
    url(r'^add_to_cart$',views.add_to_cart, name='add_to_cart'),
    url(r'^PriceRange/$',views.PriceRange, name='PriceRange'),
    url(r'^searchProduct/(?P<category>\w+)$',views.searchProduct, name='searchProduct'),
    url(r'^searchBrand/$',views.searchBrand, name='searchBrand')


    

]