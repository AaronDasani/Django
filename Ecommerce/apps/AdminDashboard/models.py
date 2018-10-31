from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ..LoginAndRegister.models import User
class ProductManager(models.Manager):

   def validate(self,form,image):
        errors=[]

        # brand validation
        if len(form['brand'])<1:
            errors.append("brand should not be blank")
        if len(form['brand'])>30:
            errors.append("brand should ne less than 30 characters")
    
        # Name validation
        if len(form['name'])<1:
            errors.append(" Product name should not be blank")
        if len(form['name'])>30:
            errors.append("Product name should ne less than 30 characters")

        # product Description
        if len(form['description'])<1:
            errors.append(" Product description should not be blank")

        # product Price
        if len(form['price'])<1:
            errors.append(" Please provide a Price")
        if form['price'].isdigit() is False:
            errors.append("Price should contain only numbers")

        # Category validation
        if len(form["addNewCategory"])<1:
            if len(form["category"])<1:
                errors.append("Please provide an category")
            else:
                category=form["category"]
        else:
            if form["category"]:
                errors.append("Please include only one category")
            else:
                if len(form["addNewCategory"])<1:
                    errors.append("Please provide an category")
                elif len(form["addNewCategory"])<3:
                    errors.append("category should be atleast 3 characters")
                else:
                    category=form["addNewCategory"]

        # product Inventory:
        if len(form['inventory'])<1:
            errors.append(" Please provide an inventory")
        if form['inventory'].isdigit() is False:
 
            errors.append("Inventory should be a numbers")

        # product Amount Sold
        if len(form['sold'])<1:
            errors.append(" Please provide a sold amount")
        if form['sold'].isdigit() is False:
            errors.append("Sold Amount should be a numbers")
        

        if errors:
            return(False,errors)
        else:
            if form['editForm']:#use try and except here
                
                print("Editing form right now<<<<<<<---------")

            else:
                # product=Product.objects.create(
                #     brand=form['brand'],
                #     itemName=form['name'],
                #     price=form['price'],
                #     description=form['description'],
                #     upload=image['image'],
                #     user=User.objects.get(id=1)
                # )
                
                # ProductInventory.objects.create(
                #     inventory=form['inventory'],
                #     quantitySold=form['sold'],
                #     category=category,
                #     product=Product.objects.get(id=product.id)
                # )
                print("Creating Produt right now<<<<<<<---------")


            return(True,errors)


class Product(models.Model):
    brand=models.CharField(max_length=40)
    itemName=models.CharField(max_length=255)
    price=models.FloatField()
    description=models.TextField()

    upload = models.ImageField(blank=True,upload_to='image/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user=models.ForeignKey(User,related_name="product",on_delete=models.DO_NOTHING)
    objects=ProductManager()

class ProductInventory(models.Model):
    inventory=models.IntegerField()
    quantitySold=models.IntegerField()
    category=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    product=models.OneToOneField(Product,related_name="inventory",on_delete=models.CASCADE)