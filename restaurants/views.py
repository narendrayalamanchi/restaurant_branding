from django.shortcuts import render

from django.shortcuts import get_object_or_404
import admin_dashboard.models  as brand_models

from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import RestaurantUsers,UserAddress,Cart, CartItem
from .forms import SignupForm,LoginForm
from django.contrib.auth import logout

def load_custom_user(view_func):
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                request.user = RestaurantUsers.objects.get(id=user_id)
            except RestaurantUsers.DoesNotExist:
                request.user = None
        else:
            request.user = None
        return view_func(request, *args, **kwargs)
    return wrapper

def home_page(request):
    brand = get_object_or_404(brand_models.BrandsDetails, title__iexact=request.host_kwargs.get('brand_name'))
    request.session["brandname"] = request.host_kwargs.get('brand_name')
    return render(request, 'restaurant/index.html', {'brand': brand})

def signout(request):
    logout(request)
    return redirect('res_home')
                  
def signup(request):
    response = {"success": True}
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            if RestaurantUsers.objects.filter(email=form.cleaned_data.get('email')).exists():
                response["message"] = "Email already exists"
                response["success"] = False
            else:
                form.save()
                return redirect('res_login')
        else:
            print(form.errors)
            response["message"] = "Invalid Details"
            response["success"] = False
    else:
        form = SignupForm()
        response["form"] = form

    return render(request,'restaurant/authentication/register.html', response)

def login(request):
    response = {"success":True}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = RestaurantUsers.objects.get(email=email)
            except RestaurantUsers.DoesNotExist:
                response["message"] = "User with this email does not exist"
                response["success"] = False

            if user.check_password(password):
                request.session["is_logged"] = True
                request.session["user_id"] = user.id
                request.session["name"] = user.name
                request.session["brand"] = user.brand.id
                request.session["brandname"] = user.brand.title
                request.session["brandlogo"] = str(user.brand.logo)
                return redirect('res_dashboard')
            else:
                response["message"] = "Invalid Password"
                response["success"] = False
    else:
        form = LoginForm
        response["form"] = form

    return render(request,'restaurant/authentication/login.html', response)

@load_custom_user
def dashboard(request):
    menu_items = brand_models.MenuItem.objects.filter(category__brand=request.session["brand"]).order_by('category__order','order')
    try:
        user_cart = Cart.objects.get(user=request.user)
        cart_items = {item.menu_item.id: item.quantity for item in user_cart.items.all()}
    except Cart.DoesNotExist:
        cart_items = {}
    return render(request, "restaurant/dashboard/dashboard.html", {"menu": menu_items, "cart_items": cart_items})