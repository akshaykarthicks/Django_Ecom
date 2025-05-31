from Store.models import product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        
        # If no cart exists, create one
        if cart is None:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
            
    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)  # get the quantity of the product
        
        if product_id in self.cart:  # if product already in the cart
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True  # save cart to session
            
    def __len__(self):
        return len(self.cart)  # return the length of the cart  
    
    
    #cart summary
    def get_prods(self):
        product_ids = self.cart.keys() #get all product ids from the cart
        # use ids to get all products from the database
        products = product.objects.filter(id__in=product_ids)
        return products
    
    def get_total_price(self):
        return sum(float(item['price']) for item in self.cart.values())
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)  # get the quantity of the product
        
        ourcart = self.cart
        #update the dict
        ourcart[product_id] = product_qty    # to find the key and update the value {4:2} -> {4:1}
        
        self.session.modified = True  # save cart to session
        
        thing = self.cart
        return thing
    
    
    def delete(self,product):
        #delete the product from the cart
        product_id = str(product)
        #delete from the dict
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True  # save cart to session
        
        
## maths for total price in the cart 
    def cart_total(self):
        product_ids = self.cart.keys() #get all product ids from the cart
        # use key in database 
        products = product.objects.filter(id__in=product_ids)
        quantity = self.cart
        #import product model up
        total = 0
        
        for key,value in quantity.items():
            # str into int
            key = int(key)
            for prod in products:
                if prod.id==key:
                    total = total + prod.price*value 
        return total
        
        
        
    