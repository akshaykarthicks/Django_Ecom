from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Store.models import product
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products=cart.get_prods #from cart..py
    quantities=cart.get_quants  #from cart..py
    totals = cart.cart_total()
    
    return render(request,'cart_summary.html',{'cart_products':cart_products,'quantities':quantities,'totals':totals})

@require_POST
def cart_add(request):
    try:
        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product_obj = get_object_or_404(product, id=product_id)
        cart.add(product=product_obj,quantity=product_qty)
        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity, 'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def cart_delete(request):
    cart=Cart(request)
    
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        
        
        response=JsonResponse({'status':'success'})
        return response
    


def cart_update(request):
    cart=Cart(request)
    
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response=JsonResponse({'status':'success'})
        return response
        
        