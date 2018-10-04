from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def validatePurchase(self,form,product_id):
        product=Product.objects.get(id=product_id)
        if form['quantity'].isdigit():
            price=float(product.price)*int(form['quantity'])
            return price
        return False
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=ProductManager()