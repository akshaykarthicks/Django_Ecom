from .cart import Cart

#to add in every set of page 

#crete context processor
def cart(request):
    # return data from  cart
    return {'cart':Cart(request)}