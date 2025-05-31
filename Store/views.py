from django.shortcuts import render,redirect
from . models import product, Category as CategoryModel
from django.contrib.auth import authenticate, login, logout # for login and logout
from django.contrib import messages
from django.contrib.auth.models import User # for register
from django.contrib.auth.forms import UserCreationForm # for register
from .forms import SignUpForm, UpdateUserForm,SetPasswordForm
from django import forms


def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=='POST':
            form=SetPasswordForm(current_user,request.POST)
            if form.is_valid():
                 form.save()
                 
                 messages.success(request,"You have been updated")
                 return redirect('login')
            else:
                messages.error(request,"yea its not working")
                
            
        else:
            form=SetPasswordForm(request.POST)
            return render(request,'update_password.html',{'user_form':SetPasswordForm(request.POST)})

    else:
        messages.error(request,"You are not logged in")
        return redirect('login')







#to update the profile of the user 
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)  # get the current user from the database
        user_form= (UpdateUserForm(request.POST, instance=current_user)) # get the form data from the request
        
        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,"You have been updated")
            return redirect('home')
        
        return render(request,'update_user.html',{'user_form':user_form})
    else:
        messages.error(request,"You are not logged in")
        return redirect('login')


#category summary
def category_summary(request):
    categories = CategoryModel.objects.all()
    return render(request,'category_summary.html' ,{'categories':categories})


#product detail page
def product_detail(request,pk):
    product_obj =product.objects.get(id=pk) # get product from the database
    return render(request,'product.html',{'product':product_obj})

# Create your views here.
def home(request):
    products = product.objects.all() # get all products from the database
    return render(request,'home.html',{'products':products})


def category(request, cn):
    # Add print to see what category name is being searched for
    print(f"Attempting to load category: {cn}")
    cn = cn.replace('-', ' ') # This replaces hyphens in the URL with spaces

    try:
        # Use the renamed model to get the category object
        category_obj = CategoryModel.objects.get(name=cn)

        # Filter products by the found category
        products = product.objects.filter(category=category_obj)

        # Add print to confirm category and product count found
        print(f"Found category '{cn}' with {products.count()} products.")

        # Render the category page with products
        return render(request, 'category.html', {'category': category_obj, 'products': products})

    except CategoryModel.DoesNotExist:
        # This block runs if the category is NOT found in the database
        messages.error(request, f"Category '{cn}' not found in the database.")
        print(f"Error: Category '{cn}' not found.")
        return redirect('home') # Redirect to home page after showing error

    except Exception as e:
        # Catch any other unexpected errors
        messages.error(request, f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
        return redirect('home')
    
    
    


def about(request):
    return render(request,'about.html')

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST) # get form data from request
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username'] #login user
            password=form.cleaned_data['password1']
            #login user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been registered")
            return redirect('home')
        else:
            messages.error(request,"yea its not working")
            return render(request,'register.html',{'form':form}) #
            
    else:
        return render(request,'register.html',{'form':form})



def login_user(request):
    if request.method == 'POST': #login
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password) #django default authentication
        
        if user is not None:
            login(request,user) #authenticate user using django default function
            messages.success(request,"You have been logged in") #django default function
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return render(request,'login.html')
            
            
    else:
        return render(request,'login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')