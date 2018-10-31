from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
import random
import string
# Create your views here.
from .models import Cart,Order
from..LoginAndRegister.models import User
import webhoseio
webhoseio.config(token='ba97ec58-a132-4dad-aa67-28e170c1c0d6')      
def dashboard(request):

    # check if their is a user_id, basically checking if a user is logged in
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # remember some information about the search history
    if 'productInfo' not in request.session:
        request.session['productInfo']={
            'categories':'shirt',
            'price':'60',
            'brand':'nike'
        }

    # those information was used to help the user be able to click on the suggestion product and be able to show the correct information about that specific product. We delete it here becuase we do not need it in this page.
    if "product" in request.session:
        del request.session["product"]
        del request.session['product_id']
        request.session.modified = True

    # miscelleneous information to make the dashboard page better
    itemsInCart=Cart.objects.all().count()
    userLevel=User.objects.get(id=request.session['user_id']).user_level
    
    # sending an API request through the 'sendingRequest' function. THe response will be some product Data
    product_list=sendingRequest(request, catergories=request.session['productInfo']['categories'])
    
    return render(request,"ecommerce/dashboard.html", {'product_list':product_list,'itemsInCart':itemsInCart,'user_level':userLevel} )
    # return render(request,"ecommerce/dashboard.html",{'itemsInCart':itemsInCart,'user_level':userLevel})



def product_page(request,product_id,product_brand):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    product_list={}

    if 'product_id' not in request.session:
        print("product_id Initialized <<<<<<<-------")
        request.session['product_id']=None
 
    if request.session['product_id'] != str(product_id) or 'product' not in request.session:
        request.session['product_id']=product_id
       
        print("data from request <<<<<-------")
        query_params = {
            "q": "product_id: "+product_id+"",
            'size':'1'
        }
    
        output = webhoseio.query("productFilter", query_params)
        product_list={
            'product_name':output['products'][0]['name'],
            'product_brand':output['products'][0]['brand'],
            'product_price':output['products'][0]['price'],
            'product_image':output['products'][0]['images'][0],
            'product_description':output['products'][0]['description']
            
        }
        request.session['product']=product_list
        # Get the next batch of products
        output = webhoseio.get_next()

        # changing the brand filter in the session
        request.session['productInfo']['brand']=product_brand
        request.session.modified = True

        suggestion_list=sendingRequest(request,catergories=request.session['productInfo']['categories'],brand=product_brand,product_id=product_id)
        request.session["suggested_product"]=suggestion_list
    else:
        print("data from session <<<<<-------")
        product_list=request.session['product']
        suggestion_list= request.session["suggested_product"]

    itemsInCart=Cart.objects.all().count()
    
    return render(request,"ecommerce/productPage.html",{'product_list':product_list,'suggested_product':suggestion_list,'itemsInCart':itemsInCart})




def checkout(request):
    cart=Cart.objects.all()
    totalCost=0
    discount=10
    for index in cart:
        price=index.price*index.quantity
        totalCost+=price


    context={
        'products':cart,
        'totalCost':totalCost-discount,
        'discount':discount,
        'totalItems':Cart.objects.all().count()
    }
    
    return render(request,"ecommerce/checkout.html",context)


def payementProcess(request):
    # Save Order
    print(request.POST)
    try:
        current_user=request.session['user_id']
    except:
        return redirect(reverse("userLG:login"))

    cart=Cart.objects.filter(user_id=request.session['user_id'])
    order_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    print(">>>>>>>>>>>>>>>" ,order_id)

    for index in cart:
        Order.objects.create(
            user=User.objects.get(id=current_user),
            order_id=order_id,
            brand=index.brand,
            itemName=index.itemName,
            price=index.price,
            quantity=index.quantity,
            totalCost=(index.price) * (index.quantity),
            OrderStatus='Order In'
        )

    # Delete Cart Items after purchase is done
    Cart.objects.filter(user_id=request.session['user_id']).delete()


    return redirect(reverse("dashboard:thankYou"))


def thankYou(request):
    context={
       'user':User.objects.get(id=request.session['user_id']).first_name
    }
    return render(request,"ecommerce/thankYou.html",context)



def add_to_cart(request):
    print(request.POST)
    try:
        current_user=request.session['user_id']
    except:
        return redirect(reverse("userLG:login"))

    Cart.objects.create(user=User.objects.get(id=current_user),product_id=request.session['product_id'],brand=request.POST['brand'],itemName=request.POST['productName'],price=request.POST['price'],quantity=request.POST['quantity'])

    ItemsInCart=Cart.objects.all().count()
    return JsonResponse({'numberOfItems': ItemsInCart})





def PriceRange(request):
    request.session['productInfo']['price']=request.POST['maxPrice']
    request.session.modified = True
    product_list=sendingRequest(request,price_range=request.POST['maxPrice'], catergories= request.session['productInfo']['categories'], brand=request.session['productInfo']['brand'])
    return render(request,"ecommerce/product_list.html",{'product_list':product_list})
	
def searchProduct(request,category="shirt"):
    
    if request.method=='POST':
        request.session['productInfo']['categories']=request.POST['searchProduct']
        request.session.modified = True
        product_list=sendingRequest(request,catergories=request.POST['searchProduct'],brand=request.session['productInfo']['brand'])
    else:
        request.session['productInfo']['categories']=category
        request.session.modified = True
        product_list=sendingRequest(request,catergories=category,brand=request.session['productInfo']['brand'])
  
    
    return render(request,"ecommerce/product_list.html",{'product_list':product_list})
	
def searchBrand(request):

    request.session['productInfo']['brand']=request.POST['searchBrand']
    request.session.modified = True
    product_list=sendingRequest(request,brand=request.POST['searchBrand'],catergories= request.session['productInfo']['categories'],price_range=request.session['productInfo']['price'])
    
    return render(request,"ecommerce/product_list.html",{'product_list':product_list})



def sendingRequest(request,brand='nike',catergories="sport shirt",price_range=50,product_id=None):
    product_list=[]

    if product_id is not None:
        print("There is a product Id <<<<<<----------")
        query_params = {
            "q": "name:("+catergories+") brand:"+brand+" ",
            'size':'5'
        }
    else:
        print("Products more diverse, because, not requesting by product_id <<<<<<----------")
        query_params = {
            "q": "name:("+catergories+") price: <"+str(price_range)+" brand:"+brand+" ",
            "size":"25"
        }
    
    try:
        output = webhoseio.query("productFilter", query_params)
    except IndexError:
        print("Not found <<<<<<<<<<----------")

    for key,value in output.items():
        if key=='products':
            for index in value:
                if len(index['images'])<1:
                    continue
                else:
                    product_list.append(
                        {
                            'product_price':index['price'],
                            'product_image':index['images'][0],
                            'product_id':index['product_id'],
                            'product_brand':index['brand']
                        }
                    )
                
    # Get the next batch of products
    output = webhoseio.get_next()

    if len(product_list)<1:
    
        return HttpResponse("<h4 class='text-center text-white bg-dark p-3 mt-5 shadow'>Items Not Found!!</h4>")
    return (product_list)
    