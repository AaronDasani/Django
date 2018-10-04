from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
from .models import Product
def index(request):
    if 'price' not in request.session:
        request.session['price']=0
    if 'counter' not in request.session:
        request.session['counter']=0
    if 'total' not in request.session:
        request.session['total']=0

    context={
        'products':Product.objects.all()
    }
    
    return render(request,'amadon/index.html',context)


def validate_purchase(request,product_id):

    response=Product.objects.validatePurchase(request.POST,product_id)
    if response==False:
        return redirect(reverse('amadon:index'))


    request.session['price']=response
    request.session['counter']= request.session['counter']+1
    request.session['total']=request.session['total']+response


    messages.success(request, "Purchase successful")

    return redirect(reverse('amadon:checkout'))



def checkout(request):
    
    return render(request,'amadon/checkout.html')





def redirect_main(request):
    return redirect(reverse('amadon:index'))