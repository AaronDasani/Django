from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from ..LoginAndRegister.models import User
from ..dashboard.models import Order
from .models import Product
import os
# Create your views here.


def admin(request):
    # if there is no 'user_id' in request.session send the user to the login page
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # if we get an error trying to get the user_level, send the user to the login page
    try:
        current_user=User.objects.get(id=request.session['user_id']).user_level   
    except:
        return redirect(reverse("userLG:login"))
    # if user_level not 1, [number 1 being the admin] send the user to the login page
    if current_user != 1:
        return redirect(reverse("userLG:login"))


    orders_list=Order.objects.raw("SELECT * FROM dashboard_order GROUP BY order_id ")  

    paginator = Paginator(orders_list, 2) 
    page = request.GET.get('page')
    orders = paginator.get_page(page)

    context={
        'orders':orders,
    
    }

    return render(request, "admin/adminDashboard.html",context)


def searchOrders(request):

    orders=Order.objects.raw("Select * from dashboard_order group by order_id")
    MatchOrder=[]
    page = request.GET.get('page')

    for index in orders:
        if((request.POST['searchOrder']).lower() in (index.user.first_name).lower()):
            MatchOrder.append(index)

    paginator = Paginator(MatchOrder, 2) # Show speficy amount orders per page
    orders = paginator.get_page(page)

    if len(MatchOrder)>0:
        return render(request,"admin/orderList.html",{'orders':orders})

    else:
        try:
            orders=Order.objects.raw("Select * from dashboard_order WHERE order_id LIKE '"+request.POST['searchOrder']+"%%' GROUP BY order_id")
            
            paginator = Paginator(MatchOrder, 2) # Show speficy amount orders per page
            orders = paginator.get_page(page)

            if orders[0] is None:
                return HttpResponse("<h4 class='font-weight-light bg-danger text-white mt-3 p-3 ml-5'>No Product Found !!</h4>")

            return render(request,"admin/orderList.html",{'orders':orders})

        except:
            return HttpResponse("<h4 class='font-weight-light bg-danger text-white mt-3 p-3 ml-5'>No Product Found !!</h4>")

def viewProduct(request,order_id):
    products=Order.objects.filter(order_id=order_id)
    totalCost=0
    discount=10
    for index in products:
        price=index.price*index.quantity
        totalCost+=price

    context={
        'products':products,
        'order': Order.objects.filter(order_id=order_id)[0],
        'subCost':str(round(totalCost,2)),
        'totalCost':str(round(totalCost-discount,2)),
        'discount':discount
    }

    return render(request,"admin/OrderDetails.html",context)

def create(request):
    print(request.POST) 
    if request.POST is False:
        return redirect(reverse("userLG:logoff"))

    print("*"*60)
    print(request.FILES)
    valid,response=Product.objects.validate(request.POST,request.FILES)

    if valid==False:
        request.session['color']="danger"
        for error in response:
            messages.error(request, error)
    else:
        request.session['color']="success"
        messages.success(request, "Successfully Added Product to Store")

    return redirect(reverse("adminDashboard:productsInStock"))



def productsInStock(request):

    context={
        'Products':Product.objects.all()
    }

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("*"*60)
    print ("base dir path", BASE_DIR)
    print("*"*60)

    return render(request,"admin/InStock.html",context)



def edit(request):

    print(request.POST)

    print("*"*60)
    print(request.FILES)
    print("*"*60)

    valid,response=Product.objects.validate(request.POST,request.FILES)

    context={
        'Products':Product.objects.all()
    }
    # return render(request,"admin/inStockProduct.html",context)
    return redirect(reverse("adminDashboard:productsInStock"))


def fetchProductInfo(request):
 
    context={
        'product':Product.objects.get(id=request.GET['product_id'])
    }
   
    return render(request,"admin/editProductInfo.html",context)



def delete(request):
    print(request.POST)
    try:
        Product.objects.get(id=request.POST['product_id']).delete()
    except:
        request.session['color']="danger"
        messages.error(request, "Product Was not delete, Please contact your Supervisor")

    context={
        'Products':Product.objects.all()
    }
    

    return render(request,"admin/inStockProduct.html",context)




def searchProduct(request):
    # pagination
        # paginator = Paginator(orders_list, 2) 
        # page = request.GET.get('page')
        # orders = paginator.get_page(page)
    pass


def ajax_pagination(request):

    # print(request.GET['page'])

    orders_list=Order.objects.raw("SELECT * FROM dashboard_order GROUP BY order_id ")
    paginator = Paginator(orders_list, 2)

    orders = paginator.get_page(request.GET['page'])

    return render(request,"admin/orderList.html",{'orders':orders})
  
